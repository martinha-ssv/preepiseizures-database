import os

import json

# Path to the directory containing the JSON files
directory = 'sessions'

# Define the fields to convert from text to numeric
fields_to_convert = ['no_clinical_seizures', 'no_electrographical_seizures']

# List all JSON files, excluding 'template.json'
json_files = [f for f in os.listdir(directory) if f.endswith('.json') and f != 'template.json']

# Process each JSON file
for file_name in json_files:
    file_path = os.path.join(directory, file_name)
    
    # Open and read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Convert the specified fields from string to integer
    for field in fields_to_convert:
        if field in data and field != 'nan' and field != 'NaN' and field != 'None' and field != 'nan':
            try:
                data[field] = int(data[field])
            except ValueError:
                print(f"Error converting field '{field}' in file {file_name}")
                    
        # Write the updated JSON back to the file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    print("All JSON files have been updated.")
