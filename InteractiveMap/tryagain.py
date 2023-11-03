import streamlit as st
import geopandas as gpd
from streamlit_folium import folium_static #Took this from the below link as was having troubles
#https://github.com/python-visualization/branca/issues/81
import folium

# Load the Washington state county GeoJSON file
wa_geojson = 'WA_County_Boundaries.geojson'
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
        icon=folium.Icon(icon='map-marker', icon_color='blue', prefix='fa', icon_size=(10, 10))  # Adjust the icon_size to make it smaller
    ).add_to(m)

# Streamlit app
st.title("Washington State County Map")
st.write("This app displays a map of Washington state with county boundaries.")

# Display the map using Streamlit and streamlit-folium
folium_static(m)