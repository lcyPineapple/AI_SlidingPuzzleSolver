# This is the file that models an nxn board
# for the sliding puzzle problem. Contains the
# heuristic function.
# AUTHOR: LEIKA YAMADA
# DATE: 7/12/2021

###################################################
# This class defines the puzzleState object, it
# stores the current and previous state of the
# sliding puzzle, to be used to trace the path
# to the solution once the goal state is reached
###################################################
class puzzleState:
    def __init__(self, current, previous, heuristic, depth):
        self.current = current
        self.previous = previous
        self.heuristic = heuristic
        self.depth = depth
###################################################
# This is method moves the blank piece left.
# Parameter: List containing the initial state of
# the puzzle, and the index of the blank tile
# returns: The next state of the puzzle
###################################################
def moveLeft(current, blankIndex):
    initialState = current.copy()
    initialState[blankIndex] = initialState[blankIndex - 1]
    initialState[blankIndex - 1] = ' '
    return initialState
###################################################
# This is method moves the blank piece right.
# Parameter: List containing the initial state of
# the puzzle, and the index of the blank tile
# returns: The next state of the puzzle
###################################################
def moveRight(current, blankIndex):
    initialState = current.copy()
    initialState[blankIndex] = initialState[blankIndex + 1]
    initialState[blankIndex + 1] = ' '
    return initialState
###################################################
# This is method moves the blank piece up.
# Parameter: List containing the initial state of
# the puzzle, and the index of the blank tile
# returns: The next state of the puzzle
###################################################
def moveUp(current, blankIndex, size):
    initialState = current.copy()
    initialState[blankIndex] = initialState[blankIndex - size]
    initialState[blankIndex - size] = ' '
    return initialState
###################################################
# This is method moves the blank piece up.
# Parameter: List containing the initial state of
# the puzzle, and the index of the blank tile
# returns: The next state of the puzzle
###################################################
def moveDown(current, blankIndex, size):
    initialState = current.copy()
    initialState[blankIndex] = initialState[blankIndex + size]
    initialState[blankIndex + size] = ' '
    return initialState
