import json
from datetime import datetime

dataJson = "src/data.json"


class Doctor:

    @staticmethod
    def SetDiseaseDetails(patient_id):

        Details = input("Enter sickness details: \n")

        # write Details to data file
        with open(dataJson, 'r') as json_data_file:
            data = json.load(json_data_file)
            data['sickness_details'].append({
                'id': patient_id,
                'sickness': Details,
                'date': str(datetime.now())[0:19],
            })
        with open(dataJson, 'w') as outfile:
            json.dump(data, outfile)

        print("Sickness details added")

    @staticmethod
    def SetPrescription(patient_id):

        Prescriptions = input("Enter drug prescription: \n")

        # write Prescription to data file
        with open(dataJson, 'r') as json_data_file:
            data = json.load(json_data_file)
            data['drug_presc'].append({
                'id': patient_id,
                'drug_presc': Prescriptions,
                'date': str(datetime.now())[0:19],
            })
        with open(dataJson, 'w') as outfile:
            json.dump(data, outfile)

        print("Drug prescription details added")

    @staticmethod
    def SetLabTest(patient_id):

        LabTest = input("Enter lab test prescription: \n")

        # write lab test prescription to data file
        with open(dataJson, 'r') as json_data_file:
            data = json.load(json_data_file)
            data['labtest_presc'].append({
                'id': patient_id,
                'labtest_presc': LabTest,
                'date': str(datetime.now())[0:19],
            })
        with open(dataJson, 'w') as outfile:
            json.dump(data, outfile)

        print("Lab test prescription details added")

    @staticmethod
    def GetDiseaseDetails(patient_id):

        # read sickness details from data file
        with open(dataJson, 'r') as json_data_file:
            data = json.load(json_data_file)
            details = data['sickness_details']

            for detail in details:
                if detail['id'] == patient_id:
                    print(detail['date'] + ' - ' + detail['sickness'])

    @staticmethod
    def GetPrescription(patient_id):

        # read drug prescription from data file
        with open(dataJson, 'r') as json_data_file:
            data = json.load(json_data_file)
            details = data['drug_presc']

            for detail in details:
                if detail['id'] == patient_id:
                    print(detail['date'] + ' - ' + detail['drug_presc'])

    @staticmethod
    def GetLabTest(patient_id):

        # read lab test prescription from data file
        with open(dataJson, 'r') as json_data_file:
            data = json.load(json_data_file)
            details = data['labtest_presc']

            for detail in details:
                if detail['id'] == patient_id:
                    print(detail['date'] + ' - ' + detail['labtest_presc'])

