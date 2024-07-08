import pandas as pd

# URL of the raw Excel file on GitHub
url ='https://github.com/R-SKumar/BIDashboard/raw/main/InputData/Walmart.csv'

# Read the csv file into a pandas DataFrame
df = pd.read_csv(url)

# Display the rows of the DataFrame
print(df)