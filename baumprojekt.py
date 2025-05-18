# 🌳 ML-gestützte Flächenanalyse zur klimaaktiven Stadtbegrünung kleiner Kommunen
#
# Lernprojekt von Nathalie Gassert 17.05.2025
#
# Ziele:
#    Einarbeiten in Kartenanalyse mit Python (z.B. osmnx, geopandas, shapely)
#    Training eines ML-Modells (z. B. Decision Tree) zur Flächenklassifikation
#    Erstellen einer Heatmap mit Empfehlungen für Baumpflanzungen
# 
# Modularer Aufbau um leicht Änderungen einarbeiten zu können
#
#

#baumprojekt/
#├── main.py                # Einstiegspunkt (z. B. Rasterung + Analyse starten)
#├── config.py              # Ort, Rastergröße, Pfade
#├── modules/
#│   ├── osm_loader.py      # lade_osm_daten()
#│   ├── raster.py          # erstelle_raster()
#│   ├── filter.py          # berechne_freie_zellen(), lade_ausschlussflächen()
#│   └── visualizer.py      # zeige_freie_zellen_karte()
#├── data/                  # gespeicherte Geo-Daten
#├── output/                # Karten und Ergebnisse
#└── README.md              # Projektbeschreibung
