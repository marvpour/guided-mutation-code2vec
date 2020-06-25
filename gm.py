import os,random, shutil
from shutil import copyfile
from refactoring_methods import *
from generate_refactoring import *

from config import Config
from code2vec import load_model_dynamically
from interactive_predict import InteractivePredictor
from tensorflow.keras.models import Model, load_model
import numpy as np
import tensorflow.keras.backend as K
from keras.layers import recurrent
from keras_attention_layer import AttentionLayer
# import state_save as ss
import gc
import tensorflow
from tensorflow.keras.utils import CustomObjectScope
from tensorflow.keras.initializers import glorot_uniform
import glob
# from keras.datasets import mnist
from keras.models import load_model
import keras.backend as K
import numpy as np
from progressbar import *
import numpy


def refactor(K , file_path):
    # print(file_path)

    for path, d, file_names in os.walk(file_path):
        for filename in file_names:
            if '.java' in filename:
                try:
                    new_code = ''
                    open_file = open(path +'/'+ filename,'r', encoding = 'ISO-8859-1')
                    code = open_file.read()
                    new_code = generate_adversarial(K, path, code, filename)
                    wr_path = path +'/'+ filename

                    if new_code is not '':
                        l = open(wr_path,'w')
                        l.write(new_code)

                    else:
                        l = open(wr_path,'w')
                        l.write(code)

                except Exception as error:
                    l = open(wr_path,'w')
                    l.write(code)
    print('DONE WITH REFACVTOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTING')

def preprocess(path):
    fname = ''
    with open('preprocess.sh', 'r+') as f: #r+ does the work of rw
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith('TRAIN_DIR='):
                lines[i] = 'TRAIN_DIR=' + path + '\n'
                lines[i+1] = 'VAL_DIR=' + path + '\n'
                lines[i+2] = 'TEST_DIR=' + path + '\n'
                lines[i+3] = 'DATASET_NAME=' + 'data' + str(i) + '\n'
                fname = 'data' + str(i)
        f.seek(0)
        for line in lines:
            f.write(line)

    return fname



def loading_model(model_path):
    config = Config(set_defaults=True, load_from_args=True, verify=True)
    model = load_model_dynamically(config)
    config.log('Done creating code2vec model')
    model.MODEL_LOAD_PATH = model_path
    model.keras_train_model.load_weights(model.config.entire_model_load_path + '/model.h5')

    return model

def mutatio_score(model_path, refactored_data_path, fname):
    score = []
    model = loading_model(model_path)

    model.config.TEST_DATA_PATH = '/Users/Vesal/Desktop/gm_model/data/' + fname + '/' + fname + '.test.c2v'
    # (.c2v)

    eval_results = model.evaluate()
    if eval_results is not None:
        f1 = float(str(eval_results)[str(eval_results).find('F1:') + 4:])

    return f1

def model_prediction(model_path , mutants_path , refactored_data_path, fname ):
    score = []

    score.append(mutatio_score(model_path, refactored_data_path, fname))

    mutant_models = glob.glob(mutants_path + '/*.h5')
    for mt_path in mutant_models:
        score.append(mutatio_score(mt_path, refactored_data_path, fname))

    avg = numpy.average(score)
    return avg


def calculate_mutation_score(orig_path):
    new_path = []
    results = []

    for p, folder_name, file_names in os.walk(orig_path):
        for folder in folder_name:
            new_path.append(p + '/' + folder)


    for pth in new_path:
        try:
            fname = preprocess(pth)
            os.system('source preprocess.sh')
            average = model_prediction(model_path, mutants_path, pth, fname)
        except:
            average = -1

        results.append(average)

    return results

def guided_mutation(generation_number, current_gen ,current_coverage, number_of_elites, mutation_rate, original_path, K):

    for current_iteration in range(generation_number):

        sorted_coverage = sorted(range(len(current_coverage)), key=lambda i: current_coverage[i], reverse=True)

        for _, list_index in enumerate(sorted_coverage[number_of_elites:]):
            print('*'*80)
            print(_ , 'out of ', len(current_gen))
            print('We are in {} th iteration'.format(current_iteration))
            print('*'*80)
            rand = random.random()

            if rand < mutation_rate:
                refactor(K, current_gen[list_index])

        current_coverage = calculate_mutation_score(original_path)

    return current_coverage


if __name__ == '__main__':
    K = 1
    mode = 'new_data/lala2' # Options: training, test
    source = '/Users/Vesal/Desktop/gm_model/'
    model_path =  '/Users/Vesal/Desktop/gm_model/models/keras_models'
    mutants_path = "/Users/Vesal/Desktop/gm_model/models/keras_models/mutants"
    new_path = []
    results = []
    orig_path = source + mode
    #
    #
    for path, folder_name, file_names in os.walk(orig_path):
        for filename in file_names:
            if '.java' in filename:
                foleder_name = path +'/'+ filename + '_file'
                if not os.path.exists(foleder_name):
                    os.mkdir(foleder_name)
                    copyfile('/Users/Vesal/Desktop/gm_model/new_data/UserShardDemo.java', foleder_name + '/' + '_____t.java')
                    # copyfile(path +'/'+ filename , foleder_name + '/' + filename)
                    shutil.move(path +'/'+ filename , foleder_name + '/' + filename)

    # os.system('rm '+ orig_path+'/*.java')

    for p, folder_name, file_names in os.walk(orig_path):
        for folder in folder_name:
            new_path.append(p + '/' + folder)


    print('--------------------------------AHMADI-----------------------------------------')


    # res = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    #
    generation_number = 2
    current_gen = new_path # should be name of folders
    # current_coverage = res # should be the results list contains mutation score
    number_of_elites = int(len(current_gen) / 2)
    mutation_rate = 0.4

    current_coverage = calculate_mutation_score(orig_path)

    final_results = guided_mutation(generation_number, current_gen ,current_coverage, number_of_elites, mutation_rate, orig_path, K)
    print(final_results)
    print(current_coverage)
