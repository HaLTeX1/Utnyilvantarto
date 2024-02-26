import os
from prettytable import PrettyTable
import shortuuid
import csv
import re
from datetime import datetime
import fitz

def generate_pdf(azonosito, table_data):
    # Azonosító generálási dátum létrehozása
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Mappa nevének és útvonalnak létrehozása a Data mappán belül
    data_folder = "Data"
    folder_name = f"route_maps_{timestamp}"
    os.makedirs(os.path.join(data_folder, folder_name), exist_ok=True)

    pdf_filename = os.path.join(data_folder, folder_name, f"gepjarmu_adatlap_{azonosito}_{timestamp}.pdf")
    existing_pdf = fitz.open()

    pdf_page = existing_pdf.new_page(-1)

    x_offset, y_offset = 50, 350
    line_height = 15

    # pdf_page.insert_text((x_offset, y_offset + line_height), "Gépjármű Adatlap", fontsize=14, fontname="helvetica-bold", color=(0, 0, 0))
    title_text = "Gépjármű Adatlap"
    pdf_page.insert_text((pdf_page.rect.width // 2 - len(title_text) * 3, pdf_page.rect.height - 30), title_text.encode("utf-8"), fontsize=16, fontname="helvetica-bold", color=(0, 0, 0))
    for row in table_data:
        for i, cell in enumerate(row):
            pdf_page.insert_text((x_offset + i * 150, y_offset), f"{cell}", fontsize=12, color=(0, 0, 0))

        y_offset -= line_height

    date_stamp = datetime.now().strftime("Dátum: %Y-%m-%d %H:%M:%S")
    pdf_page.insert_text((x_offset, 30), date_stamp, fontsize=10, color=(0, 0, 0))

    page_number_text = f"Page 1 of {existing_pdf.page_count}"
    pdf_page.insert_text((pdf_page.rect.width - 100, 20), page_number_text, fontsize=10, color=(0, 0, 0))

    existing_pdf.save(pdf_filename)

    print(f"PDF fájl létrehozva: {pdf_filename}")
