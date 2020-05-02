# %% [markdown]
# # The Algorithm
# 1. Pick any node, visit the adjacent unvisited vertex, mark it as visited, display it, and insert it in a queue.
# 2. If there are no remaining adjacent vertices left, remove the first vertex from the queue.
# 3. Repeat step 1 and step 2 until the queue is empty or the desired node is found.
# %% [markdown]
# # Create Graph
# We have to create graph like this: 
# ![alt text](https://www.educative.io/api/edpresso/shot/5410617873661952/image/6437799702036480 "Graph")


# %%
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

# %% [markdown]
# # Write BFS Algorithm code
# %%
def bfs(graph, node):
    visited = [] # Array to keep track of visited nodes.
    queue = [] # Initialize a queue
    visited.append(node)
    queue.append(node)
    
    while queue:
        Result = queue.pop(0)
        print(Result, end=" ")

        for Neighbour in graph[Result]:
            if Neighbour not in visited:
                visited.append(Neighbour)
                queue.append(Neighbour)
bfs(graph, 'A')


# %%
