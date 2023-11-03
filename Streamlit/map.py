import streamlit as st
import geopandas as gpd
import pandas as pd
from streamlit_folium import folium_static #Took this from the below link as was having troubles
#https://github.com/python-visualization/branca/issues/81
import folium

# Load fuel station locations from the CSV file
fuel_locations = pd.read_csv('fuel_loc.csv')

# Load the Washington state county GeoJSON file
wa_geojson = 'WA_County_Boundaries.geojson' #https://geo.wa.gov/datasets/wadnr::wa-county-boundaries/geoservice
counties = gpd.read_file(wa_geojson)

# Convert Timestamp column to string
counties['EDIT_DATE'] = counties['EDIT_DATE'].astype(str)

# Create a map centered at the specified coordinates
m = folium.Map(location=[47.5, -120], zoom_start=7, control_scale=True)

# Add GeoJSON layer for county boundaries
folium.GeoJson(counties, name='county boundaries').add_to(m)

# Add county names as labels to the map
for idx, row in counties.iterrows():
    folium.Marker(
        location=[row['geometry'].centroid.y, row['geometry'].centroid.x],
        popup=row['JURISDICT_NM'],  # Column from GeoDataFrame to list out counties
        icon=folium.Icon(icon='map-marker', icon_color='red', prefix='fa', icon_size=(10, 10), shadow_size=(0,0))  # Adjust the icon_size to make it smaller
    ).add_to(m)

# Add fuel station locations as markers
for idx, fuel_row in fuel_locations.iterrows():
    folium.Marker(
        location=[fuel_row['Latitude'], fuel_row['Longitude']],
        popup='Fuel Station',  
        icon=folium.Icon(icon='gas', icon_color='green', prefix='fa', icon_size=(10, 10), shadow_size=(0,0))  # Customize the marker for fuel stations
    ).add_to(m)

# Streamlit app
st.title("Washington State Fuel Locations")
st.write("This app shows an app of fuel locations with county boundaries")

# Display the map using Streamlit and streamlit-folium
folium_static(m)