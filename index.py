import requests as rq
import openpyxl
import os
mapbox_url = 'https://api.mapbox.com/geocoding/v5/mapbox.places/{country_name}.json'
param = {
    'access_token': 'pk.eyJ1IjoicmFjYW5lMTIzIiwiYSI6ImNscDJhZ2xmbDBwdmEybG9pa2w4Yms0emEifQ.vyLoKd0CBDl14MKI_9JDCQ'
}
country_name = 'Philippines'

response = rq.get(mapbox_url.format(country_name=country_name), params=param)

if response.status_code == 200:
    data = response.json()

    if data['features'] and data['features'][0]['place_name'] == 'Philippines':
        # Get the desktop path
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

        # Create a new Excel workbook
        excel_filename = os.path.join(desktop_path, 'output.xlsx')
        workbook = openpyxl.Workbook()
        sheet = workbook.active

        # Write headers to the first row
        headers = list(data['features'][0]['properties'].keys())
        sheet.append(headers)

        # Write data to the subsequent rows
        for feature in data['features']:
            properties = feature.get('properties', {})
            row_data = [properties.get(header, '') for header in headers]
            sheet.append(row_data)

        # Save the Excel file to the desktop
        workbook.save(excel_filename)
        print(f"Data has been successfully stored in '{excel_filename}'.")
    else:
        print('No data found for Cebu in the Mapbox response.')
else:
    print('Request failed with status code:', response.status_code)