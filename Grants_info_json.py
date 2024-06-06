import json

filename = input("Please enter the JSON file name(with .json extension);")

with open(filename, 'r') as json_file:
    data  = json.load(json_file)

extracted_data = []

for result in data['results']:
    doi = result.get('doi', '')

    authorships = []
    for author in result.get('authorships', []):
        author_info = {
            'author_position': author.get('author_position', ''),
            'display_name': author.get('author', {}).get('display_name', ''),
            'orcid': author.get('author', {}).get('orcid', '')
        }
        authorships.append(author_info)
    
    primary_topic = result.get('primary_topic', {}).get('display_name', '')

    grants = []
    for grant in result.get('grants', []):
        grant_info = {
            'funder_display_name': grant.get('funder_display_name', ''),
            'award_id': grant.get('award_id', '')
        }
        grants.append(grant_info)

    extracted_data.append({
        'doi': doi,
        'authorships': authorships,
        'primary_topic': primary_topic,
        'grants': grants
    })

output_file_name = 'output.json'


with open(output_file_name, 'w') as json_output_file:
    json.dump(extracted_data, json_output_file, indent=4)