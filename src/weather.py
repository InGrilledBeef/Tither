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

def jtext(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

def getWeather(location):
    wList = []
    
    f = open("apikey.txt", "r")
    apiKey = f.read()
    response = requests.get("http://api.openweathermap.org/geo/1.0/direct?q=" + location + "&limit=8&appid=" + apiKey)
    responseInfo = response.json();
    if len(responseInfo) == 0:
        wList = ["invalid"]*6
        return wList
    
    lat = responseInfo[0]["lat"]
    lon = responseInfo[0]["lon"]

    response2 = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + apiKey

    info = requests.get(response2);
    
    wList.append(jtext(int(info.json()["main"]["temp"])-273))
    wList.append(jtext(int(info.json()["main"]["feels_like"])-273))
    wList.append(jtext(int(info.json()["main"]["temp_min"])-273))
    wList.append(jtext(int(info.json()["main"]["temp_max"])-273))
    wList.append(jtext(int(info.json()["main"]["pressure"])))
    wList.append(jtext(int(info.json()["main"]["humidity"])))
    
    return wList