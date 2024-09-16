from utils.apihandler import ApiHandler


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    api_handler = ApiHandler()
    #api_handler.post_document("/Users/catherineimes/Downloads/mskrecords.pdf")
    print(api_handler.get_standardized_output())


