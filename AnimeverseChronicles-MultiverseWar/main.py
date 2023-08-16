import pygame
from pygame.locals import *
from Gameplay import *

def update():
    Gameplay.update()

if __name__ == '__main__':
    Gameplay = gameplay()
    pygame.init()
    screen = pygame.display.set_mode((1366, 768), RESIZABLE)
    pygame.display.set_caption('AnimeverseChronicles-MultiverseWar')

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
        screen.blit(Gameplay.nexus1, (20,  510))
        screen.blit(Gameplay.nexus2, (1206,  510))
        screen.blit(Gameplay.board, (-2,  -2))
        screen.blit(Gameplay.timer_text, Gameplay.timer_text_rect)
        screen.blit(Gameplay.gold_text, Gameplay.gold_text_rect)
        pygame.display.update()

        # print(pygame.mouse.get_pos())

    pygame.quit()