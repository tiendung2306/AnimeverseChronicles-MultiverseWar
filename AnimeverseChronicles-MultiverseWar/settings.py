import pygame
from pygame.locals import *
from color import *
from states import *

class settings():
    def __init__(self):
        self.buttons = ['Video setting', 'Sound setting', 'Keyboard setting', 'Back']
        self.screen = pygame.display.get_surface()
        self.settings_bg_original = pygame.image.load('GameplayAssets\\mainmenubg.png')
        self.buttons_color = Navy
        self.load_all_image()
        self.load_all_text()

    def load_all_text(self):
        self.buttons_font = pygame.font.Font('Fonts\\BigSpace-rPKx.ttf', 64)

        self.video_setting = self.buttons_font.render(self.buttons[0], True, self.buttons_color)
        self.video_setting_rect = self.video_setting.get_rect()
        self.video_setting_rect.center = (self.screen.get_rect().width / 3.0, self.screen.get_rect().height / 5.0 * 3.0)

        self.sound_setting = self.buttons_font.render(self.buttons[1], True, self.buttons_color)
        self.sound_setting_rect = self.sound_setting.get_rect()
        self.sound_setting_rect.center = (self.screen.get_rect().width / 3.0 * 2.0, self.screen.get_rect().height / 5.0 * 3.0)

        self.keyboard_setting = self.buttons_font.render(self.buttons[2], True, self.buttons_color)
        self.keyboard_setting_rect = self.keyboard_setting.get_rect()
        self.keyboard_setting_rect.center = (self.screen.get_rect().width / 3.0, self.screen.get_rect().height / 5.0 * 4.0)

        self.back_button = self.buttons_font.render(self.buttons[3], True, self.buttons_color)
        self.back_button_rect = self.back_button.get_rect()
        self.back_button_rect.center = (self.screen.get_rect().width / 3.0 * 2.0, self.screen.get_rect().height / 5.0 * 4.0)

    def load_all_image(self):
        self.settings_bg = self.settings_bg_original.copy()

        self.settings_bg = pygame.transform.smoothscale(self.settings_bg, (self.screen.get_rect().width, self.screen.get_rect().height))

    def screen_resize(self):
        self.load_all_image()
        self.load_all_text()

    def update(self):
        self.screen.blit(self.video_setting, self.video_setting_rect)
        self.screen.blit(self.sound_setting, self.sound_setting_rect)
        self.screen.blit(self.keyboard_setting, self.keyboard_setting_rect)
        self.screen.blit(self.back_button, self.back_button_rect)

    def check_click(self, mouse):
        if self.back_button_rect.left <= mouse[0] <= self.back_button_rect.right and self.back_button_rect.top <= mouse[1] <= self.back_button_rect.bottom:
            State.curr_state = State.states[0]