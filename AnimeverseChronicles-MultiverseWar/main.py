import pygame, os
from pygame.locals import *
from Gameplay import *
from states import *
from MainMenu import *
from settings import *
from screen import *
from tutorials import *

from collide_checker import *
class main():
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.set_caption('AnimeverseChronicles-MultiverseWar')

        self.cur_gameplay_mode = -1

        self.Tutorial = tutorials()
        self.MainMenu = mainmenu()
        self.Gameplay1 = gameplay(1)
        self.Gameplay1.update()
        self.Gameplay2 = gameplay(2)
        self.Gameplay2.update()
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
        elif state == 'Play mode':
            self.choose_play_mode_loop()
        elif state == 'Tutorial':
            self.tutorial_loop()
    
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
        elif state == 'Play mode':
            State.curr_state = State.states[0]
            self.main_menu_loop()
        elif state == 'Tutorial':
            self.tutorial_loop()

    def screen_resize(self):
        if self.IsResize == True or self.Settings.IsResize == True:
                self.IsResize = False
                self.Settings.IsResize = False
                self.MainMenu.screen_resize()
                self.Settings.screen_resize()
                self.Gameplay1.screen_resize()
                self.Gameplay2.screen_resize()
                self.Tutorial.screen_resize()
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

    def tutorial_loop(self):
        running = True
        while running:
            self.screen_resize()
            screen.screen.blit(self.MainMenu.main_menu_bg, (0, 0))
            mouse = pygame.mouse.get_pos()
            self.Tutorial.update()
            pygame.display.update()
            for event in pygame.event.get(): 
                if event.type == QUIT:
                    running = False
                    break
                if event.type == VIDEORESIZE:
                    self.IsResize = True
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.Tutorial.check_click(mouse)
            if State.curr_state != 'Tutorial':
                self.set_state(State.curr_state)
                return 
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
                    if event.button == 1:
                        self.MainMenu.check_click(self.mouse)
            if self.MainMenu.IsQuit == True:
                running = False
            if State.curr_state != 'Menu':
                self.set_state(State.curr_state)
                return 
        pygame.quit()
            

    def choose_play_mode_loop(self):
        running = True
        self.MainMenu.play_mode_state = 0
        while running:
            self.screen_resize()
            screen.screen.blit(self.MainMenu.main_menu_bg, (0, 0))
            self.mouse = pygame.mouse.get_pos()
            self.MainMenu.play_mode_update()
            pygame.display.update()
            gameplay_mode = -1
            for event in pygame.event.get(): 
                if event.type == QUIT:
                    running = False
                    break
                if event.type == VIDEORESIZE:
                    self.IsResize = True
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        gameplay_mode = self.MainMenu.play_mode_check_click(self.mouse)
            if State.curr_state != 'Play mode':
                if State.curr_state == State.states[1]:
                    if gameplay_mode == -1:
                        print('What the f*ck, how can it be -1. Panikkk!!!!!!!!')
                    if gameplay_mode == 3:
                        gameplay_mode = 1
                        self.Gameplay1 = gameplay(1)
                        self.Gameplay1.update()
                    if gameplay_mode == 4:
                        gameplay_mode = 2
                        self.Gameplay2 = gameplay(2)
                        self.Gameplay2.update()
                    
                    self.cur_gameplay_mode = gameplay_mode
                self.set_state(State.curr_state)
                return 
        pygame.quit()

    def gameplay_loop(self):
        if self.cur_gameplay_mode == 1:
            thisGameplay = self.Gameplay1
        else:
            thisGameplay = self.Gameplay2
        running = True
        thisGameplay.enter_gameplay()
        self.cur_gameplay_mode = thisGameplay.play_mode
        while running:
            self.screen_resize()
            thisGameplay.update()
            self.mouse = pygame.mouse.get_pos()
            if thisGameplay.play_mode == 2:
                tmp = Rect(0, 0, thisGameplay.board_1.get_rect().width // 6, thisGameplay.board_1.get_rect().width // 6)
                tmp.center = (screen.screen.get_rect().width / 2.0, 10)
                tmp.top = 10
                self.play_pause_button = (tmp.left, tmp.top)
            else:
                thisGameplay.play_pause_button = (screen.screen.get_rect().width - screen.screen.get_rect().width // 32, 10)
            Button = 'None'

            for event in pygame.event.get(): 
                if event.type == QUIT:
                    running = False
                    break
                if event.type == VIDEORESIZE:
                    self.IsResize = True
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        Button = thisGameplay.check_click(thisGameplay.play_pause_button, self.mouse)
                if event.type == pygame.KEYDOWN:
                    thisGameplay.check_press(event)
                if event.type == pygame.USEREVENT:
                    thisGameplay.time += 0.0104
                
            thisGameplay.draw_gameplay_ui()
            
            thisGameplay.object_operation()

            thisGameplay.pre_curr_time = thisGameplay.curr_time
            
            if thisGameplay.isGameover == True:
                thisGameplay.draw_gameover_panel()
            elif thisGameplay.isPlay == False:
                thisGameplay.draw_pause_pannel()
            
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