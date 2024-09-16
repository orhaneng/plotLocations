# import pandas as pd
# from gmplot import gmplot
#
# # Read the CSV file
# file_path = '/Users/omerorhan/Documents/EventDetection/csv/702581957-5e268726d67f4e2ea64ec6deef4328df.csv'
# df = pd.read_csv(file_path)
#
# # Assuming the CSV has columns 'GPSlatitude' and 'GPSlongitude'
# latitudes = df['GPSlatitude']
# longitudes = df['GPSlongitude']
#
# # Create a gmplot instance
# # Replace with your Google Maps API key
# gmap = gmplot.GoogleMapPlotter(latitudes.mean(), longitudes.mean(), 10, apikey='AIzaSyABnjWheegEj3PfzyEV8fqsRSU3XGIuIbg')
#
# # Plot points
# gmap.scatter(latitudes, longitudes, '#FF0000', size=40, marker=False)
#
# # Save the map to a file
# gmap.draw('/Users/omerorhan/Documents/EventDetection/csv/map.html')


#
# import pandas as pd
# from gmplot import gmplot
#
# # Read the CSV file
# file_path = '/Users/omerorhan/Documents/EventDetection/csv/315382144-8c43f2cd17304d358db3199f40e50eae.csv'
# df = pd.read_csv(file_path)
#
# # Assuming the CSV has columns 'GPSlatitude' and 'GPSlongitude'
# latitudes = df['GPSlatitude']
# longitudes = df['GPSlongitude']
#
# # Create a gmplot instance
# # Replace with your Google Maps API key
# gmap3 = gmplot.GoogleMapPlotter(latitudes.mean(), longitudes.mean(), 10, apikey='AIzaSyABnjWheegEj3PfzyEV8fqsRSU3XGIuIbg')
#
# # Plot points
# gmap3.scatter(latitudes, longitudes, '#FF0000', size=40, marker=False)
#
# # Save the map to a file
# gmap3.draw('/Users/omerorhan/Documents/EventDetection/csv/map.html')





import pandas as pd
import gmplot
#
# # Read the CSV file
# file_path = '/Users/omerorhan/Documents/EventDetection/csv/gpsrecords.csv'
# df = pd.read_csv(file_path)
#
# # Assuming the CSV has columns 'GPSlatitude', 'GPSlongitude', and 'timestamp'
# latitudes = df['latitude']
# longitudes = df['longitude']
# timestamps = df['timestamp']  # Your timestamp column
#
# # Create a gmplot instance
# gmap3 = gmplot.GoogleMapPlotter(latitudes.mean(), longitudes.mean(), 10, apikey='AIzaSyABnjWheegEj3PfzyEV8fqsRSU3XGIuIbg')
# gmap3.scatter(latitudes, longitudes, '#FF0000', size=5, marker=False)
#
# # # Plot points with hover text
# # for lat, lon, timestamp in zip(latitudes, longitudes, timestamps):
# #     gmap3.marker(lat, lon, title=str(timestamp))
#
# # Save the map to a file
# map_file = '/Users/omerorhan/Documents/EventDetection/csv/map.html'
# gmap3.draw(map_file)



import pandas as pd
from gmplot import gmplot

# Read the file containing latitude, longitude, and timestamp
file_path = '/Users/omerorhan/Downloads/locations_and_timestamps.txt'
data = []
with open(file_path, 'r') as f:
    for line in f:
        parts = line.strip().split(', ')
        latitude = float(parts[0].split(': ')[1])
        longitude = float(parts[1].split(': ')[1])
        timestamp = int(parts[2].split(': ')[1])
        data.append((latitude, longitude, timestamp))

# Convert to a DataFrame
df = pd.DataFrame(data, columns=['latitude', 'longitude', 'timestamp'])

# Sort the DataFrame by timestamp
df = df.sort_values(by='timestamp')

# Extract latitudes, longitudes, and timestamps
latitudes = df['latitude']
longitudes = df['longitude']
timestamps = df['timestamp']  # Your timestamp column

# Create a gmplot instance
gmap3 = gmplot.GoogleMapPlotter(latitudes.mean(), longitudes.mean(), 10, apikey='AIzaSyABnjWheegEj3PfzyEV8fqsRSU3XGIuIbg')
gmap3.scatter(latitudes, longitudes, '#FF0000', size=5, marker=False)

# Optionally, add markers with timestamps as titles
for lat, lon, timestamp in zip(latitudes, longitudes, timestamps):
    gmap3.marker(lat, lon, title=str(timestamp))

# Save the map to a file
map_file = '/Users/omerorhan/Downloads/map.html'
gmap3.draw(map_file)

print(f"Map saved to: {map_file}")
