'''
Created on 15 maj 2018

@author: Shinke
'''
import functions # Necessary when calling functions with eval()

DO_NOTHING = "functions.doNothing()"

class Node:
    def __init__(self, node_type, function=DO_NOTHING):
        self.node_type = node_type # Function (0), Sequence (1) or Fallback (2).
        self.function = function # Optional, only for function nodes. This parameter is a string.
        self.children = [] # Children nodes. A function node won't have any children.
        self.visited = False # If this is true, this node won't be computed.

    def add_child(self, node):
        self.children.append(node)           
            
    # Run a sequence (sequence = True) or fallback (sequence = False) of nodes until end or until one of them fails/succeeds.
    async def run_nodes(self, nodes, sequence, obs): # obs is necessary when calling functions with eval().
        for i in nodes:
            if (i.visited == False):
                node_type = i.node_type
                # If the node is a function, execute it and mark the node as visited if it succeeds.
                if (node_type == 0):
                    res = await eval(i.function)
                    if (res == "FAIL"):
                        if (sequence):
                            # End of sequence
                            return res
                        else:
                            # Next task in the fallback list
                            continue
                    elif (res == "RUNNING"):
                        # Wait for the action to finish
                        return res
                    else:
                        i.visited = True
                        if (sequence):
                            continue
                        else:
                            return res
                # If the node is a sequence, execute its children in sequence mode.
                elif (node_type == 1):
                    res = await self.run_nodes(i.children, True, obs)
                    if (res == "OK"):
                        i.visited = True                     
                    return res
                # If the node is a fallback, execute its children in fallback mode.
                elif (node_type == 2):
                    res = await self.run_nodes(i.children, False, obs)   
                    if (res == "OK"):
                        i.visited = True 
                    return res

        if(sequence): 
            return "OK"
        else:
            return "FAIL"



