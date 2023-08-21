import pygame
from pygame.locals import *
from color import *
from states import *

class mainmenu():
    def __init__(self):
        self.buttons = ['Play', 'Tutorial',  'Settings', 'Quit']
        self.screen = pygame.display.get_surface()
        self.buttons_color = Navy
        self.title_color = Dark_Yellow

        self.main_menu_bg_original = pygame.image.load('GameplayAssets\\mainmenubg.png')

        self.load_all_image()

        self.load_all_text()

        self.IsQuit = False

    def load_all_text(self):
        self.menu_button_font = pygame.font.Font('Fonts\\BigSpace-rPKx.ttf', 64)
        self.menu_title_font1 = pygame.font.Font('Fonts\\TargetFonts\\TarrgetExpandedItalic-3EjZ.otf', 54)
        self.menu_title_font2 = pygame.font.Font('Fonts\\TargetFonts\\TarrgetExpandedItalic-3EjZ.otf', 44)

        self.play_button = self.menu_button_font.render(self.buttons[0], True, self.buttons_color)
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.center = (self.screen.get_rect().width / 3.0, self.screen.get_rect().height / 5.0 * 3.0)

        self.tutorial_button = self.menu_button_font.render(self.buttons[1], True, self.buttons_color)
        self.tutorial_button_rect = self.tutorial_button.get_rect()
        self.tutorial_button_rect.center = (self.screen.get_rect().width / 3.0 * 2.0, self.screen.get_rect().height / 5.0 * 3.0)

        self.setting_button = self.menu_button_font.render(self.buttons[2], True, self.buttons_color)
        self.setting_button_rect = self.setting_button.get_rect()
        self.setting_button_rect.center = (self.screen.get_rect().width / 3.0, self.screen.get_rect().height / 5.0 * 4.0)

        self.quit_button = self.menu_button_font.render(self.buttons[3], True, self.buttons_color)
        self.quit_button_rect = self.quit_button.get_rect()
        self.quit_button_rect.center = (self.screen.get_rect().width / 3.0 * 2.0, self.screen.get_rect().height / 5.0 * 4.0)

        self.menu_title1 = self.menu_title_font1.render('Animeverse Chronicles', True, self.title_color)
        self.menu_title2 = self.menu_title_font2.render('Multiverse War', True, self.title_color)
        self.menu_title_rect1 = self.menu_title1.get_rect()
        self.menu_title_rect1.center = (self.screen.get_rect().width / 2.0, self.screen.get_rect().height / 32.0 * 6.0)
        self.menu_title_rect2 = self.menu_title2.get_rect()
        self.menu_title_rect2.center = (self.screen.get_rect().width / 2.0, self.screen.get_rect().height / 32.0 * 9.0)


    def load_all_image(self):
        self.main_menu_bg = self.main_menu_bg_original.copy()

        self.main_menu_bg = pygame.transform.smoothscale(self.main_menu_bg, (self.screen.get_rect().width, self.screen.get_rect().height))

    def screen_resize(self):
        self.screen = pygame.display.get_surface()
        self.load_all_image()
        self.load_all_text()

    def update(self):
        self.screen.blit(self.play_button, self.play_button_rect)
        self.screen.blit(self.tutorial_button, self.tutorial_button_rect)
        self.screen.blit(self.setting_button, self.setting_button_rect)
        self.screen.blit(self.quit_button, self.quit_button_rect)

        self.screen.blit(self.menu_title1, self.menu_title_rect1)
        self.screen.blit(self.menu_title2, self.menu_title_rect2)

    def check_click(self, mouse):
        if self.play_button_rect.left <= mouse[0] <= self.play_button_rect.right and self.play_button_rect.top <= mouse[1] <= self.play_button_rect.bottom:
            State.curr_state = State.states[1]
        if self.quit_button_rect.left <= mouse[0] <= self.quit_button_rect.right and self.quit_button_rect.top <= mouse[1] <= self.quit_button_rect.bottom:
            self.IsQuit = True
        if self.setting_button_rect.left <= mouse[0] <= self.setting_button_rect.right and self.setting_button_rect.top <= mouse[1] <= self.setting_button_rect.bottom:
            State.curr_state = State.states[3]
