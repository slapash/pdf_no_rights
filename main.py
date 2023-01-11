from PyPDF2 import PdfReader, PdfWriter
import os
from excel_converter import convert_to_pdf as ctp
path = os.getcwd()

def pdf_encrypt(file):
    reader = PdfReader(file)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(user_pwd="",owner_pwd="HCA_2023", permissions_flag= -3904)
    with open("crypté_" + file_name(file) + ".pdf", "wb") as f:
        writer.write(f)

def file_name(file):
    return os.path.splitext(file)[0]

def get_files_list(path, **kwargs):
    files_list = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            if file.endswith(kwargs.get("extension", ".pdf")):
                files_list.append(file)
    return files_list

for elem in get_files_list(path, extension=".xlsx"):
    ctp(path + "\\" + elem)


for elem in get_files_list(path, extension=".pdf"):
    pdf_encrypt(elem)