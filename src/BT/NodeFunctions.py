'''
Created on 15 maj 2018

@author: Shinke
'''

from BT import Tree, Node 

def doNothing(node):
    node.add_child(Node.Node(0, "functions.fail()"))

def trainQueen(node, amount):
    for _ in range(amount):
        node.add_child(Node.Node(0, "functions.trainQueen(obs)"))
        
def trainDrone(node, amount):
    for _ in range(amount):
        node.add_child(Node.Node(0, "functions.trainDrone(obs)"))
        
def trainOverlord(node, amount):
    for _ in range(amount):
        node.add_child(Node.Node(0, "functions.trainOverlord(obs)"))
        
def trainZergling(node, amount):
    for _ in range(amount):
        node.add_child(Node.Node(0, "functions.trainZergling(obs)"))
        
def trainRoach(node, amount):
    for _ in range(amount):
        node.add_child(Node.Node(0, "functions.trainRoach(obs)"))
        
def buildHatchery(node):
    node.add_child(Node.Node(0, "functions.buildHatchery(obs)"))

def buildExtractor(node):
    node.add_child(Node.Node(0, "functions.buildExtractor(obs)"))

def buildSpawningPool(node):
    node.add_child(Node.Node(0, "functions.buildSpawningPool(obs)"))
    
def buildRoachWarren(node):
    node.add_child(Node.Node(0, "functions.buildRoachWarren(obs)"))
    
def buildEvolutionChamber(node, amount):
    for _ in range(amount):
        node.add_child(Node.Node(0, "functions.buildEvolutionChamber(obs)"))

def researchSpeedling(node):
    node.add_child(Node.Node(0, "functions.researchSpeedling(obs)"))

def researchRangedAttackI(node):
    node.add_child(Node.Node(0, "functions.researchRangedAttackI(obs)"))

def researchArmorI(node):
    node.add_child(Node.Node(0, "functions.researchArmorI(obs)"))

def moveDronesToGas(node):
    node.add_child(Node.Node(0, "functions.moveDronesToGas(obs)"))

def attack(node):
    node.add_child(Node.Node(0, "functions.attack(obs)"))

def prepareArmy(node):
    node.add_child(Node.Node(0, "functions.prepareArmy(obs)"))

def main():
    
    # Main node
    main_node = Node.Node(1)
    
    # Build node.
    build_node = Node.Node(1)
    
    # Add children
    trainDrone(build_node, 1)
    trainOverlord(build_node, 1) # Overlord 13
    trainDrone(build_node, 3) 
    buildHatchery(build_node) # Hatchery 17
    trainDrone(build_node, 2) 
    buildExtractor(build_node) # Extractor 19
    buildSpawningPool(build_node) # Pool 18
    trainDrone(build_node, 2)
    moveDronesToGas(build_node)
    trainOverlord(build_node, 1) # Overlord 19
    trainZergling(build_node, 3) # Zergling 19
    trainQueen(build_node, 2)
    researchSpeedling(build_node) # Speedling 26
    trainDrone(build_node, 3)
    buildRoachWarren(build_node)
    trainDrone(build_node, 3)
    trainOverlord(build_node, 4)
    buildEvolutionChamber(build_node, 2)
    trainDrone(build_node, 3)
    trainOverlord(build_node, 2)
    trainRoach(build_node, 5)
    researchRangedAttackI(build_node)
    researchArmorI(build_node)
    trainOverlord(build_node, 1)
    trainDrone(build_node, 8)
    buildExtractor(build_node)
    trainDrone(build_node, 4)
    trainRoach(build_node, 3)
    moveDronesToGas(build_node)
    trainRoach(build_node, 4)
    buildExtractor(build_node)
    trainRoach(build_node, 4)
    moveDronesToGas(build_node)

    main_node.add_child(build_node)

    #Late game 
    late_game = Node.Node(1)
    for _ in range(30):
        trainOverlord(late_game, 1)
        trainRoach(late_game, 4)

    main_node.add_child(late_game)


    
    return Tree.Tree(main_node)




