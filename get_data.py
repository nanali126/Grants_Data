import requests
import json
#Brandeis institution id: i6902469

#this url is for Brandeis 2024
#api for get only 2024 grants: https://api.openalex.org/works?filter=institutions.id:https://openalex.org/I6902469,publication_year:2024&sort=publication_date:desc
base_url = 'https://api.openalex.org/works?filter=institutions.id:https://openalex.org/I6902469,publication_year:{year}&sort=publication_date:desc'

all_results = []

for year in range(2014, 2025):
    api_url = base_url.format(year=year)
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        all_results.extend(data.get('results', []))
        print(f"Successfully fetched data for {year}")
    else:
        print(f"Failed to fetch data for {year}. Status code: {response.status_code}")

file_name = input("Please enter the output file name (with .json extension): ")

with open(file_name, 'w') as json_file:
    json.dump(all_results, json_file, indent=4)

