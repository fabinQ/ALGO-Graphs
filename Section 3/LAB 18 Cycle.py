why_not = {
    'no time' : ['classify priorities'],
    'classify priorities' : [],
    'no training' : ['attend training'],
    'attend training': ['no time', 'no money motivation'],
    'no expirience' : ['work on a project'],
    'work on a project' : ['no time', 'no training', 'no expirience'],
    'no money motivation' : ['work on a project']
}

def get_path_between (V,souce, dest):
    list_to_check = [[souce]]
    list_visited = []

    while list_to_check:
        current_path = list_to_check.pop(0)
        current_node = current_path[-1]

        if current_node == dest:
            return current_path
        else:
            if current_node not in list_visited:
                list_visited.append(current_node)
                for element in V[current_node]:
                    new_path = current_path.copy()
                    new_path.append(element)
                    list_to_check.append(new_path)
    return []

def get_cycle(graph, orgin):

    for elements in graph[orgin]:
        path = get_path_between(graph, elements, orgin)
        if path:
            return path
    return []

for stements in why_not.keys():
    print(f'Path from {stements} to{stements} is {get_cycle(why_not,stements)}')