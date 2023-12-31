# -*- coding: utf-8 -*-
"""wdbc.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DmzgMnJkRzlGEYgoxbAjEgIarEz-HlIp

# Classification of benign or malignant lesions based on **WDBS – Dataset** using **Various models**

---

## Install datapackage
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install datapackage

"""**1. Collection and preparation of the dataset**

## 1. Collection and preparation of the dataset

### 1.1 Collection of the dataset
"""

import datapackage
import pandas as pd
#https://datahub.io/machine-learning/wdbc
data_url = 'https://datahub.io/machine-learning/wdbc/datapackage.json'

# to load Data Package into storage
package = datapackage.Package(data_url)

"""### 1.2 Preparation of the dataset"""

# to load only tabular data
resources = package.resources
for resource in resources:
    if resource.tabular:
        data = pd.read_csv(resource.descriptor['path'])

y = pd.DataFrame()
y['Class'] = data['Class']
data.drop(labels='Class', axis=1, inplace=True)
X = data
kolumny = ["V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10",
           "V11", "V12", "V13", "V14", "V15", "V16", "V17", "V18", "V19", "V20",
           "V21", "V22", "V23", "V24", "V25", "V26", "V27", "V28", "V29", "V30"]


X = X.to_numpy()
y = y.to_numpy()
y = y.ravel()

print(y)
print(X)

"""### 1.3 Data split"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

"""## SGDClassifier

### 2.1 Training the model
"""

from sklearn.linear_model import SGDClassifier

sgd_clf = SGDClassifier(loss='log_loss', random_state=42)
sgd_clf.fit(X_train, y_train)

y_pred_sgd = sgd_clf.predict(X_test)

"""### 2.2 Calculation of metrics"""

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

accuracy_sgd = accuracy_score(y_test, y_pred_sgd)

precision_sgd = precision_score(y_test, y_pred_sgd)

recall_sgd = recall_score(y_test, y_pred_sgd)

f1_score_sgd = f1_score(y_test, y_pred_sgd) # Harmonic mean of precision and fullness

confusion_matrix_sgd = confusion_matrix(y_test, y_pred_sgd)

"""### 2.3 Results of metrics"""

print(f'Accuracy of sgd model: {accuracy_sgd}')
print(f'Sgd model precision: {precision_sgd}')
print(f'Sgd model recall: {recall_sgd}')
print(f'F1 model sgd: {f1_score_sgd}')

"""### 2.4 Confusion Matrix"""

disp_sgd = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix_sgd, display_labels=sgd_clf.classes_)
disp_sgd.plot()
plt.show()

"""### 2.5 Cross Val Score"""

from sklearn.model_selection import cross_val_score
cross_val_score(sgd_clf, X_train, y_train, cv=3, scoring='accuracy')

some_digit = X[0]
y_scores = sgd_clf.decision_function([some_digit]) # Decision result
print(f'Wynik decyzyjny: {y_scores}')
threshold = 0
y_some_digit_pred = (y_scores > threshold)
print(f'Wynik: {y_some_digit_pred}')

"""### 2.6 ROC curve"""

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.metrics import roc_curve, auc, precision_recall_curve
import matplotlib.pyplot as plt

# Probability of belonging to a class
y_prob_sgd = sgd_clf.predict_proba(X_test)[:, 1]
fpr_sgd, tpr_sgd, _ = roc_curve(y_test, y_pred_sgd, pos_label=2)

plt.figure(figsize=(8, 6))
plt.plot(fpr_sgd, tpr_sgd, label=f'AUC: {auc(fpr_sgd, tpr_sgd)}')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve for SGDClassifier')
plt.legend(loc='lower right')
plt.grid()
plt.show()

"""### 2.7  Precision Recall Curve"""

from sklearn.metrics import precision_recall_curve
precision_sgd, recall_sgd, _ = precision_recall_curve(y_test, y_prob_sgd, pos_label=2)

plt.figure(figsize=(8, 6))
plt.plot(recall_sgd, precision_sgd)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve for SGDClassifier')
plt.grid()
plt.show()

