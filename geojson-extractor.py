import geopandas as gpd

# Load the GeoJSON file
geojson_file = 'C:/Users/Hp/Downloads/python/KARNATAKA_SUBDISTRICTS.geojson'
data = gpd.read_file(geojson_file)

# Filter the data for Mandya district
mandya_data = data[data['dtname'] == 'Mandya']

# Save the Mandya district data to a new GeoJSON file
mandya_data.to_file('mandya_district.geojson', driver='GeoJSON')

print("Extracted Mandya district data and saved to 'mandya_district.geojson'")
