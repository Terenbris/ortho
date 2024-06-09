import numpy as np
import pygame

size = 3
size*=3
board = np.zeros((size, size))
stack = [[]]
player = [[1,1]]
keysHeld = 0
keyReq = False
nKey = 5

# pygame setup
#pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
tl = 0
widthMultiple = screen.get_width()/size
heightMultiple = screen.get_height()/size


#print(stack.pop())


def checkUnvisited(x, y):
    temp = []
    for i in range(-1,2):
        for j in range(-1,2):
            if 0 < x+(i*2) < len(board) and 0 < y+(j*2) < len(board) and (i == 0 or j == 0) and board[x+(i*2)][y+(j*2)] == 0:
                temp.append([x+(i*2),y+(j*2),x+i,y+j])
    return temp

def move():
    temp = stack.pop()
    stack.append(temp)
    unv = checkUnvisited(temp[0],temp[1])
    if (len(unv)) == 0:
        stack.pop()
        return None
    else:
        mov = np.random.randint(len(unv))-1
        board[unv[mov][2]][unv[mov][3]] = 1
        board[unv[mov][0]][unv[mov][1]] = 1
        stack.append([unv[mov][0],unv[mov][1]])


def genMaze(start = [1,1]):
    stack.append(start) 
    while len(stack) > 1:
        move()
    genEnd()
    if keyReq:
        keySpawn()

def genEnd():
    board[player[0][0]][player[0][1]] = 5
    tl = np.random.randint(4)
    for z in range(4):
        if tl == 0 and board[1][1] != 5:
            board[1][1] = 6
        elif tl == 1 and board[1][-2] != 5:
            board[1][-2] = 6
        elif tl == 2 and board[-2][1] != 5:
            board[-2][1] = 6
        elif tl == 3 and board[-2][-2] != 5:
            board[-2][-2] = 6
        else:
            tl += 1
            if tl > 3:
                tl = 0
    board[player[0][0]][player[0][1]] = 1

def keySpawn():
    global keysHeld
    k = nKey
    keysHeld = 0
    while k > 0:
        tx = np.random.randint(size-1)
        ty = np.random.randint(size-1)
        if board[tx][ty] == 1:
            board[tx][ty] = 3
            k-=1

def drawScreen(s=size, screen=pygame.display.set_mode((600, 600))):
    size = s
    widthMultiple = screen.get_width()/size
    heightMultiple = screen.get_height()/size
    screen.fill("black")
    for x in range(size):
        for y in range(size):
            if size < 150:
                pygame.draw.line(screen, "gray", (x*widthMultiple, 0), (x*widthMultiple, heightMultiple*size))
                pygame.draw.line(screen, "gray", (0, y*heightMultiple), (widthMultiple*size, y*heightMultiple))
            if board[x][y] == 1:
                if (x % 2 == 0 and y % 2 != 0) or (y % 2 == 0 and x % 2 != 0):
                    clr = "white"
                else:
                    clr = "white"
                pygame.draw.rect(screen, clr, pygame.Rect(x*widthMultiple, y*heightMultiple, widthMultiple, heightMultiple))
            elif board[x][y] == 3:
                pygame.draw.rect(screen, "orange", pygame.Rect(x*widthMultiple, y*heightMultiple, widthMultiple, heightMultiple))
            elif board[x][y] == 6:
                pygame.draw.rect(screen, "green", pygame.Rect(x*widthMultiple, y*heightMultiple, widthMultiple, heightMultiple))
            
            pygame.draw.rect(screen, "purple", pygame.Rect(player[0][0]*widthMultiple, player[0][1]*heightMultiple, widthMultiple, heightMultiple))

def movement():
    global keysHeld
    global board
    if board[player[0][0]][player[0][1]] == 3 and keyReq:
        keysHeld += 1
        board[player[0][0]][player[0][1]] = 1

    #board[player[0][0]][player[0][1]] = 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and 0 < player[0][1] and board[player[0][0]][player[0][1] - 1] != 0:
        player[0][1] -= 1
    if keys[pygame.K_DOWN] and player[0][1] < len(board)-1 and board[player[0][0]][player[0][1] + 1] != 0:
        player[0][1] += 1
    if keys[pygame.K_LEFT] and 0 < player[0][0] and board[player[0][0] - 1][player[0][1]] != 0:
        player[0][0] -= 1
    if keys[pygame.K_RIGHT] and player[0][0] < len(board)-1 and  board[player[0][0] + 1][player[0][1]] != 0:
        player[0][0] += 1
    if board[player[0][0]][player[0][1]]  == 6:
        if (keyReq and keysHeld == nKey) or not(keyReq):
            board = np.zeros((size, size))
            genMaze([player[0][0],player[0][1]])

    # Example file showing a basic pygame "game loop"
genMaze()
def initMaze(array,x,y):
    global board
    global stack
    board = array
    genMaze([x,y])
    return board


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    
    movement()

    # RENDER YOUR GAME HERE
    drawScreen()
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(12)  # limits FPS to 60

pygame.quit()
