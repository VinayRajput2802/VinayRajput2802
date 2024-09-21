from math import radians, sin, cos, acos
import pandas as pd

    
ans = 0
def find(destination,location):
    destination = destination.lower()
    location = location.lower()
    
    x = pd.read_csv('India Cities LatLng.csv')
    if (destination and location)in list(x['city']):
        city1 = x[x["city"]==destination][["lat","lng"]]
        lat1 = city1["lat"]
        lon1 = city1["lng"]
        city2 = x[x["city"]== location][['lat','lng']]
        lat2 = city2["lat"]
        lon2 = city2['lng']
        mlat = radians(float(lat1))
        mlon = radians(float(lon1))
        plat = radians(float(lat2))
        plon = radians(float(lon2))
        
        ans = int(6371.01 * acos(sin(mlat)*sin(plat) + cos(mlat)*cos(plat)*cos(mlon - plon)))
        
    else:
        print(False)
    return ans
 
    

