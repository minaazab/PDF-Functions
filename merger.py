from PyPDF2 import PdfReader, PdfWriter

pdf_writer = PdfWriter()

# Add PDFs to merge
for pdf_file in ['MINA AZAB - Resume.pdf', 'printTranscript.pdf']:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        pdf_writer.add_page(page)

with open('merged.pdf', 'wb') as output_file:
    pdf_writer.write(output_file)