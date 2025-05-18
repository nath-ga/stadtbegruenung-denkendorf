# modules/ml_dataset.py

import geopandas as gpd
import pandas as pd
import os
from config import PLACE
from modules.osm_loader import ort_hash


def erzeuge_ml_dataset(geeignet, ungeeignet, ordner="ml_daten"):
    """
    Kombiniert geeignete und ungeeignete Rasterzellen zu einem ML-Trainingsdatensatz.
    Speichert diesen als CSV mit Label-Spalte (1 = geeignet, 0 = ungeeignet).
    """
    os.makedirs(ordner, exist_ok=True)
    ort_id = ort_hash(PLACE)

    def vorbereiten(gdf, label):
        df = gdf.copy()
        df["flaeche"] = df.geometry.area
        df["label"] = label
        spalten = ["flaeche", "abstand_gebaeude", "abstand_strasse", "label"]
        if "landuse_typ" in df.columns:
            spalten.insert(-1, "landuse_typ")
        return df[spalten]

    df_geeignet = vorbereiten(geeignet, label=1)
    df_ungeeignet = vorbereiten(ungeeignet, label=0)

    df = pd.concat([df_geeignet, df_ungeeignet], ignore_index=True)
    pfad = os.path.join(ordner, f"ml_daten_{ort_id}.csv")
    df.to_csv(pfad, index=False)
    print(f"✅ Trainingsdatensatz gespeichert unter: {pfad}")

    return df
