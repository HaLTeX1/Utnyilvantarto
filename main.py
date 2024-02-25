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
km = str(km_adatbekeres) + " km"
uttipus = uttipus_adatbekeres

table.field_names = ["Azonosító","Típus", "Rendszám", "Óraállás", "Úttípus", "Dátum"]
table.add_row([azonosito, tipus, rendszam, km, uttipus,date_wi_t])
print(table)
with open('gepjarmu_adatok.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    # Ellenőrizze, hogy a fejléc már létezik-e a fájlban
    if file.tell() == 0:
        writer.writerow(["Azonosító" ,"Típus", "Rendszám", "Óraállás", "Úttípus", "Dátum"])
    # Írja ki az új rekordot
    writer.writerow([azonosito, tipus, rendszam, km, uttipus, date_wi_t])
"""
adatmegtek = input("Kívánod megtekinteni az eddigi összes adatot a fájlban? (IGEN / NEM): ").upper()
if adatmegtek == "IGEN":
    with open('gepjarmu_adatok.csv', mode='r') as file:
        reader = csv.DictReader(file)
        table = PrettyTable(field_names=reader.fieldnames)
        for row in reader:
            table.add_row(row.values())
    print(table)
"""

