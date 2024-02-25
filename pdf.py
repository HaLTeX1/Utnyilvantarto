
from prettytable import PrettyTable
import shortuuid
import csv
import re
from datetime import datetime
import fitz

def generate_pdf(azonosito, table_data):
    pdf_filename = f"gepjarmu_adatlap_{azonosito}.pdf"
    existing_pdf = fitz.open()  # Új PDF létrehozása

    # Hozzáadunk egy új oldalt a PDF-hez
    page = existing_pdf.new_page(-1)

    # Táblázat adatainak elhelyezése a Page objektumon
    x_offset, y_offset = 50, 350
    line_height = 15

    for row in table_data:
        for i, cell in enumerate(row):
            page.insert_text((x_offset + i * 150, y_offset), f"{cell}", fontsize=10)

        y_offset -= line_height

    # Aláírás mező elhelyezése a jobb alsó sarokban
    signature_text = "Aláírás: ________________________"
    signature_width = 200  # Tetszőleges érték, növelheted vagy csökkentheted
    page.insert_text((page.rect.width - signature_width - 50, 50), signature_text, fontsize=10)

    # A módosított PDF fájlt mentjük
    existing_pdf.save(pdf_filename)

    print(f"PDF fájl létrehozva: {pdf_filename}")