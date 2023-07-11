# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:10:06 2022

@author: damac
"""


import pandas as pd
import numpy as np
from landsatxplore.api import API
import datetime as dt
from landsatxplore.earthexplorer import EarthExplorer
import os

# Load data
rrs_data = pd.read_csv('Data/matchups.csv')

# Your USGS  credentials
username = "XXX"
password = "XXX$"

# Initialize a new API instance
api = API(username, password)



for i in range(0, len(rrs_data)):

    data_run = rrs_data.iloc[i,]

    lat = data_run['lat']
    long = data_run['long']
    date = data_run['Date']

    # Date in the example is in the formatÇ
    a = dt.datetime.strptime(date, "%Y-%m-%d")

    # Sum X days to time-interval
    start_date = a+dt.timedelta(days=-6)
    end_date = a+dt.timedelta(days=6)

    start_date = start_date.strftime("%Y-%m-%d")
    end_date = end_date.strftime("%Y-%m-%d")

    # Search for Landsat scenes

    ## IDs: TM: landsat_tm_c2_l1
    ## ETM+: landsat_etm_c2_l1
    ## OLI: landsat_ot_c2_l1
    ## OLI-2 landsat_ot_c2_l1

    sensor = "TM"


    if sensor == 'TM':
        sensor_id = 'landsat_tm_c2_l1'

    if sensor == 'ETM+':
        sensor_id = 'landsat_etm_c2_l1'   

    if sensor == 'OLI':
        sensor_id = 'landsat_ot_c2_l1'

    if sensor == 'OLI2':
        sensor_id = 'landsat_ot_c2_l1'

    scenes = api.search(
        dataset=sensor_id,
        latitude=lat,
        longitude=long,
        start_date=start_date,
        end_date=end_date)

    print(i)
    
    if len(scenes) > 0:

        # Create a DataFrame from the scenes
        df_scenes = pd.DataFrame(scenes)
        df_scenes = df_scenes[['display_id','wrs_path', 'wrs_row','satellite','cloud_cover','acquisition_date']]
        df_scenes.sort_values('acquisition_date', ascending=False, inplace=True)
        df_scenes[['GID']] = data_run[['ID']]
        df_scenes[['Sensor']] = sensor

        if i == 0:
            matchups_df = df_scenes

        if i > 0:
            matchups_df = matchups_df.append(df_scenes)


pd.DataFrame(matchups_df).to_csv('Outputs/image_list_id.csv')




