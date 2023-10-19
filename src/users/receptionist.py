import json
from src.shared.hash import *

# Define a relative path
configJson= "src/config.json"
dataJson = "src/data.json"


class Receptionist:

    @staticmethod
    def CreatePatientAccount():
        name = input('Patient username: ')
        temp_password = HashingPassword(input('Password: '))

        # read and write user to config file
        with open(configJson, 'r') as DataJson:
            data = json.load(DataJson)
            PatientID = len(data['users'])+1
            data['users'].append({
                'id': PatientID,
                'name': name,
                'password': temp_password,
                'user_type': "patient",
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
        with open(dataJson, 'r') as DataJson:
            data = json.load(DataJson)
            data['personal_details'].append({
                'id': PatientID,
                'name': patient_name,
                'age': age,
                'nic_no': Encode(nic_no),
                'tel': Encode(tel)
            })
        with open(dataJson, 'w') as outfile:
            json.dump(data, outfile)







