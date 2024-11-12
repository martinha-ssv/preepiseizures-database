import hashlib
from termcolor import colored
import json

# Define directories
patients = '../db_files/patients/'

# Define data fields
manual_fields = ['age',
'gender',
'commorbidities',
'diagnosis',
'aura',
'medication']

sub_manual_fields = { 'diagnosis' : ['type', 'region'],
		      'region' : ['lobe', 'side'],
		      'medication' : ['name', 'dose_mg', 'freq_day'] }

auto_fields = ['sha_id',
'sessions',
'records',
'events']

# Form logic
'''Returns True when the field in question has sub-fields'''
def sub_field_check(field_name) -> bool: 
	return field_name in sub_manual_fields.keys()

'''Logic to prompt a field for input'''
def prompt_field(field_name):
	if sub_field_check(field_name):
		print('Filling field', colored(field_name, 'blue'))
		return prompt_sub_fields(field_name)
	else:
		count = 0
		vals = []
		val = ''
		while val != '.':
			count += 1
			print('Please insert value of', colored(field_name, 'blue'), f'#{count}\nENTER for next value; . + ENTER to indicate end of field.')
			print('> ', end='')
			val = input()
			vals += val
		if count == 2:
			return {field_name: vals[0]}
		elif count > 2:
			return {field_name: vals[:-1]}
   
def read_data():
	json_data = {}
	for field in manual_fields:
		json_data.update(prompt_field(field))
	return json_data

def write_data_to_json(json_data):
	with open(patients + json_data['sha_id'] + '.json', 'a') as f:
		json.dump(json_data, f)
	
def prompt_sub_fields(field_name):
	res = {}
	for field in sub_manual_fields[field_name]:
		res.update(prompt_field(field))
	return res

def generate_sha_id(data):
	full_name = input('Insert the patient\'s full name\n> ')
	real_age = input('Insert the patient\'s real age \n> ')
	data['sha_id'] = hashlib.sha256((full_name.upper() + '-' + str(real_age)).encode()).hexdigest()

	
# Form code
print('Creating JSON file for patient metadata.')
data = read_data()
generate_sha_id(data)
write_data_to_json(data)



