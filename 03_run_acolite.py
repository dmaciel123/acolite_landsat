# add acolite clone to Python path and import acolite
import sys, os
user_home = os.path.expanduser("~")
sys.path.append(user_home+'/acolite')
import acolite as ac
import pandas as pd
import glob
import numpy as np
from pathlib import Path
import shutil


# list image files with Landsat ids
img_list = pd.read_csv('Outputs/image_list_id.csv')

# load matchups files
matchups = pd.read_csv('Data/Matchups.csv')

## List all available images
# Last time run: 09:27

images_available = os.listdir('Data/downloads')


images_available_selection = [os.path.splitext(x)[0] for x in images_available]


for i in range(0, len(matchups)): 


    matchups_sel = matchups.iloc[i]

    img_id_matchup = img_list[(img_list['GID'] == matchups_sel['ID'])]

    # If ACOLITE avaialble, do:
    if len(img_id_matchup) > 0: 

        img_pos = img_id_matchup

        for k in range(0, len(img_id_matchup)):
        
            img_name = img_pos['display_id'].iloc[k]
            ID_sat = img_pos['GID'].iloc[k]
            sensor = img_pos['Sensor'].iloc[k]

            id_lat = matchups[(matchups['ID'] == ID_sat)]['lat'].iloc[0]
            id_long = matchups[(matchups['ID'] == ID_sat)]['long'].iloc[0]

            limits = (id_lat-0.1, id_long-0.1, id_lat+0.1, id_long+0.1)

            ## Read ACOLITE settings

            settings_file = None

            bundles = 'Data/downloads/'+'/'+img_id_matchup.iloc[(k),(1)] +'.tar'

            odir = 'Processed_Images' + '//' + img_id_matchup.iloc[(k),(1)] + "_" + img_id_matchup.iloc[(k),(7)]
        
            try:
                os.mkdir(path = odir)
                # import settings
                settings = ac.acolite.settings.parse(settings_file)
                # set settings provided above
                settings['limit'] = limits
                settings['inputfile'] = bundles
                settings['output'] = odir
                #settings['l2w_mask_cirrus']=True
                settings['oli_orange_band']=False
                settings['l2r_export_geotiff']=False

                print(i)

                # other settings can also be provided here, e.g.
                # settings['s2_target_res'] = 60
                # settings['dsf_aot_estimate'] = 'fixed'
                # settings['l2w_parameters'] = ['t_nechad', 't_dogliotti']

                # process the current bundle
                ac.acolite.acolite_run(settings=settings)

                path_to_extracted = odir + '//' + img_id_matchup.iloc[(k),(1)]

                try:
                    shutil.rmtree(path_to_extracted)
                    print("Directory removed successfully")
                except OSError as o:
                    print(f"Error, {o.strerror}: {path}")
            except: 
                print(f'Image already processed')










