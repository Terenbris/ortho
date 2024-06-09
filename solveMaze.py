import numpy as np
import maze

size = 9
done = False
board = np.zeros((size,size))
board = maze.initMaze(board, 1, 1)
stack = []
print(board)

def checkUnvisited(x, y, end):
    temp = []
    for i in range(-1,2):
        for j in range(-1,2):
            if 0 < x+i < len(board) and 0 < y+j < len(board) and (i == 0 or j == 0) and board[x+i][y+j] == 1 or board[x+i][y+j] == 6:
                if board[x+i][y+j] == 6 and end:
                    print("done")
                    temp = [[x+i,y+j,1]]
                    return temp
                else:
                    temp.append([x+i,y+j,0])
    return temp



def move(end):
    global done
    temp = stack.pop()
    stack.append(temp)
    unv = checkUnvisited(temp[0],temp[1], end)
    if (len(unv)) == 0:
        tstack = stack
        stack.pop()
        #print(tstack)
        return tstack
    else:
        mov = np.random.randint(len(unv))-1
        board[unv[mov][0]][unv[mov][1]] = 9
        stack.append([unv[mov][0],unv[mov][1]])
        if unv[mov][2] == 1:
            done = True
            return stack

def solve(board,playerPos):
    board[playerPos[0]][playerPos[1]] = 9
    stack.append(playerPos)
    while not(done):
        move(True)

def solveLength(board,playerPos,k):
    ends = []
    board[playerPos[0]][playerPos[1]] = 9
    stack.append(playerPos)
    move(False)
    while len(stack) > 1:
        temp = move(False)
        #print(temp)
        if temp:
            ends.append(temp)
            print(ends)


solveLength(board, [1,1], 1)

