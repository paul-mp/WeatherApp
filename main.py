import json
import requests
from tkinter import *
import re

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


def click():
    city = textentry.get()  # Gets the text from the text entry box
    state = textentry2.get()
    return textentry, textentry2


# THIS NEEDS TO BE FIXED. NEEDS TO SEARCH FOR CITY AND STATE FROM THE API BASED ON LATITUDE AND LONGITUDE
def city_search(city, state):

    temp_kelvin = data['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_c_and_f(temp_kelvin)
    return f"Temperature in {city} is: {temp_celsius.__round__()}℃ or {temp_fahrenheit.__round__()}℉"


window = Tk()
window.title("Weather App")

Label(window, text="Enter the city you would like to search for \n EX: London in first textbox, and UK in the other",
      font=("Arial", 20)).grid(row=0, column=0, columnspan=2, sticky=W)

textentry = Entry(window, width=20, bg="white")
textentry.grid(row=1, column=0, sticky=W)
textentry2 = Entry(window, width=20, bg="white")
textentry2.grid(row=1, column=1, sticky=W)

Button(window, text="Submit", width=6, command=click).grid(row=2, column=0, sticky=W)

output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=3, column=0, columnspan=2, sticky=W)

window.mainloop()
