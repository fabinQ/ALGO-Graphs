import csv
from operator import itemgetter
network ={}

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

    print('Number of airports: ',len(network.keys()))

    out_degrees = []
    for origin, destination in network.items():
        out_degrees.append({'name':origin, 'connections':len(destination)})

    print(max(out_degrees, key=lambda x: x['connections']),'\n')      # zwracanie max połączeń przez klucz i lambda czyli connections

    out_degrees.sort(key=itemgetter('connections'), reverse=True)   #funckja itemgetter też sortuje po connections
    for i in out_degrees[:10]:
        print(i['name'], i['connections'])
