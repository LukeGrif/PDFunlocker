from PyPDF2 import PdfReader, PdfWriter
# pip install PyPDF2
# pip install PyCryptodome

# Specify the input PDF and output PDF file names
input_pdf_path = r"C:\Users\Lenovo\Downloads\WeightedWeakLinear.2up.pdf" # Location of the Password Protected PDF
output_pdf_path = r"unlockedfile.pdf"
password = "ce4041"

# Open the encrypted PDF
reader = PdfReader(input_pdf_path)
if reader.is_encrypted:
    reader.decrypt(password)  # Decrypt the file with the password

# Create a new PDF writer and add the pages from the unlocked reader
writer = PdfWriter()
for page_num in range(len(reader.pages)):
    writer.add_page(reader.pages[page_num])

# Write the decrypted pages to a new file
with open(output_pdf_path, "wb") as output_pdf:
    writer.write(output_pdf)

print(f"Unlocked PDF saved as: {output_pdf_path}")
