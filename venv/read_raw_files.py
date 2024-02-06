import json
import pandas as pd

# Path to your JSON file
json_file_path = '/Users/omerorhan/Documents/EventDetection/regression_server/regressiontest/tripfiles/comparison/365/702581957/5e268726d67f4e2ea64ec6deef4328df_trip.702581957.1702360569984.bin_v4.gz.json'

# Initialize an empty list to store the data
data_list = []

# Open and read the JSON file
with open(json_file_path, 'r') as file:
    for line in file:
        try:
            json_obj = json.loads(line)
            # Check if both latitude and longitude are in the JSON object
            if 'latitude' in json_obj and 'longitude' in json_obj:
                data_list.append(json_obj)
        except json.JSONDecodeError:
            continue

# Creating a DataFrame from the list
df = pd.DataFrame(data_list)

# Extracting only the latitude and longitude columns
lat_long_df = df[['latitude', 'longitude']]

# Path for the output CSV file
csv_file_path = '/Users/omerorhan/Documents/EventDetection/regression_server/regressiontest/tripfiles/comparison/365/702581957/latitude_longitude.csv'

# Saving the DataFrame to a CSV file
lat_long_df.to_csv(csv_file_path, index=False)

print(f'CSV file created at {csv_file_path}')
