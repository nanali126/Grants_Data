import pandas as pd
import os

filename = file_name = input("Please enter the file name (with .csv extension): ")
file = os.path.join(os.getcwd(), "data", filename)
df = pd.read_csv(file, header=0)

print("Columns in the DataFrame:", df.columns.tolist())

column_name = 'funder_display_name'
n = 5
frequency_count = df[column_name].value_counts()[:n].index.tolist()

print(frequency_count)