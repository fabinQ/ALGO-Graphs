graph = {
    "Ciudad Polacca": {"Santo Subito": 15, "Senderos": 10},
    "Senderos": {"Dos Rios": 20},
    "Santo Subito": {"Al. Pacino": 50, "Dos Rios": 5},
    "Dos Rios": {"Frontera": 20, "Arboleda": 5},
    "Frontera": {"Al. Pacino": 10},
    "Arboleda": {"Al. Pacino": 10},
    "Al. Pacino": {}
}

def get_cheapest_node(cost_dic, procesed_list):
    cheapest_cost = float('inf')
    cheapest_name = None

    for name, cost in cost_dic.items():
        if name not in procesed_list and cost < cheapest_cost:
            cheapest_cost = cost
            cheapest_name = name

    return cheapest_name

current_node = "Ciudad Polacca"
cost = {}
parents = {}
processed = []

for node in graph.keys():
    cost[node] = float('inf')
cost[current_node] = 0

while current_node:

    for neighbour in graph[current_node]:
        if cost[neighbour] > cost[current_node] + graph[current_node][neighbour]:
            cost[neighbour] = cost[current_node] + graph[current_node][neighbour]
            parents[neighbour] = current_node
    processed.append(current_node)
    current_node = get_cheapest_node(cost, processed)

def get_road(graph, start, dest):
    road = [start]
    while road[-1] != dest:
        if road[-1] not in graph:
            return None
        road.append(graph[road[-1]])
    road.reverse()
    return road

current_start = 'Ciudad Polacca'
current_destination = 'Al. Pacino'
road = get_road(parents, current_destination, current_start)
for i in road:
    print('To {} cost {}'.format(i, cost[i]))