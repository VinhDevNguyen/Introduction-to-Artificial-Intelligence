# Input from file like this: 
# - 1st line: matrix  size (probably not going to use) 
# - 2nd line: initial start coordinate 
# - 3rd line: goal coordinate
# - 4rd line: tank compacity of the boat 
# - 5th line to eof: map
#      -> Start,dest marked with '1'
#      -> Re-fuel island marked with '2' 
#      -> Path (sea) marked with '0'

from collections import defaultdict
from queue import PriorityQueue

# Open file
with open("LAB01/Maps/map1.txt") as file: 
    matrixSize = file.readline()
    startCoordinate = file.readline() 
    destCoordinate = file.readline()
    distance = file.readline()
    matrixMap = file.readlines()

# Pre-processing input from file 
# Remove '\n' and convert from str to int
# TODO: improve this function to work with 2d array
def convertToInt(listStr): 
    listStr = listStr.rstrip('\n').split(' ')
    listInt = [int(ele) for ele in listStr]
    return listInt

matrixSize = convertToInt(matrixSize)
startCoordinate = convertToInt(startCoordinate)
destCoordinate = convertToInt(destCoordinate)
distance = convertToInt(distance)

# CONVERT MAP INTO DICTIONARY TYPE 
# Convert str map to int map
# TODO: After done with algo, comeback here to improve this 
for i in range(matrixSize[1]): 
    matrixMap[i] = matrixMap[i].rstrip('\n').split(' ')
    matrixMap[i] = [int(e) for e in matrixMap[i]]


# Graph class stores matrixMap 
# class Graph: 
#     # def __init__(self):
#         # self.graph = defaultdict(list)
#     def __init__(self):
#         self.graph = dict()
#     # Each v append in u, v contains coordinate [x,y] 
#     def addEdge(self,keys,vals): 
#         # self.graph[u].append(v) 
#         self.graph

def checkCollision(currCoord, matrixMap): 
    # row = len(matrixMap) 
    # column = len(matrixMap[0])
    if (0 <= currCoord[0] <= len(matrixMap)) and (0 <= currCoord[1] <= len(matrixMap[0])): 
        return False # Not collision detected 
    return True # if collision detected 

# Return list of next move based on current coordinate
# If move[idx] = [-1,-1] means invalid move 
def nextValidMove(currCoord, matrixMap): 
    move = [
        [currCoord[0]-1,currCoord[1]], # up
        [currCoord[0]+1,currCoord[1]], # down
        [currCoord[0],currCoord[1]-1], # left 
        [currCoord[0],currCoord[1]+1], # right
    ]
    # If next move[idx] is unvalid, replace with None
    for idx,ele in enumerate(move): 
        if checkCollision(ele, matrixMap) == True: 
           move[idx] = None 
    return move # Return list valid coordinate of the next move

def isReFuel(currCoord, matrixMap): 
    # currCoord is arr, receive current coordinate  
    if matrixMap[currCoord[0]][currCoord[1]] == 2: 
        return True 
    return False

# Main algorithm of exercise
# REMEMBER TO INSTALL anytree library 
from anytree import Node, RenderTree, PreOrderIter
def dfs(initialCoordinate, goalCoordinate, distance, matrixMap): 
    # Create intialize graph for traversal 
    graph = Node(initialCoordinate,parent=None,fuelLeft=distance[0]) 
    nextMove = nextValidMove(initialCoordinate,matrixMap)
    # For every move, distance decrease by 1
    nodeDistance = distance[0] - 1 
    for ele in nextMove: 
        if ele != None:
            if isReFuel(ele,matrixMap) == True: 
                Node(ele,parent=graph,children=None,fuelLeft=nodeDistance+distance[0]) 
            else:  
                Node(ele,parent=graph,children=None,fuelLeft=nodeDistance) 
    # Expansion based on current coordianate  
    # Expansion based on pre-order iterations  
    # print([node.name for node in PreOrderIter(graph)])
    # for node in PreOrderIter(graph): 
    
    # Render the graph
    # print(RenderTree(graph.children))
    # print(graph.children[0])
    # print(RenderTree(graph))

dfs(startCoordinate,destCoordinate,distance,matrixMap)







