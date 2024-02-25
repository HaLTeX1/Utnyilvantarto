"""
Ez a program egy egyszerű gépjárműadat-nyilvántartást valósít meg.
A felhasználótól bekéri a gépjármű típusát, rendszámát és a kilóméteróra állását,
majd egy táblázatban megjeleníti ezeket az adatokat.
"""

from prettytable import PrettyTable
import shortuuid
import csv
import re
from datetime import datetime
from pdf import generate_pdf
from openstreetmap_api import distmain
def valid_rendszam(rendszam):
    rendszam_regex = re.compile(r'^[A-Z0-9]{2,}(?:-[A-Z]{2,})?(?:-[A-Z0-9]{1,})?$')    # Rendszámok formátuma: AAA-123 ,AA-BB-123
    return bool(re.match(rendszam_regex, rendszam))

table = PrettyTable()
km = 0
rendszam = []
tipus = []
uttipus = ["Magánút", "Céges", "Egyéb", "Nem ismert"]

##Inputok bekérése
azonosito = shortuuid.uuid()
tipus_adatbekeres = input("Kérlek, add meg a gépjármű típusát: ")
rendszam_bekeres = input("Kérlek, add meg a gépjármű forgalmi rendszámát: ").upper()
while not valid_rendszam(rendszam_bekeres):
    print("Hibás rendszám formátum. Kérlek, adj meg egy érvényes rendszámot!")
    rendszam_bekeres = input("Kérlek, add meg a gépjármű forgalmi rendszámát: ").upper()

km_adatbekeres = int(input("Kérlek, add meg a kilóméteróra állását: "))
formatted_km = "{:,}".format(km_adatbekeres) + " km"
uttipus_adatbekeres = input("Kérlek add meg az út tipusát az alábbiak közül: // Magánút, Céges, Egyéb, Nem ismert // => ").upper()
input_date = input("Kérlek, add meg a dátumot (ÉÉÉÉ-HH-NN formátumban): ")
try:
    date_obj = datetime.strptime(input_date, "%Y-%m-%d")
except ValueError:
    print("Hibás dátum formátum. Kérem, használja az ÉÉÉÉ-HH-NN formátumot.")
    exit()
date_wi_t = date_obj.replace(hour=0, minute=0, second=0, microsecond=0)
tipus = tipus_adatbekeres
rendszam = rendszam_bekeres
uttipus = uttipus_adatbekeres

ut_adatok = distmain()
if ut_adatok:
    origin_location, destination_location, distance = ut_adatok
table.field_names = ["Azonosító" ,"Típus", "Rendszám", "Óraállás", "Úttípus", "Kiindulás", "Végállomás" ,"Távolság","Dátum"]
table.add_row([azonosito, tipus, rendszam, formatted_km, uttipus, origin_location, destination_location,distance, date_wi_t])
print(table)
with open('gepjarmu_adatok.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    # Ellenőrizze, hogy a fejléc már létezik-e a fájlban
    if file.tell() == 0:
        writer.writerow(["Azonosító" ,"Típus", "Rendszám", "Óraállás", "Úttípus", "Kiindulás", "Végállomás" ,"Távolság","Dátum"])
    # Írja ki az új rekordot
    writer.writerow([azonosito, tipus, rendszam, formatted_km, uttipus, origin_location, destination_location,distance, date_wi_t])
    print(f"Adatok mentve!")
# PDF generálás PyMuPDF segítségével
table_data = [
    ["Azonosító", azonosito],
    ["Kiinduló település", origin_location],
    ['Végállomás', destination_location],
    ['Távolság', distance],
    ["Típus", tipus],
    ["Rendszám", rendszam],
    ["Óraállás", formatted_km],
    ["Úttípus", uttipus],
    ["Dátum", date_wi_t]]
generate_pdf(azonosito, table_data)