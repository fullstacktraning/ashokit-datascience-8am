# tensorflow - Deep Learning Library (engine)
import tensorflow as tf

# keras - used to build deep learning "models" (steering)
from tensorflow import keras

# numpy used to work with lists
import numpy as np

# input
X = np.array([[1],[2],[3],[4]])

# output
y = np.array([[1],[4],[9],[16]]) 

# create model
model = keras.Sequential([
    keras.layers.Dense(3,activation='relu'),
    keras.layers.Dense(1)
])

# compile
model.compile(
    optimizer='adam',
    loss='mean_squared_error'
)

# Train the model
model.fit(X,y,epochs=1500)

# predict
print(model.predict(np.array([[5]])))



