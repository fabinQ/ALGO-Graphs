def add_node_to_dir(V,node):
    if node in V.keys():
        return
    else: V[node]=[]

def add_value_to_dir(V,source, dest):
    if not (source or dest in V.keys()):

        print(source,dest)
        return
    else:
        if not dest in V[source]:
            V[source].append(dest)


V = {}
add_node_to_dir(V,'S')
add_node_to_dir(V,'MS')
add_node_to_dir(V,'M')
add_node_to_dir(V,'HN')
add_node_to_dir(V,'F')
add_node_to_dir(V,'NR')
add_node_to_dir(V,'MS')
add_node_to_dir(V,'NT')
print(V.keys())

add_value_to_dir(V,'S','MSS')
add_value_to_dir(V,'S','MS')
add_value_to_dir(V,'MS','S')
add_value_to_dir(V,'MS','NT')
add_value_to_dir(V,'MS','NR')
add_value_to_dir(V,'MS','M')
add_value_to_dir(V,'M','HN')
add_value_to_dir(V,'M','MS')
add_value_to_dir(V,'HN','M')
add_value_to_dir(V,'HN','F')
add_value_to_dir(V,'F','HN')
add_value_to_dir(V,'F','NR')
add_value_to_dir(V,'NR','F')
add_value_to_dir(V,'NR','MS')
add_value_to_dir(V,'NT','MS')
print(V)