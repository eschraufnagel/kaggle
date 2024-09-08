import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error

# Load the data
data = pd.read_csv('../_data/kaggle/melbourne-housing-snapshot/melb_data.csv')

# Select subset of predictors
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
X = data[cols_to_use]

# Select target
y = data.Price

# Separate data into training and validation sets
X_train, X_valid, y_train, y_valid = train_test_split(X, y)

# n_estimators: how many times to go through the modeling cycle
# early_stopping_rounds: stop iterating when the validation score stops improving
# learning_rate: multiply predictions from each model by a small number before adding them in
# n_jobs: set to number of cores on machine, use parallelism to build models faster
my_model = XGBRegressor(n_estimators=1000, early_stopping_rounds=5, learning_rate=0.05, n_jobs=10)
my_model.fit(X_train, y_train,
             eval_set=[(X_valid, y_valid)],
             verbose=False)

predictions = my_model.predict(X_valid)
print("Mean Absolute Error: " + str(mean_absolute_error(predictions, y_valid)))