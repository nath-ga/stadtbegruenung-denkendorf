# modules/eignung.py

import geopandas as gpd
from config import MINDEST_GROESSE_M2, MINDEST_ABSTAND_GEBÄUDE_M, MINDEST_ABSTAND_STRASSE_M


def bewertung_freier_zellen(zellen, gebaeude, strassen):
    """
    Bewertet freie Rasterzellen anhand konfigurierbarer Kriterien:
    - Mindestfläche (aus config): MINDEST_GROESSE_M2
    - Mindestabstand zu Gebäuden (aus config): MINDEST_ABSTAND_GEBÄUDE_M
    - Mindestabstand zu Straßen (aus config): MINDEST_ABSTAND_STRASSE_M

    Gibt ein GeoDataFrame mit den Zellen zurück, die alle Kriterien erfüllen.
    """
    geeignet = zellen[
        (zellen["flaeche"] >= MINDEST_GROESSE_M2) &
        (zellen["abstand_gebaeude"] >= MINDEST_ABSTAND_GEBÄUDE_M) &
        (zellen["abstand_strasse"] >= MINDEST_ABSTAND_STRASSE_M)
    ].copy()

    return geeignet

# def bewertung_freier_zellen(freie_zellen, gebaeude_gdf, strassen_gdf):
    """
    Bewertet freie Zellen anhand Mindestfläche sowie Mindestabstand zu Gebäuden und Straßen.

    Args:
        freie_zellen (GeoDataFrame): potenzielle freie Flächen
        gebaeude_gdf (GeoDataFrame): Gebäude zur Abstandsmessung
        strassen_gdf (GeoDataFrame): Straßen zur Abstandsmessung

    Returns:
        GeoDataFrame: geeignete Flächen gemäß Kriterien
    """
#    flaechen = freie_zellen.copy()
#    flaechen["flaeche"] = flaechen.geometry.area
#    flaechen = flaechen[flaechen["flaeche"] >= MINDEST_GROESSE_M2]

#    if len(gebaeude_gdf) > 0:
#        gebaeude_union = gebaeude_gdf.geometry.unary_union
#        flaechen["abstand_gebaeude"] = flaechen.geometry.apply(lambda x: x.distance(gebaeude_union))
#        flaechen = flaechen[flaechen["abstand_gebaeude"] >= MINDEST_ABSTAND_GEBÄUDE_M]

#    if len(strassen_gdf) > 0:
#        strassen_union = strassen_gdf.geometry.unary_union
#        flaechen["abstand_strasse"] = flaechen.geometry.apply(lambda x: x.distance(strassen_union))
#        flaechen = flaechen[flaechen["abstand_strasse"] >= MINDEST_ABSTAND_STRASSE_M]

#    return flaechen.drop(columns=["flaeche", "abstand_gebaeude", "abstand_strasse"], errors="ignore")
