import requests
import json
#Brandeis institution id: i6902469

#this url is for Brandeis 2024
#api for get only 2024 grants: https://api.openalex.org/works?filter=institutions.id:https://openalex.org/I6902469,publication_year:2024&sort=publication_date:desc
api_url = 'https://api.openalex.org/works?filter=institutions.id:https://openalex.org/I6902469'  #API URL

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    
    file_name = input("Please enter the file name (with .json extension): ")

    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4) 
    
else:
    print(f"Failed to fetch data from API. Status code: {response.status_code}")