
from collections import *


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def Add_Node(self, NODE):
        self.nodes.add(NODE)

    def add_edge(self, FirstNode, SecondNode, Distance):
        self.edges[FirstNode].append(SecondNode)
        self.edges[SecondNode].append(FirstNode)
        self.distances[(FirstNode, SecondNode)] = Distance


def dijkstra(graph, start):
    visited = {start: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, Start, destination):
    visited, paths = dijkstra(graph, Start)
    FinalPath = deque()
    Dest = paths[destination]

    while Dest != Start:
        FinalPath.appendleft(Dest)
        Dest = paths[Dest]

    FinalPath.appendleft(Start)
    FinalPath.append(destination)

    return visited[destination], list(FinalPath)

graph = Graph()

for node in ['CA MAU', 'RACH GIA', 'LONG XUYEN', 'BAC LIEU', 'CAN THO', 'SOC TRANG', 'VINH LONG', 'TRA VINH', 'CAO LANH', 'MY THO', 'BEN TRE', 'TAN AN', 'HO CHI MINH']:
    graph.Add_Node(node)



graph.add_edge('CA MAU', 'RACH GIA', 127)
graph.add_edge('CA MAU', 'BAC LIEU', 74)
graph.add_edge('RACH GIA', 'LONG XUYEN', 62)
graph.add_edge('RACH GIA', 'BAC LIEU', 125)
graph.add_edge('RACH GIA', 'CAN THO', 112)
graph.add_edge('LONG XUYEN', 'CAN THO', 61)
graph.add_edge('LONG XUYEN', 'CAO LANH', 48)
graph.add_edge('CAN THO', 'CAO LANH', 86)
graph.add_edge('CAN THO', 'SOC TRANG', 62)
graph.add_edge('CAN THO', 'VINH LONG', 40)
graph.add_edge('BAC LIEU', 'SOC TRANG', 49)
graph.add_edge('SOC TRANG', 'VINH LONG', 92)
graph.add_edge('SOC TRANG', 'TRA VINH', 62)
graph.add_edge('TRA VINH', 'VINH LONG', 65)
graph.add_edge('TRA VINH', 'BEN TRE', 48)
graph.add_edge('BEN TRE', 'VINH LONG', 63)
graph.add_edge('BEN TRE', 'MY THO', 16)
graph.add_edge('MY THO', 'VINH LONG', 69)
graph.add_edge('MY THO', 'CAO LANH', 90)
graph.add_edge('CAO LANH', 'VINH LONG', 49)
graph.add_edge('CAO LANH', 'TAN AN', 100)
graph.add_edge('TAN AN', 'MY THO', 20)
graph.add_edge('TAN AN', 'HO CHI MINH', 47)

COST, path = shortest_path(graph, 'CA MAU', 'HO CHI MINH')
print('Shortest path: ', path)
print('Cost: ', COST)