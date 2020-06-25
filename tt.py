
from config import Config
from code2vec import load_model_dynamically
from interactive_predict import InteractivePredictor


config = Config(set_defaults=True, load_from_args=True, verify=True)
model = load_model_dynamically(config)
config.log('Done creating code2vec model')

#model.train()
#
# predictor = InteractivePredictor(config, model)
# ves = predictor.predict()
# print(ves)
# model.MODEL_LOAD_PATH =  'Users/Vesal/Desktop/gm_model/'
model.keras_train_model.load_weights(model.config.entire_model_load_path + '/model.h5')
model.keras_train_model.summary(print_fn=model.log)

eval_results = model.evaluate()
f1 = float(str(eval_results)[str(eval_results).find('F1:') + 4:])
print(f1)
# if eval_results is not None:
#     config.log(
#         str(eval_results).replace('topk', 'top{}'.format(config.TOP_K_WORDS_CONSIDERED_DURING_PREDICTION)))
# for path in model_path:
#         model = load_model(path)
