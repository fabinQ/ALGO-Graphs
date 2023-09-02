def get_root(graph):
    # To find the root in a graph, you need to traverse the columns of the matrix vertically.
    # Wherever the sum is equal to 0, it indicates that there is no parent, meaning that it is the root of the graph.
    the_root = None
    # review all columns
    for c in range(len(graph)):
        # chek how many parents the node has
        number_of_parents = 0
        for r in range(len(graph)):
            number_of_parents += graph[r][c]
            # if the node hasn't parents, it is the root
        if number_of_parents == 0:
            the_root = c
            break
    # return found root or none
    return the_root


def is_tree(graph):
     root = get_root(graph)
     if root == None:
         return False
     list_to_visited = [root]
     list_visited = []

     while list_to_visited:
         current = list_to_visited.pop()
         print(names[current].rsplit(' ')[1])
         if current in list_visited:
             return False
         else:
             list_visited.append(current)
             for element in range(len(graph)):
                 if graph[current][element] == 1:
                     list_to_visited.append(element)

     return len(list_visited) == len(graph)


names = ['1 CEO', '2 Cognitive', '2 Systems', '2 Operations', '3 Healthcare', '3 Cloud', '3 Research', '3 Security', '3 Storage']
structure1 = [
    [0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

structure2 = [
    [0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

structure3 = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
print(is_tree(structure1))
print(is_tree(structure2))
print(is_tree(structure3))