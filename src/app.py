from src.authentication.login import Login
from src.users.admin import Admin
from src.users.receptionist import Receptionist
from src.users.doctor import Doctor
from src.users.patient import Patient
from src.shared.Account import *
from src.shared.PatientValidity import CheckPatientValidity

def ShowSubMenu(Role,menu):
    print("To see the menu again press 0 or Press any other key to exit")
    InputOption = input()
    if InputOption == '0':
        print(menu)
        return
    else:
        print("Thank you " +Role+ " !")
        exit()

def main():

    User = Login().UserAuthentication()
    if User:
        UserID = str(User.get('id'))

        # user is admin
        if User.get('user_type') == 'admin':
            Admin().set_codes()

        # user is a receptionist
        elif User.get('user_type') == 'receptionist':
            menu = "Press 1 to create patient account\nPress 2 to edit personal account\nPress 3 to view personal account\nPress 4 to set new password\nPress -1 to exit\n"
            print(menu)
            while True:
                InputOption = input()
                if InputOption == '1':
                    Receptionist().CreatePatientAccount()
                    ShowSubMenu("receptionist",menu)
                            
                elif InputOption == '2':
                    AccountEdit(UserID)
                    ShowSubMenu("receptionist",menu)
    
                elif InputOption == '3':
                    AccountView(UserID)                  
                    ShowSubMenu("receptionist",menu)
                     
                elif InputOption == '4':
                    ChangePW(UserID)
                    ShowSubMenu("receptionist",menu)
                     
                elif InputOption == '-1':
                    print("Thank you receptionist")
                    break
                else:
                    print("Invalid input. Try again")

        # user is a doctor
        if User.get('user_type') == 'doctor':
            menu = "Press 1 to add Disease details \nPress 2 to add drug prescription \nPress 3 to add lab test prescription \nPress 4 to view Disease details \nPress 5 to view previous drug prescriptions \nPress 6 to view lab test prescription \nPress 7 to edit account \nPress 8 to renew password \nPress 9 to view account\nPress -1 to exit\n "
            print(menu)
            while True:
                InputOption = input()
                if InputOption in ['1', '2', '3', '4', '5', '6']:

                    while True:
                        patient_id = input("Enter patient id: ")
                        if CheckPatientValidity(patient_id):
                            break
                        else:
                            print("Invalid patient id")

                    if InputOption == '1':
                        Doctor().SetDiseaseDetails(patient_id)
                        ShowSubMenu("Doctor",menu)

                    elif InputOption == '2':
                        Doctor().SetPrescription(patient_id)
                        ShowSubMenu("Doctor",menu)

                    elif InputOption == '3':
                        Doctor().SetLabTest(patient_id)
                        ShowSubMenu("Doctor",menu)

                    elif InputOption == '4':
                        Doctor().GetDiseaseDetails(patient_id)
                        ShowSubMenu("Doctor",menu)

                    elif InputOption == '5':
                        Doctor().GetPrescription(patient_id)
                        ShowSubMenu("Doctor",menu)

                    elif InputOption == '6':
                        Doctor().GetLabTest(patient_id)
                        ShowSubMenu("Doctor",menu)

                elif InputOption == '7':
                    AccountEdit(UserID)
                    ShowSubMenu("Doctor",menu)
                            
                elif InputOption == '8':
                    ChangePW(UserID)
                    ShowSubMenu("Doctor",menu)
                            
                elif InputOption == '9':
                    AccountView(UserID)
                    ShowSubMenu("Doctor",menu)
                            
                elif InputOption == '-1':
                    print("Thank you doctor")
                    break
                else:
                    print("Invalid input. Try again")

        # user is a patient ; only user Privilages
        if User.get('user_type') == 'patient':
            menu = "Press 1 to change password \nPress 2 to update account \nPress 3 to view account details\nPress 4 to view sickness details \nPress 5 to view previous drug prescriptions \nPress 6 to view lab test prescription \nPress -1 to exit\n "
            print(menu)
            while True:
                InputOption = input()
                if InputOption == '1':
                    ChangePW(UserID)
                    ShowSubMenu("",menu)
                     
                elif InputOption == '2':
                    AccountEdit(UserID)
                    ShowSubMenu("",menu)
                     
                elif InputOption == '3':
                    AccountView(UserID)
                    ShowSubMenu("",menu)

                elif InputOption == '4':
                    Patient().GetDiseaseDetails(UserID)
                    ShowSubMenu("",menu)
                        
                elif InputOption == '5':
                    Patient().GetPrescription(UserID)
                    ShowSubMenu("",menu)
                        
                elif InputOption == '6':
                    Patient().GetLabTest(UserID)
                    ShowSubMenu("",menu)
                        
                elif InputOption == '-1':
                    print("Thank you")
                    break
                else:
                    print("Invalid input. Try again")






