import pandas as pd

reviews = pd.read_csv("input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

#print(reviews.head())

#print(reviews.country)
#print(reviews['country'])
#print(reviews['country'][0])

#print(reviews.iloc[0])
#print(reviews.iloc[:, 0])
#print(reviews.iloc[:3, 0])
#print(reviews.iloc[1:3, 0])

#df = reviews.iloc[0:100,[1,12]]

#one = reviews.query("country == 'Italy'")
#print(one)

#two = reviews[reviews.country == 'Italy']
#print(two)

top_oceania_wines = reviews.query('points >= 95 and (country == "Italy" or country == "New Zealand")')
print(top_oceania_wines)

top_oceania_wines2 = reviews.loc[
    (reviews.country.isin(['Australia', 'New Zealand']))
    & (reviews.points >= 95)
]
print(top_oceania_wines2)