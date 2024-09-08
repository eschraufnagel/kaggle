import pandas as pd

reviews = pd.read_csv("input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
# canadian_youtube = pd.read_csv("input/youtube-new/CAvideos.csv")
# british_youtube = pd.read_csv("input/youtube-new/GBvideos.csv")

#print(reviews.rename(columns={'points': 'score'}))
#print(reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'}))
#print(reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns'))

# print(canadian_youtube)
# print(british_youtube)
# print(pd.concat([canadian_youtube, british_youtube]))

# left = canadian_youtube.set_index(['title', 'trending_date'])
# right = british_youtube.set_index(['title', 'trending_date'])
# print(left.join(right, lsuffix='_CAN', rsuffix='_UK'))

# renamed = reviews.rename(columns={'region_1': 'region', 'region_2': 'locale'})
# print(renamed[['region', 'locale']])

reindexed = reviews.rename_axis("wines", axis='rows')
print(reindexed)