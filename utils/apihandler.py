import utils.constants as const
import base64
import requests
class ApiHandler:
    def __init__(self):
       self.api_key = const.DOCUPANDA_API_KEY
       print(type(self.api_key))

    def post_document_subset(self, fileName):
        doc_url = f"{const.DOCUPANDA_DOC_URL}"
        print(doc_url)
        payload = {"document": {"file": {
            "contents": base64.b64encode(open(fileName, 'rb').read()).decode(),
            "filename": fileName
        }},
            "pages": [3,4,5,6,7,8] #will set to pass on command line
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-Key": self.api_key
        }

        response = requests.post(doc_url, json=payload, headers=headers)
        print(response.text)
        document_id = response.json()['documentId']

        return document_id

    def post_document_all(self, fileName):
        doc_url = f"{const.DOCUPANDA_DOC_URL}"
        print (doc_url)
        payload = {"document": {"file": {
            "contents": base64.b64encode(open(fileName, 'rb').read()).decode(),
            "filename": fileName
        }}}
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-Key": self.api_key
        }
        response = requests.post(doc_url, json=payload, headers=headers)
        print(response.json())
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



