import requests

def get_coordinates(location):
    try:
        response = requests.get(f"https://nominatim.openstreetmap.org/search", params={"q": location, "format": "json"})
        data = response.json()

        if data:
            return float(data[0]["lat"]), float(data[0]["lon"])
        else:
            return None
    except Exception as e:
        print(f"Hiba a koordináták lekérdezése közben: {e}")
        return None


def get_distance(origin, destination):
    base_url = "https://router.project-osrm.org/route/v1/driving/"
    coordinates = f"{origin[1]},{origin[0]};{destination[1]},{destination[0]}"
    params = {
        "alternatives": "false",
        "steps": "false",
        "annotations": "distance",
        "geometries": "geojson",
    }

    try:
        response = requests.get(f"{base_url}{coordinates}", params=params)
        data = response.json()

        # Kinyerjük a távolságot a válaszból
        distance = data["routes"][0]["distance"]

        return distance
    except Exception as e:
        print(f"Hiba a távolság lekérdezése közben: {e}")
        return None


def distmain():
    origin_location = input("Kérem, adja meg az indulási települést: ")
    destination_location = input("Kérem, adja meg a céltelepülést: ")

    origin_coordinates = get_coordinates(origin_location)
    destination_coordinates = get_coordinates(destination_location)

    if origin_coordinates and destination_coordinates:
        distance = round(get_distance(origin_coordinates, destination_coordinates) / 1000, 2)
        print(f"Út adatai:")
        print(f"Kiinduló település: {origin_location}")
        print(f"Céltelepülés: {destination_location}")
        print(f"Távolság: {distance} km")

        return (origin_location, destination_location, distance)
    else:
        print("Hibás településnév vagy nem találhatóak koordináták.")
        return None
