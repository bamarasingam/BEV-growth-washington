import streamlit as st
import geopandas as gpd
import pandas as pd
import folium
from streamlit_folium import folium_static

#Load fuel station locations
fuel_locations = pd.read_csv('fuel_loc.csv')

#Load Washington state county GeoJSON
wa_geojson = 'WA_County_Boundaries.geojson'
counties = gpd.read_file(wa_geojson)

#Convert Timestamp column to string
counties['EDIT_DATE'] = counties['EDIT_DATE'].astype(str)

#Create map centered at coordinates
m = folium.Map(location=[47.5, -120], zoom_start=7, control_scale=True)

#Add county boundaries
folium.GeoJson(counties, name='county boundaries').add_to(m)

#Add county names as labels for map
for idx, row in counties.iterrows():
    folium.Marker(
        location=[row['geometry'].centroid.y, row['geometry'].centroid.x],
        popup=row['JURISDICT_NM'],
        icon=folium.Icon(icon='map-marker', icon_color='red', prefix='fa', icon_size=(10, 10), shadow_size=(0, 0))
    ).add_to(m)

#Put fuel station locations as markers
for idx, fuel_row in fuel_locations.iterrows():
    folium.Marker(
        location=[fuel_row['Latitude'], fuel_row['Longitude']],
        popup='Fuel Station',
        icon=folium.Icon(icon='gas', icon_color='green', prefix='fa', icon_size=(10, 10), shadow_size=(0, 0))
    ).add_to(m)

#Load ARIMA predictions
arima_preds = pd.read_csv('arima_preds_updated.csv')

#Streamlit app
st.title("Washington Map with Actual Values and ARIMA Predictions")
st.write("Enter year and month. Jan 2017 to Aug 2023 is real values, anything afterwards is predicted up until July 2026")
    
#User input for year and month
user_input_year = st.number_input("Select a Year", min_value=2017, max_value=2026, value=2023)
user_input_month = st.number_input("Select a Month", min_value=1, max_value=12, value=8)

#ARIMA prediction filtering
filtered_data = arima_preds[
    (arima_preds['Year'] == user_input_year) &
    (arima_preds['Month'] == user_input_month)
]

#Display total
if not filtered_data.empty:
    new_bev_added = filtered_data['New BEV Added'].values[0]
    st.write(f"Value in 'New BEV Added' for {user_input_month}/{user_input_year}: {new_bev_added}")
else:
    st.write(f"No data available for {user_input_month}/{user_input_year}.")

folium_static(m)
