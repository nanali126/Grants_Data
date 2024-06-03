import os
import pandas as pd
import numpy as np

filename = file_name = input("Please enter the file name (with .csv extension): ")
file = os.path.join(os.getcwd(), "data", filename)
df = pd.read_csv(file, header=0)

df_subset = df[['best_oa_location_landing_page_url', 'grants_funder_display_name', 'grants_award_id']]

file_path = 'data/file.csv'
df_subset.to_csv(file_path, index=False)

print(df_subset.head())