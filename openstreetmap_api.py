import requests
import requests
import folium
from folium import plugins
import os
import datetime

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
    origin_location = input("Kérem, adja meg a kiinduló települést: ")
    destination_location = input("Kérem, adja meg a céltelepülést: ")

    origin_coordinates = get_coordinates(origin_location)
    destination_coordinates = get_coordinates(destination_location)

    if origin_coordinates and destination_coordinates:
        distance = round(get_distance(origin_coordinates, destination_coordinates) / 1000, 2)
        print(f"Út adatai:")
        print(" ")
        print(f"Kiinduló település: {origin_location}")
        print(f"Céltelepülés: {destination_location}")
        print(f"Távolság: {distance} km")

        coordinates = [origin_coordinates, destination_coordinates]
        save_route_to_png(origin_location, destination_location, coordinates)

        return (origin_location, destination_location, distance)
    else:
        print("Hibás településnév vagy nem találhatóak koordináták.")
        return None

def save_route_to_png(origin_location, destination_location, coordinates):
    # Azonosító generálási dátum létrehozása
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    data_folder = "Data"
    folder_name = f"route_maps_{timestamp}"
    os.makedirs(os.path.join(data_folder, folder_name), exist_ok=True)
    file_path = os.path.join(data_folder, folder_name, "route_map.html")


    mid_lat = (coordinates[0][0] + coordinates[1][0]) / 2
    mid_lon = (coordinates[0][1] + coordinates[1][1]) / 2
    route_map = folium.Map(location=[mid_lat, mid_lon], zoom_start=10)

    # Add markers for origin and destination
    folium.Marker(coordinates[0], popup=origin_location).add_to(route_map)
    folium.Marker(coordinates[1], popup=destination_location).add_to(route_map)

    folium.PolyLine(locations=coordinates, color='blue').add_to(route_map)

    route_map.save(file_path)

    print(f"HTML fájl elérési útja: {file_path}")
