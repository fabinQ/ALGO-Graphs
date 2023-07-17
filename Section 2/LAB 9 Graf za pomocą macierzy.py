V = ['mouse', 'keyboard', 'computer', 'monitor', 'printer']
E = [{0,2},{1,2}, {2,3},{2,4}]
matrix = [
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1],
    [0,0,0,0,0],
    [0,0,0,0,0]
]
def translate_to_matrix(V,E):
    matrix_of_graph = []
    for index_x_in_V in range(len(V)):
        matrix_of_graph.append([1 if {index_x_in_V,index_y_in_V} in E else 0 for index_y_in_V in range(len(V))])
    return matrix_of_graph

my_matrix = translate_to_matrix(V,E)

for _ in my_matrix:
    print(_)