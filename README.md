This is a pilot to evaluate docupanda.  I'll update this readme as I perform more code updates.  So far, I'm impressed with the API documentation help on their site and it's been pretty painless to use.

For more information on Docupanda visit docupanda.io.

The code aims to take medical records (PDFs) and upload them.  Right now I'm passing them in the code but will be making updates to read them from a directory.

Docupanda will likely convert the PDFs to images and then use OCR(maybe something like Tesseract) then applies some labeling or classification.  

There is also the ability to apply a basic schema to the document, and then get a standardized version (without all of bounding box information). 

Plan is to use pytesseract to do some preprocessing to evaluate documents to send to Docupanda and learn more about it's features including advanced schemas and get an estimate for credit usage for our use cases.

