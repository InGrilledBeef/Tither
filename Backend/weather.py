# Date: 2022-06-04
# Author: Ingrid Qin

# Author: Ingrid
# Date: 2022-06-05
# Use open weather map API: https://openweathermap.org/api
# Get an API key from here to run this program

# Country codes must be ISO 3166 Country Codes
# Location should be in the form city_name, state_code, country_code
import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def getWeather(location):
    wList = []
    
    f = open("apikey.txt", "r")
    apiKey = f.read()
    response = "http://api.openweathermap.org/geo/1.0/direct?q=" + location + "&limit=8&appid=" + apiKey
    print(location)
    responseInfo = requests.get(response);
    lat = responseInfo.json()[0]["lat"]
    lon = responseInfo.json()[0]["lon"]

    response2 = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + apiKey

    info = requests.get(response2);

    #jprint(info.json())
    wList.append(info.json()[0]["temp"])

    return info.json()