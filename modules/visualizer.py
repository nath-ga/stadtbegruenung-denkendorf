# modules/visualizer.py

import folium
import os


def zeige_freie_zellen_karte(freie_zellen, gebaeude_gdf, center, dateipfad="output/freie_zellen_karte.html"):
    """
    Erstellt eine interaktive Karte mit freien Zellen farbig markiert.

    Args:
        freie_zellen (GeoDataFrame): Rasterzellen ohne Ausschlussüberschneidung
        gebaeude_gdf (GeoDataFrame): Gebäude zur Orientierung
        center (tuple): Kartenmittelpunkt (Latitude, Longitude)
        dateipfad (str): Speicherort für HTML-Karte
    """
    m = folium.Map(location=center, zoom_start=15)

    # Gebäude grau und leicht transparent
    folium.GeoJson(gebaeude_gdf.geometry, name="Gebäude", style_function=lambda x: {
        'color': 'gray',
        'weight': 0.3,
        'fillOpacity': 0.2
    }).add_to(m)

    # Freie Zellen grün hervorheben
    folium.GeoJson(freie_zellen.geometry, name="Freie Zellen", style_function=lambda x: {
        'color': 'green',
        'weight': 0.5,
        'fillOpacity': 0.3
    }).add_to(m)

    folium.LayerControl().add_to(m)
    os.makedirs(os.path.dirname(dateipfad), exist_ok=True)
    m.save(dateipfad)
    print(f"Karte gespeichert unter: {dateipfad}")
