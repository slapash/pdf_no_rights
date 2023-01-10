from PyPDF2 import PdfReader, PdfWriter
import os

path = os.getcwd()

def pdf_encrypt(file):
    reader = PdfReader(file)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(user_password="HCA",owner_password="HCA_2023", permissions_flag=-3904)
    with open("crypté_" + file_name(file) + ".pdf", "wb") as f:
        writer.write(f)

def file_name(file):
    return os.path.splitext(file)[0]

def get_files_list(path):
    files_list = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            if file.endswith(".pdf"):
                files_list.append(file)
    return files_list


for elem in get_files_list(path):
    pdf_encrypt(elem)