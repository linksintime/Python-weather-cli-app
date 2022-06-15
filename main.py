import requests
import json
from pprint import pprint
import time

def convert_kelvin_to_fahrenheit(value):
    return (value*1.8)-459.67

def show_data():
    pprint(data)

API_KEY = 'bc50760d54528b10f34315f689817b3c'

#city = input("Enter a city: ")
# Grabbing weather data
city = "Boston"

base_url =  "http://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city

data = requests.get(base_url).json()

#pprint(weather_data)
# Grabbing the json dump from weather api
dataDump = json.dumps(data)
weather_data = json.loads(dataDump)

# Print stuff

# weather_descriptions = {"🌤",["🌦"],["⛆"],["⛈"],["☀"],["🌨"]}
weather_descriptions = {'clear sky': "☀", 'scattered clouds': "🌤", 'mist': "⛆"}

sunrise = time.ctime(weather_data['sys']['sunrise'])
sunset = time.ctime(weather_data['sys']['sunset'])
feels_like = weather_data['main']['feels_like']
city = weather_data['name']
description = [i for i in weather_data['weather']]
description = description[0]['description']

# print(f"Weather feels like: {0:02d}".format(convert_kelvin_to_fahrenheit(weather_data['main']['feels_like']))
print(f"This is the current weather in {city}\n")
print(f"Weather is currently `{description}`: {weather_descriptions[description]}")
print("Weather feels like: {0:.2f} degrees\n".format(convert_kelvin_to_fahrenheit(feels_like)))

print(f"Sunrise: {sunrise}")
print(f"Sunset: {sunset}")
