# Setup plotting
import matplotlib.pyplot as plt
import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers

plt.style.use('seaborn-v0_8-whitegrid')
# Set Matplotlib defaults
plt.rc('figure', autolayout=True)
plt.rc('axes', labelweight='bold', labelsize='large',
       titleweight='bold', titlesize=18, titlepad=10)

red_wine = pd.read_csv('../../../../Data/kaggle/dl-course-data/red-wine.csv')
print(red_wine.shape) # (rows, columns)

model = keras.Sequential([
    layers.Dense(units=1, input_shape=[11])
])

print(model.weights)

#print("Weights\n{}\n\nBias\n{}".format(model.weights()))