# data_analysis_with_visuals.py
# Iris Data Analysis

## Overview
This project demonstrates basic data analysis and visualization using Python. The dataset used is the classic **Iris dataset**, which contains measurements of iris flowers from three species: Setosa, Versicolor, and Virginica.  

The objectives of this project are:  
- Load and explore a dataset using **pandas**.  
- Perform basic data analysis including descriptive statistics and group-based calculations.  
- Visualize the data using **matplotlib** and **seaborn**.  

---

## Dataset
The dataset contains the following columns:  
- `sepal length (cm)`  
- `sepal width (cm)`  
- `petal length (cm)`  
- `petal width (cm)`  
- `species`  

The `species` column represents the class of each flower: Setosa, Versicolor, or Virginica.

---

## Features
1. **Data Loading and Exploration**  
   - Load the dataset into a pandas DataFrame.  
   - Inspect the first few rows.  
   - Check data types and missing values.  
   - Clean the data (handle missing values if any).  

2. **Basic Data Analysis**  
   - Compute basic statistics (mean, median, standard deviation).  
   - Group by species and calculate mean values of numerical columns.  
   - Identify patterns or trends in the data.  

3. **Data Visualization**  
   - Line chart: cumulative sepal length by species.  
   - Bar chart: average petal length per species.  
   - Histogram: distribution of sepal width.  
   - Scatter plot: relationship between sepal length and petal length.  

---

## Libraries Used
- `pandas` – data manipulation and analysis  
- `matplotlib` – plotting and visualization  
- `seaborn` – enhanced plotting styles  
- `sklearn.datasets` – to load the Iris dataset  

---

## How to Run
1. Ensure Python is installed (version 3.7 or higher)  
2. Install required libraries if not already installed:  
   ```bash
   pip install pandas matplotlib seaborn scikit-learn
