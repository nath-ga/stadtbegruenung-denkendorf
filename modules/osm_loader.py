# modules/osm_loader.py

import os
import osmnx as ox
import geopandas as gpd
import hashlib
import unicodedata
from config import AUSSCHLUSS_TAGS

def ort_hash(place):
    """
    Gibt einen eindeutigen Hash für den Ort zur Dateibenennung zurück.
    Entfernt Umlaute und kodiert den Ortsnamen.
    """
    place_ascii = unicodedata.normalize('NFKD', place).encode('ascii', 'ignore').decode('ascii')
    return hashlib.md5(place_ascii.encode("utf-8")).hexdigest()[:8]


def lade_osm_daten(place):
    os.makedirs("data", exist_ok=True)
    hash_id = ort_hash(place)
    pfad_gebaeude = f"data/gebaeude_{hash_id}.geojson"
    pfad_grenze = f"data/grenze_{hash_id}.geojson"

    if os.path.exists(pfad_gebaeude) and os.path.exists(pfad_grenze):
        print("Lade Gebäude und Stadtgrenze aus Cache ...")
        gebaeude = gpd.read_file(pfad_gebaeude)
        grenze = gpd.read_file(pfad_grenze)
    else:
        print("Lade Gebäude und Stadtgrenze von OSM ...")
        gebaeude = ox.features_from_place(place, tags={"building": True}).to_crs(epsg=3857)
        grenze = ox.geocode_to_gdf(place).to_crs(epsg=3857)
        gebaeude.to_file(pfad_gebaeude, driver="GeoJSON")
        grenze.to_file(pfad_grenze, driver="GeoJSON")

    return gebaeude, grenze


def lade_ausschlussflachen(place):
    os.makedirs("data", exist_ok=True)
    hash_id = ort_hash(place)
    pfad_ausschluss = f"data/ausschluss_{hash_id}.geojson"

    if os.path.exists(pfad_ausschluss):
        print("Lade Ausschlussflächen aus Cache ...")
        ausschluss = gpd.read_file(pfad_ausschluss)
    else:
        print("Lade Ausschlussflächen von OSM ...")
        ausschluss = ox.features_from_place(place, tags=AUSSCHLUSS_TAGS).to_crs(epsg=3857)
        ausschluss.to_file(pfad_ausschluss, driver="GeoJSON")

    return ausschluss.geometry.union_all()


def lade_strassen(place):
    """
    Lädt Straßendaten für das gegebene Gebiet oder aus dem lokalen Cache.
    """
    os.makedirs("data", exist_ok=True)
    hash_id = ort_hash(place)
    pfad_strassen = f"data/strassen_{hash_id}.geojson"

    if os.path.exists(pfad_strassen):
        print("Lade Straßen aus Cache ...")
        strassen = gpd.read_file(pfad_strassen)
    else:
        print("Lade Straßen von OSM ...")
        strassen = ox.features_from_place(place, tags={"highway": True}).to_crs(epsg=3857)
        strassen.to_file(pfad_strassen, driver="GeoJSON")

    return strassen


def lade_landuse_flaechen(place, cache_file="data/landuse.geojson"):
    """
    Lädt landuse-Flächen (z. B. residential, industrial, forest, grass) aus OpenStreetMap.
    Nutzt lokalen Cache, wenn vorhanden.
    """
    if os.path.exists(cache_file):
        return gpd.read_file(cache_file)

    tags = {"landuse": True}
    gdf = ox.features_from_place(place, tags=tags).to_crs(epsg=3857)
    gdf.to_file(cache_file, driver="GeoJSON")
    return gdf
