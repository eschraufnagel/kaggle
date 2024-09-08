import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('../_data/kaggle/melbourne-housing-snapshot/melb_data.csv')

# Select subset of predictors
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
X = data[cols_to_use]

# Select target
y = data.Price

# Define the pipeline that uses a imputer to fill in missing values and a random forest model to make predictions
#my_pipeline = Pipeline(steps=[('preprocessor', SimpleImputer()),
                              #('model', RandomForestRegressor(n_estimators=50,
                                                              #random_state=0))
                             #])

#Obtain cross-validation scores
# Multiply by -1 since sklearn calculates *negative* MAE
#scores = -1 * cross_val_score(my_pipeline, X, y,
                              #cv=5, # number of folds
                              #scoring='neg_mean_absolute_error')

#print("MAE scores:\n", scores)

#print("Average MAE score (across experiments):")
#print(scores.mean())

def get_score(n_estimators):
    """Return the average MAE over 3 CV folds of random forest model.
    
    Keyword argument:
    n_estimators -- the number of trees in the forest
    """
    my_pipeline = Pipeline(steps=[('preprocessor', SimpleImputer()),
                              ('model', RandomForestRegressor(n_estimators=n_estimators,
                                                              random_state=0))
                             ])
    
    scores = -1 * cross_val_score(my_pipeline, X, y,
                              cv=3, # number of folds
                              scoring='neg_mean_absolute_error')
    return scores.mean()

#result = dict([x : get_score(x) for x in range(50, 450, 50)])

results = { x:get_score(x) for x in range(50, 450, 50) }

print(results)

plt.plot(list(results.keys()), list(results.values()))
plt.show()