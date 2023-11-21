# 1. Wdbc - Dataset
   
**This project presents a series of predictive models** developed and tested using the **Breast Cancer Wisconsin (Diagnostic) Data Set**. The primary application of these models is the **classification of breast cancer tumors** into **benign or malignant** categories based on extracted features from cell nuclei in digital images of breast mass biopsies.

## Comparison model
Several machine learning models have been employed and evaluated to determine their effectiveness in predicting the malignancy of breast tumors. The models tested include, but are not limited to:

- **SGDClassifier**
- **Random Forest Classifier**
- **K-Nearest Neighbors Classifier**
- **Gaussian Process Classifier**
- **MLPClassifier**
  
A comparative analysis has been conducted to assess the **accuracy, precision, recall, F1-score, and ROC-AUC** among other metrics for each of the models.
The model results are **summarized in graphs** to make it easier to understand how each model performs.

https://colab.research.google.com/drive/1DmzgMnJkRzlGEYgoxbAjEgIarEz-HlIp?usp=sharing

# 2. Fashion-MNIST Classification with Keras
**This project involves the creation of a predictive model** utilizing the Fashion-MNIST dataset to classify clothing items into ten distinct categories. The model is developed with Keras's Sequential API.

## Results of model
The results of the various metrics are displayed and plotted in graphs, providing a clear visual summary of the model's classification capabilities.

## Dataset Overview
The Fashion-MNIST set contains 70,000 grayscale images, with 60,000 for training and 10,000 for testing, each 28x28 pixels in size, and labeled from 0 to 9 to denote different fashion articles like T-shirts, trousers, and bags.

https://colab.research.google.com/drive/1z6_VHF1d1K0FUaCGITf_x_C8ICA62qCs?usp=sharing


# 2. Fashion-MNIST Classification with Keras
**This project involves the creation of a predictive model** utilizing the Fashion-MNIST dataset to classify clothing items into ten distinct categories. The model is developed with Keras's Sequential API.

## Results of model
The results of the various metrics are displayed and plotted in graphs, providing a clear visual summary of the model's classification capabilities.

## Dataset Overview
The Fashion-MNIST set contains 70,000 grayscale images, with 60,000 for training and 10,000 for testing, each 28x28 pixels in size, and labeled from 0 to 9 to denote different fashion articles like T-shirts, trousers, and bags.

https://colab.research.google.com/drive/1z6_VHF1d1K0FUaCGITf_x_C8ICA62qCs?usp=sharing

# 3. California Housing - Regression with Keras

## Overview
This project demonstrates the creation and application of regression models using the **California Housing dataset**. The main goal is to predict housing prices based on various features using different neural network architectures in Keras.

### Dataset and Preprocessing
- **Dataset:** _California Housing dataset_
- **Split:** _Training, validation, and test sets_
- **Preprocessing:** _Data normalization_

### Model Development
Several models are developed using Keras:

1. **Sequential API Model:** 
   - **Architecture:** _Multiple dense layers with ReLU activation_
   - **Metrics:** _Root Mean Squared Error (RMSE)_
   - **Training:** _20 epochs with validation data_

2. **Functional API Model:** 
   - **Complex Architecture:** _Allows multiple inputs and outputs_
   - **Feature Processing:** _Different subsets of input through various paths_
   - **Auxiliary Output:** _Includes an auxiliary output for regularization_

3. **Subclassing API Model:**
   - **Dynamic Model Building:** _Using the subclassing approach_
   - **Customized Architecture:** _A wider range of operations_
   - **Dual Outputs:** _Simultaneous training of main and auxiliary outputs_

### Results
- **Evaluation:** _Models evaluated using metrics like RMSE_
- **Visualization:** _Comparative graphs for training performance_
- **Predictions:** _Assessment of model performance on test data_

### Visualization and Code Access
- **Model Architectures:** _Visualized using plots_
- **Training Progress:** _Graphical representation_
- **Code Access:** _Available on Colab for replication and further exploration_

https://colab.research.google.com/drive/1ZXVObn1YZNkSgLAywDjVVehKkSMNtQbv?usp=sharing
