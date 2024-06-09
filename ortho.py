# Example file showing a basic pygame "game loop"
import pygame
import numpy as np

# pygame setup
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
chunkSize = 75
layer = False
widthMultiple = screen.get_width()/chunkSize
heightMultiple = screen.get_height()/chunkSize
b = "5678"
s = "45678"

def outLife(b,s,cs,gd):
    global chunkSize
    chunkSize = int(cs)
    initLife(b, s)
    for z in range(int(gd)):
        genLife(b,s)
    temp = np.zeros((chunkSize,chunkSize))
    for x in range(chunkSize):
        for y in range(chunkSize):
            temp[x][y] = chunk[x][y][0]
    return temp


def initLife(b, s):
    global chunk
    chunk = np.random.randint(0,2,size=(chunkSize,chunkSize,2))

def makeSparse():
    for z in range(1):
        for x in range(chunkSize):
            for y in range(chunkSize):
                temp = np.random.randint(0,2,size=(chunkSize,chunkSize))
                if temp[x][y] == chunk[x][y][0] == 1:
                    chunk[x][y][0] = 1
                else:
                    chunk[x][y][0] = 0

        
    genLife(b,s)

def genLife(b, s):
    #chunk = np.zeros((chunkSize,chunkSize,2))
    for x in range(chunkSize):
        for y in range(chunkSize):
            nbr = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    #print("Pos: " + str(x) + " " + str(y))
                    #print("subPos: " + str(x+i) + " " + str(y+j))
                    if (i != 0 or j != 0) and 0 <= x+i < chunkSize and 0 <= y+j < chunkSize and chunk[x+i][y+j][0] == 1:
                        nbr += 1
            chunk[x][y][1] = chunk[x][y][0]
            for z in list(s):
                if nbr == int(z) and chunk[x][y][0] == 1:
                    break
            else:
                chunk[x][y][1] = 0
            for z in list(b):
                if nbr == int(z) and chunk[x][y][0] == 0:
                    chunk[x][y][1] = 1
    
    for x in range(chunkSize):
        for y in range(chunkSize):
            chunk[x][y][0] = chunk[x][y][1]

def drawScreen():
    screen.fill("black")

    for x in range(chunkSize):
        for y in range(chunkSize):
            if chunkSize < 150:
                pygame.draw.line(screen, "gray", (x*widthMultiple, 0), (x*widthMultiple, heightMultiple*chunkSize))
                pygame.draw.line(screen, "gray", (0, y*heightMultiple), (widthMultiple*chunkSize, y*heightMultiple))
            if chunk[x][y][0] == 1:
                if (x % 2 == 0 and y % 2 != 0) or (y % 2 == 0 and x % 2 != 0):
                    clr = "white"
                else:
                    clr = "white"
                pygame.draw.rect(screen, clr, pygame.Rect(x*widthMultiple, y*heightMultiple, widthMultiple, heightMultiple))
    
initLife(b, s)

#print(chunk)

