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
def bfs(Map_Matrix, Start, destination, max_distance, m, n):
    from anytree import Node, RenderTree
    
    # create gas map
    Gas_Map = np.empty((m,n,))
    Gas_Map[:] = np.nan

    visited = [] # Array to keep track of visited nodes.
    queue = [] # Initialize a queue

    visited.append(Start)
    queue.append(Start)
    
    # Create intialize graph for traversal 
    root = Node(Start ,parent = None,fuelLeft = max_distance)
    nextMove = Neigh(Start)
    # # For every move, distance decrease by 1
    # nodeDistance = max_distance - 1 
    # for ele in nextMove: 
    #     if ele != None:
    #         if isReFuel(ele,matrixMap) == True: 
    #             Node(ele,parent=root,children=None,fuelLeft=nodeDistance+distance[0]) 
    #         else:
    #             Node(ele,parent=root,children=None,fuelLeft=nodeDistance)
    
    while queue:
        
        #  initialize gas
        if Map_Matrix[Start[0], Start[1]] == 1:
            Gas_Map[Start[0], Start[1]] = max_distance
            Gas = max_distance
            
        Result = queue.pop(0)
        print(Result, end=" ")

        # find the path
        # if the result can not find the destination
        if Result != destination:
            # find the neighbour of the node and add to queue
            for Neighbour in Neigh(Result):
                if Neighbour not in visited:
                    Gas = Gas_Map[Result[0], Result[1]]
                    
                    # if the node is the island -> refresh gas
                    if Map_Matrix[Result[0], Result[1]] == 3:
                        Gas = max_distance
                        Gas_Map[Neighbour[0], Neighbour[1]] = max_distance
                        # Node(Neighbour, parent = root, children = None, fuelLeft = Gas)
                    # if gas is still in the can:
                    if Gas > 0:
                        # if the neighbour node is an island
                        if Map_Matrix[Neighbour[0], Neighbour[1]] == 3:
                            Gas = max_distance
                            Gas_Map[Neighbour[0], Neighbour[1]] = Gas  
                        # if the neighbour node is not an island
                        else:
                            Gas -= 1
                            Gas_Map[Neighbour[0], Neighbour[1]] = Gas
                            # Node(Neighbour, parent = Result, children = None, fuelLeft = Gas)
                        visited.append(Neighbour)
                        queue.append(Neighbour)
                        
                        Result_Node = Node(Result, parent = root, children = None, fuelLeft = Gas)
                    else:
                        pass
                
                        

        else:
            break
    if D2 not in visited:
        print("can not find the path to the destination")
    print(RenderTree(root))
    return Gas_Map


# %%
bfs(Map_Matrix, D1, D2, max_distance, m, n)

# %%
max_distance


