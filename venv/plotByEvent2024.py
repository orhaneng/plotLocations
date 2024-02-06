

import pandas as pd
from gmplot import gmplot

# Read the CSV file
file_path = '/Users/omerorhan/Documents/EventDetection/csv/316166060-d8ed152803e94a58bfe3bb225de96de9.csv'
df = pd.read_csv(file_path)

# Assuming the CSV has columns 'GPSlatitude' and 'GPSlongitude'
latitudes = df['GPSlatitude']
longitudes = df['GPSlongitude']

# Create a gmplot instance
# Replace with your Google Maps API key
gmap3 = gmplot.GoogleMapPlotter(latitudes.mean(), longitudes.mean(), 10, apikey='AIzaSyABnjWheegEj3PfzyEV8fqsRSU3XGIuIbg')

# Plot points
gmap3.scatter(latitudes, longitudes, '#FF0000', size=40, marker=False)
for index, row in df.iterrows():
    if row['event'] == 'SPEEDING':
        gmap3.marker(row['GPSlatitude'], row["GPSlongitude"], color="#0000FF", title=row['timestamp'])
# Save the map to a file
gmap3.draw('/Users/omerorhan/Documents/EventDetection/csv/map.html')