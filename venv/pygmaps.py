import pygmaps

mymap5 = pygmaps.maps(30.3164945, 78.03219179999999, 15)

latitude_list = [30.343769, 30.307977]
longitude_list = [77.999559, 78.048457]

for i in range(len(latitude_list)):
    mymap5.addpoint(latitude_list[i], longitude_list[i], "# FF0000")

# list of coordinates
path = [(30.343769, 77.999559),
        (30.307977, 78.048457)]

# draw a line in b / w the given coordinates
# 1st argument is list of coordinates
# 2nd argument is colour of the line
mymap5.addpath(path, "# 00FF00")

mymap5.draw('/Users/omerorhan/Documents/EventDetection/csv/pygmap.html')