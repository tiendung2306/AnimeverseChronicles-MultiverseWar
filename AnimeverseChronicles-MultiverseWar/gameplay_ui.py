import pygame
from pygame.locals import *
from object_function import * 
from screen import *
from img_analyze import *
from animation_player import *


spawn1 = analyzed_img("GameplayAssets\spawn(1).png ", 219, 1 , 167 , 215)
spawn2 = analyzed_img("GameplayAssets\spawn(2).png ", 219, 1 , 167 , 215)
spawn3 = analyzed_img("GameplayAssets\spawn(3).png ", 219, 1 , 167 , 215)
spawn4 = analyzed_img("GameplayAssets\spawn(4).png ", 219, 1 , 167 , 215)
spawn5 = analyzed_img("GameplayAssets\spawn(5).png ", 219, 1 , 167 , 215)
spawn6 = analyzed_img("GameplayAssets\spawn(6).png ", 219, 1 , 167 , 215)
spawn7 = analyzed_img("GameplayAssets\spawn(7).png ", 219, 1 , 167 , 215)
spawn8 = analyzed_img("GameplayAssets\spawn(8).png ", 219, 1 , 167 , 215)

class button():
    def __init__(self, character_name, image_filename, gameplay):
        self.gameplay = gameplay
        self.character_type =  character_name
        self.button_image_original = pygame.image.load(image_filename)
        self.button_image_1 = self.button_image_original.copy()
        self.button_image_2 = self.button_image_original.copy()
        self.button_image_2 = pygame.transform.flip(self.button_image_2, True, False)

        self.level_up_button_original = pygame.image.load('GameplayAssets\\level_up_button1.png').convert_alpha()
        self.level_up_button = self.level_up_button_original.copy()

        self.button_num = -1
        self.key_icon_filename = '1_Key_Light.png'
        self.key_icon_original = pygame.image.load('GameplayAssets\\keyboard_and_mouse_icons\\Light\\' + self.key_icon_filename)
        self.mouse_click_icon_original = pygame.image.load('GameplayAssets\\keyboard_and_mouse_icons\\Light\\Mouse_Left_Key_Light.png')

    def load_key_icon_image(self):
        self.key_icon = self.key_icon_original.copy()
        self.key_icon = pygame.transform.smoothscale(self.key_icon, (screen.screen.get_rect().width / 75, self.key_icon.get_rect().height / (self.key_icon.get_rect().width / screen.screen.get_rect().width * 75)))

    def load_image(self):
        self.button_image_1 = self.button_image_original.copy()
        self.button_image_2 = self.button_image_original.copy()
        self.button_image_2 = pygame.transform.flip(self.button_image_2, True, False)
        self.button_image_1 = pygame.transform.smoothscale(self.button_image_1, (screen.screen.get_rect().width / 16, screen.screen.get_rect().height / 16))
        self.button_image_2 = pygame.transform.smoothscale(self.button_image_2, (screen.screen.get_rect().width / 16, screen.screen.get_rect().height / 16))

        self.level_up_button = self.level_up_button_original.copy()
        self.level_up_button = pygame.transform.smoothscale(self.level_up_button, (screen.screen.get_rect().width / 22, self.level_up_button.get_rect().height / self.level_up_button.get_rect().width * screen.screen.get_rect().height / 22))
        self.level_up_button.set_alpha(55)
        self.level_up_button_rect = pygame.Rect(0, 0, screen.screen.get_rect().width / 22, self.level_up_button.get_rect().height / self.level_up_button.get_rect().width * screen.screen.get_rect().height / 22)
        self.load_key_icon_image()
        self.mouse_click_icon = self.mouse_click_icon_original.copy()
        self.mouse_click_icon = pygame.transform.smoothscale(self.mouse_click_icon, (screen.screen.get_rect().width / 85, self.mouse_click_icon.get_rect().height / (self.mouse_click_icon.get_rect().width / screen.screen.get_rect().width * 85)))

    def draw_button(self, button_num, pos, side, pos1):
        if self.button_num == -1:
            self.button_num = button_num
            self.key_icon_filename = str(self.button_num) + '_Key_Light.png'
            self.key_icon_original = pygame.image.load('GameplayAssets\\keyboard_and_mouse_icons\\Light\\' + self.key_icon_filename)
            self.load_key_icon_image()
        if side == 1:
            screen.screen.blit(self.button_image_1, pos)
            if self.gameplay.islevel_up1 == True and self.gameplay.character_level1[button_num - 1] < self.gameplay.character_level_max[button_num - 1]:
                self.level_up_button_rect.center = (pos1[0], pos1[1] - screen.screen.get_rect().height / 200)
                screen.screen.blit(self.level_up_button, self.level_up_button_rect)
                # self.gameplay.islevel_up = False
            screen.screen.blit(self.mouse_click_icon, (pos[0] + self.button_image_1.get_rect().width / 7.95, screen.screen.get_rect().height / 97))
        else:
            screen.screen.blit(self.button_image_2, pos)
            if self.gameplay.islevel_up2 == True and self.gameplay.character_level2[button_num - 1] < self.gameplay.character_level_max[button_num - 1]:
                self.level_up_button_rect.center = (pos1[0], pos1[1] - screen.screen.get_rect().height / 200)
                screen.screen.blit(self.level_up_button, self.level_up_button_rect)
                # self.gameplay.islevel_up = False
            screen.screen.blit(self.key_icon, (pos[0] + self.button_image_2.get_rect().width - 2*self.button_image_2.get_rect().width / 5.0, screen.screen.get_rect().height / 190))

    def can_spawn(self, side):
        val_list = list(self.gameplay.character_slot_idx.values())
        idx = val_list.index(self.character_type)
        if side == 1:
            if self.gameplay.curr_gold_1 >= self.gameplay.character_cost[self.character_type][self.gameplay.character_level1[idx] - 1]:
                return True
        else:
            if self.gameplay.curr_gold_2 >= self.gameplay.character_cost[self.character_type][self.gameplay.character_level2[idx] - 1]:
                return True
        return False

    def spend_gold(self, side):
        val_list = list(self.gameplay.character_slot_idx.values())
        idx = val_list.index(self.character_type)
        if side == 1:
            self.gameplay.gold_outcome_1 += self.gameplay.character_cost[self.character_type][self.gameplay.character_level1[idx] - 1]
        else:
            self.gameplay.gold_outcome_2 += self.gameplay.character_cost[self.character_type][self.gameplay.character_level2[idx] - 1]

    def spawn(self, side):
        if side == 1:
            spawn(self.character_type, side, 4, self.gameplay)
        elif side == 2:
            spawn(self.character_type, side, self.gameplay.number_of_box - 5, self.gameplay)

