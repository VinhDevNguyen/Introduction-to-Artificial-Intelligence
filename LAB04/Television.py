import numpy as np
table = np.array([
    [None, 85  , 175 , 200 ],
    [85  , None, 125 , 175 ],
    [172 , 125 , None, 100 ],
    [200 , 175 , 100 , None]
    ])

Graph = {}
channel = []
visited = {}
ID = 0

for i in range(table.shape[0]):
    for n in range(table.shape[1]):
        if i == n: 
            break
        if(n > i):
            break
        if i in Graph:
            Graph[i].append((n,table[i,n]))
        else:
            Graph[i] = [(n,table[i,n])]

