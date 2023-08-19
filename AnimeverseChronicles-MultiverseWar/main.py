import pygame
from pygame.locals import *
from Gameplay import *
<<<<<<< Updated upstream
from states import *
from MainMenu import *
from settings import *

=======
from collide_checker import *
>>>>>>> Stashed changes
class main():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1400, 900), RESIZABLE)
        pygame.display.set_caption('AnimeverseChronicles-MultiverseWar')

        self.MainMenu = mainmenu()
        self.Gameplay = gameplay()
        self.Gameplay.update()
        self.state = State()
        self.Settings = settings()

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
        elif state == 'Settings':
            self.settings_loop()

    def settings_loop(self):
        running = True
        while running:
            if self.IsResize == True:
                self.IsResize = False
                self.Settings.screen_resize()
            self.screen.blit(self.Settings.settings_bg, (0, 0))
            self.mouse = pygame.mouse.get_pos()
            self.Settings.update()
            pygame.display.update()
            for event in pygame.event.get(): 
                if event.type == QUIT:
                    running = False
                    break
                if event.type == VIDEORESIZE:
                    self.IsResize = True
                if event.type == MOUSEBUTTONDOWN:
                    self.Settings.check_click(self.mouse)
            if State.curr_state != 'Settings':
                self.set_state(State.curr_state)
                return 
        pygame.quit()

    def main_menu_loop(self):
        running = True
        while running:
            if self.IsResize == True:
                self.IsResize = False
                self.MainMenu.screen_resize()
                self.Settings.screen_resize()
            self.screen.blit(self.MainMenu.main_menu_bg, (0, 0))
            self.mouse = pygame.mouse.get_pos()
            self.MainMenu.update()
            pygame.display.update()
            for event in pygame.event.get(): 
                if event.type == QUIT:
                    running = False
                    break
                if event.type == VIDEORESIZE:
                    self.IsResize = True
                if event.type == MOUSEBUTTONDOWN:
                    self.MainMenu.check_click(self.mouse)
            if self.MainMenu.IsQuit == True:
                running = False
            if State.curr_state != 'Menu':
                self.set_state(State.curr_state)
                return 
        pygame.quit()
            

    def gameplay_loop(self):
        running = True
        pygame.time.Clock().tick(Gameplay.FPS)     
    while running:
            if self.IsResize == True:
                self.IsResize = False
                self.Gameplay.screen_resize()
            self.Gameplay.update()
            self.mouse = pygame.mouse.get_pos()
            self.Gameplay.play_pause_button = (self.screen.get_rect().width - self.Gameplay.pause_button.get_rect().width - 10, 10)

            for event in pygame.event.get(): 
                if event.type == QUIT:
                    running = False
                    break
                if event.type == VIDEORESIZE:
                    self.IsResize = True
                if event.type == MOUSEBUTTONDOWN:
                    self.Gameplay.check_click(self.Gameplay.play_pause_button, self.mouse)
                if event.type == pygame.USEREVENT:
                    self.Gameplay.time += 0.01
                
            self.Gameplay.draw_gameplay_ui()
            self.Gameplay.archer.operation(self.screen)
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    main()