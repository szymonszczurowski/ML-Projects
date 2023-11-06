# -*- coding: utf-8 -*-
"""fashion_mnist.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z6_VHF1d1K0FUaCGITf_x_C8ICA62qCs

# Classifying images using the Keras sequence interface

## Collection and preparation of the dataset

### 1.1 Collection of the dataset
"""

import tensorflow as tf

fashion_mnist = tf.keras.datasets.fashion_mnist.load_data()

"""### 1.2 Split of the dataset"""

(X_train_full, y_train_full), (X_test, y_test) = fashion_mnist
X_train, y_train = X_train_full[:-5000], y_train_full[:-5000]
X_valid, y_valid = X_train_full[-5000:], y_train_full[-5000:]

print(f'X_train_full shape: {X_train_full.shape}')
print(f'y_train_full shape: {y_train_full.shape}')
print(f'X_train shape: {X_train.shape}')
print(f'y_train shape: {y_train.shape}')
print(f'X_valid shape: {X_valid.shape}')
print(f'y_valid shape: {y_valid.shape}')

"""### 1.3 Data scaling"""

# Scale color saturation from to range from 0 to 1
X_train, X_valid, X_test = X_train / 255., X_valid / 255., X_test / 255.

"""### 1.4 Getting to know the data"""

X_train[0]

import matplotlib.pyplot as plt
plt.imshow(X_train[0], cmap="binary")
plt.show()

class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

class_names[y_train[0]]

n_rows = 4
n_cols = 10
plt.figure(figsize=(n_cols * 1.2, n_rows * 1.2))
for row in range(n_rows):
    for col in range(n_cols):
        index = n_cols * row + col
        plt.subplot(n_rows, n_cols, index + 1)
        plt.imshow(X_train[index], cmap="binary", interpolation="nearest")
        plt.axis('off')
        plt.title(class_names[y_train[index]])
plt.subplots_adjust(wspace=0.2, hspace=0.5)

plt.show()

"""## Creating the model using the Sequential API

### 2.1 Building a neural network
"""

tf.random.set_seed(42) # tf.keras.utils.set_random_seed()
model = tf.keras.Sequential()
model.add(tf.keras.layers.InputLayer(input_shape=[28, 28]))
model.add(tf.keras.layers.Flatten()) # Transforming into one-dimensional arrays ([32, 28, 28] = [32, 784]) - X.reshape(-1, 784)
model.add(tf.keras.layers.Dense(300, activation='relu'))
model.add(tf.keras.layers.Dense(100, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax')) # Output layer

# Way with a list

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=[28, 28]),
    tf.keras.layers.Dense(300, activation='relu'),
    tf.keras.layers.Dense(100, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.summary()

tf.keras.utils.plot_model(model, "my_fashion_mnist_model.png", show_shapes=True)

"""### 2.2 List of model variants"""

model.layers

model.get_layer('flatten_1')

"""### 2.2 Model parameters"""

hidden1 = model.layers[1] # <keras.src.layers.core.dense.Dense object at 0x7a0989bc72e0>
weights, biases = hidden1.get_weights()
print(weights)
print(weights.shape, '\n')
print(biases)
print(biases.shape)

"""## Compiling the model"""

model.compile(loss='sparse_categorical_crossentropy', # rare labels (They can be replaced to one-hot vectors)
              optimizer='sgd', metrics=['accuracy'])

# model.compile(loss=tf.keras.losses.sparse_categorical_crossentropy,
#               optimizer=tf.keras.optimizers.SGD(),
#               metrics=[tf.keras.metrics.sparse_categorical_accuracy])

# shows how to convert class ids to one-hot vectors
tf.keras.utils.to_categorical([0, 5, 1, 0], num_classes=10)

import numpy as np

# shows how to convert one-hot vectors to class ids
np.argmax(
    [[1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
     [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
     [0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
     [1., 0., 0., 0., 0., 0., 0., 0., 0., 0.]],
    axis=1
)