"""## Random Forest Classifier

### 3.1 Training the model
"""

from sklearn.ensemble import RandomForestClassifier

forest_clf = RandomForestClassifier(random_state=42)
forest_clf.fit(X_train, y_train)

y_pred_forest = forest_clf.predict(X_test)

"""### 3.2 Calculation of metrics"""

accuracy_forest = accuracy_score(y_test, y_pred_forest)

precision_forest = precision_score(y_test, y_pred_forest)

recall_forest = recall_score(y_test, y_pred_forest)

f1_score_forest = f1_score(y_test, y_pred_forest)

confusion_matrix_forest = confusion_matrix(y_test, y_pred_forest)

"""### 3.3 Result of metrics"""

print(f'Accuracy of rfc model: {accuracy_sgd}')
print(f'Rfc model precision: {precision_sgd}')
print(f'Rfc model recall: {recall_sgd}')
print(f'F1 model rfc: {f1_score_sgd}')

"""### 3.4 Confusion Matrix"""

disp_forest = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix_forest, display_labels=forest_clf.classes_)
disp_forest.plot()
plt.show()

"""### 3.5 Cross Val Score"""

cross_val_score(forest_clf, X_train, y_train, cv=3, scoring='accuracy')

"""### 3.6 Roc curve"""

y_prob_forest = forest_clf.predict_proba(X_test)[:, 1]
fpr_forest, tpr_forest, _ = roc_curve(y_test, y_prob_forest, pos_label=2)

plt.figure(figsize=(8, 6))
plt.plot(fpr_forest, tpr_forest, label=f'AUC: {auc(fpr_forest, tpr_forest)}')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve for RandomForestClassifier')
plt.legend(loc='lower right')
plt.grid()
plt.show()

"""### 3.7 Precision Recall Curve"""

precision_forest, recall_forest, _ = precision_recall_curve(y_test, y_prob_forest, pos_label=2)

plt.figure(figsize=(8, 6))
plt.plot(recall_forest, precision_forest)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve for RandomForestClassifier')
plt.grid()
plt.show()

"""## K-Nearest Neighbors Classifier

### 4.1 Training the model
"""

# from sklearn.neighbors import KNeighborsClassifier
# knn_clf = KNeighborsClassifier(n_neighbors=3)
# knn_clf.fit(X_train, y_train)

# y_pred_knn = knn_clf.predict(X_test)

import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Finding the best value of k using a petal
k_values = [i for i in range (1,31)]
scores = []

for k in k_values:
    knn_clf = KNeighborsClassifier(n_neighbors=k)
    score = cross_val_score(knn_clf, X, y, cv=5)
    scores.append(np.mean(score))

best_index = np.argmax(scores)
best_k = k_values[best_index]

knn_clf = KNeighborsClassifier(n_neighbors=best_k)
knn_clf.fit(X_train, y_train)

y_pred_knn = knn_clf.predict(X_test)

"""### 4.2 Calculation of metrics"""

accuracy_knn = accuracy_score(y_test, y_pred_knn)

precision_knn = precision_score(y_test, y_pred_knn)

recall_knn = recall_score(y_test, y_pred_knn)

f1_score_knn = f1_score(y_test, y_pred_knn)

confusion_matrix_knn = confusion_matrix(y_test, y_pred_knn)

"""### 4.3 Result of metrics"""

print(f'Accuracy of knn model: {accuracy_knn}')
print(f'Knn model precision: {precision_knn}')
print(f'Knn model recall: {recall_knn}')
print(f'F1 model knn: {f1_score_knn}')

"""### 4.4 Confusion Matrix"""

disp_knn = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix_knn, display_labels=knn_clf.classes_)
disp_knn.plot()
plt.show()

"""### 4.5 Cross Val Score"""

cross_val_score(knn_clf, X_train, y_train, cv=3, scoring='accuracy')

"""### 4.6 Roc curve"""

# Prawdopodobieństwo przynależności do klasy
y_prob_knn = knn_clf.predict_proba(X_test)[:, 1]
fpr_knn, tpr_knn, _ = roc_curve(y_test, y_prob_knn, pos_label=2)

