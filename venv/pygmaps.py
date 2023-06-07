# import pygmaps
#
# mymap5 = pygmaps.maps(30.3164945, 78.03219179999999, 15)
#
# latitude_list = [30.343769, 30.307977]
# longitude_list = [77.999559, 78.048457]
#
# for i in range(len(latitude_list)):
#     mymap5.addpoint(latitude_list[i], longitude_list[i], "# FF0000")
#
# # list of coordinates
# path = [(30.343769, 77.999559),
#         (30.307977, 78.048457)]
#
# # draw a line in b / w the given coordinates
# # 1st argument is list of coordinates
# # 2nd argument is colour of the line
# mymap5.addpath(path, "# 00FF00")
#
# mymap5.draw('/Users/omerorhan/Documents/EventDetection/csv/pygmap.html')

def createHistogram():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np

    # Load CSV data into a Pandas DataFrame
    data = pd.read_csv('/Users/omerorhan/Documents/EventDetection/JIRA/ME-2837/result.csv')
    data = data[(data['status_after'] == 'SUCCESS') | (data['status_after'] == 'UNSUPPORTED_MODE')]

    # Extract the column of interest
    snappingratio_after = data['snappingratio_after']

    # Define the histogram bins to include every 0.05 from the minimum to maximum value
    min_val = np.floor(snappingratio_after.min() * 20) / 20
    max_val = np.ceil(snappingratio_after.max() * 20) / 20
    bins = np.arange(min_val, max_val + 0.05, 0.05)

    # Set up histogram
    n, bins, patches = plt.hist(snappingratio_after, bins=bins, edgecolor='black', linewidth=1.2)

    # Set count labels on bars
    for i in range(len(patches)):
        plt.text(x=bins[i] + (bins[i + 1] - bins[i]) / 2, y=n[i] + 1, s=int(n[i]), ha='center')

    # Set axis labels and title
    plt.xlabel('Snapping Ratio')
    plt.ylabel('Count')
    plt.title('Distribution of Snapping Ratio - Cargill India - ' + " (Total Unsupported Trip Count:" + str(
        len(snappingratio_after)) + ")")

    # Set different color borders for bars
    for i in range(len(patches)):
        patches[i].set_edgecolor(plt.cm.Set1(i / len(patches)))

    # Set the tick locations and labels for the x-axis
    tick_locs = np.arange(min_val, max_val + 0.05, 0.05)
    tick_labels = [f'{x:.2f}' for x in tick_locs]
    plt.xticks(tick_locs, tick_labels, rotation=90)

    # Show the histogram
    plt.show()


createHistogram()

def createbarchart():
    import pandas as pd
    import matplotlib.pyplot as plt

    # Load CSV data into a Pandas DataFrame
    data = pd.read_csv('/Users/omerorhan/Documents/EventDetection/JIRA/ME-2837/result.csv')

    # Extract the column of interest
    status_after = data['status_after']

    # Get the counts of each unique value
    value_counts = status_after.value_counts()

    # Create a bar chart
    plt.bar(value_counts.index, value_counts)

    # Add count values on top of each bar
    for i, v in enumerate(value_counts):
        plt.text(i, v + 50, str(v), ha='center')

    # Set axis labels and title
    plt.xlabel('Status')
    plt.ylabel('Count')
    plt.title('Count of Status- Cargill India' + " (Total Unsupported Trip Count:" + str(
        len(data['snappingratio_after'])) + ")")

    # Show the chart
    plt.show()

#createbarchart()