###################################################
# This is method generates all possible legal moves
# from the initialState.
# Parameter: List containing the initial state of
# the puzzle
# returns: A list of legal moves
###################################################
def findMoves(initialState, size):
    moveList = []
    myCurrent = initialState.current
    isInitial = False
    myPrevious = None
    blankPrev = None
    preLength = None
    if (initialState.previous is None):
        isInitial = True
    else:
        myPrevious = initialState.previous
        blankPrev = findBlank(myPrevious)
        prevLength = len(myPrevious)
    blank = findBlank(myCurrent)
    length = len(myCurrent)
    # Check if the blank piece is in the top left corner
    # There should only be one move in the corners
    if 0 == blank:
        right = moveRight(myCurrent, blank)
        down = moveDown(myCurrent, blank, size)
        move1 = puzzleState(right, myCurrent, 0, 0)
        move2 = puzzleState(down, myCurrent, 0, 0)
        moveList.append(move1)
        moveList.append(move2)
        if isInitial is False:
            if findBlank(right) == findBlank(myPrevious):
                moveList.remove(move1)
            else:
                moveList.remove(move2)
    # Check if the blank piece is in the top right corner
    elif (size - 1) == blank:
        left = moveLeft(myCurrent, blank)
        down = moveDown(myCurrent, blank, size)
        move1 = puzzleState(left, myCurrent, 0, 0)
        move2 = puzzleState(down, myCurrent, 0, 0)
        moveList.append(move1)
        moveList.append(move2)
        if isInitial is False:
            if findBlank(left) == findBlank(myPrevious):
                moveList.remove(move1)
            else:
                moveList.remove(move2)
    # Check if the blank piece is in the bottom left corner
    elif (length - size) == blank:
        right = moveRight(myCurrent, blank)
        up = moveUp(myCurrent, blank, size)
        move1 = puzzleState(right, myCurrent, 0, 0)
        move2 = puzzleState(up, myCurrent, 0, 0)
        moveList.append(move1)
        moveList.append(move2)
        if isInitial is False:
            if findBlank(right) == findBlank(myPrevious):
                moveList.remove(move1)
            else:
                moveList.remove(move2)
    # Check if the blank piece is in the bottom right corner
    elif (length - 1) == blank:
        left = moveLeft(myCurrent, blank)
        up = moveUp(myCurrent, blank, size)
        move1 = puzzleState(left, myCurrent, 0, 0)
        move2 = puzzleState(up, myCurrent, 0, 0)
        moveList.append(move1)
        moveList.append(move2)
        if isInitial is False:
            if findBlank(left) == findBlank(myPrevious):
                moveList.remove(move1)
            else:
                moveList.remove(move2)
    # Check if the blank piece is on the left side
    elif 0 == blank % size:
        right = moveRight(myCurrent, blank)
        up = moveUp(myCurrent, blank, size)
        down = moveDown(myCurrent, blank, size)
        move1 = puzzleState(right, myCurrent, 0, 0)
        move2 = puzzleState(up, myCurrent, 0, 0)
        move3 = puzzleState(down, myCurrent, 0, 0)
        moveList.append(move1)
        moveList.append(move2)
        moveList.append(move3)
        if isInitial is False:
            if findBlank(right) == findBlank(myPrevious):
                moveList.remove(move1)
            elif findBlank(up) == findBlank(myPrevious):
                moveList.remove(move2)
            else:
                moveList.remove(move3)
    # Check if the blank piece is on the right side
    elif size - 1 == blank % size:
        left = moveLeft(myCurrent, blank)
        up = moveUp(myCurrent, blank, size)
        down = moveDown(myCurrent, blank, size)
        move1 = puzzleState(left, myCurrent, 0, 0)
        move2 = puzzleState(up, myCurrent, 0, 0)
        move3 = puzzleState(down, myCurrent, 0, 0)
        moveList.append(move1)
        moveList.append(move2)
        moveList.append(move3)
        if isInitial is False:
            if findBlank(left) == findBlank(myPrevious):
                moveList.remove(move1)
            elif findBlank(up) == findBlank(myPrevious):
                moveList.remove(move2)
            else:
                moveList.remove(move3)
    # Check if the blank piece is on the top side
    elif blank < size:
        left = moveLeft(myCurrent, blank)
        right = moveRight(myCurrent, blank)
        down = moveDown(myCurrent, blank, size)
        move1 = puzzleState(left, myCurrent, 0, 0)
        move2 = puzzleState(right, myCurrent, 0, 0)
        move3 = puzzleState(down, myCurrent, 0, 0)
        moveList.append(move1)
        moveList.append(move2)
        moveList.append(move3)
        if isInitial is False:
            if findBlank(left) == findBlank(myPrevious):
                moveList.remove(move1)
            elif findBlank(right) == findBlank(myPrevious):
                moveList.remove(move2)
            else:
                moveList.remove(move3)
    # Check if the blank piece is on the bottom side
    elif blank >= length - size:
        left = moveLeft(myCurrent, blank)
        right = moveRight(myCurrent, blank)
        up = moveUp(myCurrent, blank, size)
        move1 = puzzleState(left, myCurrent, 0, 0)
        move2 = puzzleState(right, myCurrent, 0, 0)
        move3 = puzzleState(up, myCurrent, 0, 0)
        moveList.append(move1)
        moveList.append(move2)
        moveList.append(move3)
        if isInitial is False:
            if findBlank(left) == findBlank(myPrevious):
                moveList.remove(move1)
            elif findBlank(right) == findBlank(myPrevious):
                moveList.remove(move2)
            else:
                moveList.remove(move3)
    # The piece is not on the edge of the board
    else:
        left = moveLeft(myCurrent, blank)
        right = moveRight(myCurrent, blank)
        down = moveDown(myCurrent, blank, size)
        up = moveUp(myCurrent, blank, size)
        move1 = puzzleState(left, myCurrent, 0, 0)
        move2 = puzzleState(right, myCurrent, 0, 0)
        move3 = puzzleState(up, myCurrent, 0, 0)
        move4 = puzzleState(down, myCurrent, 0, 0)
        moveList.append(move1)
        moveList.append(move2)
        moveList.append(move3)
        moveList.append(move4)
        if isInitial is False:
            if findBlank(left) == findBlank(myPrevious):
                moveList.remove(move1)
            elif findBlank(right) == findBlank(myPrevious):
                moveList.remove(move2)
            elif findBlank(up) == findBlank(myPrevious):
                moveList.remove(move3)
            else:
                moveList.remove(move4)
    return moveList
###################################################
# This is method finds the index of the blank tile
# Parameter: List containing the initial state of
# the puzzle
# returns: the index of the blank piece, if no
# blank exists then it will return listSize + 1
###################################################
def findBlank(initialState):
    blank = 0
    for x in initialState:
        if x == ' ':
            break
        blank += 1
    return blank
###################################################
# This finds the manhattan distance of each piece
# and adds all the distances to get the greedy
# heuristic value
###################################################
def heuristic(state, size):
    currState = state.current
    myheuristic = 0
    x = 0
    y = 0
    x1 = 0
    y1 = 0
    index = 0
    while index < len(currState):
        x1 = ord(currState[index])
        if x1 != 32:
            if x1 < 65:
                x1 = x1 - 49
            else:
                x1 = x1 - 56
            y1 = x1 // size
            x1 = x1 % size
            myheuristic = abs(x1 - x) + abs(y1 - y) + myheuristic
        x = (x + 1) % size
        y = (index + 1) // size
        index += 1
    state.heuristic = myheuristic
###################################################
# This finds the manhattan distance of each piece
# and adds all the distances and adds it to the
# depth of the node to get the astar
# heuristic value
###################################################
def astarHeuristic(state, size, visitList):
    heuristic(state, size)
    myHeuristic = state.heuristic
    index = len(visitList) - 1
    currDepth = 0
    currstate = visitList[index].previous
    while index != 0:
        lookBack = visitList[index - 1].current
        if (currstate == lookBack):
            currDepth += 1
            currstate = visitList[index - 1].previous
        index -= 1
    state.heuristic = myHeuristic + currDepth
