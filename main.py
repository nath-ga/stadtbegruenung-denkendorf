# main.py
# von meinem ML-Projekt zur Stadtbegrünung

from config import PLACE
from modules.osm_loader import lade_osm_daten, lade_ausschlussflachen
from modules.raster import erstelle_raster
from modules.filter import berechne_freie_zellen
from modules.visualizer import zeige_freie_zellen_karte
from modules.osm_loader import lade_strassen
from modules.eignung import bewertung_freier_zellen
from modules.osm_loader import lade_strassen
from modules.export import speichere_zellen

def main():
    print("Starte Analyse für:", PLACE)

    # 1. Daten laden
    gebaeude, grenze = lade_osm_daten(PLACE)
    ausschluss_union = lade_ausschlussflachen(PLACE)
    strassen = lade_strassen(PLACE)
    geeignete_zellen = bewertung_freier_zellen(freie_zellen, gebaeude, strassen)

    # 2. Raster erstellen
    raster = erstelle_raster(grenze, rastergroesse=10)

    # 3. Freie Zellen berechnen
    freie_zellen = berechne_freie_zellen(raster, gebaeude, ausschluss_union)

    # 4. Karte erzeugen
    from osmnx import geocode
    center = geocode(PLACE)
    zeige_freie_zellen_karte(freie_zellen, gebaeude, center, "output/freie_zellen_karte.html")


if __name__ == "__main__":
    main()


