# config.py

# Zentrale Parameter für das Baumprojekt

# Ort für die Analyse (OpenStreetMap-kompatibel)
PLACE = "73770 Denkendorf, Deutschland"

# Rastergröße in Metern
RASTER_GROESSE = 20

# Speicherpfad für Ausgabedateien
OUTPUT_PFAD = "output/freie_zellen_karte.html"
# config.py

# Welche OSM-Tags sollen ausgeschlossen werden?
AUSSCHLUSS_TAGS = {
    "landuse": ["cemetery", "farmland", "meadow", "commercial", "industrial", "forest"],  
    "leisure": ["pitch", "playground", "track"],
    "amenity": ["parking"],
    "natural": ["water"],
    "highway": True,
    "railway": True
}

# Bewertungsparameter für geeignete Flächen
MINDEST_GROESSE_M2 = 6.0
MINDEST_ABSTAND_GEBÄUDE_M = 3.0
MINDEST_ABSTAND_STRASSE_M = 2.0

