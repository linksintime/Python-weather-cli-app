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

#city = input("Enter a city: ")
# Grabbing weather data
#city = "Tokyo"
oldList = []
timeStart = time.time()
with open("cities.txt", "r", encoding="utf-8") as oregonCities:
    cities = [i for i in oregonCities.readlines()]

cities = sorted(cities)
errCities = []

for j in cities:
    
    base_url =  "http://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+j
    data = requests.get(base_url).json()
    #pprint(weather_data)
    # Grabbing the json dump from weather api
    dataDump = json.dumps(data)
    weather_data = json.loads(dataDump)
    #errCheck(weather_data)
    # weather_descriptions = {"🌤",["🌦"],["⛆"],["⛈"],["☀"],["🌨"],["☁"],["☂"],["☄"],["⛇"],["⛈"],["🌥"],["🌩"],["🌧"],["🌩"]}
    weather_descriptions = {'clear sky': "☀", 'scattered clouds': "🌤 ☁ ☁", 'mist': "⛆⛆⛆", 'overcast clouds': "🌤", 'broken clouds': "☁ ☁ ☁", "light rain": "🌤 ⛆", "few clouds": "☀  ☁", "moderate rain": '🌦 🌧', "light intensity drizzle":"⛆", "heavy intensity rain":"🌧🌧🌧🌧🌧"}
    #sunrise = time.ctime(weather_data['sys']['sunrise'])
    #sunset = time.ctime(weather_data['sys']['sunset'])
    try:
        feels_like = weather_data['main']['feels_like']
        city = weather_data['name']
        description = [i for i in weather_data['weather']]
        description = description[0]['description']
    except:
        #print(f"Couldn't find city {j}")
        errCities.append(j)
    #humidity = weather_data['main']['humidity']
    #max_temp = convert_kelvin_to_fahrenheit(weather_data['main']['temp_max'])
    #min_temp = convert_kelvin_to_fahrenheit(weather_data['main']['temp_min'])
    
    # print(f"Weather feels like: {0:02d}".format(convert_kelvin_to_fahrenheit(weather_data['main']['feels_like']))
    #print(f"Current weather in {city}")
    #print(f"Weather is currently `{description}`: {weather_descriptions[description]}")
    #print("Temperature currently feels like: {0:.1f}° fahrenheit".format(convert_kelvin_to_fahrenheit(feels_like)))
    #print("Today has an expected forcasted of {0:.1f}° high and a low of {1:.1f}°".format(max_temp, min_temp))
    #print(f"Humidity: {humidity}%\n")
    #print(f"Sunrise: {sunrise}")
    #print(f"Sunset: {sunset}")
with open("errorCities.txt", "a", encoding="utf-8") as badCity:
    for i in errCities: badCity.writelines(i)

timeStop = time.time
# Added timing for optimization purposes in debugging
totalTime = timeStop - timeStart
print(errCities)
print(totalTime)