graph = {
    'A': {'B': 2, 'D': 4},
    'B': {'C': 3, 'D': 3},
    'C': {'E': 2},
    'D': {'C': 3, 'E': 4},
    'E': {}
}

'''Definiujemy listę kosztów i rodziców.'''
costs = {}
parents = {}


def get_cheapest_node(costs_dict, processed_list):
    cheapest_cost = float('inf')
    cheapest_key = None

    for name_, cost in costs_dict.items():
        if name_ not in processed_list and cost < cheapest_cost:
            cheapest_cost = cost
            cheapest_key = name_
    return cheapest_key


for name in graph.keys():
    '''Uzupełniamy tablice kosztów na infinity.'''
    costs[name] = float('inf')

'''Ustawiamy tablice odwiedzonych wierzchołków oraz wierzchołek startowy.'''
processed = []
current_node = 'A'
costs[current_node] = 0
parents[current_node] = None

'''Wybieranie następnego wierzchołka w algorytmie: jest to taki wierzchołek do którego możemy się dostać nie był on 
przetworzony oraz jest on najtańszy. Warunkiem kontrolnym jest current_node, czyli jeśli jest znany, jeśli nie jest tzn. 
że skończyliśmy'''
while current_node:

    for neighbour in graph[current_node]:
        '''Aktualizujemy cenę tylko jeśli znaleźliśmy tańszą drogę. Dlatego inf na początku.'''
        if costs[neighbour] > costs[current_node] + graph[current_node][neighbour]:
            costs[neighbour] = costs[current_node] + graph[current_node][neighbour]
            parents[neighbour] = current_node
    '''Gdy odwiedzimy wszystkie dzieci wierzchołka dodajemy go do odwiedzonych. Następnie ustalamy następny węzeł. '''
    processed.append(current_node)
    current_node = get_cheapest_node(costs, processed)

for d, c in costs.items():
    print(f'The cost for {d} is {c}')
