import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.plotting.register_matplotlib_converters()

# Path of the file to read
spotify_filepath = "../../../../Data/kaggle/spotify.csv"

# Read the file into a variable spotify_data
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)

#print(spotify_data.tail())

# Line chart showing daily global streams of each song 
sns.lineplot(data=spotify_data)

# Set the width and height of the figure
plt.figure(figsize=(14,6))

# Add title
plt.title("Daily Global Streams of Popular Songs in 2017-2018")

# Line chart showing daily global streams of each song 
sns.lineplot(data=spotify_data)

#plt.show()

print(list(spotify_data.columns))