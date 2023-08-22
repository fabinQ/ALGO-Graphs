V = {
    'E': ['D1'],
    'D1': ['E', 'D2', 'P'],
    'D2': ['D1', 'P'],
    'P': ['D1', 'D2', 'K', 'Q', 'H'],
    'K': ['P', 'Q', 'H'],
    'Q': ['P', 'K', 'H'],
    'H': ['P', 'Q', 'K']
}

def is_path_between(V,source, dest):
    list_to_check = [source]
    list_visited = []
    while list_to_check:
        curent_node = list_to_check.pop(0)
        if curent_node == dest:
            return True
        else:
            if curent_node not in list_visited:
                list_visited.append(curent_node)
                for element in V[curent_node]:
                    if element not in list_visited and not list_to_check :
                        list_to_check.append(element)
            # print('curent_node ', curent_node)
            # print('list_to_check ', list_to_check)
            # print('list_visited ', list_visited)
            # print()
    return False


# for s in V.keys():
#     for d in V.keys():
#         if s != d:
#             print(f' Path {s} - {d} = ', is_path_between(V, s, d))
print(' Path E - H = ', is_path_between(V, 'E', 'H'))
