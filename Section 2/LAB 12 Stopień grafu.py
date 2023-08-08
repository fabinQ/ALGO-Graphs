def max_degree(V):
    return max(len(n) for n in V.values())


def station_name(V):
    max = max_degree(V)
    for name, station in V.items():
        if len(station) == max:
            return name, max


metro = {
    'Staromestska': ['Mustek'],
    'Mustek': ['Staromestska', 'Namesti Republiky', 'Muzeum', 'Narodni trida'],
    'Muzeum': ['Mustek', 'Hlavni nadrazi'],
    'Narodni trida': ['Mustek'],
    'Namesti Republiky': ['Mustek', 'Florenc'],
    'Florenc': ['Namesti Republiky', 'Hlavni Nadrazi'],
    'Hlavni nadrazi': ['Florenc', 'Muzeum']
}
print(station_name(metro))
