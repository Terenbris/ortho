import numpy as np
import pygame

size = 5
size*=3
board = np.zeros((size, size))
stack = [[]]
player = [[1,1]]

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
widthMultiple = screen.get_width()/size
heightMultiple = screen.get_height()/size

stack.append([1,1])

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


def genMaze():
    board = np.zeros((size, size))
    stack = [[]]
    stack.append()
    while len(stack) > 1:
        move()
    if board[-2][-2] == 5:
        board[1][1] = 6
    else:
        board[-2][-2] = 6
        #print(board)
def keySpawn():
    k = 4
    while k > 0:
        tx = np.random.randint(size-1)
        ty = np.random.randint(size-1)
        if board[tx][ty] == 1:
            board[tx][ty] = 3
            k-=1
        
genMaze()

    # Example file showing a basic pygame "game loop"



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    board[player[0][0]][player[0][1]] = 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and board[player[0][0]][player[0][1] - 1] != 0:
        player[0][1] -= 1
    if keys[pygame.K_s] and board[player[0][0]][player[0][1] + 1] != 0:
        player[0][1] += 1
    if keys[pygame.K_a] and board[player[0][0] - 1][player[0][1]] != 0:
        player[0][0] -= 1
    if keys[pygame.K_d] and board[player[0][0] + 1][player[0][1]] != 0:
        player[0][0] += 1
    if board[player[0][0]][player[0][1]]  == 6:
        board[player[0][0]][player[0][1]] = 5
        genMaze()
    board[player[0][0]][player[0][1]] = 5

    # RENDER YOUR GAME HERE
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
                pygame.draw.rect(screen, "yellow", pygame.Rect(x*widthMultiple, y*heightMultiple, widthMultiple, heightMultiple))
            elif board[x][y] == 5:
                pygame.draw.rect(screen, "purple", pygame.Rect(x*widthMultiple, y*heightMultiple, widthMultiple, heightMultiple))
            elif board[x][y] == 6:
                pygame.draw.rect(screen, "green", pygame.Rect(x*widthMultiple, y*heightMultiple, widthMultiple, heightMultiple))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(12)  # limits FPS to 60

pygame.quit()
