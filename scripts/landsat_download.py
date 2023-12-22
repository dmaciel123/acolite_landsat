from landsatxplore.api import API

# Your USGS  credentials
username = "X"
password = "X"

# Initialize a new API instance
api = API(username, password)

# Perform a request
response = api.request(endpoint="dataset-catalogs")
print(response)
