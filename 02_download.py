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
from landsatxplore.earthexplorer import EarthExplorer
import os

image_list = pd.read_csv('Outputs/image_list_id.csv')

image_list = image_list.drop_duplicates()

image_list = image_list.reset_index(drop=True)

# Initialize the API

# Your USGS  credentials
username = "XX"
password = "XXX"

ee = EarthExplorer(username, password)

# stoped at

#LC08_L1TP_193028_20150715_20200908_02_T1

for i in range(0, len(image_list)):


    list_filter = image_list.loc[i]
    # Select the first scene
    ID = list_filter['display_id']

    # Download the scene 
    try: 
        ee.download(ID, output_dir='./data/downloads')
        print('{} succesful'.format(ID))
        print(i)
    # Additional error handling
    except:
        if os.path.isfile('./data/downloads/{}.tar'.format(ID)):
            print('{} error but file exists'.format(ID))
        else:
            print('{} error'.format(ID))

    #ee.logout()
