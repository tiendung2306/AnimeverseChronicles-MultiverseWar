import pygame, os
from pygame.locals import *
from Gameplay import *
from states import *
from MainMenu import *
from settings import *
from screen import *

from collide_checker import *
class main():
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.set_caption('AnimeverseChronicles-MultiverseWar')

        self.MainMenu = mainmenu()
        self.Gameplay = gameplay()
        self.Gameplay.update()
        self.Settings = settings()

        self.mouse = pygame.mouse.get_pos()
        self.IsResize = False
        self.IsFullScreen = True

        pygame.time.set_timer(pygame.USEREVENT, 10)

        pygame.display.update()

        self.set_state(State.curr_state) #Goi ra main menu state

    def set_state(self, state):
        State.list_states.append(state)
        State.curr_state = state
        if state == 'Gameplay':
            self.gameplay_loop()
        elif state == 'Menu':
            self.main_menu_loop()
        elif state == 'Settings':
            self.settings_loop()
    
    def back_state(self):
        del State.list_states[-1]
        state = State.list_states[-1]
        State.curr_state = state
        if state == 'Gameplay':
            self.gameplay_loop()
        elif state == 'Menu':
            self.main_menu_loop()
        elif state == 'Settings':
            self.settings_loop()

    def screen_resize(self):
        if self.IsResize == True or self.Settings.IsResize == True:
                self.IsResize = False
                self.Settings.IsResize = False
                self.MainMenu.screen_resize()
                self.Settings.screen_resize()
                self.Gameplay.screen_resize()
    def settings_loop(self):
        self.Settings.setting_pannel_init()
        running = True
        while running:
            self.screen_resize()
            screen.screen.blit(self.Settings.settings_bg, (0, 0))
            self.mouse = pygame.mouse.get_pos()
            # self.Settings.update()
            events = pygame.event.get()
            for event in events: 
                if event.type == QUIT:
                    running = False
                    break
                if event.type == VIDEORESIZE:
                    self.IsResize = True
            if self.Settings.IsBack == True:
                self.Settings.IsBack = False
                self.back_state()
                return 
            if self.Settings.menu.is_enabled():
                self.Settings.menu.update(events)
                self.Settings.menu.draw(screen.screen)
            pygame.display.update()
        pygame.quit()

    def main_menu_loop(self):
        running = True
        while running:
            self.screen_resize()
            screen.screen.blit(self.MainMenu.main_menu_bg, (0, 0))
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
        self.Gameplay.enter_gameplay()
        while running:
            self.screen_resize()
            self.Gameplay.update()
            self.mouse = pygame.mouse.get_pos()
            self.Gameplay.play_pause_button = (screen.screen.get_rect().width - self.Gameplay.pause_button.get_rect().width - 10, 10)
            Button = 'None'

            for event in pygame.event.get(): 
                if event.type == QUIT:
                    running = False
                    break
                if event.type == VIDEORESIZE:
                    self.IsResize = True
                if event.type == MOUSEBUTTONDOWN:
                    Button = self.Gameplay.check_click(self.Gameplay.play_pause_button, self.mouse)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.Gameplay.escape_pressed()
                if event.type == pygame.USEREVENT:
                    self.Gameplay.time += 0.01
                
            self.Gameplay.draw_gameplay_ui()

            self.Gameplay.object_operation()
            if self.Gameplay.isPlay == False:
                self.Gameplay.draw_pause_pannel()
            pygame.display.update()
            if Button == 'Back':
                self.back_state()
                return 
            elif Button == 'Settings':
                self.set_state(State.states[3])
                return

        pygame.quit()

if __name__ == '__main__':
    main()