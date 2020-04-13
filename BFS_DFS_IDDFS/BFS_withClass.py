# Breadth first search traversal 
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
        # No. of vertices 
        self.V = vertices 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    
    # BFS algorithm
    # Inorder to perform BFS traversal using function below 
    # Call bfs and add root node
    def bfs(self,rootNode):
        visited = [] # Tracking visited nodes 
        queue = [] # Tracking nodes need to be visited  
        
        # Initialize root node 
        # Enqueue and mark as visited
        queue.append(rootNode) 
        visited.append(rootNode)

        while queue: 
            node = queue.pop(0) 
            print(node,end = " ")
            for adjacentNode in self.graph[node]: 
                if adjacentNode not in visited: 
                    queue.append(adjacentNode) 
                    visited.append(adjacentNode)
                    
    # Node finder implement BFS 
    def nodeFinder(self,rootNode,target): 
        queue = []
        visited = []
        queue.append(rootNode) 
        visited.append(rootNode)

        while queue: 
            node = queue.pop(0) 
            for adjacentNode in self.graph[node]: 
                if adjacentNode == target: 
                    return True
                if adjacentNode not in visited: 
                    queue.append(adjacentNode) 
                    visited.append(adjacentNode)
        return False  

        # visited = [] # Array to keep track of visited nodes.
        # queue = [] # Initialize a queue
        # visited.append(node)
        # queue.append(node)
        # while queue:
        #     Result = queue.pop(0)
        #     print(Result, end=" ")
        #     for Neighbour in graph[Result]:
        #         if Neighbour not in visited:
        #             visited.append(Neighbour)
        #             queue.append(Neighbour)
# Sample graph 1
g = Graph(6)
g.addEdge('A','B')
g.addEdge('A','C')
g.addEdge('C','F')
g.addEdge('B','D')
g.addEdge('B','E')
g.addEdge('E','F')
g.bfs('A')
print(g.nodeFinder('A','E'))

# Sample graph 2
# g = Graph(7); 
# g.addEdge(0, 1) 
# g.addEdge(0, 2) 
# g.addEdge(2, 6) 
# g.addEdge(1, 3) 
# g.addEdge(1, 4) 
# g.addEdge(0,4) 
# g.bfs(0)