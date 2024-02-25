
# Útnyílvántartó

Ez a program egy egyszerű gépjárműadat-nyilvántartást valósít meg.
A felhasználótól bekéri a gépjármű típusát, rendszámát, kilóméteróra állását, illetve az útvonalra vonatkozó adatokat
majd egy táblázatban megjeleníti ezeket az adatokat illetve menti egy CSV fájlba és PDF kimutatást készít a különböző utakról.




## Szükséges Modulok

- [Prettytable](https://pypi.org/project/prettytable/)
- [ShortUUID](https://pypi.org/project/shortuuid/)
- [CSV](https://docs.python.org/3/library/csv.html)
- [DateTime](https://docs.python.org/3/library/datetime.html)
- [RE](https://docs.python.org/3/library/re.html)
- [PyMuPDF](https://pypi.org/project/PyMuPDF/)

## API kezelése
A program a publikusan bárki számára elérhető [OpenStreetMap](https://www.openstreetmap.org/#map=8/47.184/19.509) API segítségével kéri le az útra vonatkozó adatokat ezért külön konfigurálni már nem szükséges.

## Adatkezelés
A program rendszámokat kizárólag a jelenleg hatályos publikusan, bárki számára elérhető rendszámok közül fogad.
- AA-BB-123
- AAA-123


## Licensz

[MIT](https://choosealicense.com/licenses/mit/)


## Demonstráció

```python
Kérlek, add meg a gépjármű típusát: Mitsubishi Lancer EVO X
Kérlek, add meg a gépjármű forgalmi rendszámát: AA-BB-123
Kérlek, add meg a kilóméteróra állását: 248147
Kérlek add meg az út tipusát az alábbiak közül: // Magánút, Céges, Egyéb, Nem ismert // => Magánút
Kérlek, add meg a dátumot (ÉÉÉÉ-HH-NN formátumban): 2024-02-25
Kérem, adja meg az indulási települést: Budapest
Kérem, adja meg a céltelepülést: Pécel
Út adatai:
 
Kiinduló település: Budapest
Céltelepülés: Pécel
Távolság: 30.39 km
+------------------------+-------------------------+-----------+------------+---------+-----------+------------+----------+---------------------+
|       Azonosító        |          Típus          |  Rendszám |  Óraállás  | Úttípus | Kiindulás | Végállomás | Távolság |        Dátum        |
+------------------------+-------------------------+-----------+------------+---------+-----------+------------+----------+---------------------+
| WvKM2UqrSo3pVyNbjTdpV6 | Mitsubishi Lancer EVO X | AA-BB-123 | 248,147 km | MAGÁNÚT |  Budapest |   Pécel    |  30.39   | 2024-02-25 00:00:00 |
+------------------------+-------------------------+-----------+------------+---------+-----------+------------+----------+---------------------+
Adatok mentve!
PDF fájl létrehozva: gepjarmu_adatlap_WvKM2UqrSo3pVyNbjTdpV6.pdf

```

