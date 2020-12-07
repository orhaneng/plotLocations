import gmplot
import pandas as pd


def plott():
    data = pd.read_csv("/Users/omerorhan/Documents/EventDetection/csv/gpsrecords.csv")
    latitude_list = data["latitude"]
    longitude_list = data["longitude"]

    gmap3 = gmplot.GoogleMapPlotter(latitude_list[0],
                                    longitude_list[0], 13)
    gmap3.plot(latitude_list, longitude_list, 'cornflowerblue', edge_width=3.0)

    for index, row in data.iterrows():
        if row['event type'] == 'RIGHT_TURN':
            gmap3.marker(row['latitude'], row["longitude"], color="#FF0000", title="right")
        elif row['event type'] == 'LEFT_TURN':
            gmap3.marker(row['latitude'], row["longitude"], color="#0000FF", title="left")
        elif row['event type'] == 'STOP':
            gmap3.marker(row['latitude'], row["longitude"], color="#ffff00", title="stop")
        elif row['event type'] == 'START':
            gmap3.marker(row['latitude'], row["longitude"], color="#FFFFFF", title="start")

    gmap3.draw("/Users/omerorhan/Documents/EventDetection/csv/map.html")


plott()


def creatingchart():
    import json
    import math
    with open(
            '/Users/omerorhan/Documents/EventDetection/regression_server/amazonnewspeedingevents/jsons/temp.json') as f:
        data = json.load(f)

    from datetime import datetime, timedelta
    round = 0.138889

    end_date = datetime.fromtimestamp(data['route'][len(data['route']) - 1]['timestamp'] / 1000)
    list = []

    for item in data['route']:
        if item['speed'] * 2.2369362920544025 + round > 5:
            start_date = datetime.fromtimestamp(int(item['timestamp'] / 1000))
            break
    while start_date < end_date:
        start_date = (start_date + timedelta(0, 1))
        list.append(start_date)

    df_result = pd.DataFrame(
        columns=['time', 'speed', 'speed_limit', 'speed_limit_plus_15MPH'])

    dict = {}
    for item in data['route']:
        key = math.ceil(item['timestamp'] / 1000)
        key = datetime.fromtimestamp(key)
        dict.update({key: [item]})

    for time in list:
        speed = 0
        speed_limit = 0
        speed_limitplus15 = 0
        if time in dict:
            item = dict[time]
            speed = item[0]['speed'] * 2.2369362920544025 + round
            if 'speedLimit' in item[0]:
                speed_limit = item[0]['speedLimit'] * 2.2369362920544025 + round
                speed_limitplus15 = speed_limit + 15
        df_result = df_result.append(
            {'time': str(time.strftime('%H:%M:%S')), 'speed': speed, 'speed_limit': speed_limit,
             'speed_limit_plus_15MPH': speed_limitplus15}, ignore_index=True)

    df_result['SPEEDING_15'] = 0
    df_result['SPEEDING_20'] = 0

    for events in data['events']:
        if events['eventType'] == 'SPEEDING_15_MPH':
            start_date = datetime.fromtimestamp(events['startTimestamp'] / 1000)
            end_date = datetime.fromtimestamp(events['endTimestamp'] / 1000)
            while start_date < end_date:
                df_result.loc[
                    (df_result['time'] == start_date.strftime('%H:%M:%S')), ['SPEEDING_15']] = [15]
                start_date = (start_date + timedelta(0, 1))
        if events['eventType'] == 'SPEEDING_20_MPH':
            start_date = datetime.fromtimestamp(events['startTimestamp'] / 1000)
            end_date = datetime.fromtimestamp(events['endTimestamp'] / 1000)
            while start_date < end_date:
                df_result.loc[
                    (df_result['time'] == start_date.strftime('%H:%M:%S')), ['SPEEDING_20']] = [20]
                start_date = (start_date + timedelta(0, 1))

    from pandas import read_csv
    from matplotlib import pyplot
    import numpy as np
    df_result.plot(x='time', y=['speed_limit', 'speed', 'speed_limit_plus_15MPH', 'SPEEDING_15'])

    listindex = []
    listdata = []

    for index in range(0, len(df_result)):
        if index % 100 == 0:
            listindex.append(index)
            listdata.append(df_result['time'].to_list()[index])
    pyplot.xticks(listindex, listdata, rotation='vertical')
    pyplot.show()


# creatingchart()


def distanceanalysis():
    data = pd.read_csv(
        "/Users/omerorhan/Documents/EventDetection/regression_server/amazonnewspeedingevents/geotabspeedinglocation100.csv")
    data = data[data[""]]

# distanceanalysis()
