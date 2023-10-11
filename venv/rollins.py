import os
import folium
import pandas as pd
import random
import os
import gmplot
import pandas as pd
gmap = gmplot.GoogleMapPlotter(0, 0, 2)

# Create a map object
m = folium.Map(location=[0, 0], zoom_start=2)

# Directory where the CSV files are located
csv_dir = "/Users/omerorhan/Documents/EventDetection/csv/7d23391ba5f94ece9be3a2e6970e7ebb/"

# Create a map object
# Define a list of colors for each part
# Initialize a list to store tooltip information
tooltips = []

# Define a list of colors for each part
colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF', '#800000']

# Iterate over the CSV files in the directory
for index, file in enumerate(os.listdir(csv_dir)):
    if file.endswith(".csv"):
        # Read the CSV file using pandas
        data = pd.read_csv(os.path.join(csv_dir, file))

        # Extract latitude and longitude columns from the data
        latitudes = data['latitude']
        longitudes = data['longitude']

        # Generate a random color
        color = colors[index % len(colors)]

        # Plot the data using gmplot
        for lat, lon in zip(latitudes, longitudes):
            gmap.marker(lat, lon, title=file, color=color)

        # Store tooltip information
        tooltips.append((file, color))

# Save the map as an HTML file
gmap.draw("map.html")

# Create an interactive map using folium
m = folium.Map(location=[0, 0], zoom_start=2)

# Add markers with tooltips using folium
for tooltip, color in tooltips:
    folium.Marker(location=[0, 0], tooltip=tooltip, icon=folium.Icon(color=color)).add_to(m)

# Save the map as an HTML file
gmap.draw("/Users/omerorhan/Documents/EventDetection/csv/map.html")




