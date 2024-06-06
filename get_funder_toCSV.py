import json
import pandas as pd

input_file_name = input("Please enter the input JSON file name (with .json extension and relative path): ")

with open(input_file_name, 'r') as json_file:
    data = json.load(json_file)

funder_data = []

for item in data:
    for grant in item.get('grants', []):
        funder_info = {
            'funder_display_name': grant.get('funder_display_name', '')
        }
        funder_data.append(funder_info)

df = pd.DataFrame(funder_data)
print(df.shape)

column_name = 'funder_display_name'
n = 20
frequency_count = df[column_name].value_counts()[:n].index.tolist()
frequency_df = pd.DataFrame(frequency_count, columns=['Funder_display_name'])

output_file_name = 'top20_funder_info.csv'
frequency_df.to_csv(output_file_name, index=False)
print(f"Funder information has been successfully written to {output_file_name}")

print(frequency_count)

