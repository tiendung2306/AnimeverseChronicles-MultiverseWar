import pygame
import pygame_menu
from pygame.locals import *
from color import *
from states import *
from screen import *

class settings():
    def __init__(self):
        self.buttons = ['Video setting', 'Sound setting', 'Keyboard setting', 'Back']
        self.settings_bg_original = pygame.image.load('GameplayAssets\\mainmenubg.png')
        self.buttons_color = Navy
        self.load_all_image()
        self.load_all_text()
        self.IsResize = False
        self.IsFullScreen = True
        self.resolution_lists = [('640 x 480', 0), ('800 x 600', 1), ('1024 x 768', 2), ('1920 x 1200', 3), ('1680 x 1050', 4), ('1440 x 900', 5), 
                                ('1280 x 800', 6), ('2560 x 1440', 7), ('1920 x 1080', 8), ('1366 x 768', 9), ('1280 x 720', 10)]
        self.resolution_tmp_lists = [(640, 480), (800, 600), (1024, 768), (1920, 1200), (1680, 1050), (1440, 900), 
                                (1280, 800), (2560, 1440), (1920, 1080), (1366, 768), (1280, 720)]

    def load_all_text(self):
        self.buttons_font = pygame.font.Font('Fonts\\BigSpace-rPKx.ttf', 64)

        self.video_setting = self.buttons_font.render(self.buttons[0], True, self.buttons_color)
        self.video_setting_rect = self.video_setting.get_rect()
        self.video_setting_rect.center = (screen.screen.get_rect().width / 3.0, screen.screen.get_rect().height / 5.0 * 3.0)

        self.sound_setting = self.buttons_font.render(self.buttons[1], True, self.buttons_color)
        self.sound_setting_rect = self.sound_setting.get_rect()
        self.sound_setting_rect.center = (screen.screen.get_rect().width / 3.0 * 2.0, screen.screen.get_rect().height / 5.0 * 3.0)

        self.keyboard_setting = self.buttons_font.render(self.buttons[2], True, self.buttons_color)
        self.keyboard_setting_rect = self.keyboard_setting.get_rect()
        self.keyboard_setting_rect.center = (screen.screen.get_rect().width / 3.0, screen.screen.get_rect().height / 5.0 * 4.0)

        self.back_button = self.buttons_font.render(self.buttons[3], True, self.buttons_color)
        self.back_button_rect = self.back_button.get_rect()
        self.back_button_rect.center = (screen.screen.get_rect().width / 3.0 * 2.0, screen.screen.get_rect().height / 5.0 * 4.0)

    def load_all_image(self):
        self.settings_bg = self.settings_bg_original.copy()

        self.settings_bg = pygame.transform.smoothscale(self.settings_bg, (screen.screen.get_rect().width, screen.screen.get_rect().height))

    def set_resolution(self, selected_value, index, **kwargs):
        value_tuple, tmp = selected_value
        curr_resolution = (screen.screen.get_rect().width, screen.screen.get_rect().height)
        if curr_resolution != self.resolution_tmp_lists[index]:
            # print(curr_resolution, '  ', self.resolution_tmp_lists[index])
            if self.IsFullScreen == True:
                screen.screen = pygame.display.set_mode(self.resolution_tmp_lists[index])
            else:
                screen.screen = pygame.display.set_mode(self.resolution_tmp_lists[index])
            self.IsResize = True

    def set_display_mode(self, selected_value, index, *kwargs):
        value_tuple, tmp = selected_value
        curr_resolution = (screen.screen.get_rect().width, screen.screen.get_rect().height)
        if self.IsFullScreen == index:
            if self.IsFullScreen == True:
                # screen.screen = pygame.display.set_mode(curr_resolution)
                self.IsFullScreen = False
                pygame.display.toggle_fullscreen()
            else:
                # screen.screen = pygame.display.set_mode(curr_resolution, pygame.FULLSCREEN)
                self.IsFullScreen = True
                pygame.display.toggle_fullscreen()

    def setting_pannel_init(self):
        self.mytheme = pygame_menu.Theme(background_color=(0, 0, 0, 0), # transparent background
                title_background_color=((0, 0, 0, 0)),
                title_font_shadow=True,
                widget_padding=25,
                )
        self.menu = pygame_menu.Menu('', screen.screen.get_rect().width / 12.0 * 11.0, screen.screen.get_rect().height / 12.0 * 11.0, theme=self.mytheme)
        self.menu.add.selector('Display Mode: ', [('Fullscreen', 0), ('Windowed', 1)], default=1-self.IsFullScreen, onreturn=self.set_display_mode)
        curr_resolution = (screen.screen.get_rect().width, screen.screen.get_rect().height)
        self.menu.add.selector('Resolution: ', self.resolution_lists, default=self.resolution_tmp_lists.index(curr_resolution), onreturn=self.set_resolution)

    def screen_resize(self):
        self.load_all_image()
        self.load_all_text()

        self.setting_pannel_init()

    def update(self):
        screen.screen.blit(self.video_setting, self.video_setting_rect)
        screen.screen.blit(self.sound_setting, self.sound_setting_rect)
        screen.screen.blit(self.keyboard_setting, self.keyboard_setting_rect)
        screen.screen.blit(self.back_button, self.back_button_rect)

    def check_click(self, mouse):
        if self.back_button_rect.left <= mouse[0] <= self.back_button_rect.right and self.back_button_rect.top <= mouse[1] <= self.back_button_rect.bottom:
            return 'Back'
        return 'None'
    