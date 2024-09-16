#This is a starter program to upload documents to docupanda and retrieve them after processing.
#This pilot will also contain storage of the results in a localdb to start
#For more information on docupanda please visit https://www.docupanda.io/

from utils.apihandler import ApiHandler


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    api_handler = ApiHandler()
    #api_handler.post_document(pass your document here)

    print(api_handler.get_standardized_output())


