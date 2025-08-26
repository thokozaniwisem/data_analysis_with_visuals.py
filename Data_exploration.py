# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset


# Load the Iris dataset
iris_data = load_iris()
df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
df['species'] = iris_data.target

# Map target numbers to species names
species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
df['species'] = df['species'].map(species_map)

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Explore structure
print("\nData types and missing values:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# Task 1b: Clean dataset (no missing values in Iris, but example)
df = df.dropna()  # drop rows with missing values if any

# Task 2: Basic Data Analysis

# Basic statistics
print("\nBasic statistics for numerical columns:")
print(df.describe())

# Group by species and compute mean of numerical columns
species_group = df.groupby('species').mean()
print("\nMean of numerical columns by species:")
print(species_group)

# Task 3: Data Visualization

# Set Seaborn style for better visuals
sns.set(style="whitegrid")

# 1. Line chart: Using cumulative sepal length for each species
plt.figure(figsize=(8,5))
for species in df['species'].unique():
    species_data = df[df['species'] == species]
    plt.plot(species_data['sepal length (cm)'].cumsum(), label=species)
plt.title('Cumulative Sepal Length by Species')
plt.xlabel('Observation')
plt.ylabel('Cumulative Sepal Length (cm)')
plt.legend()
plt.show()

# 2. Bar chart: Average petal length per species
plt.figure(figsize=(6,4))
sns.barplot(x=species_group.index, y=species_group['petal length (cm)'])
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()

# 3. Histogram: Distribution of sepal width
plt.figure(figsize=(6,4))
plt.hist(df['sepal width (cm)'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter plot: Sepal length vs Petal length
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.show()

# Observations
print("\nObservations:")
print("- Setosa generally has smaller petal lengths and sepal lengths than the other species.")
print("- Versicolor and Virginica have some overlap in sepal length but are more distinguishable in petal length.")
print("- Sepal width is fairly evenly distributed across species, but Setosa shows slightly higher width.")
