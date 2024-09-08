import pandas as pd

reviews = pd.read_csv("input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

#print(reviews.groupby('points').points.count())
#print(reviews.groupby('points').price.min())
#print(reviews.groupby('winery').apply(lambda df: df.title.iloc[0]))
#print(reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()]))
#print(reviews.groupby(['country']).price.agg([len, min, max]))

#countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
#print(countries_reviewed)
#mi = countries_reviewed.index
#print(type(mi))

#countries_reviewed = countries_reviewed.reset_index()
#print(countries_reviewed)

#print(countries_reviewed.sort_values(by='len'))
#print(countries_reviewed.sort_values(by='len', ascending=False))

#print(countries_reviewed.sort_index)

#print(countries_reviewed.sort_values(by=['country', 'len'], ascending=[True, False]))

#reviews_written = reviews.groupby(['taster_twitter_handle']).size()
#print(reviews_written)

#best_rating_per_price = reviews.groupby(['price']).points.max().sort_index()
#print(best_rating_per_price)

# price_extremes = reviews.groupby(['variety']).price.agg([min, max])
#print(price_extremes)

# sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=[False, True])
# print(sorted_varieties)

# reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()
# print(reviewer_mean_ratings.describe())

country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)
print(country_variety_counts)