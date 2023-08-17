import csv
from operator import itemgetter
network ={}


def is_path_between():
    pass

with open('usa-domestic-flight-2019.csv',newline='') as csv_file:
    spanreader = csv.reader(csv_file,delimiter=',',quotechar='"', skipinitialspace=True)
    next(spanreader)
    for line in spanreader:
        passengers = float(line[0])
        origin = line[8]
        destination = line[11]
        mounth = int(line[12])

        # if mounth == 1 and passengers != 0:
        if origin in network.keys():
            if destination not in network[origin]:
                network[origin].append(destination)
        else:
            network[origin] = [destination]

current_keys = list(network.keys())
for origin in current_keys:
    for destination in network[origin]:
        if destination not in network.keys():
            network[destination] = []
