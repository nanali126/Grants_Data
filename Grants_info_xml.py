import json
import xml.etree.ElementTree as ET
import xml.dom.minidom
import pandas as pd

def extract_information(data, df_funders):
    extracted_data = []
    df_funders['Funder_display_name'] = df_funders['Funder_display_name'].astype(str)
    df_funders['funder-code'] = df_funders['funder-code'].astype(str)   
    valid_funders = set(df_funders['Funder_display_name'].dropna().tolist())

    for result in data.get('results', []):
        grants = []
        for grant in result.get('grants', []):
            funder_display_name = grant.get('funder_display_name', '')
            if funder_display_name in valid_funders:
                i = df_funders[df_funders['Funder_display_name']==funder_display_name].index.item()
                funder_code = df_funders['funder-code'][i]
                award_id = grant.get('award_id', '')
                if funder_code != None and award_id != None and funder_code != 'nan':
                    grant_info = {
                        'funder_display_name': funder_display_name,
                        'award_id': grant.get('award_id', ''),
                        'funder_code': funder_code
                    }
                    grants.append(grant_info)
        if grants: 
            extracted_data.append({
                'grants': grants
            })
    
    return extracted_data

def dict_to_xml(data):
    root = ET.Element("grants")
    
    for item in data:
        for grant in item['grants']:
            grant_elem = ET.SubElement(root, "grant")
            
            funder_display_name_elem = ET.SubElement(grant_elem, "funderAgency")
            funder_display_name_elem.text = grant['funder_display_name']
            
            award_id_elem = ET.SubElement(grant_elem, 'grantId')
            award_id_elem.text = grant['award_id']
            
            funder_code_elem = ET.SubElement(grant_elem, 'funderCode')
            funder_code_elem.text = grant['funder_code']
    
    return ET.ElementTree(root)

def pretty_print_xml(xml_tree):
    xml_str = ET.tostring(xml_tree.getroot(), 'utf-8')
    parsed_str = xml.dom.minidom.parseString(xml_str)
    return parsed_str.toprettyxml(indent="  ")

input_file_name = input("Please enter the input JSON file name (with .json extension): ")

with open(input_file_name, 'r') as json_file:
    data = json.load(json_file)

csv_file_name = 'top20_funder_info.csv'

try:
    df_funders = pd.read_csv(csv_file_name)
except FileNotFoundError:
    print(f"CSV file {csv_file_name} not found.")
    exit()

extracted_data = extract_information(data, df_funders)

xml_tree = dict_to_xml(extracted_data)

output_file_name = "output.xml"

pretty_xml_str = pretty_print_xml(xml_tree)

with open(output_file_name, 'w', encoding='utf-8') as output_file:
    output_file.write(pretty_xml_str)

print(f"Extracted data has been successfully written to {output_file_name}")
