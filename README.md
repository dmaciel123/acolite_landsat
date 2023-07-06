# Automatic download and process Landsat data with ACOLITE

This script will allow you to automatic download and process Landsat data using ACOLITE atmospheric correction method. The ACOLITE is focused on inland and coastal waters and should be used for this purpose. If you are intereseted in land targets, you can download the Landsat Collection 2 Level 2 surface reflectance data. 

For automatic downloading Landsat data from USGS you need to have an USGS account allowed to use the USGS API M2M (Machine-to-Machine). For more information, click here (https://m2m.cr.usgs.gov/api/docs/json/).

For downloading Landsat data, two scripts will be used:

1. 01_list_images.py

This script will list all Landsat images available in a determined time interval (based on a date supplied in a .CSV file) and a latitude and longitude. The result is a .CSV file with Landsat ID images listed, path, row and other informations. This should be run first.

2. 02_download.py

This script will download Landsat data based on the file created in script number 01. 

3. 03_run_acolite.py

This script will run ACOLITE for each image downloaded based on the matchups.csv file. 

More information about these methods could be obtained from Vanhllemont and Ruddick (2016) and Maciel et al. (2023). 


Acknowledgments:

These scripts were developed using 
