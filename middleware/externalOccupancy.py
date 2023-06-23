import requests
import json
import csv
import urllib.parse

def getOccupancy(city):
    dic = {"LA": 'https://data.lacity.org/resource/e7h6-4a3e.json?$query=SELECT%20%60spaceid%60%2C%20%60eventtime%60%2C%20%60occupancystate%60%0AWHERE%20%60occupancystate%60%20IN%20(%22VACANT%22)%0AORDER%20BY%20%60eventtime%60%20DESC%20NULL%20FIRST',
           "SF": 'https://data.sfgov.org/resource/8vzz-qzz9.geojson'}
    response = requests.get(dic[city])
    data = response.json()

    return data


def getOccupancyLaLoc(lat, long):
    spots = []
    # Getting the spaceids of all spots within 1km of requested lat and long
    with open("LA_Parking_Meters.csv") as f:
        dict_reader = csv.DictReader(f)
        for row in dict_reader:
            rowLat, rowLong = float(row['Lat']), float(row['Long'])
            if rowLat <= lat + 0.01 and rowLat >= lat -0.01 and rowLong <= long + 0.01 and rowLong >= long - 0.01:
                spots.append(row['SpaceID'])
    
    query = 'SELECT `spaceid`, `eventtime`, `occupancystate`\nWHERE `spaceid` IN ' + str(tuple(spots)).replace("'", '"') + '\n AND occupancystate="VACANT"\nORDER BY `eventtime` DESC NULL FIRST'
    encodedQuery = urllib.parse.quote(query).replace("%28", "(").replace("%29", ")")
    
    # Returns the data for all OPEN spots within 1km of requested lat and long
    response = requests.get('https://data.lacity.org/resource/e7h6-4a3e.json?$query=' + encodedQuery)
    

    # NEED TO EXTRACT SPACEIDS AND REQUERY FOR LAT AND LONG DATA
     
    data = response.json()
    
    return data