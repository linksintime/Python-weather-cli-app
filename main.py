import requests
import json
from pprint import pprint
import time

def convert_kelvin_to_fahrenheit(value):
    return (value*1.8)-459.67

def show_data():
    print("-"*100)
    print("API data:\n")
    pprint(data)

def errCheck(weather_data):
    if weather_data['cod'] == '404':
        raise KeyError("Couldn't locate city")

API_KEY = 'bc50760d54528b10f34315f689817b3c'

city = input("Enter a city: ")
# Grabbing weather data
#city = "Tokyo"

base_url =  "http://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city

data = requests.get(base_url).json()
#pprint(weather_data)
# Grabbing the json dump from weather api
dataDump = json.dumps(data)
weather_data = json.loads(dataDump)
errCheck(weather_data)

# weather_descriptions = {"🌤",["🌦"],["⛆"],["⛈"],["☀"],["🌨"],["☁"],["☂"],["☄"],["⛇"],["⛈"],["🌥"],["🌩"],["🌧"],["🌩"]}
weather_descriptions = {'clear sky': "☀", 'scattered clouds': "🌤 ☁ ☁", 'mist': "⛆⛆⛆", 'overcast clouds': "🌤", 'broken clouds': "☁ ☁ ☁", "light rain": "🌤 ⛆"}

sunrise = time.ctime(weather_data['sys']['sunrise'])
sunset = time.ctime(weather_data['sys']['sunset'])
feels_like = weather_data['main']['feels_like']
humidity = weather_data['main']['humidity']
max_temp = convert_kelvin_to_fahrenheit(weather_data['main']['temp_max'])
min_temp = convert_kelvin_to_fahrenheit(weather_data['main']['temp_min'])

city = weather_data['name']
description = [i for i in weather_data['weather']]
description = description[0]['description']
# print(f"Weather feels like: {0:02d}".format(convert_kelvin_to_fahrenheit(weather_data['main']['feels_like']))
print(f"Current weather in {city}\n")
print(f"Weather is currently `{description}`: {weather_descriptions[description]}\n")
print("Temperature currently feels like: {0:.1f}° fahrenheit".format(convert_kelvin_to_fahrenheit(feels_like)))
print("Today has an expected forcasted of {0:.1f}° high and a low of {1:.1f}°".format(max_temp, min_temp))
print(f"Humidity: {humidity}%\n")

print(f"Sunrise: {sunrise}")
print(f"Sunset: {sunset}")
