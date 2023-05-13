# analysis.py
# Main file for analysis of the Iris dataset. 
# Begin with descriptive analysis. We will call this section 1. Each comment will over-explain the code.
# Author: Neil Fitzgerald

# Section 1

import pandas as pd

# Set the column names for the Iris dataset.
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# Load the Iris dataset into a pandas DataFrame.
df = pd.read_csv('iris.data', names=column_names)

# 1.1 Descriptive Statistics
# We will perform additional analysis beyond basic descriptive statistics on the Iris dataset.

# 1.1.1 Missing Values Analysis
# The first analysis is to identify missing values in each column.
# We use the `isnull()` method to create a DataFrame of True/False values, where True represents a missing value (NaN) or blank cell.
# The `sum()` method adds up these True/False values, treating True as 1 and False as 0, providing the total count of missing values in each column.
missing_values = df.isnull().sum()

# 1.1.2 Outliers Analysis
# We detect outliers in the data using the Z-score method.
# The Z-score method measures how many standard deviations an element is from the mean.
# If the Z-score is greater than 3 or less than -3, it identifies outliers.
outliers = (df.select_dtypes(include=['float64', 'int64']) - df.mean()) / df.std()

# 1.1.3 Correlation Analysis
# We check the correlation between different variables to understand their relationships.
# The correlation indicates how closely related the variables are to each other.
correlation = df.corr()

# 1.1.4 Speices Distribution Analysis
# Here we count the occurrences of each class in the 'species' column to assess the dataset's balance.
# A balanced dataset has a similar number of samples for each class.
species_counts = df['species'].value_counts()

# 1.1.5 Output Summary File
# We create and open a file called 'summary.txt' in write mode ('w') to save our analyses.
with open('summary.txt', 'w') as file:
    # Write the descriptive statistics to the file with lines before and after
    file.write("Descriptive Statistics:\n")
    file.write(str(df.describe()))

    # Write the missing values to the file
    file.write("\n\nMissing Values:\n")
    file.write(str(missing_values))

    # Write the outliers to the file
    file.write("\n\nOutliers (values beyond 3 standard deviations):\n")
    file.write(str(outliers[(outliers > 3) | (outliers < -3)]))

    # Write the correlation to the file
    file.write("\n\nCorrelation:\n")
    file.write(str(correlation))

    # Write the Speices Distribution Analysis to the file
    file.write("\n\nSpeices Counts:\n")
    file.write(str(species_counts))

# Print messag to to say file has been created and saved
print("Success, the file has save down: 'summary.txt'.")
