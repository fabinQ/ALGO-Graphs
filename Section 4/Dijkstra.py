graph = {
    'A': {'B': 2, 'D': 4},
    'B': {'C': 3, 'D': 3},
    'C': {'E': 2},
    'D': {'C': 3, 'E': 4},
    'E': {}
}

'''
Definiujemy listę kosztów i rodziców.
Algorytm wygląda następująco:
1. Wypełniamy listę wierzchołków inf, żeby waga każdego nieznanego wierzchołka była mniejsza.

2. Stoimy na wierzchołku aktualnym wierzchołku (na początku początkowy) i sprawdzamy gdzie możemy iść. 
Uzupełniamy tabele najtańszym kosztem.

3. Dodajemy wierzchołek do przeprocesowanych.

4. Teraz musimy znaleźć kolejny wierzchołek o najniższym koszcie oraz taki w którym nie byliśmy. 
Przekazujemy koszt (szukamy najmniejszych) oraz przeprocesowane nody (nocy których nie byliśmy).

5. Bierzemy listę kosztów (ten sam case co z tablica inf) porównujemy koszty aby znaleźć najtańszy node 
oraz sprawdzamy czy juz tam byliśmy.

6. Zwracamy jego nazwę i zaczynamy od początku z nowy nodem. 
Wracamy do punktu 2, robimy tak długo aż (tak jak w tym przypadku dojdziemy do końca grafu.

'''
costs = {}
parents = {}


def get_cheapest_node(costs_dict, processed_list):
    '''5. Z listy kosztów (cost_dic) musimy wybrać najtańszy node którego nie ma w przeprocesowanych.
    Aby to zrobić musimy porównać z nieskończonością i schodzić do najniższego kosztu.
    Nazwa najtańszego wierzchołka defoultowo jest None. W razie, gdyby był to ostatni wierzchołek
    zwróci None i pętla while się zakończy.'''
    cheapest_cost = float('inf')
    cheapest_key = None

    for name_, cost in costs_dict.items():
        if name_ not in processed_list and cost < cheapest_cost:
            cheapest_cost = cost
            cheapest_key = name_
    return cheapest_key


for name in graph.keys():
    '''1.Uzupełniamy tablice kosztów na infinity.'''
    costs[name] = float('inf')

'''1.Ustawiamy tablice odwiedzonych wierzchołków oraz wierzchołek startowy.'''
processed = []
current_node = 'A'
costs[current_node] = 0
parents[current_node] = None

'''2.Wypełniamy koszt sąsiadów jeśli jest najmniejszy, czyli jest to taki wierzchołek do którego możemy się dostać nie był on 
przetworzony oraz jest on najtańszy. Warunkiem kontrolnym jest current_node, czyli jeśli jest znany, jeśli nie jest tzn. 
że skończyliśmy'''
while current_node:

    for neighbour in graph[current_node]:
        '''2.Sprawdzamy gdzie możemy isć i ewentualnie aktualizujemy cenę - tylko jeśli znaleźliśmy tańszą drogę. 
        Dlatego inf na początku.'''
        if costs[neighbour] > costs[current_node] + graph[current_node][neighbour]:
            costs[neighbour] = costs[current_node] + graph[current_node][neighbour]
            parents[neighbour] = current_node
    '''4. Gdy odwiedzimy wszystkie dzieci wierzchołka dodajemy go do odwiedzonych. 
    Następnie ustalamy następny najtańszy węzeł (z sumy poprzednich węzełów). '''
    processed.append(current_node)
    current_node = get_cheapest_node(costs, processed)

for d, c in costs.items():
    print(f'The cost for {d} is {c}')
