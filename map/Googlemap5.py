import folium
from folium import plugins
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

divvyStations_q3 = pd.read_csv('C:\\csv\\Divvy_Stations_2016_Q3.csv')
divvyStations_q4 = pd.read_csv('C:\\csv\\Divvy_Stations_2016_Q4.csv')

# combine and keep the first instance of id
divvyStations = pd.concat([divvyStations_q3, divvyStations_q4], axis=0).drop_duplicates(subset=['id'])

divvyStations.head()
print(divvyStations)
m = folium.Map([0,0], zoom_start=23)
m
# mark each station as a point
for index, row in divvyStations.iterrows():
    folium.CircleMarker([row['latitude'], row['longitude']],radius=15,popup=row['name'],fill_color="#3db7e4").add_to(m)
m
