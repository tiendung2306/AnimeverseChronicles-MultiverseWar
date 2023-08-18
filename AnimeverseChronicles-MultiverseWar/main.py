import pygame
from pygame.locals import *
from Gameplay import *
from states import *

class main():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1366, 768), RESIZABLE)
        pygame.display.set_caption('AnimeverseChronicles-MultiverseWar')

        self.Gameplay = gameplay()
        self.Gameplay.update()

        self.play_pause_button = (self.screen.get_rect().width - self.Gameplay.pause_button.get_rect().width - 10, 10)
        self.mouse = pygame.mouse.get_pos()
        self.IsResize = False

        pygame.time.set_timer(pygame.USEREVENT, 10)

        pygame.display.update()

        self.mainloop()

    def draw_gameplay_ui(self):
        self.screen.blit(self.Gameplay.bg, (0, 0))
        self.screen.blit(self.Gameplay.path, (0, self.screen.get_rect().height - self.Gameplay.path.get_rect().height))
        self.screen.blit(self.Gameplay.nexus1.nexus_surface, (5,  self.screen.get_rect().height - self.Gameplay.path.get_rect().height - self.Gameplay.nexus1.nexus_surface.get_rect().height + self.Gameplay.path.get_rect().height // 3))
        self.screen.blit(self.Gameplay.nexus2.nexus_surface, (self.screen.get_rect().width - 5 - self.Gameplay.nexus2.nexus_surface.get_rect().width,  self.screen.get_rect().height - self.Gameplay.path.get_rect().height - self.Gameplay.nexus1.nexus_surface.get_rect().height + self.Gameplay.path.get_rect().height // 3)) 
        self.screen.blit(self.Gameplay.board, (-2,  -2))
        self.screen.blit(self.Gameplay.timer_text, self.Gameplay.timer_text_rect)
        self.screen.blit(self.Gameplay.gold_text, self.Gameplay.gold_text_rect)
        
        if self.Gameplay.isPlay == True:
            self.screen.blit(self.Gameplay.pause_button, self.play_pause_button)
        else:
            self.screen.blit(self.Gameplay.play_button, self.play_pause_button)

    def check_click(self):
        if self.play_pause_button[0] <= self.mouse[0] <= self.play_pause_button[0] + self.Gameplay.pause_button.get_rect().width and self.play_pause_button[1] <= self.mouse[1] <= self.play_pause_button[1] + self.Gameplay.pause_button.get_rect().height:
            self.Gameplay.SwitchPlayPauseState()
            self.Gameplay.isPlay = 1 - self.Gameplay.isPlay
            return

    def mainloop(self):
        running = True
        while running:
            if self.IsResize == True:
                self.IsResize = False
                self.Gameplay.screen_resize()
            self.Gameplay.update()
            self.mouse = pygame.mouse.get_pos()
            self.play_pause_button = (self.screen.get_rect().width - self.Gameplay.pause_button.get_rect().width - 10, 10)

            for event in pygame.event.get(): 
                if event.type == QUIT:
                    running = False
                    break
                if event.type == VIDEORESIZE:
                    self.IsResize = True
                if event.type == MOUSEBUTTONDOWN:
                    self.check_click()
                if event.type == pygame.USEREVENT:
                    self.Gameplay.time += 0.01
                
            self.draw_gameplay_ui()
            self.Gameplay.archer.operation(self.screen)
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    main()