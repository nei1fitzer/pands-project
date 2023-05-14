# analysis.py
# Main file for analysis of the Iris dataset. 
# Author: Neil Fitzgerald
# reference used throughout this code: Stack Overflow, Python/Pandas documentation, GitHUB (formatting and analysis), and OpenAI's ChatGPT for error checking when stuck.
# I have over commented below to show understnading of the code. I acknowledge this will look clunky but I will not give this much detail going forward in other modules.



# Section 1: Importing necessary modules
# Pandas is used for data manipulation and analysis
import pandas as pd

# Section 1.1: Data Loading and Preprocessing
# The Iris dataset does not come with column names. 
# We manually specify them and load the data into a pandas DataFrame.
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df = pd.read_csv('iris.data', names=column_names)

# Section 1.2: Descriptive Statistics
# We will perform additional analysis beyond basic descriptive statistics on the Iris dataset.

# 1.2.1 Missing Values Analysis
# Identify the number of missing values in each column of the dataset
missing_values = df.isnull().sum()

# 1.2.2 Outliers Analysis
# Identify the outliers in the dataset (more than 3 standard deviations away from the mean).
outliers = ((df.select_dtypes(include=['float64', 'int64']) - df.mean()) / df.std()).abs() > 3
outliers = df[outliers.any(axis=1)]

# 1.2.3 Correlation Analysis
# Identify the correlation between different columns in the dataset
correlation = df.corr()

# 1.2.4 Species Distribution Analysis
# Count the number of each species present in the dataset
species_counts = df['species'].value_counts()

# 1.2.5 Output Summary File
# Write the above analyses to a summary file
with open('summary.txt', 'w') as file:
    file.write("Descriptive Statistics:\n")
    file.write(str(df.describe()))
    file.write("\n\nMissing Values:\n")
    file.write(str(missing_values))
    file.write("\n\nOutliers (values beyond 3 standard deviations):\n")
    file.write(str(outliers))
    file.write("\n\nCorrelation:\n")
    file.write(str(correlation))
    file.write("\n\nSpecies Counts:\n")
    file.write(str(species_counts))

print("Success, the file has saved down: 'summary.txt'.")

# Section 2: Data Visualisation
# Here we import libraries for data visualisation
import matplotlib.pyplot as plt
import seaborn as sns

# Section 2.1: Histograms
# For each column (excluding 'species'), a histogram is created that shows the distribution of ther values
for col in df.columns[:-1]:  
    plt.figure(figsize=(10, 6))
    sns.histplot(df, x=col, hue="species", element="step", stat="density", common_norm=False)
    plt.title(f'{col.capitalize()} Distribution')
    plt.savefig(f'{col}_distribution.png')
    plt.close()

# Section 2.2: Scatterplots
# Create a scatterplot matrix to visualise the pairwise relationships and class distributions
sns.pairplot(df, hue="species", height=3, aspect=1)
plt.savefig('scatterplot.png') 
plt.close()

# Section 2.3: Boxplots
# Create box plots for each feature to visualise the quartiles
plt.figure(figsize=(12, 8))
sns.boxplot(data=df, orient="h", palette="Set2")
plt.title('Box plot of each feature in the dataset')
plt.savefig('boxplot.png')
plt.close()

# Section 2.4: Violin Plots
# Violin plots are similar to box plots, they show the probability density of the data at different values
# For each column (excluding 'species'), a violin plot is created to show the distribution of values per species
for col in df.columns[:-1]:  
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=df, x="species", y=col)
    plt.title(f'Violin Plot of {col.capitalize()}')
    plt.savefig(f'violin_plot_{col}.png')
    plt.close()

# Section 2.5: Correlation Heatmap
# A heatmap is used to visualise the correlation matrix
# This can help to identify any relationships between different features in the dataset
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Correlation heatmap')
plt.savefig('correlation_heatmap.png')
plt.close()

# Section 2.6: Summary Visualisation
# We use a grid of subplots to display the histograms and boxplots for each feature side by side.
# This can help to get a quick overview of the data
# I was going to use this in the analysis but I have not an instead left it as a summary table for the viewer
fig, axs = plt.subplots(4, 2, figsize=(16, 24))  # Create a grid of 4 rows and 2 columns

# Iterate over each feature (column) in the DataFrame
for i, col in enumerate(df.columns[:-1]):
    # Histogram in the left column (column 0)
    sns.histplot(df, x=col, hue="species", element="step", stat="density", common_norm=False, ax=axs[i, 0])
    axs[i, 0].set_title(f'{col.capitalize()} Distribution')
    
    # Boxplot in the right column (column 1)
    sns.boxplot(data=df, y=col, x='species', ax=axs[i, 1])
    axs[i, 1].set_title(f'Box Plot of {col.capitalize()}')

# Here we adjust the layout for better visibility
plt.tight_layout()

# Save the summary figure
plt.savefig('summary_visualization.png')

# Close the fikle
plt.close()

print("Success, all visualisations have been created and saved down.")


