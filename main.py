"""
Ez a program egy egyszerű gépjárműadat-nyilvántartást valósít meg.
A felhasználótól bekéri a gépjármű típusát, rendszámát és a kilóméteróra állását,
majd egy táblázatban megjeleníti ezeket az adatokat.
"""

from prettytable import PrettyTable
import csv

table = PrettyTable()
km = 0
rendszam = []
tipus = []
uttipus = ["Magánút", "Céges", "Egyéb", "Nem ismert"]

##Inputok bekérése
tipus_adatbekeres = input("Kérlek, add meg a gépjármű típusát: ")
rendszam_bekeres = input("Kérlek, add meg a gépjármű rendszámát: ").upper()
km_adatbekeres = input("Kérlek, add meg a kilóméteróra állását: ")
uttipus_adatbekeres = input("Kérlek add meg az út tipusát az alábbiak közül: // Magánút, Céges, Egyéb, Nem ismert // => ")

tipus = tipus_adatbekeres
rendszam = rendszam_bekeres
km = km_adatbekeres + " km"
uttipus = uttipus_adatbekeres



table.field_names = ["Típus", "Rendszám", "Óraállás", "Úttípus"]
table.add_row([tipus, rendszam, km, uttipus])
print(table)
with open('gepjarmu_adatok.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    # Ellenőrizze, hogy a fejléc már létezik-e a fájlban
    if file.tell() == 0:
        writer.writerow(["Típus", "Rendszám", "Óraállás", "Úttípus"])
    # Írja ki az új rekordot
    writer.writerow([tipus, rendszam, km, uttipus])