plt.figure(figsize=(8, 6))
plt.plot(fpr_knn, tpr_knn, label=f'AUC: {auc(fpr_knn, tpr_knn)}')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve for KNeighborsClassifier')
plt.legend(loc='lower right')
plt.grid()
plt.show()

"""### 4.7 Precision Recall Curve"""

precision_knn, recall_knn, _ = precision_recall_curve(y_test, y_prob_knn, pos_label=2)

plt.figure(figsize=(8, 6))
plt.plot(recall_knn, precision_knn)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve for KNeighborsClassifier')
plt.grid()
plt.show()

"""## GaussianProcessClassifier

### 5.1 Training the model
"""

from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.gaussian_process.kernels import RBF
from sklearn.gaussian_process.kernels import DotProduct
from sklearn.gaussian_process.kernels import Matern
from sklearn.gaussian_process.kernels import RationalQuadratic
from sklearn.gaussian_process.kernels import WhiteKernel
from sklearn.model_selection import RepeatedStratifiedKFold

model = GaussianProcessClassifier()

cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
grid = dict()
grid['kernel'] = [1*RBF(), 1*DotProduct(), 1*Matern(),  1*RationalQuadratic(), 1*WhiteKernel()]
search = GridSearchCV(model, grid, scoring='accuracy', cv=cv, n_jobs=-1)
results = search.fit(X_train, y_train)

print('Best Mean Accuracy: %.3f' % results.best_score_)
print('Best Config: %s' % results.best_params_)

means = results.cv_results_['mean_test_score']
params = results.cv_results_['params']

from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.gaussian_process.kernels import RationalQuadratic


kernel = 1**2 * RationalQuadratic(alpha=1, length_scale=1)
gpc_clf = GaussianProcessClassifier(kernel=kernel, random_state=0)
gpc_clf.fit(X_train, y_train)

y_pred_gpc = gpc_clf.predict(X_test)

"""### 5.2 Calculation of metrics"""

accuracy_gpc = accuracy_score(y_test, y_pred_gpc)

precision_gpc = precision_score(y_test, y_pred_gpc)

recall_gpc = recall_score(y_test, y_pred_gpc)

f1_score_gpc = f1_score(y_test, y_pred_gpc)

confusion_matrix_gpc = confusion_matrix(y_test, y_pred_gpc)

"""### 5.3 Result of metrics



"""

print(f'Accuracy of gpc model: {accuracy_gpc}')
print(f'Gpc model precision: {precision_gpc}')
print(f'Gpc model recall: {recall_gpc}')
print(f'F1 model gpc: {f1_score_gpc}')

"""### 5.4 Confusion Matrix"""

disp_gpc = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix_gpc, display_labels=gpc_clf.classes_)
disp_gpc.plot()
plt.show()

"""### 5.5 Cross Val *Score*"""

cross_val_score(gpc_clf, X_train, y_train, cv=3, scoring='accuracy')

"""### 5.6 Roc curve"""

y_prob_gpc = gpc_clf.predict_proba(X_test)[:, 1]
fpr_gpc, tpr_gpc, _ = roc_curve(y_test, y_prob_gpc, pos_label=2)

plt.figure(figsize=(8, 6))
plt.plot(fpr_gpc, tpr_gpc, label=f'AUC: {auc(fpr_gpc, tpr_gpc)}')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve for GaussianProcessClassifier')
plt.legend(loc='lower right')
plt.grid()
plt.show()

"""### 5.7 Precision Recall Curve"""

precision_gpc, recall_gpc, _ = precision_recall_curve(y_test, y_prob_gpc, pos_label=2)

plt.figure(figsize=(8, 6))
plt.plot(recall_gpc, precision_gpc)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve for GaussianProcessClassifier')
plt.grid()
plt.show()

"""## MLPClassifier

### 6.1 Training the model
"""

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV

sc=StandardScaler()
scaler = sc.fit(X_train)

X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

