# %%
from venv import create
import numpy as np # library to handle data in a vectorized manner

import pandas as pd # library for data analsysis
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

import json # library to handle JSON files

from geopy.geocoders import Nominatim # convert an address into latitude and longitude values
import geocoder # to get coordinates

import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML and XML documents

from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe

# Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors

# import k-means from clustering stage
from sklearn.cluster import KMeans

import folium # map rendering library


def create_map(searchvar):
   # %%
    address = 'Bangalore,India'

    geolocator = Nominatim(user_agent="http")
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude
    print('The geograpical coordinate of Bangalore, India {}, {}.'.format(latitude, longitude))




    # %%
    df = pd.read_csv (r'b_grp.csv')
    pd.set_option('display.max_columns', None)
    df.head()
    #print(df.shape)



    # %%
    b_df = pd.read_csv (r'b_df.csv')
    pd.set_option('display.max_columns', None)
    b_df.head()
    #print(df.shape)


    # %%
    len(df[df[searchvar] > 0])

    # %%
    b_mall = df[["Neighborhoods",searchvar]]
    b_mall.dropna(axis=0)
    b_mall

    # %%
    from sklearn.metrics import accuracy_score
    bclusters = 3


    b_clustering = b_mall.drop(["Neighborhoods"], 1)

    # run k-means clustering
    kmeans = KMeans(n_clusters=bclusters, random_state=0).fit(b_clustering)


    # check cluster labels generated for each row in the dataframe
    kmeans.labels_[0:10]

    # %%
    bmerged = b_mall.copy()

    # add clustering labels
    bmerged["Cluster Labels"] = kmeans.labels_

    # %%

    bmerged.rename(columns={"Neighborhoods": "Neighborhood"}, inplace=True)
    bmerged.head()

    # %%
    bmerged = bmerged.join(b_df.set_index("Neighborhood"), on="Neighborhood")

    print(bmerged.shape)
    bmerged.dropna()
    bmerged.head() # check the last columns!

    # %%
    print(bmerged.shape)
    bmerged.sort_values(["Cluster Labels"], inplace=True)
    ab  = bmerged.dropna(axis=0)
    ab


    # %%
    latitude : ab["Latitude"]
    longitude : ab["Longitude"]
    map_clusters = folium.Map(location=[latitude, longitude], zoom_start=11)

    # set color scheme for the clusters
    x = np.arange(bclusters)
    ys = [i+x+(i*x)**2 for i in range(bclusters)]
    colors_array = cm.rainbow(np.linspace(0, 1, len(ys)))
    rainbow = [colors.rgb2hex(i) for i in colors_array]

    # add markers to the map
    markers_colors = []
    for lat, lon, poi, cluster in zip(ab['Latitude'],ab['Longitude'], ab['Neighborhood'],ab['Cluster Labels']):
        label = folium.Popup(str(poi) + ' - Cluster ' + str(cluster), parse_html=True)
        folium.CircleMarker(
            [lat, lon],
            radius=5,
            popup=label,
            color=rainbow[cluster-1],
            fill=True,
            fill_color=rainbow[cluster-1],
            fill_opacity=0.6).add_to(map_clusters)
        
    map_clusters

    # %%
    map_clusters.save('static/map_clusters.html')


    # %%
    #bmerged.loc[bmerged['Cluster Labels'] == 0]

    # %%
    my_array = np.array(bmerged.loc[bmerged['Cluster Labels'] == 1])
    return my_array
    """ use this list to display at the front page"""

    # %%
    #bmerged.loc[bmerged['Cluster Labels'] == 2]


#create_map("Restaurant")


    # if __name__ == '__main__':
    #     create_map()