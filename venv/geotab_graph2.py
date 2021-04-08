import matplotlib.pyplot as plt
import json
import copy
import requests
import pandas as pd


def getgraph(x, y, pmevents):
    plt.plot(x, y)
    plt.plot(x, pmevents)
    plt.xlabel("Time")
    plt.ylabel("Speed")
    plt.show()


def getgraphdataframe(dataframe, events):
    plt.plot(dataframe['timeOffset'], dataframe['speed'])
    plt.axvspan(events[0][0], events[0][1], color='red', alpha=0.5)
    # plt.plot(x, pmevents)
    plt.xlabel("Time")
    plt.ylabel("Speed")
    plt.show()


def geotab_graph_geopoints():
    f = open('/Users/omerorhan/Downloads/302686453-17b463eebb344d5cbe08e2eee7235247_reprocessed.json', )
    data = json.load(f)
    pmevents = []

    newgeopoints = []

    pointlen = len(data['route'][0]['geoPoints'])
    startoffset = int(data['route'][0]['geoPoints'][0]['timeOffset'] / 1000)
    endoffset = int(data['route'][0]['geoPoints'][pointlen - 1]['timeOffset'] / 1000)

    for startoffset in range(endoffset):
        newpoint = {'latitude': "", 'longitude': '', 'timeOffset': startoffset * 1000, 'speed': 0.0}
        newgeopoints.append(newpoint)

    newgeopoints = sorted(newgeopoints, key=lambda i: i['timeOffset'])
    pmevents = copy.deepcopy(newgeopoints)

    if 'route' in data and len(data) > 0 and 'geoPoints' in data['route'][0]:
        for point in data['route'][0]['geoPoints']:
            newgeopoints.append(point)
            temp = copy.deepcopy(point)
            temp['speed'] = 0.0
            pmevents.append(temp)

    newgeopoints = sorted(newgeopoints, key=lambda i: i['timeOffset'])
    if 'events' in data:
        for event in data['events']:
            if event['eventType'] == 'PHONE_MANIPULATION':
                startoffset = event['startOffset']
                newpoint = {'latitude': "", 'longitude': '', 'timeOffset': startoffset, 'speed': 3.0}
                pmevents.append(newpoint)
                pmevents.remove(pmevents[0])
                startoffset = int((startoffset + 1000) / 1000)
                endoffset = int(event['endOffset'] / 1000)
                for startoffset in range(startoffset, endoffset):
                    newpoint = {'latitude': "", 'longitude': '', 'timeOffset': startoffset * 1000, 'speed': 3.0}
                    pmevents.append(newpoint)
                    pmevents.remove(pmevents[0])
                newpoint = {'latitude': "", 'longitude': '', 'timeOffset': event['endOffset'], 'speed': 3.0}
                pmevents.append(newpoint)
                pmevents.remove(pmevents[0])
    pmevents = sorted(pmevents, key=lambda i: i['timeOffset'])

    x = [data['timeOffset'] for data in newgeopoints]
    y = [data['speed'] * 2.23694 for data in newgeopoints]
    pmevens = [data['speed'] for data in pmevents]

    plt.plot(x, y)
    plt.plot(x, pmevens)
    plt.show()


geotab_graph_geopoints()

