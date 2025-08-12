# 🧠 Guided Mutation  
A code2vec-based model training framework for learning code embeddings and refactoring suggestions

## 📌 Overview  
Guided Mutation is a toolkit designed to extract and learn vector representations of source code snippets and apply refactoring suggestions using neural networks. This project leverages code2vec methodology and deep learning models to analyze, predict, and generate code improvements in Java.

## 🚀 Features  
- **Code Embedding Extraction** – Extract path contexts from Java code using a custom extractor.  
- **Neural Network Training** – Train deep learning models (code2vec-based) on preprocessed code datasets.  
- **Refactoring Generation** – Generate and evaluate code refactorings automatically.  
- **Multiple Model Architectures** – Includes several neural network layers implemented with Keras.  
- **Preprocessing and Evaluation Scripts** – Convenient bash scripts for dataset preparation, training, and testing.

## 🛠 How it works  
1. Preprocess Java source code to extract path contexts and generate training data.  
2. Use `train.sh` to initiate training on the dataset with configurable parameters.  
3. The neural network model learns vector representations of code snippets.  
4. Optionally, generate refactoring suggestions and evaluate with test scripts.

## 📦 Installation  
1. Make sure Python 3.6+ and bash shell are installed.  
2. Install required Python packages (example):  
```
pip install tensorflow keras numpy
```
3- Clone or download this repository.
4- Ensure your dataset is placed under `data/orig` or the appropriate data directory.
5- Review and modify paths and parameters in `train.sh` as needed.

## ▶️ Usage
1- Customize `train.sh` to set the model name, dataset, and directories:
```
type=hundred_epoch_mutated
dataset_name=orig2
data_dir=data/${dataset_name}
data=${data_dir}/${dataset_name}
test_data=${data_dir}/${dataset_name}.val.c2v
model_dir=models/${type}
```
2- Run the script:
```
bash ./train.sh
```
3- Monitor training output and model saving under `models/${type}`.
4- Use other scripts like `interactive_predict.py` or `generate_refactoring.py` for inference and evaluation.

## 📚 Technologies Used
- **Python** – Core scripting language
- **TensorFlow & Keras** – Deep learning frameworks
- **Bash scripting** – Automation of training and preprocessing steps
- **code2vec** – Model architecture for code embedding
- **Java** – Source code input language for analysis
