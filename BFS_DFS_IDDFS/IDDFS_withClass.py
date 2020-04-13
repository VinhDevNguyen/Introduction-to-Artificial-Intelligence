# Python program to print DFS traversal from a given graph  
from collections import defaultdict 

# This class represents a directed graph using adjacency 
# list representation 
class Graph: 
    def __init__(self,vertices): 
        # Number of vertices 
        self.V = vertices 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
     
    # TODO: Consider if the graph is connected  
    # A function to perform a Depth-Limited search 
    # from given source 'src' 
    def DLS(self,src,target,maxDepth): 
        if src == target : 
            return True
        # If reached the maximum depth, stop recursing. 
        if maxDepth <= 0 : 
            return False
        # Recursive for all the vertices adjacent to this vertex 
        for i in self.graph[src]: 
            # TODO: print traverse position
            print(i,end = " ") # NOT WORKING HERE 
            if(self.DLS(i,target,maxDepth-1)): 
                return True
        return False
  
    # IDDFS to search if target is reachable from v. 
    # It uses recursive DLS() 
    def IDDFS(self,src, target, maxDepth): 
        # Repeatedly depth-limit search till the 
        # maximum depth 
        for i in range(maxDepth): 
            if (self.DLS(src, target, i)): 
                return True
        return False

# Diagram 
#                   0
#                 /   \
#               1       2
#             /  \     /  \                             
#            3   4     5  6        
#
# Graph add sample
# g = Graph(7); 
# g.addEdge(0, 1) 
# g.addEdge(0, 2) 
# g.addEdge(2, 6) 
# g.addEdge(1, 3) 
# g.addEdge(1, 4) 
# # g.addEdge(2, 5) 
# g.addEdge(0,4)  


#                    0
#                 /   |  \
#               1     2   \
#             /  \    |    4                         
#            3   5    6    |    
#                |_________|
# Create a graph given in the above diagram 

# Setting parameter for graph finder 
# target = 6; maxDepth = 3; src = 0

# Sample 2 
g = Graph(6)
g.addEdge('A','B')
g.addEdge('A','C')
g.addEdge('C','F')
g.addEdge('B','D')
g.addEdge('B','E')
g.addEdge('E','F')
target = 'E'; maxDepth = 3; src = 'B'

# Output 
if g.IDDFS(src, target, maxDepth) == True: 
    print ("Target is reachable from source within max depth") 
else : 
    print ("Target is NOT reachable from source max depth") 
  