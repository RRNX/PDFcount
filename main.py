from pypdf import PdfReader
from pypdf import errors
#import pypdf
import os
totalPages = 0
input = str(input("Path to files: "))

for i in os.listdir(path=input):
    try:
        doc = PdfReader(input+'/'+i)
    except (errors.EmptyFileError, errors.PdfStreamError) as error:
        print(i + " has a wrong format. Skipping.")
        break
    current_pages = len(doc.pages)
    totalPages += current_pages
    print("Pages for \"" + i + "\":", current_pages)
print("Total pages:", totalPages)