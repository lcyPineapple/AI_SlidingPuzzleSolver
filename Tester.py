# This is the driver file for the Puzzle Solver program.
# AUTHOR: LEIKA YAMADA

# Import the board and solver files
import Board
import Solver


# Global Variables
size = 0
initialState = "none"
initList = []
algo = "none"
depth = -1
numCreated = 0
numExpanded = 0
maxFringe = 0
pathList = []
goalState = []
goalSize2 = "123 "
goalSize3 = "12345678 "
goalSize4 = "123456789ABCDEF "
solvable = 0


# Methods
#############################################################
# acceptInput()
# This method prompts the user for input and parses user
# input for the size, initial state and the search algorithm
# to use. Side effects: stores size, initalState, and algo
# in the global vars of the same name
#############################################################
def acceptInput():
    global size
    global initialState
    global algo
    global initList
    global goalState
    global goalSize2
    global goalSize3
    global goalSize4
    print('Enter the puzzle size, initial puzzle state, and search method')
    myString = input('in the form [size], ["Initial State"], [Search Algorithm]: ')
    myInputList = myString.split(',')
    size = int(myInputList[0])
    initialState = myInputList[1].split('"')[1]
    algo = myInputList[2]
    initList = [char for char in initialState]
    if 2 == size:
        goalState = [char for char in goalSize2]
    elif 3 == size:
        goalState = [char for char in goalSize3]
    else:
        goalState = [char for char in goalSize4]

#############################################################
# outputResult()
# This method writes the results to the readme file. It
# takes the data generated during the solving process and
# writes it to the readMe file. If the file does not exist
# it creates the file. If the file does exist, it will
# overwrite the data in the file.
#############################################################
def outputResult():
    global size
    global initialState
    global initList
    global algo
    global depth
    global numCreated
    global numExpanded
    global maxFringe
    global goalState
    global pathList
    global solvable
    depth = Solver.getDepth()
    numCreated = Solver.getnumCreated()
    numExpanded = Solver.getnumExpanded()
    maxFringe = Solver.getmaxFringe()
    File_object = open(r"Readme.txt", "w")
    if solvable != True:
        print('Puzzle is not Solvable')
        File_object.write("Puzzle is not Solvable, default values are printed below \n")
    File_object.write("Size: " + str(size) + "\n")
    File_object.write("Initial State: \"" + initialState + "\"\n")
    File_object.write("Goal State: \"")
    for x in goalState:
        File_object.write(x)
    File_object.write("\"\n")
    File_object.write("Search Method:" + algo + "\n")
    File_object.write("Solution Discovered at [depth, numCreated, numExpanded, maxFringe]: "
                      + str(depth) + ", " + str(numCreated)
                      + ", " + str(numExpanded) + ", " + str(maxFringe) + "\n")
    File_object.close()
    index = len(pathList) - 1
    while index >= 0:
        print(pathList[index].current)
        index -= 1

#############################################################
# This is the main method of the program.
# The program starts here:
#############################################################
acceptInput()
solvable = Solver.solvability(size, initList)
if solvable:
    if "BFS" in algo:
        pathList = Solver.bfs(initList, goalState, size)
    elif "DFS" in algo:
        pathList = Solver.dfs(initList, goalState, size)
    elif "GBFS" in algo:
        pathList = Solver.gbfs(initList, goalState, size)
    elif "Astar" in algo:
        pathList = Solver.astar(initList, goalState, size)
    else:
        print("User inputted algorithm is not supported")
        print("Please enter: BFS, DFS, GBFS, or Astar")
outputResult()


