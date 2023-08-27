import pygame
from pygame.locals import *
from color import *
from object_manager import * 
from nexus import *
from pause_pannel import *
from states import *
from screen import *

class gameplay():
    def __init__(self):
        pygame.init()

        self.bg_original = pygame.image.load('GameplayAssets\\bg1.jpg')
        self.path_original = pygame.image.load('GameplayAssets\\path1.png')
        self.board_original = pygame.image.load('GameplayAssets\\board.png')
        self.settings_button_original = pygame.image.load('GameplayAssets\\settings_button.png')
        self.play_button_original = pygame.image.load('GameplayAssets\\play_button.png')
        self.pause_button_original = pygame.image.load('GameplayAssets\\pause_button.png')

        self.load_all_gameplay_image()
        self.nexus1 = Nexus('GameplayAssets\\nexus1.png')
        self.nexus2 = Nexus('GameplayAssets\\nexus2.png')

        self.play_pause_button = (screen.screen.get_rect().width - self.pause_button.get_rect().width - 10, 10)

        self.timer_font = pygame.font.Font('Fonts\\joystix_monospace.otf', 16)
        self.start_time = 0.0
        self.curr_time = 0.0
        self.pause_time = 0.0
        self.start_pause_time = 0.0
        self.time = 0.0 # dung giong voi time.time()

        self.gold_font = pygame.font.Font('Fonts\\joystix_monospace.otf', 20)
        self.curr_gold = 0
        self.tmp_gold = 0
        self.gold_income = 0
        self.gold_outcome = 0

        self.isPlay = True
        self.fade = pygame.Surface((screen.screen.get_rect().width, screen.screen.get_rect().height))
        self.fade.fill((0,0,0))
        self.fade.set_alpha(200)
        self.Pause_Pannel = pause_pannel()

        self.spawn_point_height = self.path.get_rect().top + self.path.get_rect().height / 7.0

        self.FPS = 60
        self.box_size = (screen.screen.get_rect().width / 40 , screen.screen.get_rect().height / 20)
        self.path_height = screen.screen.get_rect().height - self.path.get_rect().height + 20
    #Object import:
        self.side1 = []
        self.side2 = []
        self.side3 = []

        spawn(straw_doll,1,3,self)
        spawn(archer,2,9,self)
        spawn(archer,2,8,self)
     
        # spawn(tanker,2,10,self)
        # spawn(archer,2,15,self)
        # spawn(straw_doll,2,8,self)
        # spawn(archer,1,1,self)
        # spawn(tanker,1,2,self)
        # spawn(tanker,1,3,self)
        # spawn(sword_man,1,4,self)

        # spawn(archer,2,15,self)
        # spawn(tanker,2,14,self)
        # spawn(tanker,2,13,self)
        # spawn(sword_man,2,12,self)

    def load_all_gameplay_image(self):
        self.bg = self.bg_original.copy()
        self.path = self.path_original.copy()
        self.board = self.board_original.copy()
        self.settings_button = self.settings_button_original.copy()
        self.play_button = self.play_button_original.copy()
        self.pause_button = self.pause_button_original.copy()

        info = pygame.display.Info()
        self.bg = pygame.transform.smoothscale(self.bg, (info.current_w, info.current_h))
        self.path = pygame.transform.smoothscale(self.path, (self.bg.get_rect().width, screen.screen.get_rect().height // 7))
        self.board = pygame.transform.smoothscale(self.board, (screen.screen.get_rect().width / 7, screen.screen.get_rect().width / 7 / 2.4))
        self.settings_button = pygame.transform.smoothscale(self.settings_button, (self.board.get_rect().width // 6, self.board.get_rect().width // 6))
        self.play_button = pygame.transform.smoothscale(self.play_button, (self.board.get_rect().width // 6, self.board.get_rect().width // 6))
        self.pause_button = pygame.transform.smoothscale(self.pause_button, (self.board.get_rect().width // 6, self.board.get_rect().width // 6))

        self.spawn_point_height = self.path.get_rect().top + self.path.get_rect().height / 7.0

    def screen_resize(self):
        self.Pause_Pannel.screen_resize()
        self.fade = pygame.Surface((screen.screen.get_rect().width, screen.screen.get_rect().height))
        self.fade.fill((0,0,0))
        self.fade.set_alpha(200)

        self.load_all_gameplay_image()
        self.nexus1.screen_resize('GameplayAssets\\nexus1.png')
        self.nexus2.screen_resize('GameplayAssets\\nexus2.png')

    def set_fade(self): 
        screen.screen.blit(self.fade, (0,0))

    def check_click(self, play_pause_button, mouse):
        if self.isPlay == True: #neu game dang chay
            if play_pause_button[0] <= mouse[0] <= play_pause_button[0] + self.pause_button.get_rect().width and play_pause_button[1] <= mouse[1] <= play_pause_button[1] + self.pause_button.get_rect().height:
                self.SwitchPlayPauseState()
                self.isPlay = 1 - self.isPlay
                return 'None'
        else: #neu game dang duoc pause
            if self.Pause_Pannel.check_click(mouse) == self.Pause_Pannel.buttons[0]: #an vao nut continue
                self.SwitchPlayPauseState()
                self.isPlay = 1 - self.isPlay
                return 'None'
            if self.Pause_Pannel.check_click(mouse) == self.Pause_Pannel.buttons[1]: #an vao nut settings
                return 'Settings'
            if self.Pause_Pannel.check_click(mouse) == self.Pause_Pannel.buttons[2]: #an vao nut thoat game
                return 'Back'

    def SwitchPlayPauseState(self):
        if self.isPlay == True:
            self.start_pause_time = self.time
        else:
            self.pause_time = self.pause_time + self.time - self.start_pause_time

    def enter_gameplay(self):
        self.screen_resize()
        if self.isPlay == False:
            self.SwitchPlayPauseState()
            self.isPlay = 1 - self.isPlay



    def draw_gameplay_ui(self):
        screen.screen.blit(self.bg, (0, 0))
        screen.screen.blit(self.path, (0, screen.screen.get_rect().height - self.path.get_rect().height))
        screen.screen.blit(self.nexus1.nexus_surface, (5,  screen.screen.get_rect().height - self.path.get_rect().height - self.nexus1.nexus_surface.get_rect().height + self.path.get_rect().height // 3))
        screen.screen.blit(self.nexus2.nexus_surface, (screen.screen.get_rect().width - 5 - self.nexus2.nexus_surface.get_rect().width,  screen.screen.get_rect().height - self.path.get_rect().height - self.nexus1.nexus_surface.get_rect().height + self.path.get_rect().height // 3)) 
        screen.screen.blit(self.board, (-2,  -2))
        screen.screen.blit(self.timer_text, self.timer_text_rect)
        screen.screen.blit(self.gold_text, self.gold_text_rect)
        screen.screen.blit(self.settings_button, self.play_pause_button)
            
        # else:
        #     screen.screen.blit(self.play_button, self.play_pause_button)

    def draw_pause_pannel(self):
        self.set_fade()
        self.Pause_Pannel.update()

    def update(self): #update cac thong so cua game, chay theo tung frame cua gamplay_loop
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
        self.curr_gold = int(curr_tmp_min * 60 + curr_tmp_sec) * 10 + self.gold_income - self.gold_outcome #luong vang hien tai = luong vang theo thoi gian + luong vang kiem duoc - luong vang da tieu
        
        self.timer_text = self.timer_font.render(curr_min + ':' + curr_sec, True, Black)
        self.timer_text_rect = self.timer_text.get_rect()
        self.timer_text_rect.center = (self.board.get_rect().width // 2, self.board.get_rect().height // 3 * 2)

        self.gold_text = self.gold_font.render(str(self.curr_gold), True, Yellow)
        self.gold_text_rect = self.gold_text.get_rect()
        self.gold_text_rect.center = (self.board.get_rect().width // 2, self.board.get_rect().height // 3)


    def object_operation(self):
        for object in self.side2 + self.side1 + self.side3:
            object.operation()




        
