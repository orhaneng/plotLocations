import matplotlib.pyplot as plt
import json
import copy
import requests
import pandas as pd


def getgraph(x, y, pmevents):
    plt.plot(x, y)
    plt.xlabel("Time")
    plt.ylabel("Speed (MPH)")
    plt.plot(x, pmevents)
    plt.show()


def getgraphdataframe(dataframe, events):
    plt.plot(dataframe['timeOffset'], dataframe['speed'])
    plt.axvspan(events[0][0], events[0][1], color='red', alpha=0.5)
    # plt.plot(x, pmevents)
    plt.xlabel("Time")
    plt.ylabel("Speed")
    plt.show()


def geotab_graph_geopoints():
    f = open('/Users/omerorhan/Downloads/302952908-e963e9e1af704f3f8bb105f0e4fa96e3_reprocessed (1).json', )
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

    dataframe = pd.DataFrame(data['route'][0]['geoPoints'])

    orgdict = copy.deepcopy(data['route'][0]['geoPoints'])
    lasttimestamp = orgdict[len(orgdict) - 1]['timeOffset']
    orgdict.append({'latitude': '', 'longitude': '', 'timeOffset': -1000.0, 'speed': 0.0, 'speedLimit': ''})
    orgdict.append({'latitude': '', 'longitude': '', 'timeOffset': -2000.0, 'speed': 0.0, 'speedLimit': ''})
    orgdict.append({'latitude': '', 'longitude': '', 'timeOffset': -3000.0, 'speed': 0.0, 'speedLimit': ''})

    diclist = data['route'][0]['geoPoints']
    diclist.append({'latitude': '', 'longitude': '', 'timeOffset': -1000.0, 'speed': 0.0, 'speedLimit': ''})
    diclist.append({'latitude': '', 'longitude': '', 'timeOffset': -2000.0, 'speed': 0.0, 'speedLimit': ''})
    diclist.append({'latitude': '', 'longitude': '', 'timeOffset': -3000.0, 'speed': 0.0, 'speedLimit': ''})

    diclist = sorted(diclist, key=lambda i: i['timeOffset'])
    orgdict = sorted(orgdict, key=lambda i: i['timeOffset'])

    orgdictmod = []

    for index, val in enumerate(orgdict):
        if index < 2:
            continue
        orgdict[index-3]['speed'] = orgdict[index]['speed']

    dataframeshifted = pd.DataFrame(diclist)
    orgdataframe = pd.DataFrame(orgdict)

    plt.plot(dataframeshifted['timeOffset'], dataframeshifted['speed'], color='black')
    plt.plot(orgdataframe['timeOffset'], orgdataframe['speed'], color='red')

    # plt.axvspan(events[0][0], events[0][1], color='red', alpha=0.5)
    # plt.plot(x, pmevents)
    plt.xlabel("Time")
    plt.ylabel("Speed")
    plt.show()

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

    # plt.plot(x, y)
    # plt.xlabel("Time")
    # plt.ylabel("Speed (MPH)")
    # plt.plot(x, pmevens)
    # plt.show()


geotab_graph_geopoints()


def geotab_graph_dynamo():
    jsonurl = "http://prod-uploader-845833724.us-west-2.elb.amazonaws.com/api/v2/drivers/305442165/trips/305442165-672071106ae04c27b1c236cb856a3a3b?facet=all"
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
        newpoint = {'latitude': "", 'longitude': '', 'timeOffset': offset * 1000, 'speed': 0.0}
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
    if 'events' in data:
        for event in data['events']:
            if event['eventType'] == 'PHONE_MANIPULATION':
                startoffset = event['startTimestamp']
                newpoint = {'latitude': "", 'longitude': '', 'timeOffset': startoffset, 'speed': 10.0}
                pmevents.append(newpoint)
                pmevents.remove(pmevents[0])
                startoffset = int((startoffset + 1000) / 1000)
                endoffset = int(event['endTimestamp'] / 1000)
                for startoffset in range(startoffset, endoffset):
                    newpoint = {'latitude': "", 'longitude': '', 'timeOffset': startoffset * 1000, 'speed': 10.0}
                    pmevents.append(newpoint)
                    pmevents.remove(pmevents[0])
                newpoint = {'latitude': "", 'longitude': '', 'timeOffset': event['endTimestamp'], 'speed': 10.0}
                pmevents.append(newpoint)
                pmevents.remove(pmevents[0])
    pmevents = sorted(pmevents, key=lambda i: i['timeOffset'])

    x = [data['timeOffset'] for data in newgeopoints]
    y = [data['speed'] * 2.23694 for data in newgeopoints]
    pmevents = [data['speed'] for data in pmevents]

    getgraph(x, y, pmevents)

    # plt.plot(dataframe['timeOffset'], dataframe['speed'])
    # plt.axvspan(events[0][0], events[0][1], color='red', alpha=0.5)
    # plt.plot(x, pmevents)
    # plt.xlabel("Time")
    # plt.ylabel("Speed")
    # plt.show()

#geotab_graph_dynamo()
