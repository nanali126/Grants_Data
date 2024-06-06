import json
import xml.etree.ElementTree as ET

def extract_information(data):
    extracted_data = []
    
    for result in data.get('results', []):
        
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
            'authorships': authorships,
            'primary_topic': primary_topic,
            'grants': grants
        })
    
    return extracted_data

def dict_to_xml(data):
    root = ET.Element("grant")
    
    for item in data:
        result_elem = ET.SubElement(root, "grants")
        
        authorships_elem = ET.SubElement(result_elem, "authorships")
        for author in item['authorships']:
            author_elem = ET.SubElement(authorships_elem, "author")
            
            author_position_elem = ET.SubElement(author_elem, "author_position")
            author_position_elem.text = author['author_position']
            
            author_display_name_elem = ET.SubElement(author_elem, "display_name")
            author_display_name_elem.text = author['display_name']
            
            orcid_elem = ET.SubElement(author_elem, "orcid")
            orcid_elem.text = author['orcid']
        
        primary_topic_elem = ET.SubElement(result_elem, "primary_topic")
        primary_topic_elem.text = item['primary_topic']
        
        grants_elem = ET.SubElement(result_elem, "grants")
        for grant in item['grants']:
            grant_elem = ET.SubElement(grants_elem, "grant")
            
            funder_display_name_elem = ET.SubElement(grant_elem, "funder_display_name")
            funder_display_name_elem.text = grant['funder_display_name']
            
            award_id_elem = ET.SubElement(grant_elem, "award_id")
            award_id_elem.text = grant['award_id']
    
    return ET.ElementTree(root)


input_file_name = input("Please enter the input JSON file name (with .json extension): ")

with open(input_file_name, 'r') as json_file:
    data = json.load(json_file)

extracted_data = extract_information(data)

xml_tree = dict_to_xml(extracted_data)

output_file_name = "output.xml"

xml_tree.write(output_file_name, encoding='utf-8', xml_declaration=True)

