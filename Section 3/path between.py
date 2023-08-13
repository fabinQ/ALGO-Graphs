V = {
    'E': ['D1'],
    'D1': ['E', 'D2', 'P'],
    'D2': ['D1', 'P'],
    'P': ['D1', 'D2', 'K', 'Q', 'H'],
    'K': ['P', 'Q', 'H'],
    'Q': ['P', 'K', 'H'],
    'H': ['P', 'Q', 'K']
}

def is_path_between(V, source, dest):
    list_to_check = source
    list_visit = []
    print('list_to_check ', list_to_check)
    print('list_visit ', list_visit)
    while list_to_check:
        curent_node = list_to_check.pop(0)
        print('\tcurent_node ',curent_node)
        if curent_node == dest:
            return True
        else:
            if curent_node not in list_visit:
                list_visit.appdend(curent_node)
            for i in V[curent_node]:
                if V[curent_node] not in list_to_check:
                    list_to_check.append(i)


for n in V.keys():
    for d in V.values():
        is_path_between(V,d,'H')