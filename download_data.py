import pandas as pd
import requests

# URL of the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Send a HTTP request to the URL
response = requests.get(url)

# Save the content of the response to a file
with open('iris.data', 'w') as file:
    file.write(response.text)

# Load the dataset into pandas DataFrame
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv('iris.data', names=column_names)

# Display the first 5 rows of the DataFrame
print(df.head())
