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
    list_visit = []
    # print('list_to_check ', list_to_check)
    # print('list_visit ', list_visit)
    while list_to_check:
        curent_node = list_to_check.pop(0)
        # print('\tlist_to_check pop ',list_to_check)
        # print('\tlist_visit ', list_visit)
        # print('\tcurent_node ',curent_node)
        if curent_node == dest:
            # print('BINGO!')
            return True
        else:
            if curent_node not in list_visit:
                list_visit.append(curent_node)
                list_to_check.extend(V[curent_node])
            print('\t\tlist_to_check ', list_to_check)
            print('\t\tlist_visit ', list_visit)
            print('\t\tcurent_node ', curent_node)
    return False


for s in V.keys():
    for d in V.keys():
        if s != d:
            print(f' Path {s} - {d} = ', is_path_between(V, s, d))
print(' Path E - H = ', is_path_between(V, 'E', 'H'))
