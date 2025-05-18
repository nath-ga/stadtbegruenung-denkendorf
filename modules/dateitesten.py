import geopandas as gpd
gdf = gpd.read_file("data/gebaeude.geojson")
print(gdf.shape)
