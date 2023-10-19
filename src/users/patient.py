import json

dataJson = "src/data.json"

class Patient:

    @staticmethod
    def GetDiseaseDetails(PatientID):

        # read disease details from data file
        with open(dataJson, 'r') as json_data_file:
            data = json.load(json_data_file)
            details = data['sickness_details']

            for detail in details:
                if detail['id'] == PatientID:
                    print(detail['date'] + ' - ' + detail['sickness'])

    @staticmethod
    def GetPrescription(PatientID):

        # read prescription from data file
        with open(dataJson, 'r') as json_data_file:
            data = json.load(json_data_file)
            details = data['drug_presc']

            for detail in details:
                if detail['id'] == PatientID:
                    print(detail['date'] + ' - ' + detail['drug_presc'])

    @staticmethod
    def GetLabTest(PatientID):

        # read lab test from data file
        with open(dataJson, 'r') as json_data_file:
            data = json.load(json_data_file)
            details = data['labtest_presc']

            for detail in details:
                if detail['id'] == PatientID:
                    print(detail['date'] + ' - ' + detail['labtest_presc'])

