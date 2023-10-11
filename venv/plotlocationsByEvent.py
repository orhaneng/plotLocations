import gmplot
import pandas as pd
import geopy.distance

#CSVUTILS saveturngpsrecord FUNCTION

def plott():
    data = pd.read_csv("/Users/omerorhan/Documents/EventDetection/JIRA/TLM-783/ecolab_japan/HERE VS HEREJAPAN/305062891-540ba005f9614af79ea5c27fc8c4bb97/305062891-540ba005f9614af79ea5c27fc8c4bb97_HERE.csv")
    data = data.dropna(subset=["SNAPlatitude"])
    data = data.reset_index(drop=True)
    latitude_list = data["SNAPlatitude"]
    longitude_list = data["SNAPlongitude"]


    gmap3 = gmplot.GoogleMapPlotter(latitude_list[0],
                                    longitude_list[0], 18)
    gmap3.scatter(latitude_list, longitude_list, '# FF0000',
                  size=2, marker=False)
    gmap3.plot(latitude_list, longitude_list,
               'red', edge_width=1)
    
    gmap3.plot(latitude_list, longitude_list, 'cornflowerred', edge_width=1.0)

    for index, row in data.iterrows():
        # #if row['confidece'] > 0.0:
        # gmap3.marker(row['latitude'], row["longitude"], color="#ffff00", title=row['snapconfidence'])
        if row['event'] == 'SPEEDING':
            gmap3.marker(row['GPSlatitude'], row["GPSlongitude"], color="#0000FF", title=row['timestamp'])
    #     elif row['Event_id'] == 'STOP':
    #         gmap3.marker(row['latitude'], row["longitude"], color="#ffff00", title=row['timestamp'])
    #     elif row['Event_id'] == 'START':
    #         gmap3.marker(row['latitude'], row["longitude"], color="#FFFFFF", title=row['timestamp'])

    dict = {}

    # for index, row in data.iterrows():
    #
    #     if row['Event_id'] == 'PHONE_MANIPULATION':
    #         gmap3.marker(row['latitude'], row["longitude"], color="#0000FF", title=row['timestamp'])


    print(dict)


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


def getlocations():
    import requests
    import json
    # jsonurl = "http://prod-uploader-845833724.us-west-2.elb.amazonaws.com/api/v2/drivers/303623452/trips/303623452-4e4064e0a434467da251c7528ba0bcd7?facet=all"
    # response_json = requests.get(jsonurl).content.decode(
    #     "utf-8")
    # trip = json.loads(response_json)

    f = open('/Users/omerorhan/Documents/EventDetection/csv/trip.json', )
    trip = json.load(f)

    if 'route' in trip:
        # data = pd.DataFrame(trip['route'])
        data = pd.DataFrame(trip['route'][0]['geoPoints'])
        data.to_csv("/Users/omerorhan/Documents/EventDetection/csv/triplocations.csv")

    print(data)

# getlocations()


#
# data = pd.read_csv("/Users/omerorhan/Documents/EventDetection/csv/turkey/304287611-10eff5aa5a434d99921cc41d0b571689/speedlimitHEREcopy.csv",index_col=False)
# datamap = pd.read_csv("/Users/omerorhan/Documents/EventDetection/csv/turkey/304287611-10eff5aa5a434d99921cc41d0b571689/speedlimit_mapbox.csv",index_col=False)
#
# data = pd.merge(data, datamap, on=['timestamp']).to_csv("/Users/omerorhan/Documents/EventDetection/csv/turkey/304287611-10eff5aa5a434d99921cc41d0b571689/speedlimitmerged.csv")






