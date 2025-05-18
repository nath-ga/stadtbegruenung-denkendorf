# modules/export.py

import os

def speichere_zellen(gdf, ortsname, ordner="export", formate=("geojson", "csv")):
    """
    Speichert ein GeoDataFrame in gewünschten Formaten (.geojson, .csv) im angegebenen Ordner.

    Args:
        gdf (GeoDataFrame): Die zu speichernden Flächen
        ortsname (str): Ortsname zur Dateibenennung
        ordner (str): Zielordner für die Dateien
        formate (tuple): Formate, die gespeichert werden sollen
    """https://github.com/dashboard
    os.makedirs(ordner, exist_ok=True)
    basisname = ortsname.lower().replace(" ", "_").replace(",", "").replace("-", "_")

    if "geojson" in formate:
        pfad_geojson = os.path.join(ordner, f"{basisname}.geojson")
        gdf.to_file(pfad_geojson, driver="GeoJSON")
        print(f"✅ gespeichert: {pfad_geojson}")

    if "csv" in formate:
        pfad_csv = os.path.join(ordner, f"{basisname}.csv")
        gdf.drop(columns="geometry").to_csv(pfad_csv, index=False)
        print(f"✅ gespeichert: {pfad_csv}")
