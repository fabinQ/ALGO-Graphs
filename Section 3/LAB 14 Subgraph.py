def subgraph(V, V_supgraph):

    for v in V_supgraph.keys():
        if v not in V.keys():
            print("Missing node.", v)
            return False
        else:
            for e in V_supgraph[v]:
                if e not in V[v]:
                    print('Missing connection!', v, e)
                    return False
    return print("GOOD!")


cantor = {
 'EUR' : ['USD', 'GBP', 'CHF'],
 'USD' : ['EUR', 'GBP', 'CHF'],
 'SEK' : ['EUR'],
 'JPY' : ['EUR', 'USD'],
 'CAD' : ['USD', 'EUR'],
 'GBP' : [],
 'CHF' : []
}
client1 = {
 'EUR' : ['USD'],
 'USD' : []
}
client2 = {
 'EUR' : ['CAD'],
 'USD' : ['EUR' ],
 'SEK' : ['EUR'],
 'CAD' : []
}
client3 = {
 'JPY' : [],
 'EUR' : ['USD'],
 'USD' : ['JPY']
}

subgraph(cantor,client1)
subgraph(cantor,client2)
subgraph(cantor,client3)