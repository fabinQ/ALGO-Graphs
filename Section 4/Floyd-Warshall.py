names = ['A','B','C','D','E']

graph = [#   A  B  C  D  E
            [0, 2, 0, 4, 0], # A
            [0, 0, 3, 3, 0], # B
            [0, 0, 0, 0, 2], # C
            [0, 0,-1, 0, 4], # D
            [0, 0, 0, 0, 0]  # E
]
'''Algorytm szuka najkrótszej ścieżki pomiędzy wszystkimi parami wierzchołków. Graf może mieć ujemne wagi ale nie może
mieć ujemnych cykli. Do algorytmu potrzebujemy 2 tablic. Tablice kosztów opisująca w pierwotnej postaci koszt 
poszczególnych krawędzi. Potem taki koszt przy kolejnych iteracjach jest uzupełniany sumę wag. Tablice rodziców która 
opisuje z którego wierzchołka trzeba wyjść aby dojść do wierzchołka docelowego.
1.  Tworzymy tablice kosztów i rodziców. Zaczynamy od całej macierzy z inf kosztów oraz całej pustej macierzy rodziców
2.  Uzupełniamy o dane z grafu. Tablica kosztów na przekątnej 0, a rodziców na przekątnej wierzchołek aktualny np. B->B
3.  Musimy przejść przez potrójną zagnieżdżoną pętle.
    Przechodzimy przez przekątną macierzy czyli przez ilość nodów A do E czyli od 0 do 4.
    Oraz przechodzimy przez każdą komórkę w grafie czyli dla grafu od 0 do 4 - range(5) oraz znowu od 0 do 4
4.  Tam sprawdzamy czy znajdziemy tańszą drogę dla par nodów przechodząc przez node na przekątnej. W ten sposób 
    uzupełniamy naszą tabele kosztów o nowe połączenia czyli nie da się za pierwszym razem przejść z A do C bezpośrednio.
    Musimy być bezpośrednio na przekątnej B żeby dojść z A do C, oraz musimy uzupełnić tabele rodzica o node z którego 
    musimy wyjść.
'''
def print_matrix(matrix, names):
    N = len(matrix)
    line = '    '
    for n in names:
        line += f'{n:>4}'
    print(line)
    for row in range(N):
        line = f'{names[row]:>4}'
        for col in range(N):
            line += f'{matrix[row][col]:>4}'
        print(line)


N = len(graph)
cost_matrix = [[float('inf') for x in range(N)] for x in range(N)]
parent_matrix = [['' for x in range(N)] for x in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            cost_matrix[i][j] = 0
            parent_matrix[i][j] = i
        elif graph[i][j] != 0:
            cost_matrix[i][j] = graph[i][j]
            parent_matrix[i][j] = i


print()
print_matrix(cost_matrix, names)
print()
print_matrix(parent_matrix, names)

for p in range(N):
    for i in range(N):
        for j in range(N):
            if cost_matrix[i][j] > cost_matrix[i][p] + cost_matrix[p][j]:
                cost_matrix[i][j] = cost_matrix[i][p] + cost_matrix[p][j]
                parent_matrix[i][j] = parent_matrix[p][j]

print()
print_matrix(cost_matrix, names)
print()
print_matrix(parent_matrix, names)

start_node = 0
end_node = 4
path = []

while start_node != end_node:
    end_node = parent_matrix[start_node][end_node]
    path.append(end_node)
path.reverse()
path.append(4)

start_node = 0
end_node = 4
print(f'From node {names[start_node]} to {names[end_node]} you must go through {"->".join(names[x] for x in path)}')


for i in range(N):
    for j in range(N):
        if parent_matrix[i][j] != '':
            parent_matrix[i][j] = names[parent_matrix[i][j]]

print_matrix(parent_matrix,names)