graph = [
    [1, 4],
    [2, 3, 4],
    [3],
    [],
    [0, 5],
    [],
    [7],
    [6]
]
def has_cycle_to_node(graph, node, visited, path):
    '''W tabeli visited zmienia swój index na True, oraz dodaje się do path która ustali ścieżkę cyklu.'''
    visited[node] = True
    path.append(node)

    for neighbour in graph[node]:
        '''Przechodzi przez wszystkich sąsiadów noda. Jeśli nie był odwiedzony wywołuje rekurencyjnie swoją funkcję
        dla nowego wierzchołka w głąb. DFS. Jak dochodzi do końca grafu opuszcza pętle for i wycofuje się node wyżej, 
        (del path[-1]) aż do momentu w którym znajdzie się wierzchołek który nie był odwiedzony (zwraca False). '''
        if not visited[neighbour]:
            if has_cycle_to_node(graph, neighbour, visited, path):
                return True
        '''Jeśli sprawdzany wierzchołek był odwiedzony sprawdza się wtedy czy jest w ścieżce. Jeśli jest to szuka się 
        miejsca w którym cykl występuje.'''
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
    ''''
    Ta funkcja sprawdza cykle dla każdego noda w przypadku kiedy graf nie jest spójny
    Tworzy tablice visited które indeksy odpowiadają wierzchołką grafu
    Path jako ścieżka cykli
    '''
    visited = [False] * len(graph)
    path = []

    for node in range(len(graph)):
        '''Jeśli graf nie jest spójny to przejdzie przez wszystkie wierzchołki które nie są w liście już odwiedzonych'''
        if not visited[node]:
            if has_cycle_to_node(graph, node, visited, path):
                '''Przechodzi do funkcji która szuka cykli dla konkretnego noda, przekazując odwiedzoną listę nodów.
                Jeśli funkcja zwróci True to warunek prawdziwy.'''
                return True

    return False

if has_cycle(graph):
    print('Graph has a cycle')
else:
    print('Graph has no cycle')