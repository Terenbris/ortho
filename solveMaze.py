import numpy as np
#import maze

size = 9
done = False
#board = np.zeros((size,size))
#board = maze.initMaze(board, 1, 1)
stack = [[]]
sboard = []

def checkUnvisited(x, y, end):
    temp = []
    for i in range(-1,2):
        for j in range(-1,2):
            if 0 < x+i < len(sboard) and 0 < y+j < len(sboard) and (i == 0 or j == 0) and sboard[x+i][y+j] != 0:
                if sboard[x+i][y+j] == 6 and end:
                    print("done")
                    temp = [[x+i,y+j,1]]
                    return temp
                elif sboard[x+i][y+j] == 9:
                    temp.append([x+i,y+j,2])
                else:
                    temp.append([x+i,y+j,0])
    for x in temp[:]:
        if x[2] == 2:
            temp.remove(x)
    return temp
def move(end):
    global stack
    global done
    temp = stack.pop()
    stack.append(temp[:])
    unv = []
    unvtemp = checkUnvisited(temp[0],temp[1], end)
    for x in unvtemp:
        if x[2] != 2:
            #print(stack)
            unv.append(x[:])
    #print(unv)
    if len(unv) == 0:
        tstack = np.copy(stack)
        stack.pop()
        return tstack
    elif unv[0][2] == 3:
        print("blocked")
        return None
    else:
        mov = np.random.randint(len(unv))-1
        sboard[unv[mov][0]][unv[mov][1]] = 9
        stack.append([unv[mov][0],unv[mov][1]])
        if unv[mov][2] == 1:
            done = True
            return stack

def solve(sboard,playerPos):
    sboard[playerPos[0]][playerPos[1]] = 9
    stack.append(playerPos)
    while not(done):
        move(True)

def keyFunc(e):
    return len(str(e))

def solveLength(b,playerPos):
    global sboard
    sboard = np.copy(b)
    ends = []
    sboard[playerPos[0]][playerPos[1]] = 9
    stack.append(playerPos)
    move(False)
    while len(stack) > 1:
        temp = move(False)
        #print(temp)
        if temp != []:
            ends.append(temp)
    if len(ends) > 1:
        ends.sort(key=keyFunc)
    #print(sboard)
    #print()
    return ends


#solveLength(board, [1,1])

