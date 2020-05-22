# %% [markdown]
# Work only on Linux

# %%
from colors import *

# %%
graph = {
    'A': ['B', 'D', 'C'],
    'B': ['A', 'D', 'A'],
    'C': ['A', 'D', 'F'],
    'D': ['A', 'B', 'E', 'F', 'C'],
    'E': ['B', 'D', 'F'],
    'F': ['C', 'E']
    }

# %%

colors = [(255,0,0), (0,255,0), (0,0,255)] # RGB color
visited = {}

for node in graph:
    if node not in visited:
        visited[node] = colors[0]
    for Neighbor in graph[node]:
        if Neighbor in visited:
            if(visited[Neighbor] == visited[node] == colors[0]):
                visited[node] = colors[1]
    for Neighbor in graph[node]:
        if Neighbor in visited:     
            if(visited[Neighbor] == visited[node] == colors[1]):
                visited[node] = colors[2]




# %%
for element in visited:
    print(GColor.RGB(visited[element][0],visited[element][1],visited[element][2]),element, GColor.END)

# %%
