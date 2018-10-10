import os
import pandas as pd
import googlemaps
df=pd.read_csv("C:\\csv\\1.csv")
print(df)
gmaps_key=googlemaps.Client(key="AIzaSyDFJNmf0Ynzk_u5QUdQF3klY3mvjXHZHTg")
df['LAN']=None
df['LON']=None
for i in range(0,len(df)):
    geocode_result=gmaps_key.geocode(df.iat[i,0])
    try:
        lat=geocode_result[0]["geometry"]["location"]["lat"]
        lon=geocode_result[0]["geometry"]["location"]["lon"]
        df.iat[i,df.columns.get_loc("LAT")]=lat
        df.iat[i,df.columns.get_loc("LON")]=lon
    except:
        lat=None
        lon=None
