graph = [
    [1, 4],
    [2, 3, 4],
    [3],
    [],
    [5],
    [],
    [7],
    [6]
]
def has_cycle_to_node(graph, node, visited, path):

    visited[node] = True
    path.append(node)

    for neighbour in graph[node]:
        if not visited[neighbour]:
            if has_cycle_to_node(graph, neighbour, visited, path):
                return True
        if neighbour in path:
            cycle = path.copy()
            while cycle[0] != neighbour:
                del cycle[0]
            cycle.append(neighbour)
            print('cycle: ', cycle)
            return True
    del path[-1]
    return False

def has_cycle(graph):
    visited = [False] * len(graph)
    path = []

    for node in range(len(graph)):
        if not visited[node]:
            if has_cycle_to_node(graph, node, visited, path):
                return True

    return False

if has_cycle(graph):
    print('Graph has a cycle')
else:
    print('Graph has no cycle')