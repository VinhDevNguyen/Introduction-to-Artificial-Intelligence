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
Neigh_List = []
try:
    Map_Matrix[D1[0]+1, D1[1]]
except IndexError as e:
    print("Ngoai matrix")
else:
    print(D1[0]+1, D1[1])
    Neigh_List.append([D1[0]+1, D1[1]])
# %%
try:
    Map_Matrix[D1[0]-1, D1[1]]
except IndexError as e:
    print("Ngoai matrix")
else:
    print(D1[0]-1, D1[1])
    Neigh_List.append([D1[0]-1, D1[1]])
# %%
try:
    Map_Matrix[D1[0], D1[1]+1]
except IndexError as e:
    print("Ngoai matrix")
else:
    print(D1[0], D1[1]+1)
    Neigh_List.append([D1[0], D1[1]+1])

# %%
try:
    Map_Matrix[D1[0], D1[1]-1]
except IndexError as e:
    print("Ngoai matrix")
else:
    print(D1[0], D1[1]-1)
    Neigh_List.append([D1[0], D1[1]-1])

# %%
