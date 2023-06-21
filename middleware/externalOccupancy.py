import requests
import json


def getOccupancy(city):
    dic = {"LA": 'https://data.lacity.org/resource/e7h6-4a3e.json?$query=SELECT%20%60spaceid%60%2C%20%60eventtime%60%2C%20%60occupancystate%60%0AWHERE%20%60occupancystate%60%20IN%20(%22VACANT%22)%0AORDER%20BY%20%60eventtime%60%20DESC%20NULL%20FIRST',
           "SF": 'https://data.sfgov.org/resource/8vzz-qzz9.geojson'}
    response = requests.get(dic[city])
    data = response.json()

    return data