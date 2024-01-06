from pdfreader import PDFDocument
import os
totalPages = 0

for i in os.listdir(path='./input'):
    fd = open('./input/'+i, "rb")
    if i[-4:] == ".pdf":
        try:
            doc = PDFDocument(fd)
        except TypeError:
            print("File", i, "is corrupted")
            exit()
        current_pages = [p for p in doc.pages()]
        totalPages += len(current_pages)
        print("Pages for \"" + i + "\":", len(current_pages))
    else:
        print("There is at least one file that isn't a .pdf file.")

print("Total pages:", totalPages)