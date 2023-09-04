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
    '''Ustawiamy noda na odwiedzonego dodajemy do ścieżki, aby potem móc znaleźć cykl.
    current_neighbours jest to lista nodów dla wierzchołka.'''
    visited[node] = True
    path.append(node)
    current_neighbours = []

    for n in range(len(graph)):
        '''Tutaj szukamy sąsiadów. Bierzemy to z funkcji która wywołuje funkcje, 
        tam zmienia się układ "znajomych" aby znaleźć wierzchołek w którym nie powstaną cykle.'''
        if graph[node][n] == 1:
            current_neighbours.append(n)

    for neighbour in current_neighbours:
        '''Jeśli są znajomi i nie ma na liście visited będzie szukał głębiej. 
        Jeśli nie ma wycofa się ze ścieżki i poszuka innej. '''
        if not visited[neighbour]:
            '''Wywołuje się rekurencyjnie - wchodzi w głąb. Nie trzeba zwracać False bo jest na końcu funkcji.'''
            visited[neighbour] = True
            if has_cycle_to_node(graph, neighbour, visited, path):
                return True
        if neighbour in path:
            '''Jeśli jest node w ścieżce to znajdzie cykl i zwróci True.'''
            cycle = path.copy()
            if cycle[0] != neighbour:
                del cycle[0]
            cycle.append(neighbour)
            print('cycle ',cycle)
            return True
    del path[-1]
    return False


'Początkowy node z którego zaczynamy planować dawanie prezentu.'
source = 4

for candidate in range(len(names)):
    '''Funkcje wywołujemy z wierzchołków - w tym przypadku index-ów tablicy. 
    Path oraz visited dla każdego wierzchołka się czyszczą. 
    Najważniejsza rzecz zmiana połączenia wierzchołka zależnie od candidate.'''
    path = []
    visited = [False] * len(names)
    history[source][candidate] = 1
    '''Jeśli znajdzie cykl zeruje znajomość aby drugi raz nie wywołać funkcji dla tego samego argumentu.
    Jeśli nie znajdzie to wyświetla nazwę kandydata na prezent.'''
    if has_cycle_to_node(history, source, visited, path):
        history[source][candidate] = 0
    else:
        history[source][candidate] = 0
        print("It's works!")
        print(f'You can give gift to {names[candidate]}')
