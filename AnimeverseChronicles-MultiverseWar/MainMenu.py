import pygame
from pygame.locals import *
from color import *

class mainmenu():
    def __init__(self):
        self.buttons = ['Play', 'Tutorial',  'Setting', 'Quit']
        self.screen = pygame.display.get_surface()
        self.load_all_image()

        self.menu_font = pygame.font.Font('Fonts\\BigSpace-rPKx.ttf', 64)

        self.play_button = self.menu_font.render('Play', True, Navy)
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.center = (self.screen.get_rect().width / 3.0, self.screen.get_rect().height / 5.0 * 3.0)

        self.tutorial_button = self.menu_font.render('Tutorial', True, Navy)
        self.tutorial_button_rect = self.tutorial_button.get_rect()
        self.tutorial_button_rect.center = (self.screen.get_rect().width / 3.0 * 2.0, self.screen.get_rect().height / 5.0 * 3.0)

        self.setting_button = self.menu_font.render('Settings', True, Navy)
        self.setting_button_rect = self.setting_button.get_rect()
        self.setting_button_rect.center = (self.screen.get_rect().width / 3.0, self.screen.get_rect().height / 5.0 * 4.0)

        self.quit_button = self.menu_font.render('Quit', True, Navy)
        self.quit_button_rect = self.quit_button.get_rect()
        self.quit_button_rect.center = (self.screen.get_rect().width / 3.0 * 2.0, self.screen.get_rect().height / 5.0 * 4.0)

    def load_all_image(self):
        self.main_menu_bg = pygame.image.load('GameplayAssets\\mainmenubg.png')

        self.main_menu_bg = pygame.transform.smoothscale(self.main_menu_bg, (self.screen.get_rect().width, self.screen.get_rect().height))

    def update(self):
        self.screen.blit(self.play_button, self.play_button_rect)
        self.screen.blit(self.tutorial_button, self.tutorial_button_rect)
        self.screen.blit(self.setting_button, self.setting_button_rect)
        self.screen.blit(self.quit_button, self.quit_button_rect)