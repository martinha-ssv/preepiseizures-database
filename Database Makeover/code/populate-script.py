import pandas as pd
import os

# Path to the directory containing the JSON files and the Excel file
directory = 'sessions'
excel_file = '~/Documents/Universidade/Projetos/ScientISST/Epilepsy/Original Metadata/PreEpiSeizuresMetadata.xlsx'

# Read the Excel data
data = pd.read_excel(excel_file)

# Define the mapping from Excel columns to JSON fields
mappings = {
    'ID': 'patientID',
    'Number Clinical Seizures': 'no_clinical_seizures',
    'Number Electrographic Seizures': 'no_electrographical_seizures',
    'Main Lobe': 'main_lobe',
    'Interictal Activity': 'interictal_activity'
}

# List all JSON files, excluding 'template.json'
json_files = [f for f in os.listdir(directory) if f.endswith('.json') and f != 'template.json' and f != 'BBYZ.json']

# Process each JSON file
for file_name in json_files:
    file_path = os.path.join(directory, file_name)
    
    # Read the contents of the JSON file
    with open(file_path, 'r') as file:
        contents = file.read()
    
    # Find the ID from the filename (assuming ID is the filename without extension)
    patient_id = file_name.split('.')[0]
    
    # Find the corresponding row in the Excel file
    row = data[data['ID'] == patient_id]
    
    if not row.empty:
        # Replace the placeholder text in the file contents
        for key, json_field in mappings.items():
            value = row[key].values[0]
            # Building the line to search for and the replacement line
            search_pattern = f'"{json_field}":'
            replacement_line = f'"{json_field}": "{value}",'
            contents = contents.replace(search_pattern, replacement_line)
    
    # Save the modified contents back to the file
    with open(file_path, 'w') as file:
        file.write(contents)

print("JSON files have been updated.")