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
    pass

current_node = "Ciudad Polacca"
cost = {}
parents = {}
processed = []

for node in graph.keys():
    cost[node] = float('int')

while current_node:

    for neighbour in graph[current_node]:
        if cost[neighbour] > cost[current_node] + graph[current_node][neighbour]:
            cost[neighbour] = cost[current_node] + graph[current_node][neighbour]
            parents[neighbour] = current_node
        processed.append(current_node)
        current_node = get_cheapest_node(cost, processed)
