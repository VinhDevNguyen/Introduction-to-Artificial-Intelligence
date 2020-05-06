# %% 
from anytree import RenderTree, Node 
print('Import libraries successfully')

# %%


# %% 
# check whether or not currNode is existing in the graph 
# So that we can use to kill the branch in graph  
def checkExistNode(currNode, currGraph):
    return True

# %% 
# Receive Node object
# currNode = Node([2,-1]) # Millionares, thieves 
# Expect to receive Node (anytree) object
def checkConstraint(currNode): 
    if (currNode.name[0] >= currNode.name[1]) and (currNode.name[1] != 0) and (currNode.name[0] >= 0 and currNode.name[1] >= 0): 
        return True 
    return False 

# %%
# main algorithm
# Expected to receive node object  
def bfs(graph): 
   return None 



# %% 
# def dfs(): 


# %% 
# This function is for testing purpose 
# to make the program running 
# TODO: Improve by using ``transfer``` 
# return array 
def nextExpandedNode(currNode): 
    listNode = [
        [currNode.name[0] - 1, currNode.name[1] - 0],
        [currNode.name[0] - 0, currNode.name[1] - 1],
        [currNode.name[0] - 1, currNode.name[1] - 1],
    ]
    return listNode 


# %%
# TODO: REMOVE DUPLICATED NODES 
# This function used to create graph 
# Expected to receive Node obj 
def graphExpansion(graph): 
    toVisit = nextExpandedNode(graph) # receive array  
    # visited = []
    # while len(toVisit) != 0: 
    idx = 0
    while idx != 5:
        currNode = toVisit.pop() 
        # visited.append(currNode)
        toVisit = nextExpandedNode(Node(currNode)) 
        currNode = toVisit.pop()
        idx = idx + 1

    print(toVisit)




graph = Node([3,3])
graphExpansion(graph)

# %%
initMT = [3,3] # 3 millionares, 3 thieves  
transfer = [1,2] # boat can trasfer 1 or 2 people 
def main(): 
    graph = Node(initMT)
    print(RenderTree(graph))
    # graph.name[0] = graph.name[0] - 1
    print(graph.name[0]) # get value in node 

if __name__ == '__main__': 
    main()



# %% 
depth = 5 
while depth != 0: 
    depth = depth +
    print(depth)
