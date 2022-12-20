import json
import requests
import tkinter as tk

# Gets the user's location
location_api = "http://ip-api.com/json"
response = requests.get(location_api)
data = response.json()

# Gets the user's location
user_Location = f"{data['city']}"
long = f"{data['lon']}"
lat = f"{data['lat']}"
API_KEY = open('api_key', "r").read()


# Converts kelvin to both Celsius and Fahrenheit
def kelvin_to_c_and_f(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    return celsius, fahrenheit


# Takes the users current location
def location_gather(long, lat, city, API_KEY):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={API_KEY}"
    response = requests.get(url)
    data = json.loads(response.text)

    temp_kelvin = data['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_c_and_f(temp_kelvin)

    return f"Temperature in {city} is: {temp_celsius.__round__()}℃ or {temp_fahrenheit.__round__()}℉"


print(location_gather(long, lat, user_Location, API_KEY))
