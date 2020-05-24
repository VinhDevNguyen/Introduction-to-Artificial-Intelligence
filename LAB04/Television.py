import numpy as np
table = np.array([
    [None, 85  , 175 , 200, 20, 100 ],
    [85  , None, 125 , 175, 100, 160 ],
    [172 , 125 , None, 100, 200, 250 ],
    [200 , 175 , 100 , None, 210, 220],
    [20, 100, 200, 210, None, 100],
    [100, 160, 250, 220, 100, None]
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
        if str(i) in Graph:
            Graph[str(i)][str(n)] = table[i,n]
        else:
            Graph[str(i)] = {str(n): table[i,n]}


Graph_New = {}

for dedicate in range(table.shape[0]):
        for i in Graph:
            if str(dedicate) in Graph[i]:
                if str(dedicate) in Graph_New:
                    Graph_New[str(dedicate)][str(i)] = Graph[i][str(dedicate)]
                else:
                    Graph_New[str(dedicate)] = {str(i): Graph[i][str(dedicate)]}

def Merge(dict1, dict2): 
    return(dict2.update(dict1)) 
Merge(Graph,Graph_New)

for node in Graph_New:
    i = 0
    if channel == []:
        channel.append(ID)
        ID = ID + 1
    visited[node] = channel[i]
    for Neighbor in Graph_New[node]:
        for CheckID in range(len(channel)):
            if Neighbor in visited: 
                if(visited[Neighbor] ==  visited[node] == CheckID):
                    i = CheckID
                    if Graph_New[node][Neighbor] <= 150:
                        i = i + 1
                        if len(channel)-1 < i:
                            channel.append(ID)
                            ID = ID + 1
                        visited[node] = channel[i]


print(visited)
# Test key is correct

