import maze
import ortho
import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
running = True
temp = ortho.outLife("5678","45678",70,100)

temp = maze.initMaze(temp, -2, -2)
maze.genEnd()
maze.keySpawn()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    
    maze.movement()

    # RENDER YOUR GAME HERE
    maze.drawScreen(len(temp),screen)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(12)  # limits FPS to 60

pygame.quit()