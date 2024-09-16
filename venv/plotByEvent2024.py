import pandas as pd
from gmplot import gmplot

# Read the CSV file
file_path = '/Users/omerorhan/Documents/EventDetection/csv/gpsrecordsLocationOnOff.csv'
df = pd.read_csv(file_path)

# Assuming the CSV has columns 'latitude', 'longitude', 'event type', and 'timestamp'
latitudes = df['latitude']
longitudes = df['longitude']

# Create a gmplot instance
# Replace with your Google Maps API key
gmap3 = gmplot.GoogleMapPlotter(latitudes.mean(), longitudes.mean(), 10, apikey='AIzaSyABnjWheegEj3PfzyEV8fqsRSU3XGIuIbg')

# Plot points
gmap3.scatter(latitudes, longitudes, '#FF0000', size=5, marker=False)

# # Iterate over the rows to add markers based on event type
# for index, row in df.iterrows():
#     if row['event type'] == 'LOCATION_OFF':
#         gmap3.marker(row['latitude'], row['longitude'], color="#0000FF", title='LOCATION_OFF')
#     if row['event type'] == 'LOCATION_ON':
#         gmap3.marker(row['latitude'], row['longitude'], color="#0000FF", title='LOCATION_ON')

# Add flags at specified timestamps and within ±10000 of those timestamps
timestamps_to_flag = [1714058535022, 1714058542552, 1714058562526]
time_delta = 30000

for timestamp in timestamps_to_flag:
    flag_rows = df[(df['timestamp'] >= timestamp - time_delta) & (df['timestamp'] <= timestamp + time_delta)]
    for index, flag_row in flag_rows.iterrows():
        gmap3.marker(flag_row['latitude'], flag_row['longitude'], color="#FFFF00", title='FLAG')

# Save the map to a file
gmap3.draw('/Users/omerorhan/Documents/EventDetection/csv/map.html')
