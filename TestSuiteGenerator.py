from numpy import pad
import numpy as np
from zztestObjective import *
import random





def log_tracking(current_iteration, current_gen):
    if current_iteration%10 == 9:
                File_object = open(r"current_gen.txt","a")
                File_object.write("Current Iteration is: {}th:".format(current_iteration) + str(current_gen))
                File_object.write('\n')



def guided_mutation(generation_number, current_gen ,current_coverage, number_of_elites, mutation_rate):

    print(current_gen)
    next_gen = []
    changed_index = []
    temp_coverage = []

    generation_number = 100
    current_gen = 1 # should be the codes appended in a list
    current_coverage =1 # should be the results list contains mutation score
    number_of_elites = int(len(current_gen) / 10)
    mutation_rate = 0.05

    for current_iteration in range(generation_number):

        sorted_coverage = sorted(range(len(current_coverage)), key=lambda k: current_coverage[k], reverse=True)

        for list_index in sorted_coverage[:number_of_elites]:

            next_gen.append(current_gen[list_index])

        for k, list_index in enumerate(sorted_coverage[number_of_elites:]):
            rand = random.random()

            if rand < mutation_rate:
                mutated_input = mutation(current_gen[list_index])

                if  check_duplicate(mutated_input , current_gen[list_index]):
                    next_gen.append(current_gen[list_index])

                else:
                    next_gen.append(mutated_input)
                    changed_index.append(list_index)

            else:
                next_gen.append(current_gen[list_index])



        for i,item in enumerate(changed_index):
            print('Current iteration in the changed_index:' , i)
            current_coverage[item] = calculate_neuron_coverage(current_gen[item] , nctoe)

        current_gen = next_gen

        changed_index = []
        next_gen= []

        log_tracking(current_iteration, current_gen)


    mutated_input = current_gen

    return mutated_input

# def generateTestSuite(model, model_input, chunk_size, generation_number, mutation_rate):
#
#     number_of_elites = int(chunk_size / 10)
#
#     test_input = []
#     current_coverage = []
#
#     for i in range(chunk_size):
#         test_input.append(model_input[i])
#
#     nctoe = set_neuron_coverage(model, test_input)
#
#     print(nctoe)
#     #
#     # for i in range(chunk_size):
#     #     print("Current iteration is: " , i)
#     #     current_coverage.append(calculate_neuron_coverage(test_input[i], nctoe))
#     #
#     # print('Current Coverage is:', current_coverage)
#     #
#     # mutated_input = GA(generation_number, test_input , current_coverage, number_of_elites, mutation_rate, nctoe)
#     #
#     # print('mutated_input', mutated_input)
#     #
#     # return mutated_input
