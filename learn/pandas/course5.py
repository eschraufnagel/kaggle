import pandas as pd

reviews = pd.read_csv("input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

#print(reviews.price.dtype)
#print(reviews.dtypes)
#print(reviews.points.astype('float64'))
#print(reviews.index.dtype)

#print(reviews[pd.isnull(reviews.country)])
#print(reviews.region_2.fillna("Unknown"))
#print(reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino"))

# dtype = reviews.points.dtype
# print(dtype)

# points_string = reviews.points.astype('str')
# print(points_string.dtype)

# n_missing_prices = reviews['price'].isna().sum()
# print(n_missing_prices)

#reviews[reviews['region_1'].isna()].fillna('Unknown', inplace=True)
ß

#print(reviews[pd.isnull(reviews['region_1'])])
#21247
#reviews[pd.isna(reviews.region_1)].fillna('Unknown', inplace=True)

# reviews.fillna(value={'region_1':"Unknown"}, inplace=True)
# reviews_per_region = reviews.groupby(['region_1']).size().sort_values(ascending=False)
# print(reviews_per_region)

reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
print(reviews_per_region)