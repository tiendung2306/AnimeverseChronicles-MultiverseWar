import pygame
from pygame.locals import *
from color import *
from screen import *

class gameover_panel():
    def __init__(self, gameplay):
        self.gameplay = gameplay

        self.flag = True
        self.status_color = Yellow
        self.status_text = 'DRAW!!!'

        self.buttons_color = White
        self.button_text = 'Back to menu'

        self.load_all_text()

    def load_all_text(self):
        self.status_font = pygame.font.Font('Fonts\\AznKnucklesTrial-z85pa.otf', 148)
        self.status = self.status_font.render(self.status_text, True, self.status_color)
        self.status_rect = self.status.get_rect()
        self.status_rect.center = (screen.screen.get_rect().width / 2.0, screen.screen.get_rect().height / 6.0 * 2.5)

        self.button_font = pygame.font.Font('Fonts\\BigSpace-rPKx.ttf', 64)
        self.back_to_menu_button = self.button_font.render(self.button_text, True, self.buttons_color)
        self.back_to_menu_button_rect = self.back_to_menu_button.get_rect()
        self.back_to_menu_button_rect.center = (screen.screen.get_rect().width / 2.0, screen.screen.get_rect().height / 6.0 * 4.0)

    def screen_resize(self):
        self.load_all_text()

    def update(self):
        if self.flag == True:
            self.flag = False
            if self.gameplay.Gameover_status == 1:
                self.status_text = 'PLAYER 2 WIN!!!'
            elif self.gameplay.Gameover_status == 2:
                self.status_text = 'PLAYER 1 WIN!!!'
            self.load_all_text()
        screen.screen.blit(self.status, self.status_rect)
        screen.screen.blit(self.back_to_menu_button, self.back_to_menu_button_rect)