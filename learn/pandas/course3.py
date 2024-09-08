import pandas as pd
import numpy as np


reviews = pd.read_csv("input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

#print(reviews)

#print(reviews.points.describe())

#print(reviews.taster_name.describe())

#print(reviews.points.mean())

#print(reviews.taster_name.value_counts())

review_points_mean = reviews.points.mean()

#print(reviews.points.map(lambda p: p - review_points_mean))

def remean_points(row):
    row.points = row.points - review_points_mean
    return row

#print(reviews.apply(remean_points, axis='columns'))

#print(reviews.points - review_points_mean)

#print(reviews.country + " - " + reviews.region_1)

#print(reviews.points.median())

#print(reviews.country.unique())

#print(reviews.country.value_counts())

#print(reviews.price - reviews.price.mean())

#reviews['value'] = reviews.points / reviews.price
#print(reviews.loc[reviews['value'].idxmax()].title)

#bargain_idx = (reviews.points / reviews.price).idxmax()
#bargain_wine = reviews.loc[bargain_idx, 'title']

#split_desc = reviews.head(10).description.str.split(expand=True).stack()

#print(split_desc.value_counts()['tropical','fruity'])


#print(reviews.description.apply(lambda p: True if 'tropical' in p else False))
#print(reviews.description.apply(lambda p: True if 'fruity' in p else False))

# tropical_count1 = reviews.description.apply(lambda p: p.count('tropical')).sum()
# fruity_count1 = reviews.description.apply(lambda p: p.count('fruity')).sum()
# descriptor_counts1 = pd.Series([tropical_count1, fruity_count1], index=['tropical', 'fruity'])
# print(descriptor_counts1)

# tropical_count2 = reviews.description.apply(lambda p: "tropical" in p).sum()
# fruity_count2 = reviews.description.apply(lambda p: "fruity" in p).sum()
# descriptor_counts2 = pd.Series([tropical_count2, fruity_count2], index=['tropical', 'fruity'])
# print(descriptor_counts2)

def calc_stars(row):
    if row.points >= 95 or row.country == "Canada":
        return 3
    if row.points >= 85:
        return 2
    return 1

stars2 = reviews.apply(calc_stars, axis='columns')
print(stars2)

#stars = reviews.points.map(lambda p: 3 if p >= 95 else (2 if p >= 85 else 1))
#print(stars)