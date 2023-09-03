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
        if not neighbour in visited:
            print(neighbour)
            # pass
            # has_cycle_to_node(graph, neighbour, visited, path)

source = 4

for candidate in range(len(names)):
    path = []
    visited = [False] * len(names)
    history[source][candidate] = 1
    # print(candidate,'\n')
    # if candidate not in visited[candidate]:
    has_cycle_to_node(history, source, visited, path)
