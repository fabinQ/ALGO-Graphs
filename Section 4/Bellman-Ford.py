graph = {
    'A': {'B': 2, 'D': 4},
    'B': {'C': 3, 'D': 3},
    'C': {'E': 2},
    'D': {'C': -1, 'E':4},
    'E': {}
}

costs = {}
parents = {}
for name in graph.keys():
    costs[name] = float('inf')
    parents[name] = None

start = 'A'
costs[start] = 0

for _ in range(len(graph)-1):

    there_are_changes = False

    for s in graph.keys():
        for d,w in graph[s].items():
            if costs[s] != float('inf') and costs[s] + w < costs[d]:
                costs[d] = costs[s] + w
                parents[d] = s
                there_are_changes = True
                
    if not there_are_changes:
        break
      
for d,c in costs.items():
    print(f'The cost for {d} is {c}')

    current_d = d
    while parents[current_d]:
        print(current_d)
        current_d = parents[current_d]
    else:
        print(current_d)