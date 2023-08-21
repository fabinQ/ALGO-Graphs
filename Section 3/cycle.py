actions1 = {
    'F1': ['F2','F3'],
    'F2': ['F4'],
    'F3': ['F4'],
    'F4': []
}
actions2 = {
    'F1': ['F2', 'F3'],
    'F2': [],
    'F3': ['F4'],
    'F4': ['F1']
}

# Młody patrz na to
# https://www.youtube.com/watch?v=dQw4w9WgXcQ

def get_path_between(V, source, dest):
    list_to_check = [[source]]
    list_visited = []

    while list_to_check:
        current_path = list_to_check.pop(0)
        current_node = current_path[-1]
        if current_node == dest:
            return current_path
        else:
            if current_node not in list_visited:
                list_visited.append(current_node)
                for elements in V[current_node]:
                    new_path = current_path.copy()
                    new_path.append(elements)
                    list_to_check.append(new_path)
    return []


def get_cycle(graph, node):

    for neighbour in graph[node]:
        path = get_path_between(graph, neighbour, node)
        if path:
            return path
    return []

start = 'F1'

print(f'Path from {start} to {start} is {get_cycle(actions1,start)}')
print(f'Path from {start} to {start} is {get_cycle(actions2,start)}')