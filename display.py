import pygame


def drawScreen(array, sz):

    pygame.init()
    screen = pygame.display.set_mode((sz, sz))
    clock = pygame.time.Clock()
    running = True
    size = len(array)
    widthMultiple = screen.get_width()/size
    heightMultiple = screen.get_height()/size
