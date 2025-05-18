# modules/features.py

from shapely.geometry import GeometryCollection

def berechne_features(zellen, gebaeude, strassen):
    """
    Fügt den Zellen Spalten hinzu:
    - flaeche (m²)
    - abstand_gebaeude
    - abstand_strasse
    Gibt ein neues GeoDataFrame zurück.
    """
    df = zellen.copy()
    df["flaeche"] = df.geometry.area

    if len(gebaeude) > 0:
        gebaeude_union = gebaeude.geometry.union_all()
        df["abstand_gebaeude"] = df.geometry.apply(lambda x: x.distance(gebaeude_union))
    else:
        df["abstand_gebaeude"] = 0

    if len(strassen) > 0:
        strassen_union = strassen.geometry.union_all()
        df["abstand_strasse"] = df.geometry.apply(lambda x: x.distance(strassen_union))
    else:
        df["abstand_strasse"] = 0

    return df

def berechne_landuse_typ(zellen, landuse_gdf):
    return annotiere_landuse_typ(zellen, landuse_gdf)
