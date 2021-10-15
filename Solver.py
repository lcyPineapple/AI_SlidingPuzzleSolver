# This is the file that implements breadth first search,
# depth first search, greedy best first search, and AStar
# in order to solve an n x n sliding puzzle.
# AUTHOR: LEIKA YAMADA
# DATE: 7/12/2021
import Board
depth = -1
numCreated = 0
numExpanded = 0
maxFringe = 0
visitList = []
fringeList = []

#############################################################
# Getter methods for search stats
#############################################################
def getDepth():
    return depth
def getnumCreated():
    return numCreated
def getnumExpanded():
    return numExpanded
def getmaxFringe():
    return maxFringe
#############################################################
# This method uses Breadth First Search to find a solution
# to a puzzle predetermined to be solvable.
# Parameter: size (int), initialState (List)
# Return: List that contains the path to the goal
#############################################################
def bfs(initState, goalState, size):
    global numCreated
    global numExpanded
    global maxFringe
    firstNode = Board.puzzleState(initState, None, 0, 0)
    fringeList.append(firstNode)
    numCreated += 1
    visitList.append(fringeList.pop(0))
    numExpanded += 1
    maxFringe += 1
    index = 0
    while visitList[index].current != goalState:
        currState = visitList[index]
        legalMoves = Board.findMoves(currState, size)
        for x in legalMoves:
            numCreated += 1
            fringeList.append(x)
        if len(fringeList) > maxFringe:
            maxFringe = len(fringeList)
        visitList.append(fringeList.pop(0))
        numExpanded += 1
        index += 1
    return recovery(visitList)
#############################################################
# This method uses Depth First Search to find a solution
# to a puzzle predetermined to be solvable.
# Parameter: size (int), initialState (List)
# Return: List that contains the path to the goal
#############################################################
def dfs(initState, goalState, size):
    global numCreated
    global numExpanded
    global maxFringe
    firstNode = Board.puzzleState(initState, None, 0, 0)
    fringeList.append(firstNode)
    numCreated += 1
    visitList.append(fringeList.pop(0))
    numExpanded += 1
    maxFringe += 1
    index = 0
    while visitList[index].current != goalState:
        currState = visitList[index]
        legalMoves = Board.findMoves(currState, size)
        for x in legalMoves:
            alreadyVisited = False
            for y in visitList:
                if y.current == x.current:
                    alreadyVisited = True
            if alreadyVisited == False:
                numCreated += 1
                fringeList.append(x)
        if len(fringeList) > maxFringe:
            maxFringe = len(fringeList)
        visitList.append(fringeList.pop(len(fringeList)-1))
        numExpanded += 1
        index += 1
    return recovery(visitList)
#############################################################
# This method uses Greedy Best First Search to find a solution
# to a puzzle predetermined to be solvable.
# Parameter: size (int), initialState (List)
# Return: List that contains the path to the goal
#############################################################
def gbfs(initState, goalState, size):
    global numCreated
    global numExpanded
    global maxFringe
    firstNode = Board.puzzleState(initState, None, 0, 0)
    fringeList.append(firstNode)
    numCreated += 1
    visitList.append(fringeList.pop(0))
    numExpanded += 1
    maxFringe += 1
    index = 0
    while visitList[index].current != goalState:
        currState = visitList[index]
        legalMoves = Board.findMoves(currState, size)
        for x in legalMoves:
            alreadyVisited = False
            for y in visitList:
                if y.current == x.current:
                    alreadyVisited = True
            if alreadyVisited == False:
                numCreated += 1
                Board.heuristic(x, size)
                if len(fringeList) == 0:
                    fringeList.append(x)
                else:
                    zcount = 0
                    for z in fringeList:
                        if z.heuristic > x.heuristic:
                            fringeList.insert(zcount, x)
                            break
                        zcount = zcount + 1
        if len(fringeList) > maxFringe:
            maxFringe = len(fringeList)
        visitList.append(fringeList.pop(0))
        numExpanded += 1
        index += 1
    return recovery(visitList)
#############################################################
# This method uses Astar Search to find a solution
# to a puzzle predetermined to be solvable.
# Parameter: size (int), initialState (List)
# Return: List that contains the path to the goal
#############################################################
def astar(initState, goalState, size):
    global numCreated
    global numExpanded
    global maxFringe
    firstNode = Board.puzzleState(initState, None, 0, 0)
    fringeList.append(firstNode)
    numCreated += 1
    visitList.append(fringeList.pop(0))
    numExpanded += 1
    maxFringe += 1
    index = 0
    while visitList[index].current != goalState:
        currState = visitList[index]
        legalMoves = Board.findMoves(currState, size)
        for x in legalMoves:
            alreadyVisited = False
            for y in visitList:
                if y.current == x.current:
                    alreadyVisited = True
            if alreadyVisited == False:
                numCreated += 1
                Board.astarHeuristic(x, size, visitList)
                if len(fringeList) == 0:
                    fringeList.append(x)
                else:
                    zcount = 0
                    for z in fringeList:
                        if z.heuristic > x.heuristic:
                            fringeList.insert(zcount, x)
                            break
                        zcount = zcount + 1
        if len(fringeList) > maxFringe:
            maxFringe = len(fringeList)
        visitList.append(fringeList.pop(0))
        numExpanded += 1
        index += 1
    return recovery(visitList)
#############################################################
# This method checks if the puzzle is solvable from the
# given initial state.
# Parameter: size (int), initialState (List)
# Return: boolean, true when solvable, false otherwise
#############################################################
def solvability(size, initialState):
    inversionCount = 0
    i = 0
    j = 0
    space = 0
    spaceChar = 32
    # Count inversions in the puzzle
    while i < len(initialState):
        x = ord(initialState[i])
        # Store the index of the space character
        if spaceChar == x:
            space = i
        j = i
        i += 1
        while j < len(initialState):
            y = ord(initialState[j])
            # Do not count inversion if it is the space char
            if x > y and y != spaceChar:
                inversionCount += 1
            j += 1
    # If the board is odd, then the puzzle is solvable when inversions are even
    if 1 == (size % 2):
        if 0 == (inversionCount % 2):
            return True
        else:
            return False
    # If the board is even, then the puzzle is solvable when inverisons + blank is odd
    else:
        if 1 == (inversionCount + space//size) % 2:
            return True
        else:
            return False
#############################################################
# This method finds the solution path from the list of
# visited nodes. And finds the depth of the solution.
# Return: List that contains the path to the goal
#############################################################
def recovery(visitList):
    global depth
    index = len(visitList) - 1
    path = []
    path.append(visitList[index])
    state = visitList[index].previous
    while index != 0:
        lookBack = visitList[index - 1].current
        if (state == lookBack):
            path.append(visitList[index - 1])
            state = visitList[index - 1].previous
        index -= 1
    depth = len(path) - 1
    return path