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
Potrzebujemy 3 zmiennych R,P,Q
'''
R = []
P = list(g.keys())
X = []

def search_clicques(R, P, X, g):

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
        search_clicques(R2, P2, X2, g)
        P.remove(person)
        X.append(person)

search_clicques(R, P, X, g)