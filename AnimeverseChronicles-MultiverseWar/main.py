import pygame
from pygame.locals import *
from Gameplay import *
<<<<<<< Updated upstream
from states import *

=======
from collide_checker import *
>>>>>>> Stashed changes
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1366, 768), RESIZABLE)
    pygame.display.set_caption('AnimeverseChronicles-MultiverseWar')

    Gameplay = gameplay(screen)
    Gameplay.update()

    play_pause_pos = (screen.get_rect().width - Gameplay.pause_button.get_rect().width - 10, 10)
    mouse = pygame.mouse.get_pos()
    IsResize = False


    pygame.display.update()

def draw_gameplay_ui():
    screen.blit(Gameplay.bg, (0, 0))
    screen.blit(Gameplay.path, (0, screen.get_rect().height - Gameplay.path.get_rect().height))
    screen.blit(Gameplay.nexus1, (5,  screen.get_rect().height - Gameplay.path.get_rect().height - Gameplay.nexus1.get_rect().height + Gameplay.path.get_rect().height // 3))
    screen.blit(Gameplay.nexus2, (screen.get_rect().width - 5 - Gameplay.nexus2.get_rect().width,  screen.get_rect().height - Gameplay.path.get_rect().height - Gameplay.nexus1.get_rect().height + Gameplay.path.get_rect().height // 3)) 
    screen.blit(Gameplay.board, (-2,  -2))
    screen.blit(Gameplay.timer_text, Gameplay.timer_text_rect)
    screen.blit(Gameplay.gold_text, Gameplay.gold_text_rect)
    
    if Gameplay.isPlay == True:
        screen.blit(Gameplay.pause_button, play_pause_pos)
    else:
        screen.blit(Gameplay.play_button, play_pause_pos)

def check_click():
    if play_pause_pos[0] <= mouse[0] <= play_pause_pos[0] + Gameplay.pause_button.get_rect().width and play_pause_pos[1] <= mouse[1] <= play_pause_pos[1] + Gameplay.pause_button.get_rect().height:
        Gameplay.SwitchPlayPauseState()
        Gameplay.isPlay = 1 - Gameplay.isPlay
        return


if __name__ == '__main__':
    running = True
    pygame.time.Clock().tick(Gameplay.FPS)     
    while running:
        if IsResize == True:
            IsResize = False
            Gameplay.screen_resize()
            Gameplay.SetScreen(screen)
        Gameplay.update()
        mouse = pygame.mouse.get_pos()
        play_pause_pos = (screen.get_rect().width - Gameplay.pause_button.get_rect().width - 10, 10)

        for event in pygame.event.get(): 
            if event.type == QUIT:
                running = False
                break
            if event.type == VIDEORESIZE:
                IsResize = True
                
            if event.type == MOUSEBUTTONDOWN:
                check_click()
<<<<<<< Updated upstream
            
=======
>>>>>>> Stashed changes
        draw_gameplay_ui()
        Gameplay.archer.operation()
        Gameplay.sword_man.operation()
        Gameplay.tanker.operation()
        # Gameplay.straw_doll.operation()
        # Gameplay.straw_doll2.operation()
        # Gameplay.straw_doll3.operation()

        
        pygame.display.update()

    pygame.quit()