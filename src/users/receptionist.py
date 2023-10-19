import json
from src.shared.hash import *

# Define a relative path
configJson= "src/config.json"
dataJson = "src/data.json"


class Receptionist:

    @staticmethod
    def create_patient_account():
        name = input('Patient username: ')
        temp_password = HashingPassword(input('Password: '))

        # read and write user to config file
        with open(configJson, 'r') as json_data_file:
            data = json.load(json_data_file)
            patient_id = len(data['users'])+1
            data['users'].append({
                'id': patient_id,
                'name': name,
                'password': temp_password,
                'user_type': "patient",
                #'privilege_level': '4'
            })
        with open(configJson, 'w') as outfile:
            json.dump(data, outfile)

        print("Account created successfully")
        print("Please enter personal details of patient")

        patient_name = input('Patient name: ')
        age = input('Age: ')
        nic_no = input('NIC number: ')
        tel = input('Telephone number: ')

        # read and write patient details to data file
        with open(dataJson, 'r') as json_data_file:
            data = json.load(json_data_file)
            data['personal_details'].append({
                'id': patient_id,
                'name': patient_name,
                'age': age,
                'nic_no': Encode(nic_no),
                'tel': Encode(tel)
            })
        with open(dataJson, 'w') as outfile:
            json.dump(data, outfile)







