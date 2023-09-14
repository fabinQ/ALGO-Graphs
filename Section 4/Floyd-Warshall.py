names = ['A','B','C','D','E']
names_index = list(map(lambda x: names.index(x), names))

graph = [#   A  B  C  D  E
            [0, 2, 0, 4, 0], # A
            [0, 0, 3, 3, 0], # B
            [0, 0, 0, 0, 2], # C
            [0, 0,-1, 0, 4], # D
            [0, 0, 0, 0, 0]  # E
]

def print_matrix(matrix, names):
    global N
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


print_matrix(graph, names)
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