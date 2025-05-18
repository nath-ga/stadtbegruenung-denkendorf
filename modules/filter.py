# modules/filter.py


def berechne_freie_zellen(raster_gdf, gebaeude_gdf, zusatz_union=None):
    """
    Gibt alle Rasterzellen zurück, die keine Gebäude und ggf. keine weiteren Ausschlussflächen überdecken.

    Args:
        raster_gdf (GeoDataFrame): Rasterzellen
        gebaeude_gdf (GeoDataFrame): Gebäude als Polygone
        zusatz_union (shapely.geometry.base.BaseGeometry, optional): Weitere Ausschlussflächen als kombinierte Geometrie

    Returns:
        GeoDataFrame: freie Rasterzellen
    """
    ausschluss = gebaeude_gdf.geometry.union_all()

    if zusatz_union:
        ausschluss = ausschluss.union(zusatz_union)

    freie_zellen = raster_gdf[~raster_gdf.intersects(ausschluss)]
    return freie_zellen
