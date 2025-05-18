# modules/raster.py

import geopandas as gpd
from shapely.geometry import box


def erstelle_raster(grenze_gdf, rastergroesse=10):
    """
    Erstellt ein Raster über der gegebenen Stadtgrenze mit quadratischen Zellen der angegebenen Größe.

    Args:
        grenze_gdf (GeoDataFrame): Stadtgrenze im metrischen Koordinatensystem (EPSG:3857)
        rastergroesse (int): Seitenlänge der Rasterzellen in Metern

    Returns:
        GeoDataFrame: zugeschnittenes Raster innerhalb der Stadtgrenze
    """
    grenze = grenze_gdf.to_crs(epsg=3857)
    minx, miny, maxx, maxy = grenze.total_bounds

    raster = []
    x = minx
    while x < maxx:
        y = miny
        while y < maxy:
            raster.append(box(x, y, x + rastergroesse, y + rastergroesse))
            y += rastergroesse
        x += rastergroesse

    raster_gdf = gpd.GeoDataFrame(geometry=raster, crs=grenze.crs)
    raster_clip = gpd.overlay(raster_gdf, grenze, how="intersection")
    return raster_clip

def berechne_freie_zellen(raster, ausschluss_union):
    """
    Entfernt alle Rasterzellen, die mit Ausschlussflächen überlappen.
    Gibt nur die freien Zellen zurück.
    """
    raster["frei"] = ~raster.geometry.intersects(ausschluss_union)
    return raster[raster["frei"]].copy()
