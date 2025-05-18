# main_ml.py

from config import PLACE
from modules.osm_loader import lade_osm_daten, lade_ausschlussflachen, lade_strassen
from modules.raster import erstelle_raster, berechne_freie_zellen
from modules.eignung import bewertung_freier_zellen
from modules.features import berechne_features
from modules.ml_dataset import erzeuge_ml_dataset

print(f"Starte ML-Datensatz-Erstellung für: {PLACE}")

# Daten laden
gebaeude, grenze = lade_osm_daten(PLACE)
ausschluss_union = lade_ausschlussflachen(PLACE)
strassen = lade_strassen(PLACE)

# Raster & freie Zellen mit Features
raster = erstelle_raster(grenze)
freie_zellen_roh = berechne_freie_zellen(raster, ausschluss_union)
freie_zellen = berechne_features(freie_zellen_roh, gebaeude, strassen)

# Eignungsbewertung & Aufteilen
geeignete = bewertung_freier_zellen(freie_zellen, gebaeude, strassen)
ungeeignete = freie_zellen[~freie_zellen.index.isin(geeignete.index)].copy()

# landuse als Merkmale hinzufügen
from modules.osm_loader import lade_landuse_flaechen, annotiere_landuse_typ

landuse = lade_landuse_flaechen(PLACE)
geeignete = annotiere_landuse_typ(geeignete, landuse)
ungeeignete = annotiere_landuse_typ(ungeeignete, landuse)

# ML-Datensatz erzeugen
ml_df = erzeuge_ml_dataset(geeignete, ungeeignete)
print(ml_df.head())

