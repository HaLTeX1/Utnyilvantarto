from prettytable import PrettyTable
import shortuuid
import csv
import re
from datetime import datetime
import fitz

def generate_pdf(azonosito, table_data):
    pdf_filename = f"gepjarmu_adatlap_{azonosito}.pdf"
    existing_pdf = fitz.open()

    pdf_page = existing_pdf.new_page(-1)

    x_offset, y_offset = 50, 350
    line_height = 15

   # pdf_page.insert_text((x_offset, y_offset + line_height), "Gépjármű Adatlap", fontsize=14, fontname="helvetica-bold", color=(0, 0, 0))
    # Title at the top of the page
    title_text = "Gépjármű Adatlap"
    pdf_page.insert_text((pdf_page.rect.width // 2 - len(title_text) * 3, pdf_page.rect.height - 30), title_text.encode("utf-8"), fontsize=16, fontname="helvetica-bold", color=(0, 0, 0))
    for row in table_data:
        for i, cell in enumerate(row):
            pdf_page.insert_text((x_offset + i * 150, y_offset), f"{cell}", fontsize=12, color=(0, 0, 0))

        y_offset -= line_height


    # Date stamp in the bottom-left corner
    date_stamp = datetime.now().strftime("Dátum: %Y-%m-%d %H:%M:%S")
    pdf_page.insert_text((x_offset, 30), date_stamp, fontsize=10, color=(0, 0, 0))


    # Adding a footer with page number
    page_number_text = f"Page 1 of {existing_pdf.page_count}"
    pdf_page.insert_text((pdf_page.rect.width - 100, 20), page_number_text, fontsize=10, color=(0, 0, 0))

    existing_pdf.save(pdf_filename)

    print(f"PDF file created: {pdf_filename}")

# The rest of your code remains the same
