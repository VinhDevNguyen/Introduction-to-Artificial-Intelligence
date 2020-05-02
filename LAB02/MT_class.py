# This class using anytree library as it core function
# In order for this program to work, you'll need to install 
# anytree first. Use pip to install, here's the syntax:  
# >>> pip install anytree 

# LIBRARIES 
from anytree import RenderTree,Node

class MT: # Millionares and thieves  
    # check this function again about the constructor
    # it may cause problem because of init value 
    # Constructor
    def __init__(self,initMillionares=None,
        initThieves=None,maxTransfer=None):
        self.maxTransfer = maxTransfer or 2  # Max transfer per trip 
        self.initThieves = initThieves or 3 
        self.initMillionares = initMillionares or 3 

        # This attribute used for create dictionary 
        # in order used for searching like dfs,bfs,...
        self.graph = Node([initMillionares,initThieves])        


    # def initGraph(self): 



    # Breadth first search 
    def bfs(self): 
        print(self.maxTransfer)
    # Depth first search 
    def dfs(self): 
        print(self.maxTransfer)







def main(): 
    river = MT() 
    river.bfs()
if __name__ == '__main__': 
    main()