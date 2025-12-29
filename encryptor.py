from PyPDF2 import PdfReader, PdfWriter


pdf_writer = PdfWriter()
writer = PdfWriter()

# saving the pdf that needs encryption


# opens 
with open("merged.pdf", "rb") as enc:
    reader = PdfReader(enc)
    for page in reader.pages:
        writer.add_page(page)

writer.encrypt("1223")

with open("encrypted.pdf", "wb") as output_file2:
    writer.write(output_file2)