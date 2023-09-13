import pygame
from pygame.locals import *
from color import *
from screen import *

class pause_pannel():
    def __init__(self):
        self.Screen = screen()
        self.buttons = ['Continue', 'Settings', 'Back To Menu']
        self.buttons_color = White
        self.load_all_text()

    def load_all_text(self):
        self.menu_button_font = pygame.font.Font('Fonts\\BigSpace-rPKx.ttf', 64)
        self.continue_button = self.menu_button_font.render(self.buttons[0], True, self.buttons_color)
        self.continue_button_rect = self.continue_button.get_rect()
        self.continue_button_rect.center = (self.Screen.screen.get_rect().width / 2.0, self.Screen.screen.get_rect().height / 6.0 * 2.0)

        self.Settings_button = self.menu_button_font.render(self.buttons[1], True, self.buttons_color)
        self.Settings_button_rect = self.Settings_button.get_rect()
        self.Settings_button_rect.center = (self.Screen.screen.get_rect().width / 2.0, self.Screen.screen.get_rect().height / 6.0 * 3.0)

        self.Leave_Game_button = self.menu_button_font.render(self.buttons[2], True, self.buttons_color)
        self.Leave_Game_button_rect = self.Leave_Game_button.get_rect()
        self.Leave_Game_button_rect.center = (self.Screen.screen.get_rect().width / 2.0, self.Screen.screen.get_rect().height / 6.0 * 4.0)

    def screen_resize(self):
        self.load_all_text()


    def update(self):
        self.Screen.screen.blit(self.continue_button, self.continue_button_rect)
        self.Screen.screen.blit(self.Settings_button, self.Settings_button_rect)
        self.Screen.screen.blit(self.Leave_Game_button, self.Leave_Game_button_rect)

    def check_click(self, mouse):
        if self.continue_button_rect.left <= mouse[0] <= self.continue_button_rect.right and self.continue_button_rect.top <= mouse[1] <= self.continue_button_rect.bottom:
            return self.buttons[0]
        if self.Settings_button_rect.left <= mouse[0] <= self.Settings_button_rect.right and self.Settings_button_rect.top <= mouse[1] <= self.Settings_button_rect.bottom:
            return self.buttons[1]
        if self.Leave_Game_button_rect.left <= mouse[0] <= self.Leave_Game_button_rect.right and self.Leave_Game_button_rect.top <= mouse[1] <= self.Leave_Game_button_rect.bottom:
            return self.buttons[2]
