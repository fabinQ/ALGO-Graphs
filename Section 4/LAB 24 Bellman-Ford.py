# graph = {
#     'Ciudad Polacca': {'Santo Subito': 15, 'Senderos': 10},
#     'Senderos': {'Dos Rios': 20},
#     'Santo Subito': {'Dos Rios': 5, 'Al Pacino': 50},
#     'Dos Rios': {'Frontera': -5, 'Arboleda': 5},
#     'Frontera': {'Al Pacino': 10},
#     'Arboleda': {'Al Pacino': 10},
#     'Al Pacino': {}
# }
graph = {
 'Ciudad Polacca': {'Santo Subito': 15, 'Senderos': 10},
 'Senderos': {'Dos Rios': 20},
 'Santo Subito': {'Dos Rios': 5, 'Al Pacino': 50},
 'Dos Rios': {'Frontera': 20, 'Arboleda': 5},
 'Frontera': {'Al Pacino': 10},
 'Arboleda': {'Al Pacino': 10},
 'Al Pacino': {}
}

current_node = "Ciudad Polacca"
cost = {}
parents = {}

for name in graph.keys():
    cost[name] = float('inf')
    parents[name] = None

cost[current_node] = 0
def change_cost(graph, cost, parents):
    there_is_change = False

    for node in graph.keys():
        for d, c in graph[node].items():
            if cost[node] != float('inf') and cost[d] > cost[node] + c:
                cost[d] = cost[node] + c
                parents[d] = node
                there_is_change = True
    return there_is_change

for _ in range(len(graph)-1):

    if not change_cost(graph, cost, parents):
        break

if change_cost(graph, cost, parents):
    print('There is a negative cycle.')
else:
    print('There is NOT a negative cycle.')
    for n,m in cost.items():
        print(f'The cost for {n} is {m}')
        current_n = n
        while parents[current_n]:
            print(parents[current_n])
            current_n = parents[current_n]
        else:
            print(current_n)

