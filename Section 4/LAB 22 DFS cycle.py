names = ['Dad', 'Mum', 'Grandma', 'Grandpa','Doughter', 'Son']
history = [
    [0,1,0,0,0,0], # Dad
    [0,0,1,0,0,0], # Mum
    [0,0,0,0,1,0], # Grandma
    [0,0,0,0,0,0], # Grandpa
    [0,0,0,0,0,0], # Doughter
    [0,0,0,0,0,0] # Son
]

def has_cycle_to_node(graph, node, visited, path):

    visited[node] = True
    path.append(node)
    current_neighbours = []

    for n in range(len(graph)):
        # print('neighbours ', neighbours)
        # print(graph[node][neighbours])
        if graph[node][n] == 1:
            current_neighbours.append(n)

    for neighbour in current_neighbours:
        print(neighbour, visited[neighbour])
        if not visited[neighbour]:
            visited[neighbour] = True
            if has_cycle_to_node(graph, neighbour, visited, path):
                return True
    if neighbour in path:
        cycle = path.copy()
        if cycle[0] != neighbour:
            del cycle[0]
        cycle.append(neighbour)
        print('cycle ',cycle)
    del path[-1]
    return False


source = 4

for candidate in range(len(names)):
    path = []
    visited = [False] * len(names)
    history[source][candidate] = 1
    # print(candidate,'\n')
    # if candidate not in visited[candidate]:
    if not has_cycle_to_node(history, source, visited, path):
        history[source][candidate] = 0
    else:
        print("Udało się!")
        print()
