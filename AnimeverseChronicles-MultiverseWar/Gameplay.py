import pygame
from pygame.locals import *
from color import *
from character import * 
from nexus import *
from pause_pannel import *
from states import *
from screen import *
from gameplay_ui import *
from key_binding_manager import *
from gameover_panel import *
from list_function import*
from object_function import *
from PvC_mode import *
from Random import *
import random


class gameplay():
    def __init__(self, play_mode):
        pygame.init()

        self.play_mode = play_mode #1 la player vs computer, 2 la pvp

        self.spawn_time = 2 #thoi gian de spawn mot con nhan vat tinh theo s
        self.spawn_queue1 = []
        self.spawn_queue2 = []
        self.rand = Random()

        path_num = (self.rand.get_truly_random_seed_through_os()) % 5  + 1
        # print(path_num)
        # self.fake_bg_original = pygame.image.load('GameplayAssets\\bg1.png')
        self.bg_original = pygame.image.load('GameplayAssets\\bg({}).jpg'.format(path_num))
        self.path_original = pygame.image.load('GameplayAssets\\path' + str(path_num) + '.png')
        self.board_original = pygame.image.load('GameplayAssets\\board.png')
        self.settings_button_original = pygame.image.load('GameplayAssets\\settings_button.png')
        self.play_button_original = pygame.image.load('GameplayAssets\\play_button.png')
        self.pause_button_original = pygame.image.load('GameplayAssets\\pause_button.png')
        
        self.character_cost = {
            tankerclass : 20,
            sword_manclass : 30,
            archerclass : 40,
            wizardclass : 50,
            gokuclass : 100,
            narutoclass : 150
        }

        self.character_slot_idx = {
            0 : tankerclass,
            1 : sword_manclass,
            2 : archerclass,
            3 : wizardclass,
            4 : gokuclass,
            5 : narutoclass,
        }

        #character type
        self.sword_manclass = sword_manclass
        self.archerclass = archerclass
        self.tankerclass = tankerclass
        self.wizardclass = wizardclass
        self.gokuclass = gokuclass
        self.nexusclass = Nexusclass
        self.narutoclass = narutoclass
        self.cloneclass = cloneclass


        if self.play_mode == 2:
            tmp = Rect(0, 0, 0, 0)
            tmp.center = (screen.screen.get_rect().width / 2.0, 10)
            tmp.top = 10
            self.play_pause_button = (tmp.left, tmp.top)
        else:
            self.play_pause_button = (screen.screen.get_rect().width - screen.screen.get_rect().width // 32, 10)


        self.gold_per_sec = 10
        #level
        self.islevel_up1 = False
        self.islevel_up2 = False
        self.level_up_cost = [200, 250, 280, 300, 340, 380, 420, 450, 500, 600, 700, 800, 850, 900, 1000, 1100, 1250, 1500, 1750, 2000]
        self.curr_level1 = 1
        self.curr_level2 = 1
        self.character_level_max = [5, 5, 5, 5, 3, 2]
        self.character_level1 = [1, 1, 1, 1, 1, 1] # ung voi cac con lan luot tu trai sang theo thu tu spawn
        self.character_level2 = [1, 1, 1, 1, 1, 1]

        self.timer_font = pygame.font.Font('Fonts\\joystix_monospace.otf', 16)
        self.start_time = 0.0
        self.pre_curr_time = 0.0
        self.curr_time = 0.0
        self.pause_time = 0.0
        self.start_pause_time = 0.0
        self.time = 0.0 # dung giong voi time.time()
        self.end = False

        self.gold_font = pygame.font.Font('Fonts\\joystix_monospace.otf', 20)
        self.curr_gold_1 = 0
        self.gold_income_1 = 0
        self.gold_outcome_1 = 0
        self.curr_gold_2 = 0
        self.gold_income_2 = 0
        self.gold_outcome_2 = 0

        self.isPlay = True
        self.isGameover = False
        self.Gameover_status = 0 #0 la hoa`, 1 la player 1 thua, 2 la player 2 thua
        self.fade = pygame.Surface((screen.screen.get_rect().width, screen.screen.get_rect().height))
        self.fade.fill((0,0,0))
        self.fade.set_alpha(200)
        self.Pause_Pannel = pause_pannel()
        self.Gameover_panel = gameover_panel(self)

        self.gameplay_ui = gameplay_ui(self)

        self.load_all_gameplay_image()

        self.spawn_point_height = self.path.get_rect().top + self.path.get_rect().height / 7.0

        self.number_of_box = 45
        self.box_size = (screen.screen.get_rect().width / self.number_of_box , screen.screen.get_rect().height * 3 / self.number_of_box)
        self.path_height = screen.screen.get_rect().height - self.path.get_rect().height * 7 / 10
        self.screen = screen.screen.get_size()
    #Object import:
        self.side1 = []
        self.side2 = []
        self.side3 = []
        self.side4 = []
        self.side0 = []

        self.nexus1 = Nexusclass(1, self)
        self.nexus2 = Nexusclass(2, self)


        # spawn(tankerclass, 2, 40, self)
        # spawn(tankerclass, 2, 40, self)
        # spawn(tankerclass, 2, 40, self)
        # spawn(tankerclass, 2, 40, self)
        # spawn(tankerclass, 2, 40, self)

        self.selected_object = None
        self.AI = PvC_mode(self)

    def AI_process(self):
        if self.play_mode == 1:
            self.AI.update()

    def side(self, side):
        if side == 1:
            return self.side1
        elif side == -1 :
            return self.side2

    def load_all_gameplay_image(self):
        self.fake_bg = self.bg_original.copy()
        self.bg = self.bg_original.copy()
        self.path = self.path_original.copy()
        self.board_1 = self.board_original.copy()
        self.board_2 = self.board_original.copy()
        self.board_2 = pygame.transform.flip(self.board_2, True, False)
        self.settings_button = self.settings_button_original.copy()
        self.play_button = self.play_button_original.copy()
        self.pause_button = self.pause_button_original.copy()

        info = pygame.display.Info()
        self.bg = pygame.transform.smoothscale(self.bg, (info.current_w, info.current_h))
        self.fake_bg = self.bg.copy()
        # self.board_1_fake = pygame.transform.smoothscale(self.board_1, (info.current_w, info.current_h))
        self.path = pygame.transform.smoothscale(self.path, (self.bg.get_rect().width, screen.screen.get_rect().height // 7))
        self.board_1 = pygame.transform.smoothscale(self.board_1, (screen.screen.get_rect().width / 7, screen.screen.get_rect().width / 7 / 2.4))
        self.board_2 = pygame.transform.smoothscale(self.board_2, (screen.screen.get_rect().width / 7, screen.screen.get_rect().width / 7 / 2.4))
        self.settings_button = pygame.transform.smoothscale(self.settings_button, (self.board_1.get_rect().width // 5, self.board_1.get_rect().width // 5))
        self.play_button = pygame.transform.smoothscale(self.play_button, (self.board_1.get_rect().width // 5, self.board_1.get_rect().width // 5))
        self.pause_button = pygame.transform.smoothscale(self.pause_button, (self.board_1.get_rect().width // 5, self.board_1.get_rect().width // 5))


        if self.play_mode == 2:
            tmp = Rect(0, 0, self.board_1.get_rect().width // 6, self.board_1.get_rect().width // 6)
            tmp.center = (screen.screen.get_rect().width / 2.0, 10)
            tmp.top = 10
            self.play_pause_button = (tmp.left, tmp.top)
        else:
            self.play_pause_button = (screen.screen.get_rect().width - screen.screen.get_rect().width // 32, 10)

        self.spawn_point_height = self.path.get_rect().top + self.path.get_rect().height / 7.0

        self.gameplay_ui.load_image()

    def screen_resize(self):
        self.Pause_Pannel.screen_resize()
        self.Gameover_panel.screen_resize()
        self.fade = pygame.Surface((screen.screen.get_rect().width, screen.screen.get_rect().height))
        self.fade.fill((0,0,0))
        self.fade.set_alpha(200)

        self.load_all_gameplay_image()
 

        self.box_size = (screen.screen.get_rect().width / self.number_of_box , screen.screen.get_rect().height * 3 / self.number_of_box)
        self.path_height = screen.screen.get_rect().height - self.path.get_rect().height * 7 / 10

        for object in self.side2 + self.side1:
            object.resize()
            
        self.screen = screen.screen.get_size()
        self.gameplay_ui.screen_resize()

    def set_fade(self): 
        screen.screen.blit(self.fade, (0,0))

    def check_click(self, play_pause_button, mouse):
        if self.isPlay == True: #neu game dang chay
            self.gameplay_ui.check_click(mouse)
            if play_pause_button[0] <= mouse[0] <= play_pause_button[0] + self.pause_button.get_rect().width and play_pause_button[1] <= mouse[1] <= play_pause_button[1] + self.pause_button.get_rect().height:
                self.SwitchPlayPauseState()
                self.isPlay = 1 - self.isPlay
                return 'None'
        else: #neu game dang duoc pause
            if self.isGameover == False and self.Pause_Pannel.check_click(mouse) == self.Pause_Pannel.buttons[0]: #an vao nut continue
                self.SwitchPlayPauseState()
                self.isPlay = 1 - self.isPlay
                return 'None'
            if self.isGameover == False and  self.Pause_Pannel.check_click(mouse) == self.Pause_Pannel.buttons[1]: #an vao nut settings
                return 'Settings'
            if self.Pause_Pannel.check_click(mouse) == self.Pause_Pannel.buttons[2]: #an vao nut back to menu
                return 'Back'


    def check_press(self, event):
        if event.key == pygame.K_ESCAPE:
            self.escape_pressed()
        if self.islevel_up2 == False:
            if event.key == keybindingmanager.key_map['Slot 1']:
                self.gameplay_ui.insert_in_spawn_queue(0, 2)
            if event.key == keybindingmanager.key_map['Slot 2']:
                self.gameplay_ui.insert_in_spawn_queue(1, 2)
            if event.key == keybindingmanager.key_map['Slot 3']:
                self.gameplay_ui.insert_in_spawn_queue(2, 2)
            if event.key == keybindingmanager.key_map['Slot 4']:
                self.gameplay_ui.insert_in_spawn_queue(3, 2)
            if event.key == keybindingmanager.key_map['Slot 5']:
                self.gameplay_ui.insert_in_spawn_queue(4, 2)
            if event.key == keybindingmanager.key_map['Slot 6']:
                self.gameplay_ui.insert_in_spawn_queue(5, 2)
            if event.key == keybindingmanager.key_map['Slot 7']:
                self.gameplay_ui.insert_in_spawn_queue(6, 2)

        #an p de len cap
        if event.key == keybindingmanager.key_map['Player_2_level_up']:
            self.gameplay_ui.lvl_up_button2.level_up2()
        #an ctrl + so de tang cap cho nhan vat
        keys = pygame.key.get_pressed()
        # if keys[pygame.K_LCTRL]:
        if keys[keybindingmanager.key_map['Slot 1']]:
                if self.islevel_up2 == True:
                    if self.character_level_up(1, 2) == True:
                        self.islevel_up2 = False
        if keys[keybindingmanager.key_map['Slot 2']]:
                if self.islevel_up2 == True:
                    if self.character_level_up(2, 2) == True:
                        self.islevel_up2 = False
        if keys[keybindingmanager.key_map['Slot 3']]:
                if self.islevel_up2 == True:
                    if self.character_level_up(3, 2) == True:
                        self.islevel_up2 = False
        if keys[keybindingmanager.key_map['Slot 4']]:
                if self.islevel_up2 == True:
                    if self.character_level_up(4, 2) == True:
                        self.islevel_up2 = False
        if keys[keybindingmanager.key_map['Slot 5']]:
                if self.islevel_up2 == True:
                    if self.character_level_up(5, 2) == True:
                        self.islevel_up2 = False
        if keys[keybindingmanager.key_map['Slot 6']]:
                if self.islevel_up2 == True:
                    if self.character_level_up(6, 2) == True:
                        self.islevel_up2 = False


    def escape_pressed(self):
        if self.isPlay == True: #neu game dang chay
            self.SwitchPlayPauseState()
            self.isPlay = 1 - self.isPlay
        else:
            self.SwitchPlayPauseState()
            self.isPlay = 1 - self.isPlay

    def SwitchPlayPauseState(self):
        if self.isPlay == True:
            self.start_pause_time = self.time
        else:
            self.pause_time = self.pause_time + self.time - self.start_pause_time

    # def reset_gameplay(self):
    #     self.spawn_queue1 = []
    #     self.spawn_queue2 = []

    #     self.gameplay_ui = gameplay_ui(self)
    #     if self.play_mode == 2:
    #         tmp = Rect(0, 0, 0, 0)
    #         tmp.center = (screen.screen.get_rect().width / 2.0, 10)
    #         tmp.top = 10
    #         self.play_pause_button = (tmp.left, tmp.top)
    #     else:
    #         self.play_pause_button = (screen.screen.get_rect().width - screen.screen.get_rect().width // 32, 10)

    #     self.nexus1 = Nexus('GameplayAssets\\nexus1.png')
    #     self.nexus2 = Nexus('GameplayAssets\\nexus2.png')

    #     self.timer_font = pygame.font.Font('Fonts\\joystix_monospace.otf', 16)
    #     self.start_time = 0.0
    #     self.curr_time = 0.0
    #     self.pause_time = 0.0
    #     self.start_pause_time = 0.0
    #     self.time = 0.0 # dung giong voi time.time()

    #     self.gold_font = pygame.font.Font('Fonts\\joystix_monospace.otf', 20)
    #     self.curr_gold_1 = 0
    #     self.gold_income_1 = 0
    #     self.gold_outcome_1 = 0
    #     self.curr_gold_2 = 0
    #     self.gold_income_2 = 0
    #     self.gold_outcome_2 = 0

    #     self.isPlay = True

    #     self.spawn_point_height = self.path.get_rect().top + self.path.get_rect().height / 7.0

    #     self.FPS = 60
    #     self.box_size = (screen.screen.get_rect().width / 40 , screen.screen.get_rect().height / 20)
    #     self.path_height = screen.screen.get_rect().height - self.path.get_rect().height + 20

    def enter_gameplay(self):
        # if(cur_gameplay_mode != -1 and cur_gameplay_mode != self.play_mode):
        #     self.reset_gameplay()
        self.screen_resize()
        if self.isPlay == False:
            self.SwitchPlayPauseState()
            self.isPlay = 1 - self.isPlay


    def draw_gameplay_ui(self):
        screen.screen.blit(self.bg , (0, 0))
        # screen.screen.blit(self.nexus1.nexus_surface, (5,  screen.screen.get_rect().height - self.path.get_rect().height - self.nexus1.nexus_surface.get_rect().height + self.path.get_rect().height // 3))
        # screen.screen.blit(self.nexus2.nexus_surface, (screen.screen.get_rect().width - 5 - self.nexus2.nexus_surface.get_rect().width,  screen.screen.get_rect().height - self.path.get_rect().height - self.nexus1.nexus_surface.get_rect().height + self.path.get_rect().height // 3)) 
        screen.screen.blit(self.board_1, (-2,  -2))
        if self.play_mode == 2:
            screen.screen.blit(self.board_2, (screen.screen.get_rect().width + 2 - self.board_2.get_rect().width,  -2))
        screen.screen.blit(self.timer_text1, self.timer_text1_rect)
        if self.play_mode == 2:
            screen.screen.blit(self.timer_text2, self.timer_text2_rect)
        screen.screen.blit(self.gold_text1, self.gold_text1_rect)
        if self.play_mode == 2:
            screen.screen.blit(self.gold_text2, self.gold_text2_rect)
        # screen.screen.blit(self.settings_button, self.play_pause_button)
        if self.isPlay == True:
            screen.screen.blit(self.pause_button, self.play_pause_button)
        else: 
            screen.screen.blit(self.play_button, self.play_pause_button)


        self.gameplay_ui.update()

    def draw_pause_pannel(self):
        self.set_fade()
        self.Pause_Pannel.update()

    def character_level_up(self, character_num, side):
        if side == 1:
            if self.character_level1[character_num - 1] < self.character_level_max[character_num - 1]:
                self.character_level1[character_num - 1] += 1
                return True
            else:
                return False
        else:
            if self.character_level2[character_num - 1] < self.character_level_max[character_num - 1]:
                self.character_level2[character_num - 1] += 1
                return True
            else:
                return False

    def level_up(self, side):
        # self.update()
        if side == 1:
            if self.curr_gold_1 >= self.level_up_cost[self.curr_level1 - 1]:
                self.gold_outcome_1 += self.level_up_cost[self.curr_level1 - 1]
                self.curr_level1 += 1
                self.islevel_up1 = True
        else:
            if self.curr_gold_2 >= self.level_up_cost[self.curr_level2 - 1]:
                self.gold_outcome_2 += self.level_up_cost[self.curr_level2 - 1]
                self.curr_level2 += 1
                self.islevel_up2 = True

    def update(self): #update cac thong so cua game, chay theo tung frame cua gameplay_loop
        #timer process
        if self.isPlay == True:
            self.curr_time = self.time - self.start_time - self.pause_time
        curr_tmp_min = int(self.curr_time/60.0)
        curr_tmp_sec = int(self.curr_time - curr_tmp_min * 60)
        if curr_tmp_min < 10:
            curr_min = '0' + str(curr_tmp_min)
        else:
            curr_min = str(curr_tmp_min)
        if curr_tmp_sec < 10:
            curr_sec = '0' + str(curr_tmp_sec)
        else:
            curr_sec = str(curr_tmp_sec)

            #gold process
        self.curr_gold_1 = int(curr_tmp_min * 60 + curr_tmp_sec) * self.gold_per_sec + self.gold_income_1 - self.gold_outcome_1 #luong vang hien tai = luong vang theo thoi gian + luong vang kiem duoc - luong vang da tieu
        self.curr_gold_2 = int(curr_tmp_min * 60 + curr_tmp_sec) * self.gold_per_sec + self.gold_income_2 - self.gold_outcome_2 #luong vang hien tai = luong vang theo thoi gian + luong vang kiem duoc - luong vang da tieu
        
        self.timer_text1 = self.timer_font.render(curr_min + ':' + curr_sec, True, Black)
        self.timer_text1_rect = self.timer_text1.get_rect()
        self.timer_text1_rect.center = (self.board_1.get_rect().width // 2, self.board_1.get_rect().height // 3 * 2)
        self.timer_text2 = self.timer_font.render(curr_min + ':' + curr_sec, True, Black)
        self.timer_text2_rect = self.timer_text2.get_rect()
        self.timer_text2_rect.center = (screen.screen.get_rect().width - self.board_2.get_rect().width // 2, self.board_2.get_rect().height // 3 * 2)

        self.gold_text1 = self.gold_font.render(str(self.curr_gold_1), True, Yellow)
        self.gold_text1_rect = self.gold_text1.get_rect()
        self.gold_text1_rect.center = (self.board_1.get_rect().width // 2, self.board_1.get_rect().height // 3)
        self.gold_text2 = self.gold_font.render(str(self.curr_gold_2), True, Yellow)
        self.gold_text2_rect = self.gold_text2.get_rect()
        self.gold_text2_rect.center = (screen.screen.get_rect().width - self.board_2.get_rect().width // 2, self.board_2.get_rect().height // 3)

        player1_gameover = self.nexus1.check_gameover()
        player2_gameover = self.nexus2.check_gameover()
        if player1_gameover and player2_gameover:
            self.isGameover = True
            self.Gameover_status = 0 #hoa`
            if self.isPlay == True:
                self.SwitchPlayPauseState()
                self.isPlay = 1 - self.isPlay
        elif player1_gameover:
            self.isGameover = True
            self.Gameover_status = 1 #player 1 thua
            if self.isPlay == True:
                self.SwitchPlayPauseState()
                self.isPlay = 1 - self.isPlay
        elif player2_gameover:
            self.isGameover = True
            self.Gameover_status = 2 #player 2 thua
            if self.isPlay == True:
                self.SwitchPlayPauseState()
                self.isPlay = 1 - self.isPlay

    def draw_gameover_panel(self):
        self.set_fade()
        self.Gameover_panel.update()

    def draw_character_panel(self, mouse_position):
        if self.selected_object == None:
            draw_panel = False
            (a,b) = mouse_position
            selected_list = []
            distance_list = []
            for object in self.side1 + self.side2 :
                if not object.index == 0:
                    distance = math.sqrt((a - object.box.centerx) ** 2 + (b - object.box.centery) ** 2)
                    if distance < self.box_size[1] * 4:
                        character_outline_box = pygame.Rect(0,0,self.box_size[0], self.box_size[1])
                        character_outline_box.center = object.box.center
                        if character_outline_box.top < b and b < character_outline_box.bottom and character_outline_box.left < a and a < character_outline_box.right :
                            selected_list.append(object)
                            distance_list.append(distance)
                            draw_panel = True
                            screen.screen.blit(pygame.transform.smoothscale(pygame.image.load("GameplayAssets\character_box.png"), self.box_size) , character_outline_box)
                        else:
                            pygame.draw.rect(screen.screen, White, character_outline_box, 1, 10)
            if draw_panel:              
                selected_distance = max(distance_list)
                selected_object = selected_list[list_find(distance_list, selected_distance)]

                object = selected_object
                if self.right_click == True:
                    self.selected_object = object

        else:
            if self.selected_object.alive == True:
                object = self.selected_object
                draw_panel = True
                if self.right_click == True:
                    character_outline_box = pygame.Rect(0,0,self.box_size[0], self.box_size[1])
                    character_outline_box.center = object.box.center
                    (a,b) = mouse_position
                    if not (character_outline_box.top < b and b < character_outline_box.bottom and character_outline_box.left < a and a < character_outline_box.right) :
                        draw_panel = False
                        self.selected_object = None
            elif self.selected_object.alive == False:
                self.selected_object = None
                draw_panel = False

        if draw_panel:

            panel_center = (object.box.centerx, object.box.centery - self.box_size[1] * 4)
            panel_width = self.box_size[0] * 15

            scale = panel_width / 600

            panel = pygame.Rect(0,0,panel_width,panel_width /2)
            panel.center = panel_center
            boder = 20 * scale
            board = pygame.Rect(0,0,panel.width - boder * 2, panel.height - boder * 2)
            board.center = panel_center

            character_box = pygame.Rect(0 , 0 , 155 * scale , 235 * scale)
            character_box.center = board.center
            character_blit_box = pygame.Rect(0, 0 , 114 * scale , 197 * scale)
            character_blit_box.center = board.center

            pygame.draw.rect(screen.screen,Gray, panel, border_radius = 10)
            pygame.draw.rect(screen.screen,Black, board,border_radius = 10) 

            img = object.animation_player.img_lib[object.animation_player.clock.Return - 1].img
            imgbox = get_spawn_imgbox( object, character_blit_box)
            img = pygame.transform.smoothscale(img, (imgbox.width, imgbox.height))
            img_area = (board.left - imgbox.left, board.top - imgbox.top, board.width, board.height)
            screen.screen.blit(img, board.topleft, img_area)

            def class_display(class_name):
                tmp = pygame.font.Font('Fonts\\AznKnucklesTrial-z85pa.otf', int(31 * scale)).render(class_name,True,White) #co chu phair ngi=uyennnnnn
                screen.screen.blit(tmp, ((board.left + character_box.left) / 2.0 - tmp.get_width() / 2.0, character_box.top))

            def text_display(text, font_size, topleft, color):
                tmp = pygame.font.Font('Fonts\\AznKnucklesTrial-z85pa.otf', font_size).render(text,True,color) #co chu phair ngi=uyennnnnn
                screen.screen.blit(tmp, topleft)
            def bar_display(data1,data2, center, color):
                hcn1 = pygame.Rect(0,0,167 * scale,11 * scale)
                hcn2 = pygame.Rect(0,0,167 * scale - 2, 11 * scale - 2)
                hcn1.center = hcn2.center = center
                pygame.draw.rect(screen.screen, Gray, hcn1,border_radius = 12)
                if data1 < 0:
                    data1 = 0
                elif data1 >=  data2:
                        data1 = data2

                hcn3 = pygame.Rect(0,0,hcn2.width * data1 / data2, 11 - 2 * 1)
                hcn3.topleft = hcn2.topleft
                pygame.draw.rect(screen.screen, Black, hcn2,border_radius = 12)
                pygame.draw.rect(screen.screen, color, hcn3, border_top_left_radius = 12, border_bottom_left_radius = 12)


            class_display(object.name)
            text_display("Bacsic statics :", int(16 * scale), (panel.left + 35 * scale ,panel.top + 72 * scale), White)

            text_display("Health : {} / {}".format(round(object.health, 2), object.health_max), int(14 * scale), (panel.left + 35 * scale ,panel.top + 93 * scale), White)
            if object.health >= 50:
                bar_display(object.health,object.health_max,(panel.left + 117 * scale ,panel.top + 121 * scale), Green)
            else:
                bar_display(object.health,object.health_max,(panel.left + 117 * scale ,panel.top + 121 * scale), Red)

            text_display("Mana : {} / {}".format(object.mana, object.mana_max), int(14 * scale), (panel.left + 35 * scale ,panel.top + 138 * scale), White)
            bar_display(object.mana,object.mana_max, (panel.left + 117 * scale ,panel.top + (121 + 45) * scale), Blue)

            text_display("Damage : {} / 100".format(object.attack_damage), int(14 * scale), (panel.left + 35 * scale ,panel.top + (93 + 45 * 2) * scale), White)
            bar_display(object.attack_damage,100, (panel.left + 117 * scale ,panel.top + (121 + 45 * 2) * scale), Yellow)

            text_display("Attack speed : {} sec per attack".format(round(1 / object.attack_speed, 2)), int(14 * scale), (panel.left + 35 * scale ,panel.top + (93 + 45 * 3) * scale), White)
            if object.attack_coundowner.counter == None:
                bar_display(1,1, (panel.left + 117 * scale ,panel.top + (121 + 45 * 3) * scale), Silver)
            else:
                bar_display(object.attack_coundowner.counter - self.curr_time,1 / object.attack_speed, (panel.left + 117 * scale ,panel.top + (121 + 45 * 3) * scale), Silver)

            text_display("Level : {}".format(object.level),int(18 * scale), (panel.left + 394 * scale, character_box.top), White)
            
            text_display("Status :",   int(18 * scale), (panel.left + 394 * scale ,panel.top + 72 * scale), White)
            color = White
            if object.special_status or object.status == 4:
                text = "Special"
                color = Red_Orange
            elif object.status == 1:
                text = "Attacking"
                color = Red
            elif object.status == 2 or object.status == 5 :
                ispass = False
                for effect in object.effect_list:
                    if effect.__class__ == dizzy:
                        text = "Soul_sucking"
                        ispass = True
                        color = Purple
                        break

                    elif effect.__class__ == soul_sucking:
                        text = "Stunning"
                        ispass = True
                        color = Purple
                        break
                if not ispass:
                    text = "Standing"
            elif object.status ==  6 or object.status == 5.5:
                text = "Defending"    
            elif object.status == 3:
                text = "Moving"
            elif object.status == -1:
                text = "Knock back"
                color = Purple
            elif object.status == -2:
                text = "On Air"
                color = Purple
            elif object.status == -3:
                text = "Falling"
                color = Purple
            text_display(text, int(16 * scale), (panel.left + 435 * scale,panel.top + 112 * scale), color) 

            text_display("Effect :",   int(18 * scale), (panel.left + 394 * scale,panel.top + 158 * scale), White)
            checked_effect_list = []
            for effect in object.effect_list:
                if list_find(checked_effect_list, effect.__class__) == -1:
                    checked_effect_list.append(effect.__class__)
                    if effect.__class__ == dizzy:
                        text = "Dizzy"
                        color = Purple
                    elif effect.__class__ == soul_sucking:
                        text = "Soul Sucking"
                        color = Purple
                    elif effect.__class__ == knock_back:
                        text = "Knock Back"               
                        color = Purple
                    elif effect.__class__ == flying:
                        text = "Flying"
                        color = Purple
                    elif effect.__class__ == falling:
                        text = "Falling"
                        color = Purple
                    elif effect.__class__ == iron_body:
                        text = "Iron Body"
                        color = Yellow
                    elif effect.__class__ == heal:
                        text = "Heal"
                        color = Green
                    elif effect.__class__ == shield:
                        text = " shield"
                        color = Gray
                    text_display(text,int(16 * scale),(panel.left + 435 *  scale ,panel.top + (177 + 20 * len(checked_effect_list) )* scale), color)
                
            


    def object_operation(self):
        self.bg.blit(self.fake_bg, (0,0))
        self.bg.blit(self.path, (0, screen.screen.get_rect().height - self.path.get_rect().height))
        self.nexus1.operation()
        self.nexus2.operation()
        def operation(object):
            if not  object.__class__ == self.nexusclass:
                object.operation()
        list_browser(self.side1 , operation)
        list_browser(self.side2 , operation)
        list_browser(self.side0 + self.side3 , operation)


class Save_game(): #day la ester egg cua game
    def __init__(self, gameplay):
        self.gameplay = gameplay
