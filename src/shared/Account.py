import json
from src.shared.hash import *

# Define a relative path
configJson = "src/config.json"
dataJson = "src/data.json"

def AccountEdit(user_id):  #AccountEdit
    UpdatedName = input('Enter new name: ')
    UpdatedAge = input('Enter new age: ')
    UpdatedTel = input('Enter new telephone number: ')

    # read and write new account details to data file
    with open(dataJson, 'r') as data_file:
        f_data = json.load(data_file)
        details = f_data['personal_details']
        i = 0  # Initialize the loop variable
        while i < len(details):
            if user_id == str(details[i]['id']):
                details[i]['name'] = UpdatedName
                details[i]['age'] = UpdatedAge
                details[i]['tel'] = Encode(UpdatedTel)
                break 
            i += 1 


    with open(dataJson, 'w') as f_outfile:
        json.dump(f_data, f_outfile)

    print("Account updated successfully")


def AccountView(user_id):
    # read account details from data file
    with open(dataJson, 'r') as data_file:
        f_data = json.load(data_file)
        details = f_data['personal_details']
        i = 0  # Initialize the loop variable
        while i < len(details):
            if user_id == str(details[i]['id']):
                print("Account name: " + details[i]['name'])
                print("Age: " + details[i]['age'])
                print("NIC number: " + Decode(details[i]['nic_no']))
                print("Telephone: " + Decode(details[i]['tel']))
                break
            i += 1  # Increment the loop variable

#changing the password
def ChangePW(user_id):
    NewPW = input('Enter a password including an upper-case letter, lower-case letter, a digit and length not less than 6: \n')
    while True:
        if not (any(x.isupper() for x in NewPW) and any(x.islower() for x in NewPW) and any(x.isdigit() for x in NewPW) and len(NewPW) >= 6):
            NewPW = input("Password is too weak. Please re-enter: ")
        else:
            break
    HashedNewPW = HashingPassword(NewPW)

    with open(configJson, 'r') as data_file:
        f_data = json.load(data_file)
        account = f_data['users']
        for i in range(len(account)):
            if user_id == str(account[i]['id']):
                account[i]['password'] = HashedNewPW

    with open(configJson, 'w') as f_outfile:
        json.dump(f_data, f_outfile)
    print("Password updated successfully")





