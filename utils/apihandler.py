import utils.constants as const
import base64
import requests
class ApiHandler:
    def __init__(self):
       self.api_key = const.DOCUPANDA_API_KEY

    def post_document(self, fileName):
        doc_url = f"{const.DOCUPANDA_DOC_URL}{fileName}"
        payload = {"document": {"file": {
            "contents": base64.b64encode(open(fileName, 'rb').read()).decode(),
            "filename": fileName
        }},
            "pages": [2, 3, 4, 5, 6] #will set to pass on command line
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-Key": self.api_key
        }
        response = requests.post(doc_url, json=payload, headers=headers)
        document_id = response.json()['documentId']

        return document_id

    def get_full_ouptut(self, document_id):
        url = f"{const.DOCUPANDA_DOC_URL}{document_id}"
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-Key": self.api_key
        }
        response = requests.get(url,headers=headers)
        return response


    def get_standardized_output(self):
        std_url = f"{const.DOCUPANDA_STD_URL}"
        print(std_url)
        headers = {"accept": "application/json",
                   "X-API-KEY": self.api_key}

        response = requests.get(std_url, headers=headers)
        return response



