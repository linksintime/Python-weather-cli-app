import requests
import json
from pprint import pprint
import time

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Changes color based on temp (eg. temp > 100 = red, temp <= 80 = orange, temp <= 60 = blue)
# NOTE: WIP
def tempRangeSystem(temp):
    pass

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

#city = input("Enter a city: ")
# Grabbing weather data
city = "Boston"

base_url =  "http://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city

data = requests.get(base_url).json()
#pprint(weather_data)
# Grabbing the json dump from weather api
dataDump = json.dumps(data)
weather_data = json.loads(dataDump)
errCheck(weather_data)

# weather_descriptions = {"🌤",["🌦"],["⛆"],["⛈"],["☀"],["🌨"],["☁"],["☂"],["☄"],["⛇"],["⛈"],["🌥"],["🌩"],["🌧"],["🌩"]}
weather_descriptions = {'clear sky': "☀", 'scattered clouds': "🌤 ☁ ☁", 'mist': "⛆⛆⛆", 'overcast clouds': "🌤", 'broken clouds': "☁ ☁ ☁", "light rain": "🌤 ⛆"}

# Getting information from weather JSON File
sunrise = time.ctime(weather_data['sys']['sunrise'])
sunset = time.ctime(weather_data['sys']['sunset'])
feels_like = weather_data['main']['feels_like']
humidity = weather_data['main']['humidity']
max_temp = convert_kelvin_to_fahrenheit(weather_data['main']['temp_max'])
min_temp = convert_kelvin_to_fahrenheit(weather_data['main']['temp_min'])
city = weather_data['name']
description = [i for i in weather_data['weather']]
description = description[0]['description']

### What user actually sees

# Current weather description and city
print(f"{color.BOLD}Current weather in: {color.END}{color.BLUE}{city}{color.END}\n")
print(f"{color.BOLD}Weather is currently {color.END}{color.BLUE}`{description}`{color.END}{color.BOLD}: {weather_descriptions[description]}{color.END}\n")

# Current Temperature, Max Temperature, Min Temperature with nice formatting and colors! >:)
print(f"{color.BOLD}Temperature currently feels like: {color.END}{color.BLUE}{convert_kelvin_to_fahrenheit(feels_like):.1f}{color.END}°{color.BOLD}fahrenheit{color.END}")
print(f"{color.BOLD}Today has an expected forcasted of {color.END}{color.BLUE}{max_temp:.1f}°{color.END}{color.BOLD} high and a low of {color.END}{color.BLUE}{min_temp:.1f}°{color.END}\n")

# Humidity
print(f"{color.BOLD}Humidity:{color.END} {color.BLUE}{humidity}%{color.END}\n")

print(f"{color.BOLD}Sunrise: {color.END}{color.BLUE}{sunrise}{color.END}")
print(f"{color.BOLD}Sunset: {color.END}{color.BLUE}{sunset}{color.END}")
