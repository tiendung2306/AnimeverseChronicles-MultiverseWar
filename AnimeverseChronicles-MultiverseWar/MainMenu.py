import pygame
from pygame.locals import *
from color import *
from states import *
from screen import *

class mainmenu():
    def __init__(self):
        self.buttons = ['Play', 'Tutorial',  'Settings', 'Quit']
        self.play_mode_buttons = ['1 Player', '2 Players', 'Back', 'New Game', 'Continue']
        self.Screen = screen()
        self.buttons_color = White
        self.title_color = Blue
        self.play_mode_state = 0

        self.main_menu_bg_original = pygame.image.load('GameplayAssets\\mainmenubg.jpg')

        self.load_all_image()

        self.load_all_text()

        self.IsQuit = False

    def load_all_text(self):
        self.menu_button_font = pygame.font.Font('Fonts\\BigSpace-rPKx.ttf', 64)
        self.menu_title_font1 = pygame.font.Font('Fonts\\TargetFonts\\TarrgetExpandedItalic-3EjZ.otf', 54)
        self.menu_title_font2 = pygame.font.Font('Fonts\\TargetFonts\\TarrgetExpandedItalic-3EjZ.otf', 44)

        self.play_button = self.menu_button_font.render(self.buttons[0], True, self.buttons_color)
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.center = (self.Screen.screen.get_rect().width / 3.0, self.Screen.screen.get_rect().height / 5.0 * 3.0)

        self.tutorial_button = self.menu_button_font.render(self.buttons[1], True, self.buttons_color)
        self.tutorial_button_rect = self.tutorial_button.get_rect()
        self.tutorial_button_rect.center = (self.Screen.screen.get_rect().width / 3.0 * 2.0, self.Screen.screen.get_rect().height / 5.0 * 3.0)

        self.setting_button = self.menu_button_font.render(self.buttons[2], True, self.buttons_color)
        self.setting_button_rect = self.setting_button.get_rect()
        self.setting_button_rect.center = (self.Screen.screen.get_rect().width / 3.0, self.Screen.screen.get_rect().height / 5.0 * 4.0)

        self.quit_button = self.menu_button_font.render(self.buttons[3], True, self.buttons_color)
        self.quit_button_rect = self.quit_button.get_rect()
        self.quit_button_rect.center = (self.Screen.screen.get_rect().width / 3.0 * 2.0, self.Screen.screen.get_rect().height / 5.0 * 4.0)

        self.menu_title1 = self.menu_title_font1.render('Animeverse Chronicles', True, self.title_color)
        self.menu_title2 = self.menu_title_font2.render('Multiverse War', True, self.title_color)
        self.menu_title_rect1 = self.menu_title1.get_rect()
        self.menu_title_rect1.center = (self.Screen.screen.get_rect().width / 2.0, self.Screen.screen.get_rect().height / 32.0 * 6.0)
        self.menu_title_rect2 = self.menu_title2.get_rect()
        self.menu_title_rect2.center = (self.Screen.screen.get_rect().width / 2.0, self.Screen.screen.get_rect().height / 32.0 * 9.0)

        self.one_player_button = self.menu_button_font.render(self.play_mode_buttons[0], True, self.buttons_color)
        self.one_player_button_rect = self.one_player_button.get_rect()
        self.one_player_button_rect.center = (self.Screen.screen.get_rect().width / 3.5, self.Screen.screen.get_rect().height / 6.0 * 3.0)

        self.two_players_button = self.menu_button_font.render(self.play_mode_buttons[1], True, self.buttons_color)
        self.two_players_button_rect = self.two_players_button.get_rect()
        self.two_players_button_rect.center = (self.Screen.screen.get_rect().width / 3.5, self.Screen.screen.get_rect().height / 6.0 * 4.0)

        self.back_button = self.menu_button_font.render(self.play_mode_buttons[2], True, self.buttons_color)
        self.back_button_rect = self.back_button.get_rect()
        self.back_button_rect.center = (self.Screen.screen.get_rect().width / 3.5, self.Screen.screen.get_rect().height / 6.0 * 5.0)

        self.New_Game_button = self.menu_button_font.render(self.play_mode_buttons[3], True, self.buttons_color)
        self.New_Game_button_rect = self.New_Game_button.get_rect()
        # self.New_Game_button_rect.center = (self.Screen.screen.get_rect().width / 3.5, self.Screen.screen.get_rect().height / 6.0 * 3.0)

        self.Continue_button = self.menu_button_font.render(self.play_mode_buttons[4], True, self.buttons_color)
        self.Continue_button_rect = self.Continue_button.get_rect()
        # self.Continue_button_rect.center = (self.Screen.screen.get_rect().width / 3.5, self.Screen.screen.get_rect().height / 6.0 * 3.0)


    def load_all_image(self):
        self.main_menu_bg = self.main_menu_bg_original.copy()

        self.main_menu_bg = pygame.transform.smoothscale(self.main_menu_bg, (self.Screen.screen.get_rect().width, self.Screen.screen.get_rect().height))

    def screen_resize(self):
        self.load_all_image()
        self.load_all_text()

    def update(self):
        self.Screen.screen.blit(self.play_button, self.play_button_rect)
        self.Screen.screen.blit(self.tutorial_button, self.tutorial_button_rect)
        self.Screen.screen.blit(self.setting_button, self.setting_button_rect)
        self.Screen.screen.blit(self.quit_button, self.quit_button_rect)

        self.Screen.screen.blit(self.menu_title1, self.menu_title_rect1)
        self.Screen.screen.blit(self.menu_title2, self.menu_title_rect2)

    def check_click(self, mouse):
        if self.play_button_rect.left <= mouse[0] <= self.play_button_rect.right and self.play_button_rect.top <= mouse[1] <= self.play_button_rect.bottom:
            State.curr_state = State.states[5]
        if self.quit_button_rect.left <= mouse[0] <= self.quit_button_rect.right and self.quit_button_rect.top <= mouse[1] <= self.quit_button_rect.bottom:
            self.IsQuit = True
        if self.setting_button_rect.left <= mouse[0] <= self.setting_button_rect.right and self.setting_button_rect.top <= mouse[1] <= self.setting_button_rect.bottom:
            State.curr_state = State.states[3]
        if self.tutorial_button_rect.left <= mouse[0] <= self.tutorial_button_rect.right and self.tutorial_button_rect.top <= mouse[1] <= self.tutorial_button_rect.bottom:
            State.curr_state = State.states[4]

    def play_mode_update(self):
        self.Screen.screen.blit(self.one_player_button, self.one_player_button_rect)
        self.Screen.screen.blit(self.two_players_button, self.two_players_button_rect)
        self.Screen.screen.blit(self.back_button, self.back_button_rect)

        if self.play_mode_state != 0:
            self.Screen.screen.blit(self.New_Game_button, self.New_Game_button_rect)
            self.Screen.screen.blit(self.Continue_button, self.Continue_button_rect)

        self.Screen.screen.blit(self.menu_title1, self.menu_title_rect1)
        self.Screen.screen.blit(self.menu_title2, self.menu_title_rect2)

    def play_mode_check_click(self, mouse):
        if self.one_player_button_rect.left <= mouse[0] <= self.one_player_button_rect.right and self.one_player_button_rect.top <= mouse[1] <= self.one_player_button_rect.bottom:
            self.play_mode_state = 1
            self.New_Game_button_rect.center = (self.one_player_button_rect.right + self.Screen.screen.get_rect().width / 9.0, self.Screen.screen.get_rect().height / 6.0 * 3.0)
            self.Continue_button_rect.center = (self.New_Game_button_rect.right + self.Screen.screen.get_rect().width / 9.0, self.Screen.screen.get_rect().height / 6.0 * 3.0)
            # return 1
        if self.two_players_button_rect.left <= mouse[0] <= self.two_players_button_rect.right and self.two_players_button_rect.top <= mouse[1] <= self.two_players_button_rect.bottom:
            self.play_mode_state = 2
            self.New_Game_button_rect.center = (self.two_players_button_rect.right + self.Screen.screen.get_rect().width / 9.0, self.Screen.screen.get_rect().height / 6.0 * 4.0)
            self.Continue_button_rect.center = (self.New_Game_button_rect.right + self.Screen.screen.get_rect().width / 9.0, self.Screen.screen.get_rect().height / 6.0 * 4.0)
            # return 2
        if self.play_mode_state == 1:
            if self.New_Game_button_rect.left <= mouse[0] <= self.New_Game_button_rect.right and self.New_Game_button_rect.top <= mouse[1] <= self.New_Game_button_rect.bottom:
                State.curr_state = State.states[1]
                return 3
            if self.Continue_button_rect.left <= mouse[0] <= self.Continue_button_rect.right and self.Continue_button_rect.top <= mouse[1] <= self.Continue_button_rect.bottom:
                State.curr_state = State.states[1]
                return 1
        if self.play_mode_state == 2:
            if self.New_Game_button_rect.left <= mouse[0] <= self.New_Game_button_rect.right and self.New_Game_button_rect.top <= mouse[1] <= self.New_Game_button_rect.bottom:
                State.curr_state = State.states[1]
                return 4
            if self.Continue_button_rect.left <= mouse[0] <= self.Continue_button_rect.right and self.Continue_button_rect.top <= mouse[1] <= self.Continue_button_rect.bottom:
                State.curr_state = State.states[1]
                return 2
        if self.back_button_rect.left <= mouse[0] <= self.back_button_rect.right and self.back_button_rect.top <= mouse[1] <= self.back_button_rect.bottom:
            State.curr_state = State.states[0]
            return -1