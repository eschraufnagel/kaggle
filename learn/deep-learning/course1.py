from tensorflow import keras
from tensorflow.keras import layers

# Create a network with 1 linear unit
# input_shape=[num_columns]
model = keras.Sequential([
    layers.Dense(units=1, input_shape=[3])
])