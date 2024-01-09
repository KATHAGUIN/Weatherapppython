import streamlit as st
import requests
from config import API_KEY

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.title("Weather App")
st.write("Forecasting Tomorrow, Today: Your Weather Companion")

city = st.text_input("Enter city name:", "Berlin")
api_key = API_KEY
base_url = "http://api.openweathermap.org/data/2.5/weather"



if st.button("Get Weather"):
    response = requests.get(f"{base_url}?q={city}&appid={api_key}")
    data = response.json()

    if response.status_code == 200:
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        description = data['weather'][0]['description']
        weather_icon = data['weather'][0]['icon']

        st.write(f"Weather in {city}: {temperature_celsius:.2f}°C, {description}")
    else:
        st.write(f"Error: {data.get('message', 'Unknown error')}")