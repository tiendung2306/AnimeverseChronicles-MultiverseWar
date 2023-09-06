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

    def can_spawn(self, side):
        if side == 1:
            if self.gameplay.curr_gold_1 >= self.gameplay.character_cost[self.character_type]:
                return True
        else:
            if self.gameplay.curr_gold_2 >= self.gameplay.character_cost[self.character_type]:
                return True
        return False

    def spend_gold(self, side):
        if side == 1:
            self.gameplay.gold_outcome_1 += self.gameplay.character_cost[self.character_type]
        else:
            self.gameplay.gold_outcome_2 += self.gameplay.character_cost[self.character_type]

    def spawn(self, side):
        if side == 1:
            spawn(self.character_type, side, 0, self.gameplay)
        else:
            spawn(self.character_type, side, 39, self.gameplay)

class spawn_process():
    def __init__(self, gameplay, side):
        self.gameplay = gameplay
        self.side = side
        self.position1 = (screen.screen.get_rect().width / 550, screen.screen.get_rect().width / 7 / 2.4)
        self.size = (screen.screen.get_rect().width / 8.7, screen.screen.get_rect().height / 130)
        self.position2 = (screen.screen.get_rect().width - screen.screen.get_rect().width / 550 - self.size[0], screen.screen.get_rect().width - screen.screen.get_rect().width / 7 / 2.4 - self.size[1])
        self.color = Black

        self.is_spawn = False
        self.start_spawn_time = 0.0
        self.spawn_time = self.gameplay.spawn_time

    def draw(self):
        if self.side == 1:
            self.position1 = (screen.screen.get_rect().width / 550, screen.screen.get_rect().width / 7 / 2.4)
            self.size = (screen.screen.get_rect().width / 8.7, screen.screen.get_rect().height / 130)
            pygame.draw.rect(screen.screen, self.color, pygame.Rect(self.position1[0], self.position1[1], self.size[0], self.size[1]), 1, 7)

            process_bar_fill_percent = (self.gameplay.curr_time - self.start_spawn_time) / self.spawn_time * 100
            if len(self.gameplay.spawn_queue1) > 0:
                if process_bar_fill_percent < 100.0:
                    self.is_spawn = False
                    pygame.draw.rect(screen.screen, self.color, pygame.Rect(self.position1[0], self.position1[1], self.size[0] * process_bar_fill_percent / 100.0, self.size[1]), 0, 7)
                else:
                    self.is_spawn = True
                    self.start_spawn_time = self.gameplay.curr_time
            circle1 = 1
            circle2 = 1
            circle3 = 1
            if len(self.gameplay.spawn_queue1) > 2:
                circle3 = 0
            if len(self.gameplay.spawn_queue1) > 1:
                circle2 = 0
            if len(self.gameplay.spawn_queue1) > 0:
                circle1 = 0
            pygame.draw.circle(screen.screen, self.color, (self.position1[0] + self.size[0] + screen.screen.get_rect().width / 150, self.position1[1] + self.size[1] / 1.8), self.size[1] / 1.75, circle1)
            pygame.draw.circle(screen.screen, self.color, (self.position1[0] + self.size[0] + 2*screen.screen.get_rect().width / 150, self.position1[1] + self.size[1] / 1.8), self.size[1] / 1.75, circle2)
            pygame.draw.circle(screen.screen, self.color, (self.position1[0] + self.size[0] + 3*screen.screen.get_rect().width / 150, self.position1[1] + self.size[1] / 1.8), self.size[1] / 1.75, circle3)
        else:
            self.position2 = (screen.screen.get_rect().width - screen.screen.get_rect().width / 550 - self.size[0], screen.screen.get_rect().width / 7 / 2.4)
            self.size = (screen.screen.get_rect().width / 8.7, screen.screen.get_rect().height / 130)
            pygame.draw.rect(screen.screen, self.color, pygame.Rect(self.position2[0], self.position2[1], self.size[0], self.size[1]), 1, 7)
            
            process_bar_fill_percent = (self.gameplay.curr_time - self.start_spawn_time) / self.spawn_time * 100.0
            if len(self.gameplay.spawn_queue2) > 0:
                if process_bar_fill_percent < 100.0:
                    self.is_spawn = False
                    pygame.draw.rect(screen.screen, self.color, pygame.Rect(self.position2[0] + self.size[0] - self.size[0] * process_bar_fill_percent / 100.0 - 1, self.position2[1], self.size[0] * process_bar_fill_percent / 100.0, self.size[1]), 0, 7)
                else:
                    self.is_spawn = True
                    self.start_spawn_time = self.gameplay.curr_time
            
            circle1 = 1
            circle2 = 1
            circle3 = 1
            if len(self.gameplay.spawn_queue2) > 2:
                circle3 = 0
            if len(self.gameplay.spawn_queue2) > 1:
                circle2 = 0
            if len(self.gameplay.spawn_queue2) > 0:
                circle1 = 0
            pygame.draw.circle(screen.screen, self.color, (self.position2[0] - screen.screen.get_rect().width / 150, self.position2[1] + self.size[1] / 1.8), self.size[1] / 1.75, circle1)
            pygame.draw.circle(screen.screen, self.color, (self.position2[0] - 2*screen.screen.get_rect().width / 150, self.position2[1] + self.size[1] / 1.8), self.size[1] / 1.75, circle2)
            pygame.draw.circle(screen.screen, self.color, (self.position2[0] - 3*screen.screen.get_rect().width / 150, self.position2[1] + self.size[1] / 1.8), self.size[1] / 1.75, circle3)

    def start_fill_process_bar(self):
        self.start_spawn_time = self.gameplay.curr_time   

