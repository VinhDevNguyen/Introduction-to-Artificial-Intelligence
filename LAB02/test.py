from anytree import Node,RenderTree
from anytree import LevelOrderIter, LevelOrderGroupIter
initMT = [3,3]
graph = Node(initMT)

def nextExpandedNode(currNode):
    temp = currNode.name
    listNode = [
        [temp[0] - 1, temp[1] - 0],
        [temp[0] - 0, temp[1] - 1],
        [temp[0] - 1, temp[1] - 1],
    ]
    return listNode 
    # listNode = [
    #     [currNode.name[0] - 1, currNode.name[1] - 0],
    #     [currNode.name[0] - 0, currNode.name[1] - 1],
    #     [currNode.name[0] - 1, currNode.name[1] - 1],
    # ]

def graphExpansion(graph): 
    # level 0
    listNodes = nextExpandedNode(graph)
    # print(listNodes)

    # init first 3 children for root
    # level 1
    for node in listNodes: 
        Node(node,parent=graph)
    # print(RenderTree(graph))

    # level 2
    track = [] # keep tracking nodes need to expand 
    for children in graph.children: 
        listNodes = nextExpandedNode(children)
        for node in listNodes: 
            track.append(Node(node,parent=children))


    currNode = track[0].name 
    Node(currNode, )


    print(track[0].name)
    # for node in track: 
    #     print(node.name) 




    # print([child for child in graph.children])
    # print(graph.height)
    # print(RenderTree(graph))
    # for children in graph.children: 
    # #     a = children.descendants
    #     print(children.descendants)
    # #     print(a.name)

    # for children in LevelOrderGroupIter(graph.children): 
    #     for node in children: 
    #         print(node.name)


graph = Node([3,3])
graphExpansion(graph)


# def checkConstraint(currNode): 
    # receive Node object
    # if (currNode.name[0] >= currNode.name[1]) and (currNode.name[1] != 0) and (currNode.name[0] >= 0 and currNode.name[1] >= 0): 
    # if ():
        # return True 
    # return False 


# def graphExpansion(graph): 
    # toVisit = nextExpandedNode(graph) # receive array  
    # idx = 0
    # for element in toVisit: 
    #     Node(element, parent=graph)

    # for child in graph.children: 
    #     Node('1',parent = child)
 
    # for child in graph.children: 
    #     Node('1',parent = child)

    # print(RenderTree(graph))
    # depth = len(graph.children)
    # print(depth)
    # print([node.name for node in LevelOrderIter(graph)])
    # print([[node.name for node in children] for children in LevelOrderGroupIter(graph)])



# def graphExpansion(root):
#     for children in LevelOrderGroupIter(root): 
#         for node in children: 
#             print(node.name)
#             toVisit = nextExpandedNode(node)
#             print(toVisit)

# root = Node([3,3])
# graphExpansion(root)



# graph = Node([3,3])
# graphExpansion(graph)

# def nextExpandedNode(temp): 
#     listNode = [
#         [temp[0] - 1, temp[1] - 0],
#         [temp[0] - 0, temp[1] - 1],
#         [temp[0] - 1, temp[1] - 1],
#     ]
#     return listNode 


# def graphExpansion(root): 
#     listNodes = nextExpandedNode(root) 
#     root.append(listNodes)
#     print(root)





# root = [[3,3]]
# graphExpansion(root)