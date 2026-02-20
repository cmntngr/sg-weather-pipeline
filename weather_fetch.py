import requests
import pandas as pd
import streamlit as st

@st.cache_data(ttl=300)  # caches for 5 minutes
def get_weather():
    # NEA API for real-time air temperature
    url = "https://api.data.gov.sg/v1/environment/air-temperature"
    response = requests.get(url)
    data = response.json()

    # 1. Extract stations
    stations = data['metadata']['stations']
    df_stations = pd.json_normalize(stations)


    # 2. Rename columns so Streamlit's st.map can recognize them
    df_stations = df_stations.rename(columns={
        'location.latitude': 'latitude',
        'location.longitude': 'longitude'
    })

    # 3. Extract actual temperature readings
    readings = data['items'][0]['readings']
    df_readings = pd.DataFrame(readings)

    # 4. Merge station info with temperature values
    df = pd.merge(df_stations, df_readings, left_on='id', right_on='station_id')

    return df[['name', 'value', 'latitude', 'longitude']]

# Streamlit UI
st.title("🇸🇬 Real-Time Singapore Temperature")
if st.button('Refresh Data'):
    df = get_weather()
    st.map(df)  # Shows a map of SG with temperature locations
    st.dataframe(df, use_container_width=True)
