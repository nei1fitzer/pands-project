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

# Section 2 - Data Visualization

# For this section we need libraries for visualisation
import matplotlib.pyplot as plt
import seaborn as sns

# 2.1 Histograms
# For each of the features in the dataset, we will create a histogram.
# This is to help us visualize the distribution of each individual variable.

for col in df.columns[:-1]:  # this excludes the non-numerical column of data 'speices' in the last (5th column)

    plt.figure(figsize=(10, 6))  # Set the size of the histogram plot

    # Create the histogram using seaborn (sns)
    # We set the DataFrame 'df' as source, and 'x' as the column to plot
    # 'hue' helps us add additional level of details for the 'species' column
    # 'element="step"'shoes the histogram bars using step function. Shows clear visual representation of the distribution & position of data points in each bin.
    # 'stat="density"' scales the histogram so  total area equals 1 (represent probability density).
    # This allows us to compare the shapes and proportions of different bins
    # and 'common_norm' as 'False' to normalise each 'species' separately.
    sns.histplot(df, x=col, hue="species", element="step", stat="density", common_norm=False)

    # Title of the histogram using current column name
    plt.title(f'{col.capitalize()} Distribution')

    # Save the histogram as a .png file using the current column name
    plt.savefig(f'{col}_distribution.png')

    # Show the histogram plot
    plt.show()


# 2.2 Scatterplots
# We will create scatterplots for each pair of features. 
# This will visualise the relationship between two variables.
sns.pairplot(df, hue="species", height=3, aspect=1);
plt.savefig('scatterplot.png')  # save the scatterplot as a .png file
plt.show()

# 2.3 Boxplots
# We will create boxplots for each feature. 
# This will show us the distibution of the data. 
# (“minimum”, first quartile (Q1), median, third quartile (Q3), and “maximum”).
plt.figure(figsize=(12, 8))  # set the figure size
sns.boxplot(data=df, orient="h", palette="Set2")
plt.title('Box plot of each feature in the dataset')  # set the boxplot title
plt.savefig('boxplot.png')  # save the boxplot as a .png file
plt.show()

# 2.4 Correlation Heatmap
# We will create a heatmap of the correlation between different features.
plt.figure(figsize=(10, 8))  # set the figure size
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Correlation heatmap')  # set the heatmap title
plt.savefig('correlation_heatmap.png')  # save the heatmap as a .png file
plt.show()



