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
import random

class gameplay():
    def __init__(self, play_mode):
        pygame.init()

        self.play_mode = play_mode #1 la player vs computer, 2 la pvp

        self.spawn_time = 2 #thoi gian de spawn mot con nhan vat tinh theo s
        self.spawn_queue1 = []
        self.spawn_queue2 = []

        path_num = random.randint(1, 5)
        # print(path_num)
        self.fake_bg_original = pygame.image.load('GameplayAssets\\bg1.png')
        self.bg_original = pygame.image.load('GameplayAssets\\bg1.png')
        self.path_original = pygame.image.load('GameplayAssets\\path' + str(path_num) + '.png')
        self.board_original = pygame.image.load('GameplayAssets\\board.png')
        self.settings_button_original = pygame.image.load('GameplayAssets\\settings_button.png')
        self.play_button_original = pygame.image.load('GameplayAssets\\play_button.png')
        self.pause_button_original = pygame.image.load('GameplayAssets\\pause_button.png')
        
        self.character_cost = {
            sword_manclass : 10,
            archerclass : 20,
            tankerclass : 30,
            wizardclass : 50,
            gokuclass : 100,
            narutoclass : 150
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

        #level
        self.islevel_up1 = False
        self.islevel_up2 = False
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

        self.box_size = (screen.screen.get_rect().width / 60 , screen.screen.get_rect().height / 20)
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

        # spawn(narutoclass, 1, 20, self)
        # spawn(tankerclass, 2, 36, self)
        # spawn(tankerclass, 2, 37, self)
        # spawn(tankerclass, 2, 38, self)
        # spawn(tankerclass, 2, 39, self)
        # spawn(tankerclass, 2, 40, self)



    def side(self, side):
        if side == 1:
            return self.side1
        elif side == -1 :
            return self.side2

    def load_all_gameplay_image(self):
        self.fake_bg = self.fake_bg_original.copy()
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
 

        self.box_size = (screen.screen.get_rect().width / 60 , screen.screen.get_rect().height / 20)
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
        if side == 1:
            self.curr_level1 += 1
            self.islevel_up1 = True
        else:
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
        self.curr_gold_1 = int(curr_tmp_min * 60 + curr_tmp_sec) * 50 + self.gold_income_1 - self.gold_outcome_1 #luong vang hien tai = luong vang theo thoi gian + luong vang kiem duoc - luong vang da tieu
        self.curr_gold_2 = int(curr_tmp_min * 60 + curr_tmp_sec) * 50 + self.gold_income_2 - self.gold_outcome_2 #luong vang hien tai = luong vang theo thoi gian + luong vang kiem duoc - luong vang da tieu
        
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

    def object_operation(self):
        self.bg.blit(self.fake_bg, (0,0))
        self.bg.blit(self.path, (0, screen.screen.get_rect().height - self.path.get_rect().height))
        for object in self.side2 + self.side1 :
            object.operation()
        list_operation(self.side0)
        for object in self.side3 :
            object.operation()




class Save_game(): #day la ester egg cua game
    def __init__(self, gameplay):
        self.gameplay = gameplay
