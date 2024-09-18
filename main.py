#This is a starter program to upload documents to docupanda and retrieve them after processing.
#This pilot will also contain storage of the results in a localdb to start
#For more information on docupanda please visit https://www.docupanda.io/

from utils.apihandler import ApiHandler

if __name__ == '__main__':
    api_handler = ApiHandler()
    #api_handler.post_document(pass the path to your document here)

    print(api_handler.get_standardized_output().text)
    print(api_handler.get_full_ouptut("fb838180").text)


