import pygame, os
from pygame.locals import *
from Gameplay import *

def update():
    Gameplay.update()

if __name__ == '__main__':
    Gameplay = gameplay()

    os.environ['SDL_VIDEO_CENTERED'] = '1' # You have to call this before pygame.init()
    pygame.init()
    screen = pygame.display.set_mode((1366, 768), RESIZABLE)
    Gameplay.update()
    pygame.display.update()

    running = True
    while running:
        update()
        for event in pygame.event.get(): 
            if event.type == QUIT:
                running = False
                break
        screen.blit(Gameplay.bg, (0, 0))
        pygame.display.update()

    pygame.quit()