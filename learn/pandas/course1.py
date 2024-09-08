import pandas as pd

one = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(one.describe())

two = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
print(two.describe())

three = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
print(three.describe())

four = pd.Series([1, 2, 3, 4, 5])
print(four.describe())

five = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(five.describe())

wine_reviews = pd.read_csv("input/wine-reviews/winemag-data-130k-v2.csv")
wine_reviews.shape
print(wine_reviews.head())

wine_reviews = pd.read_csv("input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
print(wine_reviews.head())