class gameplay_ui():
    def __init__(self, gameplay):
        self.gameplay = gameplay
        self.button_border_original = pygame.image.load('GameplayAssets\\spawn_button.png')
        self.character_spawn_buttons = []
        self.button_border = self.button_border_original.copy()
        self.button_border = pygame.transform.smoothscale(self.button_border, (screen.screen.get_rect().width / 20, screen.screen.get_rect().width / 20))
        self.button_rect_1 = []
        self.button_rect_2 = []

        self.spawn_bar1 = spawn_process(self.gameplay, 1)
        self.spawn_bar2 = spawn_process(self.gameplay, 2)

        self.add_button()
        self.load_image()
        self.draw_button()
    
    def load_image(self):
        for x in self.character_spawn_buttons:
            x.load_image()
        self.button_border = self.button_border_original.copy()
        self.button_border = pygame.transform.smoothscale(self.button_border, (screen.screen.get_rect().width / 20, screen.screen.get_rect().width / 20))

    def add_button(self):
        self.character_spawn_buttons.append(button(sword_man, 'GameplayAssets\\sword_man_avatar.png', self.gameplay))
        self.character_spawn_buttons.append(button(archer, 'GameplayAssets\\archer_avatar.png', self.gameplay))
        self.character_spawn_buttons.append(button(tanker, 'GameplayAssets\\tanker_avatar.png', self.gameplay))
        self.character_spawn_buttons.append(button(wizard, 'GameplayAssets\\wizard_avatar.png', self.gameplay))

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
            pygame.draw.rect(screen.screen, Gray62, pygame.Rect(self.button_rect_1[i].left, self.button_rect_1[i].top, screen.screen.get_rect().width / 20, screen.screen.get_rect().width / 20), border_radius=int(screen.screen.get_rect().width / 80))
            screen.screen.blit(self.button_border, (self.button_rect_1[i].left, self.button_rect_1[i].top))
            character_rect = self.character_spawn_buttons[i].button_image_1.get_rect()
            character_rect.center = self.button_rect_1[i].center
            self.character_spawn_buttons[i].draw_button((character_rect.left, character_rect.top), 1)
            prev_pos_width = prev_pos_width + self.button_border.get_rect().width + screen.screen.get_rect().width / 250
            
        if self.gameplay.play_mode == 2:
            prev_pos_width = screen.screen.get_rect().width / 7.0 * 6.0 - self.button_border.get_rect().width
            for i in range(0, len(self.character_spawn_buttons)):
                pygame.draw.rect(screen.screen, Gray62, pygame.Rect(self.button_rect_2[i].left, self.button_rect_2[i].top, screen.screen.get_rect().width / 20, screen.screen.get_rect().width / 20), border_radius=int(screen.screen.get_rect().width / 80))
                screen.screen.blit(self.button_border, (self.button_rect_2[i].left, self.button_rect_2[i].top))
                character_rect = self.character_spawn_buttons[i].button_image_2.get_rect()
                character_rect.center = self.button_rect_2[i].center
                self.character_spawn_buttons[i].draw_button((character_rect.left, character_rect.top), 2)
                prev_pos_width = prev_pos_width - self.button_border.get_rect().width - screen.screen.get_rect().width / 250

    def spawn(self, button_num, side):
        self.character_spawn_buttons[button_num].spawn(side)

    def insert_in_spawn_queue(self, button_num, side): #bat dau an vao nut de spawn
        if len(self.character_spawn_buttons) <= button_num:
            return
        if self.character_spawn_buttons[button_num].can_spawn(side) == True:
                    self.click_spawn_button(button_num, side)

    def click_spawn_button(self, button_num, side):
        if side == 1:
            if len(self.gameplay.spawn_queue1) == 0:
                self.spawn_bar1.start_fill_process_bar()
            if len(self.gameplay.spawn_queue1) < 3:
                self.gameplay.spawn_queue1.append(button_num)
                self.character_spawn_buttons[button_num].spend_gold(side)
        else: 
            if len(self.gameplay.spawn_queue2) == 0:
                self.spawn_bar2.start_fill_process_bar()
            if len(self.gameplay.spawn_queue2) < 3:
                self.gameplay.spawn_queue2.append(button_num)
                self.character_spawn_buttons[button_num].spend_gold(side)

    def check_click(self, mouse):
        if len(self.character_spawn_buttons) != len(self.button_rect_1) :
            return
        if self.gameplay.play_mode == 2 and len(self.character_spawn_buttons) != len(self.button_rect_2) :
            return
        for i in range(0, len(self.character_spawn_buttons)):
            if self.button_rect_1[i].left <= mouse[0] <= self.button_rect_1[i].right and self.button_rect_1[i].top <= mouse[1] <= self.button_rect_1[i].bottom:
                self.insert_in_spawn_queue(i, 1)
        if self.gameplay.play_mode == 2:
            for i in range(0, len(self.character_spawn_buttons)):
                if self.button_rect_2[i].left <= mouse[0] <= self.button_rect_2[i].right and self.button_rect_2[i].top <= mouse[1] <= self.button_rect_2[i].bottom:
                    self.insert_in_spawn_queue(i, 2)
    def draw_spawn_bar(self):
        self.spawn_bar1.draw()
        if self.gameplay.play_mode == 2:
            self.spawn_bar2.draw()

    def update(self):
        self.draw_button()
        self.draw_spawn_bar()
        if len(self.gameplay.spawn_queue1) > 0 and self.spawn_bar1.is_spawn == True:
            self.spawn(self.gameplay.spawn_queue1[0], 1)
            del self.gameplay.spawn_queue1[0]
            self.spawn_bar1.is_spawn == False
        
        if len(self.gameplay.spawn_queue2) > 0 and self.spawn_bar2.is_spawn == True:
            self.spawn(self.gameplay.spawn_queue2[0], 2)
            del self.gameplay.spawn_queue2[0]
            self.spawn_bar2.is_spawn == False

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