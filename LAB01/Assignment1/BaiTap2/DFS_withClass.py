
# graph = {
#     'A' : ['B', 'C'],
#     'B' : ['D', 'E'],
#     'C' : ['F'],
#     'D' : [],
#     'E' : ['F'],
#     'F' : []
# }

from collections import defaultdict 

class Graph: 
    def __init__(self,vertices): 
        # Number of vertices 
        self.V = vertices 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    Visited = [] # Array to keep track of visited nodes.
    def dfs(self, node, visited= Visited):
        if node not in visited:
            print(node, end = " ")
            visited.append(node)
            for neighbour in self.graph[node]:
                self.dfs(neighbour, visited)


g = Graph(6)
g.addEdge('A','B')
g.addEdge('A','C')
g.addEdge('C','F')
g.addEdge('B','D')
g.addEdge('B','E')
g.addEdge('E','F')
g.dfs('A')