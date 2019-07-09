'''
Created on 15 maj 2018

@author: Shinke
'''

class Tree:
    def __init__(self, root):
        self.root = root
        
    # See Node.py
    async def runTree(self, obs):
        if (self.root.node_type == 1):
            await self.root.run_nodes(self.root.children, True, obs)
        elif (self.root.node_type == 2):
            await self.root.run_nodes(self.root.children, False, obs)
            
    