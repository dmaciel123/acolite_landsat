from landsatxplore.api import API

# Your USGS  credentials
username = "dmaciel123"
password = "Madaisa1234$"

# Initialize a new API instance
api = API(username, password)

# Perform a request
response = api.request(endpoint="dataset-catalogs")
print(response)