names = ['CP', 'S', 'DR', 'SS', 'F', 'A', 'AP']
graph = [ #   CP  S  DR  SS   F  A   AP
            [ 0, 10,  0, 15,  0, 0,  0], # CP
            [ 0,  0, 20,  0,  0, 0,  0], # S
            [ 0,  0,  0,  0, -5, 5,  0], # DR
            [ 0,  0,  5,  0,  0, 0, 50], # SS
            [ 0,  0,  0,  0,  0, 0, 10], # F
            [ 0,  0,  0,  0,  0, 0, 10], # A
            [ 0,  0,  0,  0,  0, 0,  0] # AP
]

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

N = len(names)
cost_matrix = [[float('inf') for x in range(N)] for x in range(N)]
parents_matrix = [['' for x in range(N)] for x in range(N)]


for i in range(N):
    for j in range(N):
        if i == j:
            cost_matrix[i][j] = 0
            parents_matrix[i][j] = i
        elif graph[i][j] != 0:
            cost_matrix[i][j] = graph[i][j]
            parents_matrix[i][j] = i


for s in range(N):
    for i in range(N):
        for j in range(N):
            if cost_matrix[i][j] > cost_matrix[s][j] + cost_matrix[i][s]:
                cost_matrix[i][j] = cost_matrix[s][j] + cost_matrix[i][s]
                parents_matrix[i][j] = parents_matrix[s][j]

print_matrix(cost_matrix, names)
print_matrix(parents_matrix, names)

start = 0
end = 4
path = []
path.append(end)

while start != end:
    end = parents_matrix[start][end]
    path.append(end)

path.reverse()
start = 0
end = 4

print(f'From node {names[start]} to {names[end]} you must go through {"->".join(names[x] for x in path)}')

for i in range(N):
    for j in range(N):
        if parents_matrix[i][j] != '':
            parents_matrix[i][j] = names[parents_matrix[i][j]]

print_matrix(parents_matrix, names)