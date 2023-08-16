import pygame
from pygame.locals import *

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((1080, 720))

    running = True
    while running:
        for event in pygame.event.get(): 
            if event.type == QUIT:
                running = False
                break

    pygame.quit()