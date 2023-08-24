mission_control = {
    'FC' : ['Engine', 'Weather', 'Crew'],
    'Engine' : ['Engine Temp', 'Fuel'],
    'Engine Temp' : [],
    'Fuel' : [],
    'Weather' : ['Wind', 'Air Temp', 'Clouds'],
    'Wind' : [],
    'Air Temp' : [],
    'Clouds' : [],
    'Crew' : ['Health', 'Communication'],
    'Communication' : [],
    'Health' : []
}

status = {
    'Engine Temp' : True,
    'Fuel' : True,
    'Wind' : True,
    'Air Temp' : True,
    'Clouds' : True,
    'Health' : False,
    'Communication' : True
}

def can_start(graph, status, start_node):
    if graph[start_node]:
        for node in graph[start_node]:
            if not can_start(graph, status, node):
                print(f'{start_node} - False')
                return False
        print(f'{start_node} - True')
        return True
    else:
        print(f'{start_node} - {status[start_node]}')
        return status[start_node]

print(f'Can we start? {can_start(mission_control, status, "FC")}')

