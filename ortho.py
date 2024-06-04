# Example file showing a basic pygame "game loop"
import pygame
import numpy as np

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
chunkSize = 75
genDepth = 0
layer = False
widthMultiple = screen.get_width()/chunkSize
heightMultiple = screen.get_height()/chunkSize
b = "5678"
s = "45678"

chunk = np.random.randint(0,2,size=(chunkSize,chunkSize,2))
#chunk = np.zeros((chunkSize,chunkSize,2))
for z in range(genDepth):
    for x in range(chunkSize):
        for y in range(chunkSize):
            nbr = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    #print("Pos: " + str(x) + " " + str(y))
                    #print("subPos: " + str(x+i) + " " + str(y+j))
                    if (i != 0 or j != 0) and 0 <= x+i < chunkSize and 0 <= y+j < chunkSize and chunk[x+i][y+j][0] == 1:
                        nbr += 1
            if chunk[x][y][0] == 1 and (nbr > 3 or nbr < 2):
                chunk[x][y][1] = 0
            elif chunk[x][y][0] == 0 and nbr == 3:
                chunk[x][y][1] = 1
            else: 
                chunk[x][y][1] = chunk[x][y][0]
    for x in range(chunkSize):
        for y in range(chunkSize):
            chunk[x][y][0] = chunk[x][y][1]

    


#print(chunk)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

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

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(12)  # limits FPS to 60

pygame.quit()