param_grid = {
    'hidden_layer_sizes': [(150,100,50), (120,80,40), (100,50,30)],
    'max_iter': [50, 100, 150],
    'activation': ['tanh', 'relu'],
    'solver': ['sgd', 'adam'],
    'alpha': [0.0001, 0.05],
    'learning_rate': ['constant','adaptive'],
}


mlp_clf = MLPClassifier()

grid_mlp_clf = GridSearchCV(mlp_clf, param_grid, n_jobs= -1, cv=5)
grid_mlp_clf.fit(X_train_scaled, y_train)

print(grid_mlp_clf.best_params_)

y_pred_mlp = grid_mlp_clf.predict(X_test_scaled)

"""### 6.2 Calculation of metric"""

accuracy_mlp = accuracy_score(y_test, y_pred_mlp)

precision_mlp = precision_score(y_test, y_pred_mlp)

recall_mlp = recall_score(y_test, y_pred_mlp)

f1_score_mlp = f1_score(y_test, y_pred_mlp)

confusion_matrix_mlp = confusion_matrix(y_test, y_pred_mlp)

"""### 6.3 Result of metrics"""

print(f'Accuracy of mlp model: {accuracy_sgd}')
print(f'Mlp model precision: {precision_sgd}')
print(f'Mlp model recall: {recall_sgd}')
print(f'F1 model mlp: {f1_score_sgd}')

"""### 6.4 Confusion Matrix"""

disp_MLP = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix_mlp, display_labels=grid_mlp_clf.classes_)
disp_MLP.plot()
plt.show()

"""### 6.5 Roc Curve"""

y_prob_mlp = grid_mlp_clf.predict_proba(X_test)[:, 1]
fpr_mlp, tpr_mlp, _ = roc_curve(y_test, y_prob_mlp, pos_label=2)

plt.figure(figsize=(8, 6))
plt.plot(fpr_mlp, tpr_mlp, label=f'AUC: {auc(fpr_mlp, tpr_mlp)}')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve for GaussianProcessClassifier')
plt.legend(loc='lower right')
plt.grid()
plt.show()

"""### 6.6 Precision Recall Curve

## Model comparison

### 7.1 ROC Curve Comparison
"""

plt.figure(figsize=(8, 6))

# Chart for SGDClassifier
plt.plot(fpr_sgd, tpr_sgd, label=f'SGDClassifier AUC: {auc(fpr_sgd, tpr_sgd)}')

# Chart for RandomForestClassifier
plt.plot(fpr_forest, tpr_forest, label=f'RandomForestClassifier AUC: {auc(fpr_forest, tpr_forest)}', linestyle='--')

# Chart for K-Nearest Neighbors Classifier
plt.plot(fpr_knn, tpr_knn, label=f'Nearest Neighbors Classifier AUC: {auc(fpr_knn, tpr_knn)}', linestyle=':')

# Chart for GaussianProcessClassifier
plt.plot(fpr_gpc, tpr_gpc, label=f'GaussianProcessClassifier AUC: {auc(fpr_gpc, tpr_gpc)}', linestyle='-.')

# Chart for MLPCLassifier
plt.plot(fpr_gpc, tpr_gpc, label=f'MLPCLassifier AUC: {auc(fpr_mlp, tpr_mlp)}', linestyle='-')

plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve Comparison')
plt.legend(loc='lower right')
plt.grid()
plt.show()

"""### 7.2 Precision Recall Curve Comparison"""

plt.figure(figsize=(8, 6))

# Chart for SGDClassifier
plt.plot(recall_sgd, precision_sgd, label='SGDClassifier')

# Chart for RandomForestClassifier
plt.plot(recall_forest, precision_forest, label='RandomForestClassifier', linestyle='--')

# Chart for K-Nearest Neighbors Classifier
plt.plot(recall_knn, precision_knn, label='Nearest Neighbors Classifier', linestyle=':')

# Chart for GaussianProcessClassifier
plt.plot(recall_gpc, precision_gpc, label='GaussianProcessClassifier', linestyle='-.')

# Chart for MLPCLassifier
plt.plot(recall_mlp, precision_mlp, label='MLPCLassifier', linestyle='-')

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve Comparison')
plt.grid()
plt.legend()
plt.show()