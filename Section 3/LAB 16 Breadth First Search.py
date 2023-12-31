import csv
network = {}


def is_path_between(V, source, dest):
    list_to_check = [source]
    list_visited = []

    while list_to_check:
        current_node = list_to_check.pop(0)
        if current_node == dest:
            return True
        else:
            list_visited.append(current_node)
            for i in V[current_node]:
                if i not in list_to_check and list_visited:
                    list_to_check.append(i)
    return False


with open('..\\Section 2\\usa-domestic-flight-2019.csv',newline='') as csv_file:
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