class spawn_process():
    def __init__(self, gameplay, side):
        self.gameplay = gameplay
        self.side = side
        self.position1 = (screen.screen.get_rect().width / 550, screen.screen.get_rect().width / 7 / 2.4)
        self.size = (screen.screen.get_rect().width / 8.7, screen.screen.get_rect().height / 130)
        self.position2 = (screen.screen.get_rect().width - screen.screen.get_rect().width / 550 - self.size[0], screen.screen.get_rect().width - screen.screen.get_rect().width / 7 / 2.4 - self.size[1])
        self.color = Black
        if self.gameplay.path_num <= 2:
            self.color = White

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

class lvl_up_button():
    def __init__(self, gameplay, side):
        self.gameplay = gameplay
        self.side = side
        self.button_image_original = pygame.image.load('GameplayAssets\\level_up_button.png')
        self.button_image_1 = self.button_image_original.copy()
        self.button_image_2 = self.button_image_original.copy()
        # self.button_image_2 = pygame.transform.flip(self.button_image_2, True, False)

        self.level_font = pygame.font.Font('Fonts\\Minecraft.ttf', 14)
        self.text_color = Black
        if self.gameplay.path_num <= 2:
            self.text_color = White
        self.level1 = self.level_font.render('Lv: ' + str(self.gameplay.curr_level1), True, self.text_color)
        self.level2 = self.level_font.render('Lv: ' + str(self.gameplay.curr_level2), True, self.text_color)
        
    def load_image(self):
        self.button_image_1 = self.button_image_original.copy()
        self.button_image_2 = self.button_image_original.copy()
        # self.button_image_2 = pygame.transform.flip(self.button_image_2, True, False)
        self.button_image_1 = pygame.transform.smoothscale(self.button_image_1, (screen.screen.get_rect().width / 23, self.button_image_1.get_rect().height / self.button_image_1.get_rect().width * screen.screen.get_rect().height / 23))
        self.button_image_2 = pygame.transform.smoothscale(self.button_image_2, (screen.screen.get_rect().width / 23, self.button_image_2.get_rect().height / self.button_image_2.get_rect().width * screen.screen.get_rect().height / 23))
        self.button_image_1_rect = self.button_image_1.get_rect()
        self.button_image_1_rect.left = screen.screen.get_rect().width / 250
        self.button_image_1_rect.top = screen.screen.get_rect().height / 8.25
        self.button_image_2_rect = self.button_image_2.get_rect()
        self.button_image_2_rect.right = screen.screen.get_rect().width - screen.screen.get_rect().width / 250
        self.button_image_2_rect.top = screen.screen.get_rect().height / 8.25

        self.level1_rect = self.level1.get_rect()
        self.level1_rect.center = self.button_image_1_rect.center
        self.level1_rect.top = self.button_image_1_rect.bottom + screen.screen.get_rect().height / 500
        self.level2_rect = self.level2.get_rect()
        self.level2_rect.center = self.button_image_2_rect.center
        self.level2_rect.top = self.button_image_2_rect.bottom + screen.screen.get_rect().height / 500

    def draw(self):
        if self.side == 1:
            screen.screen.blit(self.button_image_1, self.button_image_1_rect)
            screen.screen.blit(self.level1, self.level1_rect)
        elif self.gameplay.play_mode == 2:
            screen.screen.blit(self.button_image_2, self.button_image_2_rect)
            screen.screen.blit(self.level2, self.level2_rect)

    def level_up2(self):
        if self.side == 2 and self.gameplay.play_mode == 2 and self.gameplay.islevel_up2 == False:
            self.gameplay.level_up(self.side)
            self.level2 = self.level_font.render('Lv: ' + str(self.gameplay.curr_level2), True, self.text_color)

    def on_hover(self, mouse):
        if self.side == 1:
            if self.button_image_1_rect.left <= mouse[0] <= self.button_image_1_rect.right and self.button_image_1_rect.top <= mouse[1] <= self.button_image_1_rect.bottom:
                return True
        if self.side == 2 and self.gameplay.play_mode == 2:
            if self.button_image_2_rect.left <= mouse[0] <= self.button_image_2_rect.right and self.button_image_2_rect.top <= mouse[1] <= self.button_image_2_rect.bottom:
                return True
        return False

    def check_click(self, mouse):
        if self.side == 1:
            if self.button_image_1_rect.left <= mouse[0] <= self.button_image_1_rect.right and self.button_image_1_rect.top <= mouse[1] <= self.button_image_1_rect.bottom:
                self.gameplay.level_up(self.side)
                self.level1 = self.level_font.render('Lv: ' + str(self.gameplay.curr_level1), True, self.text_color)
        if self.side == 2 and self.gameplay.play_mode == 2:
            if self.button_image_2_rect.left <= mouse[0] <= self.button_image_2_rect.right and self.button_image_2_rect.top <= mouse[1] <= self.button_image_2_rect.bottom:
                self.level_up2()
            

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

        self.lvl_up_button1 = lvl_up_button(self.gameplay, 1)
        self.lvl_up_button2 = lvl_up_button(self.gameplay, 2)

        self.level_font = pygame.font.Font('Fonts\\Minecraft.ttf', int(screen.screen.get_rect().width / 140))

        self.text_beside_mouse_font = pygame.font.Font('Fonts\\joystix_monospace.otf', 14)

        self.add_button()
        self.load_image()
        self.draw_button()
    
    def load_image(self):
        for x in self.character_spawn_buttons:
            x.load_image()
        self.button_border = self.button_border_original.copy()
        self.button_border = pygame.transform.smoothscale(self.button_border, (screen.screen.get_rect().width / 20, screen.screen.get_rect().width / 20))
        self.lvl_up_button1.load_image()
        self.lvl_up_button2.load_image()

    def add_button(self):
        self.character_spawn_buttons.append(button(self.gameplay.tankerclass, 'GameplayAssets\\tanker_avatar.png', self.gameplay))
        self.character_spawn_buttons.append(button(self.gameplay.sword_manclass, 'GameplayAssets\\sword_man_avatar.png', self.gameplay))
        self.character_spawn_buttons.append(button(self.gameplay.archerclass, 'GameplayAssets\\archer_avatar.png', self.gameplay))
        self.character_spawn_buttons.append(button(self.gameplay.wizardclass, 'GameplayAssets\\wizard_avatar.png', self.gameplay))
        self.character_spawn_buttons.append(button(self.gameplay.gokuclass, 'GameplayAssets\\goku_avatar1.png', self.gameplay))
        self.character_spawn_buttons.append(button(self.gameplay.narutoclass, 'GameplayAssets\\naruto_avatar.png', self.gameplay))

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
        #ve nut spawn
        prev_pos_width = screen.screen.get_rect().width / 7
        for i in range(0, len(self.character_spawn_buttons)):
            pygame.draw.rect(screen.screen, Gray62, pygame.Rect(self.button_rect_1[i].left, self.button_rect_1[i].top, screen.screen.get_rect().width / 20, screen.screen.get_rect().width / 20), border_radius=int(screen.screen.get_rect().width / 80))
            screen.screen.blit(self.button_border, (self.button_rect_1[i].left, self.button_rect_1[i].top))
            character_rect = self.character_spawn_buttons[i].button_image_1.get_rect()
            character_rect.center = self.button_rect_1[i].center
            self.character_spawn_buttons[i].draw_button(i + 1, (character_rect.left, character_rect.top), 1, self.button_rect_1[i].center)
            prev_pos_width = prev_pos_width + self.button_border.get_rect().width + screen.screen.get_rect().width / 250

            level = self.level_font.render('Lv: ' + str(self.gameplay.character_level1[i]), True, Black)
            screen.screen.blit(level, (self.button_rect_1[i].center[0] - screen.screen.get_rect().width / 250, self.button_rect_1[i].top + screen.screen.get_rect().height / 150))
            
        if self.gameplay.play_mode == 2:
            prev_pos_width = screen.screen.get_rect().width / 7.0 * 6.0 - self.button_border.get_rect().width
            for i in range(0, len(self.character_spawn_buttons)):
                pygame.draw.rect(screen.screen, Gray62, pygame.Rect(self.button_rect_2[i].left, self.button_rect_2[i].top, screen.screen.get_rect().width / 20, screen.screen.get_rect().width / 20), border_radius=int(screen.screen.get_rect().width / 80))
                screen.screen.blit(self.button_border, (self.button_rect_2[i].left, self.button_rect_2[i].top))
                character_rect = self.character_spawn_buttons[i].button_image_2.get_rect()
                character_rect.center = self.button_rect_2[i].center
                self.character_spawn_buttons[i].draw_button(i + 1, (character_rect.left, character_rect.top), 2, self.button_rect_2[i].center)
                prev_pos_width = prev_pos_width - self.button_border.get_rect().width - screen.screen.get_rect().width / 250

                level = self.level_font.render('Lv: ' + str(self.gameplay.character_level2[i]), True, Black)
                screen.screen.blit(level, (self.button_rect_2[i].center[0] - screen.screen.get_rect().width / 100, self.button_rect_2[i].top + screen.screen.get_rect().height / 150))

        #ve nut lvl_up nha chinh
        self.lvl_up_button1.draw()
        self.lvl_up_button2.draw()
        

    def spawn(self, button_num, side): #spawn tuong
        self.character_spawn_buttons[button_num].spawn(side)

    def insert_in_spawn_queue(self, button_num, side): #bat dau an vao nut de spawn
        if len(self.character_spawn_buttons) <= button_num:
            return
        if self.character_spawn_buttons[button_num].can_spawn(side) == True:
            self.click_spawn_button(button_num, side)


    def spawn_state(self, button_num, side):
        return (self.character_spawn_buttons[button_num].can_spawn(side) and len(self.gameplay.spawn_queue1) < 3)

    def click_spawn_button(self, button_num, side):
        spawning(side, self.gameplay)
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
                if self.gameplay.islevel_up1 == True:
                    if self.gameplay.character_level_up(i + 1, 1) == True:
                        self.gameplay.islevel_up1 = False
                else:
                    self.insert_in_spawn_queue(i, 1)
        if self.gameplay.play_mode == 2:
            for i in range(0, len(self.character_spawn_buttons)):
                if self.button_rect_2[i].left <= mouse[0] <= self.button_rect_2[i].right and self.button_rect_2[i].top <= mouse[1] <= self.button_rect_2[i].bottom:
                    if self.gameplay.islevel_up2 == True:
                        if self.gameplay.character_level_up(i + 1, 2) == True:
                            self.gameplay.islevel_up2 = False
                    else:
                        self.insert_in_spawn_queue(i, 2)
        if self.gameplay.islevel_up1 == False:
            self.lvl_up_button1.check_click(mouse)
        if self.gameplay.islevel_up2 == False:
            self.lvl_up_button2.check_click(mouse)

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

    def display_text_beside_mouse(self, text, mouse):
        text_surface = self.text_beside_mouse_font.render(text, True, Yellow)
        screen.screen.blit(text_surface, (mouse[0] + screen.screen.get_rect().width / 100, mouse[1] + screen.screen.get_rect().width / 100))
        # print(text)

    def on_hover(self, mouse):
        if len(self.character_spawn_buttons) != len(self.button_rect_1) :
            return
        if self.gameplay.play_mode == 2 and len(self.character_spawn_buttons) != len(self.button_rect_2) :
            return
        for i in range(0, len(self.character_spawn_buttons)):
            if self.button_rect_1[i].left <= mouse[0] <= self.button_rect_1[i].right and self.button_rect_1[i].top <= mouse[1] <= self.button_rect_1[i].bottom:
                if self.gameplay.islevel_up1 == False:
                    self.display_text_beside_mouse(str(self.gameplay.get_character_cost(i, 1)), mouse)
        if self.gameplay.play_mode == 2:
            for i in range(0, len(self.character_spawn_buttons)):
                if self.button_rect_2[i].left <= mouse[0] <= self.button_rect_2[i].right and self.button_rect_2[i].top <= mouse[1] <= self.button_rect_2[i].bottom:
                    if self.gameplay.islevel_up2 == False:
                        self.display_text_beside_mouse(str(self.gameplay.get_character_cost(i, 2)), mouse)

        if self.lvl_up_button1.on_hover(mouse) == True:
            self.display_text_beside_mouse(str(self.gameplay.level_up_cost[self.gameplay.curr_level1 - 1]), mouse)
        if self.lvl_up_button2.on_hover(mouse) == True:
            self.display_text_beside_mouse(str(self.gameplay.level_up_cost[self.gameplay.curr_level2 - 1]), mouse)

class spawning():
    def __init__(self, side, gameplay):
        self.gameplay = gameplay
        self.box = pygame.Rect(0,0,gameplay.box_size[0], gameplay.box_size[1] / 2 )
        if side == 1:
            self.box.center = (4 * gameplay.box_size[0], gameplay.path_height - gameplay.box_size[1] / 4)
        else:
            self.box.center = ((gameplay.number_of_box - 4) * gameplay.box_size[0], gameplay.path_height - gameplay.box_size[1] / 4)
        self.imgbox = spawn1.hitbox_to_imgbox(self.box)        
        self.animation = animation_player([spawn1, spawn2, spawn3, spawn4, spawn5, spawn6], side ,0.65,self.imgbox ,gameplay)
        gameplay.side0.append(self)
        self.clock = timing_clock(gameplay.spawn_time, gameplay)
        self.clock.start()

    def remove(self):
        self.animation.remove()
        self.clock.remove()
        self.gameplay.side0.remove(self)
        
    def operation(self):
        if self.clock.Return:
            self.animation.play()
        else:
            self.remove()