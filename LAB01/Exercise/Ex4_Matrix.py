# %%
# Read data
import numpy as np
data = open("Maps/map1.txt")
m, n = data.readline().split()
m = int(m)
n = int(n)
D1 = []
D2 = []
max_distance = int(data.readline())
Map_Matrix = []
for i in range(n):
    Map_Matrix.append(data.readline().rstrip('\n').split(' '))
    Map_Matrix[i] = [int(e) for e in Map_Matrix[i]]
Map_Matrix = np.reshape(Map_Matrix, (-1,n))

# %% [markdown]
# Locate D1 and D2
for i in range(m):
    for e in range(n):
        if Map_Matrix[i][e] == 1:
            D1.append(i)
            D1.append(e)
        if Map_Matrix[i][e] == 2:
            D2.append(i)
            D2.append(e)


# %% [markdown]
# Find Neigbor
def Neigh(node):
    Neigh_List = []
    try:
        Map_Matrix[node[0]+1, node[1]]
    except IndexError as e:
        pass
    else:
        if node[0] + 1 >= 0:
            Neigh_List.append([node[0] + 1, node[1]])
        else:
            pass

    try:
        Map_Matrix[node[0]-1, node[1]]
    except IndexError as e:
        pass
    else:
        if node[0] - 1 >= 0:
            Neigh_List.append([node[0] - 1, node[1]])
        else:
            pass

    try:
        Map_Matrix[node[0], node[1] + 1]
    except IndexError as e:
        pass
    else:
        if node[1] + 1 >= 0:
            Neigh_List.append([node[0], node[1] + 1])
        else:
            pass

    try:
        Map_Matrix[node[0], node[1] - 1]
    except IndexError as e:
        pass
    else:
        if node[1] - 1 >= 0:
            Neigh_List.append([node[0], node[1] - 1])
        else:
            pass

    return Neigh_List
# %%
Neigh([0,0])

# %% [markdown]
# BFS
def bfs(Map_Matrix, node):
    visited = [] # Array to keep track of visited nodes.
    queue = [] # Initialize a queue
    visited.append(node)
    queue.append(node)
    
    while queue:
        Result = queue.pop(0)
        print(Result, end=" ")

        for Neighbour in Neigh(Result):
            if Neighbour not in visited:
                visited.append(Neighbour)
                queue.append(Neighbour)



# %%
bfs(Map_Matrix, D1)

# %%
