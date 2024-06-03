import os
import pandas as pd
import numpy as np

filename = "works-2024-06-03T15-29-17.csv"
file = os.path.join(os.getcwd(), "data", filename)
df = pd.read_csv(file, header=0)

df_subset = df[['best_oa_location_landing_page_url', 'grants_funder_display_name', 'grants_award_id']]

file_path = 'data/file.csv'
df_subset.to_csv(file_path, index=False)

print(df_subset.head())