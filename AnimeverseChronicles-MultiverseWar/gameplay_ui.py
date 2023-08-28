import pygame
from pygame.locals import *
from object_manager import * 
from screen import *

class button():
    def __init__(self, character_name, image_filename, gameplay):
        self.gameplay = gameplay
        self.character_type =  character_name
        self.button_image_original = pygame.image.load(image_filename)
        self.button_image_1 = self.button_image_original.copy()
        self.button_image_2 = self.button_image_original.copy()
        self.button_image_2 = pygame.transform.flip(self.button_image_2, True, False)

    def load_image(self):
        self.button_image_1 = self.button_image_original.copy()
        self.button_image_2 = self.button_image_original.copy()
        self.button_image_2 = pygame.transform.flip(self.button_image_2, True, False)
        self.button_image_1 = pygame.transform.smoothscale(self.button_image_1, (screen.screen.get_rect().width / 16, screen.screen.get_rect().height / 16))
        self.button_image_2 = pygame.transform.smoothscale(self.button_image_2, (screen.screen.get_rect().width / 16, screen.screen.get_rect().height / 16))

    def draw_button(self, pos, side):
        if side == 1:
            screen.screen.blit(self.button_image_1, pos)
        else:
            screen.screen.blit(self.button_image_2, pos)

    def spawn(self, side):
        if side == 1:
            if self.gameplay.curr_gold_1 >= self.gameplay.character_cost[self.character_type]:
                spawn(self.character_type, side, 0, self.gameplay)
                self.gameplay.gold_outcome_1 += self.gameplay.character_cost[self.character_type]
        else:
            if self.gameplay.curr_gold_2 >= self.gameplay.character_cost[self.character_type]:
                spawn(self.character_type, side, 39, self.gameplay)
                self.gameplay.gold_outcome_2 += self.gameplay.character_cost[self.character_type]



class gameplay_ui():
    def __init__(self, gameplay):
        self.gameplay = gameplay
        self.button_border_original = pygame.image.load('GameplayAssets\\spawn_button.png')
        self.character_spawn_buttons = []
        self.button_border = self.button_border_original.copy()
        self.button_border = pygame.transform.smoothscale(self.button_border, (screen.screen.get_rect().width / 20, screen.screen.get_rect().width / 20))
        self.button_rect_1 = []
        self.button_rect_2 = []

        self.add_button()
        self.load_image()
        self.draw_button()
    
    def load_image(self):
        for x in self.character_spawn_buttons:
            x.load_image()
        self.button_border = self.button_border_original.copy()
        self.button_border = pygame.transform.smoothscale(self.button_border, (screen.screen.get_rect().width / 20, screen.screen.get_rect().width / 20))

    def add_button(self):
        self.character_spawn_buttons.append(button(sword_man, 'GameplayAssets\\sword_man(14).png', self.gameplay))
        self.character_spawn_buttons.append(button(archer, 'GameplayAssets\\archer(14).png', self.gameplay))
        self.character_spawn_buttons.append(button(tanker, 'GameplayAssets\\tanker(31).png', self.gameplay))
        self.character_spawn_buttons.append(button(wizard, 'GameplayAssets\\wizard(13).png', self.gameplay))

        prev_pos_width = screen.screen.get_rect().width / 7
        for i in range(0, len(self.character_spawn_buttons)):
            self.button_rect_1.append(self.button_border.get_rect())
            self.button_rect_1[i].left = prev_pos_width
            self.button_rect_1[i].top = screen.screen.get_rect().height / 300
            prev_pos_width = prev_pos_width + self.button_border.get_rect().width + screen.screen.get_rect().width / 250
        if self.gameplay.play_mode == 2:
            prev_pos_width = screen.screen.get_rect().width / 7.0 * 6.0 - self.button_border.get_rect().width
            for i in range(0, len(self.character_spawn_buttons)):
                self.button_rect_2.append(self.button_border.get_rect())
                self.button_rect_2[i].left = prev_pos_width
                self.button_rect_2[i].top = screen.screen.get_rect().height / 300
                prev_pos_width = prev_pos_width - self.button_border.get_rect().width - screen.screen.get_rect().width / 250

    def draw_button(self):
        prev_pos_width = screen.screen.get_rect().width / 7
        for i in range(0, len(self.character_spawn_buttons)):
            screen.screen.blit(self.button_border, (self.button_rect_1[i].left, self.button_rect_1[i].top))
            character_rect = self.character_spawn_buttons[i].button_image_1.get_rect()
            character_rect.center = self.button_rect_1[i].center
            self.character_spawn_buttons[i].draw_button((character_rect.left, character_rect.top), 1)
            prev_pos_width = prev_pos_width + self.button_border.get_rect().width + screen.screen.get_rect().width / 250
            
        if self.gameplay.play_mode == 2:
            prev_pos_width = screen.screen.get_rect().width / 7.0 * 6.0 - self.button_border.get_rect().width
            for i in range(0, len(self.character_spawn_buttons)):
                screen.screen.blit(self.button_border, (self.button_rect_2[i].left, self.button_rect_2[i].top))
                character_rect = self.character_spawn_buttons[i].button_image_2.get_rect()
                character_rect.center = self.button_rect_2[i].center
                self.character_spawn_buttons[i].draw_button((character_rect.left, character_rect.top), 2)
                prev_pos_width = prev_pos_width - self.button_border.get_rect().width - screen.screen.get_rect().width / 250


    def check_click(self, mouse):
        if len(self.character_spawn_buttons) != len(self.button_rect_1):
            return
        for i in range(0, len(self.character_spawn_buttons)):
            if self.button_rect_1[i].left <= mouse[0] <= self.button_rect_1[i].right and self.button_rect_1[i].top <= mouse[1] <= self.button_rect_1[i].bottom:
                self.character_spawn_buttons[i].spawn(1)
        if self.gameplay.play_mode == 2:
            for i in range(0, len(self.character_spawn_buttons)):
                if self.button_rect_2[i].left <= mouse[0] <= self.button_rect_2[i].right and self.button_rect_2[i].top <= mouse[1] <= self.button_rect_2[i].bottom:
                    self.character_spawn_buttons[i].spawn(2)


    def update(self):
        self.draw_button()

    def screen_resize(self):
        self.load_image()
        self.button_rect_1.clear()
        prev_pos_width = screen.screen.get_rect().width / 7
        for i in range(0, len(self.character_spawn_buttons)):
            self.button_rect_1.append(self.button_border.get_rect())
            self.button_rect_1[i].left = prev_pos_width
            self.button_rect_1[i].top = screen.screen.get_rect().height / 300
            prev_pos_width = prev_pos_width + self.button_border.get_rect().width + screen.screen.get_rect().width / 250
        if self.gameplay.play_mode == 2:
            self.button_rect_2.clear()
            prev_pos_width = screen.screen.get_rect().width / 7.0 * 6.0 - self.button_border.get_rect().width
            for i in range(0, len(self.character_spawn_buttons)):
                self.button_rect_2.append(self.button_border.get_rect())
                self.button_rect_2[i].left = prev_pos_width
                self.button_rect_2[i].top = screen.screen.get_rect().height / 300
                prev_pos_width = prev_pos_width - self.button_border.get_rect().width - screen.screen.get_rect().width / 250