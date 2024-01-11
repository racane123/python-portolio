
import requests
import pandas as pd
import os
mapbox_url = 'https://api.mapbox.com/geocoding/v5/mapbox.places/{country_name}.json'
param = {
    'access_token': 'pk.eyJ1IjoicmFjYW5lMTIzIiwiYSI6ImNscDJhZ2xmbDBwdmEybG9pa2w4Yms0emEifQ.vyLoKd0CBDl14MKI_9JDCQ'
}
country_name = 'Philippines'

url = mapbox_url.format(country_name=country_name)

# Send the API request
response = requests.get(url, params=param)

# Get the JSON response
json_data = response.json()

# Extract relevant information from the JSON response
places = json_data['features']
data = []
for place in places:
    place_name = place['place_name']
    place_type = place['properties'].get('category', 'N/A')
    coordinates = place['geometry']['coordinates']
    data.append([place_name, place_type, coordinates[0], coordinates[1]])

# Create a DataFrame from the extracted data
df = pd.DataFrame(data, columns=['Place Name', 'Place Type', 'Longitude', 'Latitude'])

# Save the DataFrame to an Excel file on the desktop
desktop_path = os.path.expanduser("~/Desktop")
file_path = os.path.join(desktop_path, 'geocoding_data.xlsx')
df.to_excel(file_path, index=False)