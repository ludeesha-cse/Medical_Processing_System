import json
from src.shared.hash import *

#relative path for json files
configJson="src/config.json"
dataJson = "src/data.json"

class SignUp:
    roles = {'1': "doctor", '2': "receptionist"}

    def UserCreate(self):

        name = input('Username:')
        password = input('Enter a password including an upper-case letter, lower-case letter, a digit and length not less than 6: \n')
        while True:
            if not (any(x.isupper() for x in password) and any(x.islower() for x in password) and any(x.isdigit() for x in password) and len(password) >= 6):
                password = input("Password is too weak. Please re-enter: ")
            else:
                break
        safe_password = HashingPassword(password)

        # read config file for doctor and receptionist codes
        with open(configJson, 'r') as json_data_file:
            data = json.load(json_data_file)
            doc_code = data['codes'].get('doctor')
            rec_code = data['codes'].get('receptionist')

        # hotel staff accounts can only be created by using the relevant code for security
        while True:

            InputOption = input('Press 1 for "doctor account" or 2 for "receptionist account": ')
            
            # if doctor
            if InputOption == '1':
                code = HashingPassword(input("Please enter the doctor code to create account: "))
                if code == doc_code:
                    user_type = self.roles.get('1')
                    break
                else:
                    print("Invalid code")

            # if receptionist
            elif InputOption == '2':
                code = HashingPassword(input("Please enter the receptionist code to create account: "))
                if code == rec_code:
                    user_type = self.roles.get('2')
                    break
                else:
                    print("Invalid code")
            else:
                print("Invalid input. Try again")

        # read and write user to config file
        with open(configJson, 'r') as json_data_file:
            data = json.load(json_data_file)
            user_id = len(data['users'])+1
            data['users'].append({
                'id': user_id,
                'name': name,
                'password': safe_password, # safe_password is the hashed password
                'user_type': user_type,
            })
        with open(configJson, 'w') as outfile:
            json.dump(data, outfile)

        print("Account created successfully")

        # fill account details
        print("Fill in personal account details")
        acc_name = input('Your name: ')
        age = input('Age: ')
        nic_no = input('NIC number: ')
        tel = input('Telephone number: ')

        # write account details to data file
        with open(dataJson, 'r') as json_data_file:
            data = json.load(json_data_file)
            data['personal_details'].append({
                'id': user_id,
                'name': acc_name,
                'age': age,
                'nic_no': Encode(nic_no),
                'tel': Encode(tel)
            })
        with open(dataJson, 'w') as outfile:
            json.dump(data, outfile)

        print("Account completed")


