# Setup plotting
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import make_column_transformer, make_column_selector
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
# Set Matplotlib defaults
plt.rc('figure', autolayout=True)
plt.rc('axes', labelweight='bold', labelsize='large',
       titleweight='bold', titlesize=18, titlepad=10)
plt.rc('animation', html='html5')

fuel = pd.read_csv('../../../../Data/kaggle/dl-course-data/fuel.csv')

X = fuel.copy()
# Remove target
y = X.pop('FE')

preprocessor = make_column_transformer(
    (StandardScaler(),
     make_column_selector(dtype_include=np.number)),
    (OneHotEncoder(sparse_output=False),
     make_column_selector(dtype_include=object)),
)

X = preprocessor.fit_transform(X)
y = np.log(y) # log transform target instead of standardizing

input_shape = [X.shape[1]]
print("Input shape: {}".format(input_shape))

# Uncomment to see original data
print(fuel.head())
# Uncomment to see processed features
print(pd.DataFrame(X[:10,:]).head())

model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=input_shape),
    layers.Dense(128, activation='relu'),    
    layers.Dense(64, activation='relu'),
    layers.Dense(1),
])

model.compile(
    optimizer='adam',
    loss='mae',
)

history = model.fit(
    X, y,
    batch_size=128, 
    epochs=200,      
)

history_df = pd.DataFrame(history.history)
# Start the plot at epoch 5. You can change this to get a different view.
history_df.loc[5:, ['loss']].plot();
plt.show(block=True)

# You probably saw that smaller batch sizes gave noisier weight updates and loss curves. 
# This is because each batch is a small sample of data and smaller samples tend to give noisier estimates. 
# Smaller batches can have an "averaging" effect though which can be beneficial.

# Smaller learning rates make the updates smaller and the training takes longer to converge. 
# Large learning rates can speed up training, but don't "settle in" to a minimum as well. 
# When the learning rate is too large, the training can fail completely. 
# (Try setting the learning rate to a large value like 0.99 to see this.)
