import pygame
from pygame.locals import *
from object_manager import * 
from screen import *

class button():
    def __init__(self, character_name, image_filename, gameplay):
        self.gameplay = gameplay
        self.character_type =  character_name
        self.button_image_original = pygame.image.load(image_filename)
        self.button_image = self.button_image_original.copy()

    def load_image(self):
        self.button_image = self.button_image_original.copy()
        self.button_image = pygame.transform.smoothscale(self.button_image, (screen.screen.get_rect().width / 16, screen.screen.get_rect().height / 16))

    def draw_button(self, pos):
        screen.screen.blit(self.button_image, pos)

    def spawn(self):
        spawn(self.character_type, 1, 0, self.gameplay)



class gameplay_ui():
    def __init__(self, gameplay):
        self.gameplay = gameplay
        self.character_spawn_buttons = []
        self.button_border_original = pygame.image.load('GameplayAssets\\spawn_button.png')
        self.add_button()
        self.load_image()
        self.draw_button()
    
    def load_image(self):
        for x in self.character_spawn_buttons:
            x.load_image()
        self.button_border = self.button_border_original.copy()
        self.button_border = pygame.transform.smoothscale(self.button_border, (screen.screen.get_rect().width / 20, screen.screen.get_rect().width / 20))
        self.button_rect = []

    def add_button(self):
        self.character_spawn_buttons.append(button(sword_man, 'GameplayAssets\\sword_man1(2).png', self.gameplay))
        self.character_spawn_buttons.append(button(archer, 'GameplayAssets\\archer1(2).png', self.gameplay))
        self.character_spawn_buttons.append(button(tanker, 'GameplayAssets\\tanker1(3).png', self.gameplay))
        self.character_spawn_buttons.append(button(wizard, 'GameplayAssets\\wizard(2).png', self.gameplay))

    def draw_button(self):
        prev_pos_width = screen.screen.get_rect().width / 7
        for i in range(0, len(self.character_spawn_buttons)):
            self.button_rect.append(self.button_border.get_rect())
            self.button_rect[i].left = prev_pos_width
            self.button_rect[i].top = screen.screen.get_rect().height / 300
            screen.screen.blit(self.button_border, (self.button_rect[i].left, self.button_rect[i].top))
            # button_center = (prev_pos_width + self.button_border.get_rect().width / 2.0, screen.screen.get_rect().height / 300 + self.button_border.get_rect().height / 2.0)
            character_rect = self.character_spawn_buttons[i].button_image.get_rect()
            character_rect.center = self.button_rect[i].center
            self.character_spawn_buttons[i].draw_button((character_rect.left, character_rect.top))
            prev_pos_width = prev_pos_width + self.button_border.get_rect().width + screen.screen.get_rect().width / 250

    def check_click(self, mouse):
        for i in range(0, len(self.character_spawn_buttons)):
            if self.button_rect[i].left <= mouse[0] <= self.button_rect[i].right and self.button_rect[i].top <= mouse[1] <= self.button_rect[i].bottom:
                self.character_spawn_buttons[i].spawn()


    def update(self):
        self.draw_button()