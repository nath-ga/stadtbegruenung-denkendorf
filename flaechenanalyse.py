# 🌳 ML-gestützte Flächenanalyse zur klimaaktiven Stadtbegrünung kleiner Kommunen
#
# Lernprojekt von Nathalie Gassert 16.05.2025
#
# Ziele:
#    Einarbeiten in Kartenanalyse mit Python (z.B. osmnx, geopandas, shapely)
#    Training eines ML-Modells (z. B. Decision Tree) zur Flächenklassifikation
#    Erstellen einer Heatmap mit Empfehlungen für Baumpflanzungen
#
#
#
#

import osmnx as ox
import folium

# Stadt wählen
place = "Denkendorf, Deutschland"

# Straßennetz laden
graph = ox.graph_from_place(place, network_type='walk')

# Gebäude laden
buildings = ox.features_from_place(place, tags={'building': True})

# Karte zentrieren
center = ox.geocode(place)
m = folium.Map(location=center, zoom_start=15)

# Gebäude einzeichnen
folium.GeoJson(buildings.geometry).add_to(m)
m

m.save("karte.html")

