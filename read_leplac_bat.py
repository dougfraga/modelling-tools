"""
Script to read LEPLAC bathymetry file and convert to MOHID standards
Data source: https://www.marinha.mil.br/dhn/sites/www.marinha.mil.br.dhn/files/DTM_BR_LEPLAC_FEV23_1000m_LatLongProf.zip
Author: Douglas F Rodrigues
"""

import pandas as pd
import geopandas as gpd
from shapely import geometry


# Define column names and import file 
colnames = ['E', 'N', 'Depth']
f = pd.read_csv('DTM_BR_LEPLAC_FEV23_1000m.xyz', delim_whitespace=True, encoding='utf-8', names=colnames, header=None)

# Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(f, geometry=gpd.points_from_xy(f.E, f.N))
gdf = gdf.set_crs('epsg:3395')

# Reproject to Geographic Coordinates
geo_gdf = gdf.to_crs({'init': 'epsg:4326'})

# Create bounding area (Rio de Janeiro coast)
lat_min = -26
lat_max = -20
lon_min = -47
lon_max = -38

pointList = [(lon_min, lat_min),(lon_min, lat_max),(lon_max, lat_max),(lon_max, lat_min)]
poly = geometry.Polygon(pointList)
geo_poly = gpd.GeoSeries([poly], crs='epsg:4326')

# Create a subset dataframe of points within the bounding area
subset = geo_gdf[geo_gdf.within(geo_poly.geometry.iloc[0])]

# Managing resulting dataset
subset['Longitude'] = subset.geometry.x
subset['Latitude'] = subset.geometry.y
subset.drop(['E', 'N', 'geometry'], axis=1, inplace=True)

# Remove bad values
subset.drop(subset[(subset['Depth'] >= 0)].index, inplace=True)

# Convert bathymetry values to MOHID standards
subset['Depth'] = subset['Depth'] * -1

# Select useful columns
subset = subset[['Longitude', 'Latitude', 'Depth']]

# Export results
subset.to_csv('batimetria_marinha.xyz', encoding='utf-8', sep=' ', index_label=False, index=False)

