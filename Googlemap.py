import tkinter as tk
import pandas as pd
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
print("hi")
plt.figure(figsize=(14, 14))
m = Basemap(llcrnrlat = 30,
            llcrnrlon = -126,
            urcrnrlat = 45,
            urcrnrlon = -114,
           resolution='h')
# Get the area of interest imagery
m.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 2500, verbose= True,alpha= .6)
# Draw the coasts
m.drawcoastlines(color='blu', linewidth=3)
# Draw the states
m.drawstates(color='red',linewidth=3)
