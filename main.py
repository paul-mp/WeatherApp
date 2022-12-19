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


# Converts kelvin to both Celsius and Fahrenheit
def kelvin_to_c_and_f(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    return celsius, fahrenheit


# Takes the users current location
def location_gather(long, lat, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid=e5bd1a889b363d608b95e43875f020c2"
    response = requests.get(url)
    data = json.loads(response.text)

    temp_kelvin = data['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_c_and_f(temp_kelvin)

    return f"Temperature in {city} is: {temp_celsius.__round__()}℃ or {temp_fahrenheit.__round__()}℉"


print(location_gather(long, lat, user_Location))



