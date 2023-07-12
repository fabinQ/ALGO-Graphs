V = ['Prinzess', 'Dwarfs', 'Queen', 'King', 'Hunter']
E = [
    [0,1],
    [0,2],
    [0,3],
    [0,4],
    [2,3],
    [2,4],
    [3,4]
]
def who_knows_person(person,E,V):
    friends = []
    print(person,E,V)
    for p1,p2 in E:
        print(p1,p2)
        print(V[p1],V[p2])
        if person == V[p1]:
            friends.append(V[p2])
        elif person == V[p2]:
            friends.append(V[p1])
        else:pass
    return friends

print(who_knows_person('Prinzess',E,V))