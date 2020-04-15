# Input from file like this: 
# - 1st line: matrix  size 
# - 2nd line: initial start coordinate 
# - 3rd line: tank compacity of the boat 
# - 4th line to eof: map
#      -> Start,dest marked with '1'
#      -> Re-fuel island marked with '2' 
#      -> Path (sea) marked with '0'


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
from collections import defaultdict
class Graph: 
    def __init__(self,vertices): 
        self.V = vertices
        self.graph = defaultdict(list)

    # Each v append in u, v contains coordinate [x,y] 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 

# TODO: Convert matrix into class graph 
# The idea here is to convert matrixMap into dictionary type 
# For every key:value -> key is parent node, value is adjancent node 
# value can use set(coord1, coord2)
# def mapIntoDict(mapMatrix)

# Graph expansion based on movement 
# Boat can only move UP,DOWN,LEFT,RIGTH
# Based on that, graph expansion should be smiliar to that 


# Path finding 
# Check if the next coordinate is valid 
def isValidCoordinate(inputCoord, matrixMap): 
    x,y = inputCoord[0], inputCoord[1]
    try: 
        matrixMap[x][y] 
    except: 
        return False 
    return True

# Return coordinate of the next movement 
def nextMoveCoordinate(move, currCoord, matrixMap): 
    # move = UP -> return coordinate when moving up
    # move is str 
    # currCoord is array dtype 
    if move == 'U': 
        return [currCoord[0]+1,currCoord[1]]
    elif move == 'D': 
        return [currCoord[0]-1,currCoord[1]]
    elif move == 'L': 
        return [currCoord[0],currCoord[1]+1]
    elif move == 'R': 
        return [currCoord[0],currCoord[1]-1]






# Main algorithm of exercise
# DFS doesn't found the most optimal solution
from queue import PriorityQueue
# TODO: Problem with passing parameter
def dfs(initialCoordinate, goalCoordinate, matrixMap, distance): 
    # Distinct between initialCoordinate and startCoodinate 
    visited = []
    path = [] # return travel path when function is complete 
    fringe = PriorityQueue() # fringe stores deeepest nodes 
    fringe.put((0, initialCoordinate, path, visited))
    #TODO: Add stop branch when run out of fuel
    # Ideas: 




# This function return list of movement the boat able to move 
# by this order: UP, DOWN, LEFT, RIGHT
# currCoord = [0,0]
# def nextMove(currCoord, matrixMap): 
#     move = [0,0,0,0]
#     try: 
#     return move





# print(matrixSize)
# print(startCoordinate)
# print(distance)
# print(matrixMap)








