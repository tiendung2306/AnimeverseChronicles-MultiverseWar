import pygame
from pygame.locals import *
from Gameplay import *
from states import *
from MainMenu import *

class main():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1400, 900))
        pygame.display.set_caption('AnimeverseChronicles-MultiverseWar')

        self.MainMenu = mainmenu()
        self.Gameplay = gameplay()
        self.Gameplay.update()
        self.state = State()

        self.play_pause_button = (self.screen.get_rect().width - self.Gameplay.pause_button.get_rect().width - 10, 10)
        self.mouse = pygame.mouse.get_pos()
        self.IsResize = False

        pygame.time.set_timer(pygame.USEREVENT, 10)

        pygame.display.update()

        self.set_state(self.state.curr_state) #Goi ra main menu state

    def set_state(self, state):
        if state == 'Gameplay':
            self.gameplay_loop()
        elif state == 'Menu':
            self.main_menu_loop()

    def main_menu_loop(self):
        running = True
        while running:
            self.screen.blit(self.MainMenu.main_menu_bg, (0, 0))
            self.mouse = pygame.mouse.get_pos()
            self.MainMenu.update()
            pygame.display.update()
            for event in pygame.event.get(): 
                if event.type == QUIT:
                    running = False
                    break
                if event.type == MOUSEBUTTONDOWN:
                    self.MainMenu.check_click(self.mouse)
            if self.MainMenu.IsQuit == True:
                running = False
            if State.curr_state != 'Menu':
                self.set_state(State.curr_state)
                return 
        pygame.quit()
            

    #def draw_main_menu_ui(self):


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

    def gameplay_loop(self):
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
                    self.Gameplay.check_click(self.play_pause_button, self.mouse)
                if event.type == pygame.USEREVENT:
                    self.Gameplay.time += 0.01
                
            self.draw_gameplay_ui()
            self.Gameplay.archer.operation(self.screen)
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    main()