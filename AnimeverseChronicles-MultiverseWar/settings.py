import pygame
import pygame_menu
from pygame.locals import *
from color import *
from states import *
from screen import *

class settings():
    def __init__(self):
        self.buttons = ['Apply', 'Back']
        self.settings_bg_original = pygame.image.load('GameplayAssets\\mainmenubg.png')
        self.buttons_color = Navy
        self.load_all_image()
        self.load_all_text()
        self.IsResize = False
        self.IsFullScreen = True
        self.all_resolution_lists = [('640 x 480', 0), ('800 x 600', 1), ('1024 x 768', 2), ('1920 x 1200', 3), ('1680 x 1050', 4), ('1440 x 900', 5), 
                                ('1280 x 800', 6), ('2560 x 1440', 7), ('1920 x 1080', 8), ('1366 x 768', 9), ('1280 x 720', 10), ('3840 x 2160', 11)]
        self.all_resolution_tmp_lists = [(640, 480), (800, 600), (1024, 768), (1920, 1200), (1680, 1050), (1440, 900), 
                                (1280, 800), (2560, 1440), (1920, 1080), (1366, 768), (1280, 720), (3840, 2160)]
        self.resolution_lists = []
        self.resolution_tmp_lists = []
        self.process_resolution()
        self.IsBack = False

    def process_resolution(self):
        flag = False
        for i in range(0, len(self.all_resolution_tmp_lists)):
            if self.all_resolution_tmp_lists[i][0] <= screen.curr_monitor_resolution[0] and self.all_resolution_tmp_lists[i][1] <= screen.curr_monitor_resolution[1]:
                self.resolution_lists.append(self.all_resolution_lists[i])
                self.resolution_tmp_lists.append(self.all_resolution_tmp_lists[i])
            if self.all_resolution_tmp_lists[i][0] == screen.curr_monitor_resolution[0] and self.all_resolution_tmp_lists[i][1] == screen.curr_monitor_resolution[1]:
                flag = True
        if flag == False:
            self.resolution_lists.append((str(screen.curr_monitor_resolution[0]) + ' x ' + str(screen.curr_monitor_resolution[1]), 2306))
            self.resolution_tmp_lists.append(screen.curr_monitor_resolution)

    def load_all_text(self):
        self.buttons_font = pygame.font.Font('Fonts\\BigSpace-rPKx.ttf', 64)

        # self.apply_button = self.buttons_font.render(self.buttons[0], True, self.buttons_color)
        # self.apply_button_rect = self.apply_button.get_rect()
        # self.apply_button_rect.center = (screen.screen.get_rect().width / 2.0, screen.screen.get_rect().height / 15.0 * 10.5)

        # self.back_button = self.buttons_font.render(self.buttons[1], True, self.buttons_color)
        # self.back_button_rect = self.back_button.get_rect()
        # self.back_button_rect.center = (screen.screen.get_rect().width / 2.0, screen.screen.get_rect().height / 15.0 * 12.0)

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
                pygame.display.toggle_fullscreen()
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

    def hit_back_button(self):
        self.IsBack = True

    def setting_pannel_init(self):
        self.mytheme = pygame_menu.Theme(background_color=(0, 0, 0, 0), # transparent background
                title_background_color=((0, 0, 0, 0)),
                title_font_shadow=True,
                widget_padding=25,
                )
        self.menu = pygame_menu.Menu('', screen.screen.get_rect().width / 12.0 * 11.0, screen.screen.get_rect().height / 12.0 * 11.0, theme=self.mytheme)
        self.menu.add.dropselect('Display Mode: ', [('Fullscreen', 0), ('Windowed', 1)], default=1-self.IsFullScreen, onchange=self.set_display_mode, font_size=30, selection_option_font_size=30, selection_color=pygame.color.Color(0,0,128))
        curr_resolution = (screen.screen.get_rect().width, screen.screen.get_rect().height)
        self.menu.add.dropselect('Resolution: ', self.resolution_lists, default=self.resolution_tmp_lists.index(curr_resolution), onchange=self.set_resolution, font_size=30, selection_option_font_size=30, selection_color=pygame.color.Color(0,0,128))
        self.menu.add.button('Back', self.hit_back_button)

    def screen_resize(self):
        self.load_all_image()
        self.load_all_text()

        self.setting_pannel_init()

    # def update(self):
        # screen.screen.blit(self.apply_button, self.apply_button_rect)
        # screen.screen.blit(self.back_button, self.back_button_rect)