def geotab_graph_dynamo():
    jsonurl = "http://prod-uploader-845833724.us-west-2.elb.amazonaws.com/api/v2/drivers/305300821/trips/305300821-aa9856f1dcd54ad082499cb3aaa75043?facet=all"
    response_json = requests.get(jsonurl).content.decode(
        "utf-8")
    data = json.loads(response_json)

    # f = open('/Users/omerorhan/Downloads/302686453-17b463eebb344d5cbe08e2eee7235247_reprocessed.json', )
    # data = json.load()
    pmevents = []

    newgeopoints = []

    pointlen = len(data['route'])
    startoffset = int(data['route'][0]['timestamp'] / 1000)
    endoffset = int(data['route'][pointlen - 1]['timestamp'] / 1000)

    for offset in range(startoffset, endoffset):
        newpoint = {'timeOffset': offset * 1000, 'speed': 0.0, 'event': 0}
        newgeopoints.append(newpoint)

    newgeopoints = sorted(newgeopoints, key=lambda i: i['timeOffset'])
    pmevents = copy.deepcopy(newgeopoints)

    if 'route' in data and len(data) > 0:
        for point in data['route']:
            point['timeOffset'] = point['timestamp']
            newgeopoints.append(point)
            temp = copy.deepcopy(point)
            temp['speed'] = 0.0
            pmevents.append(temp)

    newgeopoints = sorted(newgeopoints, key=lambda i: i['timeOffset'])
    pmevents = copy.deepcopy(newgeopoints)
    if 'events' in data:
        for event in data['events']:
            if event['eventType'] == 'PHONE_MANIPULATION':
                startoffset = event['startTimestamp']
                newpoint = {'timeOffset': startoffset, 'speed': 10.0, 'event': 10}
                pmevents.append(newpoint)
                pmevents.remove(pmevents[0])
                startoffset = int((startoffset + 1000) / 1000)
                endoffset = int(event['endTimestamp'] / 1000)
                for startoffset in range(startoffset, endoffset):
                    newpoint = {'timeOffset': startoffset * 1000, 'speed': 10.0, 'event': 10}
                    pmevents.append(newpoint)
                    pmevents.remove(pmevents[0])
                newpoint = {'timeOffset': event['endTimestamp'], 'speed': 10.0, 'event': 10}
                pmevents.append(newpoint)
                pmevents.remove(pmevents[0])
    pmevents = sorted(pmevents, key=lambda i: i['timeOffset'])

    dataframe = pd.DataFrame(pmevents)
    # dataframe['speed'] = dataframe['speed']* 2.23694
    # x = [data['timeOffset'] for data in newgeopoints]
    # y = [data['speed'] * 2.23694 for data in newgeopoints]
    # pmevents = [data['speed'] for data in pmevents]

    # getgraph(x, y, pmevents)
    getgraphdataframe(dataframe)


def geotab_graph_dynamonew():
    jsonurl = "http://prod-uploader-845833724.us-west-2.elb.amazonaws.com/api/v2/drivers/305300821/trips/305300821-aa9856f1dcd54ad082499cb3aaa75043?facet=all"
    response_json = requests.get(jsonurl).content.decode(
        "utf-8")
    data = json.loads(response_json)

    newgeopoints = []

    events = []

    if 'events' in data:
        for event in data['events']:
            if event['eventType'] == 'PHONE_MANIPULATION':
                startoffset = event['startTimestamp']
                startnewpoint = {'timeOffset': startoffset, 'speed': 0, 'event': 10}
                # newgeopoints.append(startnewpoint)
                endnewpoint = {'timeOffset': event['endTimestamp'], 'speed': 0, 'event': 10}
                # newgeopoints.append(endnewpoint)
                events.append([event['startTimestamp'], event['endTimestamp']])

    if 'route' in data and len(data) > 0:
        route = data['route']
        for idx, val in enumerate(route):
            if idx + 1 == len(route):
                break
            startflag = False
            endflag = False

            for ev in events:

                if ev[0] >= route[idx]['timestamp'] and ev[0] < route[idx + 1]['timestamp']:
                    newpoint = {'timeOffset': ev[0], 'speed': route[idx]['speed'], 'event': 10}
                    newgeopoints.append(newpoint)
                    startflag = True
                if ev[1] >= route[idx]['timestamp'] and ev[1] < route[idx + 1]['timestamp']:
                    newpoint = {'timeOffset': ev[1], 'speed': route[idx]['speed'], 'event': 10}
                    newgeopoints.append(newpoint)
                    endflag = True
                if startflag and endflag:
                    startflag = False
                    endflag = False
                    continue

            newpoint = {'timeOffset': route[idx]['timestamp'], 'speed': route[idx]['speed'], 'event': 0}
            newgeopoints.append(newpoint)
            if route[idx + 1]['timestamp'] - route[idx]['timestamp'] > 2100:
                temp = route[idx]['timestamp'] + 1000
                while temp < route[idx + 1]['timestamp']:
                    newpoint = {'timeOffset': temp, 'speed': -3.0, 'event': 0}
                    newgeopoints.append(newpoint)
                    temp = temp + 1000

    newgeopoints = sorted(newgeopoints, key=lambda i: i['timeOffset'])
    # pmevents = copy.deepcopy(newgeopoints)

    newgeopoints = sorted(newgeopoints, key=lambda i: i['timeOffset'])

    # pmevents = sorted(pmevents, key=lambda i: i['timeOffset'])

    dataframe = pd.DataFrame(newgeopoints)
    # dataframe['speed'] = dataframe['speed']* 2.23694
    # x = [data['timeOffset'] for data in newgeopoints]
    # y = [data['speed'] * 2.23694 for data in newgeopoints]
    # pmevents = [data['speed'] for data in pmevents]

    # getgraph(x, y, pmevents)
    getgraphdataframe(dataframe, events)


#geotab_graph_dynamonew()


