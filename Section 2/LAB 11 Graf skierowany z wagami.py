def add_node_to_dir(V,node):
    if node in V.keys():
        return
    else: V[node]={}

def add_value_to_dir(V,source, dest, weight):
    if not (source or dest in V.keys()):
        print(source,dest)
        return
    else:
        if not dest in V[source].keys():
            V[source][dest] = weight

def my_roads(my_road, person):
    sum_of_weights = 0
    start = my_road[0]
    for road in my_road[1:]:
        # print(V[start][road])
        sum_of_weights += V[start][road]
        start = road
    print('Sum of weight for all person: ',sum_of_weights*person)

V = {}
add_node_to_dir(V,'RS')
add_node_to_dir(V,'U')
add_node_to_dir(V,'M')
add_node_to_dir(V,'T')
add_node_to_dir(V,'S')

add_value_to_dir(V,'RS','M',1.5)
add_value_to_dir(V,'M','U',1.5)
add_value_to_dir(V,'RS','U',9)
add_value_to_dir(V,'RS','T',1)
add_value_to_dir(V,'T','S',1)
add_value_to_dir(V,'S','U',1)
print(V)

my_road = ['RS','T','S','U']
my_roads(my_road,3)

my_road = ['RS','U']
my_roads(my_road,1)