def is_complete(V):
    V_len = len(V)-1
    print(V_len)
    for i in V.values():
        print(i)
        if V_len != len(i):
            return False
    else:
        return True

net = {
'Umbrella': ['Puddle','Drizzle', 'Storm', 'Rain'],
'Puddle': ['Umbrella','Drizzle', 'Storm', 'Rain'],
'Drizzle': ['Umbrella','Puddle', 'Storm', 'Rain'],
'Storm': ['Umbrella','Puddle', 'Drizzle', 'Rain'],
'Rain': ['Umbrella','Puddle', 'Drizzle', 'Storm']
}

print(is_complete(net))