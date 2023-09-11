graph = {
    'A': {'B': 2, 'D': 4},
    'B': {'C': 3, 'D': 3},
    'C': {'E': 2},
    'D': {'C': -1, 'E':4},
    'E': {}
}


'''
Algorym Bellmana - Forda różni się od Dijksty tym że może miec cykle ale nie może mieć ujemnych cykli, 
oraz tym że przechodzi przez wsztskie wierzchołki n-1 razy (n-ilość wierzchołków). Jeśli przechodzi wiecej razy tzn. że 
ma w sobie cykl ujemny.
1. Podobnie jak w Dijkstry uzupełniamy tabele kosztów i rodziców o inf, oraz None. Zazdnaczamy od razu starts oraz koszt 
startu.
2. Wchodzimy do pętli for dla n-1 i ustawiamy zmienna kontrolną która sprawdza zmiany.
3. Przechodzimy do funkcji która będzie szukała kolejnych dzieci danego wierzchołka. Pętla w pętli.
4. Następnie sprawdzamy czy koszt dla wierzchołka RODZICA jest różny od nieskończoności i czy znaleziony nowy koszt 
jest mniejszy. Jeśli tak to zapisujemy koszt i rodziców, oraz zmieniamy naszą zmienną kontrolną.
5. Jak juź przejdziemy RAZ przez algorytm który miał ujemny koszt trzeba zaktualizować resztę grafu (max. n-1 razy)
6. Przechodzimy do momentu kiedy zmienna kontrolna pokaże brak zmiany lub skończy nam sie pętla.
7. Wywołujemy jeszcze jeden funkcje. Jeśli zwróci True tzn. że jest w niej cykl ujemny. 
Jeśli False możemy wyświetlić wynik. 
8. Dla każdego elementu w liście cost czyli dla każdego wierzchołka wyświetlana jest cena. 
W pętli while wyświetlany jest rodzić wierzchołka i tak dopóki nie trafimy na None.
'''
costs = {}
parents = {}
for name in graph.keys():
    costs[name] = float('inf')
    parents[name] = None

start = 'A'
costs[start] = 0

def change_cost(graph, costs, parents):
    there_are_changes = False

    for s in graph.keys():
        for d, w in graph[s].items():
            if costs[s] != float('inf') and costs[s] + w < costs[d]:
                costs[d] = costs[s] + w
                parents[d] = s
                there_are_changes = True

    if there_are_changes:
        return True
    else:
        return False

for _ in range(len(graph)-1):

    if not change_cost(graph,costs, parents):
        break

if change_cost(graph, costs, parents):
    print('There is a negative cycle')
else:
    print('There is not a negative cycle')
    for d,c in costs.items():
        print(f'The cost for {d} is {c}')

        current_d = d
        while parents[current_d]:
            print(current_d)
            current_d = parents[current_d]
        else:
            print(current_d)