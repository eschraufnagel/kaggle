import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.plotting.register_matplotlib_converters()

# Path of the file to read
iris_filepath = "../../../../Data/kaggle/iris.csv"

# Read the file into a variable iris_data
iris_data = pd.read_csv(iris_filepath, index_col="Id")

print(iris_data.head())

# Histogram 
# sns.histplot(iris_data['Petal Length (cm)'])

# KDE plot 
#sns.kdeplot(data=iris_data['Petal Length (cm)'], fill=True)

# 2D KDE plot
#sns.jointplot(x=iris_data['Petal Length (cm)'], y=iris_data['Sepal Width (cm)'], kind="kde")

# Histograms for each species
# sns.histplot(data=iris_data, x='Petal Length (cm)', hue='Species')
# plt.title("Histogram of Petal Lengths, by Species")

# KDE plots for each species
sns.kdeplot(data=iris_data, x='Petal Length (cm)', hue='Species', fill=True)
plt.title("Distribution of Petal Lengths, by Species")

plt.show()