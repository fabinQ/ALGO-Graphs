g = {
    'E': ['D1'],
    'D1': ['E', 'D2', 'P'],
    'D2': ['D1', 'P'],
    'P': ['D1', 'D2', 'K', 'Q', 'H'],
    'K': ['P', 'Q', 'H'],
    'Q': ['P', 'K', 'H'],
    'H': ['P', 'Q', 'K']
}
'''
Potrzebujemy 3 zmiennych R,P,X. 
R jest zbiorem który zawiera coraz mniejsze zbiory aby znaleźć klikę.
P jest zbiorem wszystkich wierzchołków, ponieważ zakłądamy że wszyscy są w jednej klice.
X jest zbiorem kontrolnym.

1.  Na początku tworzymy trzy zbiory: R, P i X. R to zbiór wierzchołków, które są aktualnie rozważane jako część kliki. 
    P to zbiór wierzchołków, które mogą być dodane do R w celu utworzenia większej kliki. X to zbiór wierzchołków, które 
    zostały już rozważone i usunięte z P.

2.  Następnie wywołujemy funkcję search_cliques, która działa rekurencyjnie, przeglądając wszystkie możliwe kliki.

3.  Jeśli zarówno P, jak i X są puste, oznacza to, że znaleźliśmy klikę, którą drukujemy.

4.  W przeciwnym razie, dla każdego wierzchołka w P, tworzymy nowe zbiory R, P i X, dodając ten wierzchołek do R, 
    usuwając go z P i dodając jego sąsiadów do P i X. Następnie wywołujemy funkcję rekurencyjnie na tych nowych zbiorach.

5.  Po zakończeniu przeglądania wszystkich sąsiadów danego wierzchołka, usuwamy go z P i dodajemy do X.

Algorytm ten jest efektywny dla grafów o małej gęstości, ale może być wolny dla grafów o dużej gęstości 
ze względu na dużą liczbę klik.
'''
R = []
P = list(g.keys())
X = []

def search_cliques(R, P, X, g):

    if not P and not X:
        print(f'Clicque: {R}')
        return

    P_copy = P.copy()
    for person in P_copy:

        neighbours = g[person]
        R2 = R.copy()
        R2.append(person)
        P2 = [x for x in P if x in neighbours]
        X2 = [x for x in X if x in neighbours]
        search_cliques(R2, P2, X2, g)
        P.remove(person)
        X.append(person)

search_cliques(R, P, X, g)