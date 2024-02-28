
# Útnyílvántartó

Ez a program egy egyszerű gépjárműadat-nyilvántartást valósít meg.
A felhasználótól bekéri a gépjármű típusát, rendszámát, kilóméteróra állását, illetve az útvonalra vonatkozó adatokat
majd egy táblázatban megjeleníti ezeket az adatokat illetve menti egy CSV fájlba és PDF kimutatást készít a különböző utakról.


## Szükséges Modulok

- [Prettytable](https://pypi.org/project/prettytable/)
- [Requests](https://pypi.org/project/requests/)
- [ShortUUID](https://pypi.org/project/shortuuid/)
- [CSV](https://docs.python.org/3/library/csv.html)
- [DateTime](https://docs.python.org/3/library/datetime.html)
- [RE](https://docs.python.org/3/library/re.html)
- [PyMuPDF](https://pypi.org/project/PyMuPDF/)
- [Folium](https://pypi.org/project/folium/)
- [OS](https://docs.python.org/3/library/os.html)

## API kezelése
A program a publikusan bárki számára elérhető [OpenStreetMap](https://www.openstreetmap.org/#map=8/47.184/19.509) API segítségével kéri le az útra vonatkozó adatokat ezért külön konfigurálni már nem szükséges.
Az API a megadott két település ( *Kiindulás - Végállomás* ) koordinátái alapján kalkulálja ki a távolságot kilóméterben két tizedesjegyre kerekítve.
A kiinduló illetve végállomásnál **pontos cím is megadható**, nem csak település. Ebben az esetben a program pontosabban számítja ki a távolságot. 

## Adatkezelés
A program rendszámokat kizárólag a jelenleg hatályos publikusan, bárki számára elérhető rendszámok közül fogad.
- AA-BB-123
- AAA-123

A program minden adatbevitelhez egy egyedi azonosítót generál amellyel a generált PDF-et elnevezi illetve ennek megfelelően beilleszti a CSV állományba.
Az óraállást **kizárólag számokkal szükséges megadni**, a program automatikusan tagolja ezres nagyságrendben.

Az állományok generálásakor a **Data** mappán belül hoz létre minden lekérdezéshez egy mappát amiben tárolja a létrehozott fájlokat.  A mappastruktúra: Data/route_maps_{timestamp} 
Legenerálja a PDF kimutatást az utazásról illetve a HTML grafikus térképet az útvonalról. A CSV állományt *gepjarmu_adatok.csv* a Data mappába helyezi közvetlenül és ezt az állományt bővíti az újonnan bevitt adatokkal.

## Állományok
A **pdf.py** Állományban teljes mértékben testreszabható a PDF fájl generálása a PyMuPDF könyvtár segítségével.
Az OpenStreetMap HTML állománygenerálása illetve az API egyéb funkció az **openstreetmap_api.py** állományban módosíthatóak.

## Demonstráció

```text
Kérlek, add meg a gépjármű típusát: Opel Astra F 1.4 8V
Kérlek, add meg a gépjármű forgalmi rendszámát: HSJ-128
Kérlek, add meg a kilóméteróra állását: 147148
Kérlek add meg az út tipusát az alábbiak közül: // Magánút, Céges, Egyéb, Nem ismert // => Magánút
Kérlek, add meg a dátumot (ÉÉÉÉ-HH-NN formátumban): 2024-08-05
Kérem, adja meg a kiinduló települést: Fegyvernek
Kérem, adja meg a céltelepülést: Kelebia
Út adatai:
 
Kiinduló település: Fegyvernek
Céltelepülés: Kelebia
Távolság: 189.29 km
HTML fájl elérési útja: Data\route_maps_20240226_215447\route_map.html
+------------------------+---------------------+----------+------------+---------+------------+------------+----------+------------+
|       Azonosító        |        Típus        | Rendszám |  Óraállás  | Úttípus | Kiindulás  | Végállomás | Távolság |   Dátum    |
+------------------------+---------------------+----------+------------+---------+------------+------------+----------+------------+
| 8PhPkxFBhgrUMr8FiC7Aoa | Opel Astra F 1.4 8V | HSJ-128  | 147,148 km | MAGÁNÚT | Fegyvernek |  Kelebia   |  189.29  | 2024-08-05 |
+------------------------+---------------------+----------+------------+---------+------------+------------+----------+------------+
Adatok mentve!
PDF fájl létrehozva: Data\route_maps_20240226_215447\gepjarmu_adatlap_8PhPkxFBhgrUMr8FiC7Aoa_20240226_215447.pdf

```
## Használat
A Projekt Python 3.11 alatt tesztelt. 
Az **RE** modul előre beépített, nem szükséges külön telepíteni!

```bash
pip install os
pip install prettytable
pip install shortuuid
pip install csv
pip install datetime
pip install requests
pip install folium
pip install fitz # PyMuPDF
```

## Licensz

[GNU General Public License Version 3](https://raw.githubusercontent.com/HaLTeX1/Utnyilvantarto/main/LICENSE)
