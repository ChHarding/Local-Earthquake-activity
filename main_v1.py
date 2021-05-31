# run this .py file to start the project

#
# fake user input (hard coded for now)
#

# selected location (LA)
lat = 34.052235
lon = -118.243683

# radius (in km)
radius = 70

# max numbers of quakes to show
max_quakes = 20


# 
# request data from the USGS 
#
qparam = {} # make a dict with parameter name (key) and value (string)

# search parameters: see http://earthquake.usgs.gov/fdsnws/event/1/ -> Query method Parameters
qparam["format"]    = "csv" # data format will be a simple csv file
qparam["starttime"] ="1900-01-01" 
qparam["endtime"] = "2020-01-01"
#qparam["minmagnitude"] = "7"  # limit to high magnitudes -> fewer points
qparam["limit"] = str(max_quakes)   
qparam["orderby"]  = "magnitude" 
qparam["latitude"] = str(lat)
qparam["longitude"] = str(lon)
qparam["maxradiuskm"] = str(radius)

# glue together all query parameters
all_query_params = ""
for k in list(sorted(qparam.keys())):
    all_query_params += "&" + k + "=" + qparam[k]



# make full URL with all query parameters
base_URL = "http://earthquake.usgs.gov/fdsnws/event/1/query?"
url = base_URL + all_query_params
print(url)

# how much time has past from request to result?
import datetime

# make request and get result as csv string
import requests
start = datetime.datetime.now()
req = requests.get(url)
req.raise_for_status()
stop = datetime.datetime.now()    
data = req.text # string in csv format
print(f"request took {(stop - start).seconds} seconds")

# convert string data into a  
from io import StringIO
import pandas as pd
df = pd.read_csv(StringIO(data))

# show table, should have a few high mag events
print(df.head())

# save to file (could be use as cache later ...)
df.to_csv(f"quakes_{lat}_{lon}_{radius}.csv") # save it to file so we can view it

# print out some descriptive stats
num_quakes = len(df)
mag = df["mag"]
print(num_quakes, "quakes with min/avg/max", mag.min(), mag.mean(), mag.max())

# find mag of most recent quake
r = df["time"].max() # most recent timestamp
ri = df.set_index('time').index.get_loc(r) # index of most recent row https://stackoverflow.com/questions/16683701/in-pandas-how-to-get-the-index-of-a-known-value
print("most recent quake", r, "had mag", float(df.iloc[[ri]]["mag"]))

#
# Show result on web map (for now just a html file!) 
import folium  # to create a web map

# make a basemap and zoom to an area
map = folium.Map(
    location=[lat, lon], 
    zoom_start=8, #  zoom level, a high number zooms in more 
    tiles= "CartoDB positron"    
    #tiles= "Stamen Terrain"
    #tiles= "Mapbox Control Room"
)

# loop through all rows and get each as a Series
for r in df.iterrows(): 
    i,s = r  # r[1] is a pandas Series, r[0] is the index part 
    
    # text shown when you click on the marker
    text = "Mag. " + str(s['mag']) + " at "+ str(s['time']) 
    
    # red color if most recent else yellow
    color  = "#FFFF00" if i != ri else "#FF0000"

    # <marker>.add_to(map) will add the marker to the map
    folium.CircleMarker(  
        location = [s["latitude"], s["longitude"]],
        radius = 7, # in pixels 
        popup = text,
        color = '#000000', # black outline
        width = 1, # outline width
        fill = True,
        fill_color = color, # yellow interior
        fill_opacity = 0.9,
    ).add_to(map)

# load this into a browser!
map.save('quakemap.html')