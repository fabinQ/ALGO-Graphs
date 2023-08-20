import csv

network = {}

def is_path_between(V, origin, dest):
    list_to_check = [[origin]]
    list_visited = []
    while list_to_check:
        current_path = list_to_check.pop(0)
        current_node = current_path[-1]
        if current_node == dest:
            return current_path
        else:
            pass


with open('..\\Section 2\\usa-domestic-flight-2019.csv',newline='') as csv_file:
    for i in csv_file:
        spanreader = csv.reader(csv_file, delimiter=',', quotechar='"', skipinitialspace=True)
        for line in spanreader:
            passagers = float(line[0])
            origin = str(line[8])
            destination = str(line[11])
            mounth = int(line[12])

            if origin in network.keys():
                if destination not in network[origin]:
                    network[origin]. append(destination)
            else:
                network[origin]=[destination]

current_keys = list(network.keys())
for origin in network.keys():
    for destination in network[origin]:
        if destination not in network.keys():
            network[destination]=[]

start = 'San Francisco, CA'
stop = 'Vernal, UT'
print(id(start), id(stop))
print(f'connection from {start} to {stop}: {is_path_between(network, start, stop)}')
start = 'Vernal, UT'
stop = 'San Francisco, CA'
print(id(start), id(stop))
print(f"connection from {start} to {stop}: {is_path_between(network, start, stop)}")
start = 'Kotzebue, AK'
stop = 'Danger Bay, AK'
print(id(start), id(stop))
print(f"connection from {start} to {stop}: {is_path_between(network, start, stop)}")