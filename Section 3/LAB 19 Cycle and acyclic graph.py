why_not = {
    'no time' : ['classify priorities'],
    'classify priorities' : [],
    'no training' : ['attend training'],
    'attend training': ['no time', 'no money motivation'],
    'no expirience' : ['work on a project'],
    'work on a project' : ['no time', 'no training', 'no expirience'],
    'no money motivation' : ['work on a project']
}

def get_path_between(V, source, dest):
    list_to_check = [[source]]
    list_visited = []
    while list_to_check:
        curent_path = list_to_check.pop(0)
        curent_node = curent_path[-1]

        if curent_node == dest:
            return curent_path
        else:
            if curent_node not in list_visited:
                list_visited.append(curent_node)
                for element in V[curent_node]:
                    new_path = curent_path.copy()
                    new_path.append(element)
                    list_to_check.append(new_path)
    return []

def get_cycle(graph, node):

    for element in graph[node]:
        path = get_path_between(graph, element, node)
        if path:
            return path
    return []

def is_cycle(graph):

    for node in graph:
        if get_cycle(graph,node):
            return True
    return False

print(f'Cycle path in graph? {is_cycle(why_not)}')