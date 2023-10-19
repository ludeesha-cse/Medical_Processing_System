import json

dataJson = "src/data.json"

class Patient:

    @staticmethod
    def read_sickness_details(patient_id):

        # read sickness details from data file
        with open(dataJson, 'r') as json_data_file:
            data = json.load(json_data_file)
            details = data['sickness_details']

            for detail in details:
                if detail['id'] == patient_id:
                    print(detail['date'] + ' - ' + detail['sickness'])

    @staticmethod
    def read_drug_prescription(patient_id):

        # read drug prescription from data file
        with open(dataJson, 'r') as json_data_file:
            data = json.load(json_data_file)
            details = data['drug_presc']

            for detail in details:
                if detail['id'] == patient_id:
                    print(detail['date'] + ' - ' + detail['drug_presc'])

    @staticmethod
    def read_labtest_prescription(patient_id):

        # read lab test prescription from data file
        with open(dataJson, 'r') as json_data_file:
            data = json.load(json_data_file)
            details = data['labtest_presc']

            for detail in details:
                if detail['id'] == patient_id:
                    print(detail['date'] + ' - ' + detail['labtest_presc'])

