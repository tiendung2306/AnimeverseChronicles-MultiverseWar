import pygame
from pygame.locals import *
from color import *
from archer import *
from straw_doll import *
from sword_man import *
from tanker import *
from nexus import *
from pause_pannel import *
from states import *

class gameplay():
    def __init__(self):
        pygame.init()

        self.FPS = 60
        self.screen = pygame.display.get_surface()

        self.bg_original = pygame.image.load('GameplayAssets\\bg1.jpg')
        self.path_original = pygame.image.load('GameplayAssets\\path1.png')
        self.board_original = pygame.image.load('GameplayAssets\\board.png')
        self.settings_button_original = pygame.image.load('GameplayAssets\\settings_button.png')
        self.play_button_original = pygame.image.load('GameplayAssets\\play_button.png')
        self.pause_button_original = pygame.image.load('GameplayAssets\\pause_button.png')

        self.load_all_gameplay_image()
        self.nexus1 = Nexus('GameplayAssets\\nexus1.png')
        self.nexus2 = Nexus('GameplayAssets\\nexus2.png')

        self.play_pause_button = (self.screen.get_rect().width - self.pause_button.get_rect().width - 10, 10)

        self.timer_font = pygame.font.Font('Fonts\\joystix_monospace.otf', 16)
        self.start_time = 0.0
        self.curr_time = 0.0
        self.pause_time = 0.0
        self.start_pause_time = 0.0
        self.time = 0.0

        self.gold_font = pygame.font.Font('Fonts\\joystix_monospace.otf', 20)
        self.curr_gold = 0
        self.tmp_gold = 0
        self.prev_gold_time = 0.0

        self.isPlay = True
        self.fade = pygame.Surface((self.screen.get_rect().width, self.screen.get_rect().height))
        self.fade.fill((0,0,0))
        self.fade.set_alpha(200)
        self.Pause_Pannel = pause_pannel()

        self.spawn_point_height = self.path.get_rect().top + self.path.get_rect().height / 7.0

        self.straw_doll1 = straw_doll_class(1000, 560,self)
        self.straw_doll2 = straw_doll_class(800, 560,self)
        self.straw_doll3 = straw_doll_class(600, 560,self)
        # self.tanker = tankerclass(900,560,self)

        self.side2 = []
        self.side2.append(self.straw_doll1)
        self.side2.append(self.straw_doll2)
        self.side2.append(self.straw_doll3)
        # self.side2.append(self.tanker)


        self.archer = archerclass(100, 560,self)
        self.sword_man = sword_manclass(100, 567,self)
        self.side1 = []
        self.side1.append(self.archer)
        self.side1.append(self.sword_man)

    def load_all_gameplay_image(self):
        self.bg = self.bg_original.copy()
        self.path = self.path_original.copy()
        self.board = self.board_original.copy()
        self.settings_button = self.settings_button_original.copy()
        self.play_button = self.play_button_original.copy()
        self.pause_button = self.pause_button_original.copy()

        info = pygame.display.Info()
        self.bg = pygame.transform.smoothscale(self.bg, (info.current_w, info.current_h))
        self.path = pygame.transform.smoothscale(self.path, (self.bg.get_rect().width, self.screen.get_rect().height // 7))
        self.board = pygame.transform.smoothscale(self.board, (self.screen.get_rect().width / 7, self.screen.get_rect().width / 7 / 2.4))
        self.settings_button = pygame.transform.smoothscale(self.settings_button, (self.board.get_rect().width // 6, self.board.get_rect().width // 6))
        self.play_button = pygame.transform.smoothscale(self.play_button, (self.board.get_rect().width // 6, self.board.get_rect().width // 6))
        self.pause_button = pygame.transform.smoothscale(self.pause_button, (self.board.get_rect().width // 6, self.board.get_rect().width // 6))

        self.spawn_point_height = self.path.get_rect().top + self.path.get_rect().height / 7.0

    def screen_resize(self):
        self.Pause_Pannel.screen_resize()
        self.fade = pygame.Surface((self.screen.get_rect().width, self.screen.get_rect().height))
        self.fade.fill((0,0,0))
        self.fade.set_alpha(200)

        self.load_all_gameplay_image()
        self.nexus1.screen_resize('GameplayAssets\\nexus1.png')
        self.nexus2.screen_resize('GameplayAssets\\nexus2.png')

    def set_fade(self): 
        self.screen.blit(self.fade, (0,0))

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
            self.tmp_gold = self.curr_gold

            self.start_pause_time = self.time
        else:
            self.pause_time = self.pause_time + self.time - self.start_pause_time

    def enter_gameplay(self):
        self.screen_resize()
        if self.isPlay == False:
            self.SwitchPlayPauseState()
            self.isPlay = 1 - self.isPlay



    def draw_gameplay_ui(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.path, (0, self.screen.get_rect().height - self.path.get_rect().height))
        self.screen.blit(self.nexus1.nexus_surface, (5,  self.screen.get_rect().height - self.path.get_rect().height - self.nexus1.nexus_surface.get_rect().height + self.path.get_rect().height // 3))
        self.screen.blit(self.nexus2.nexus_surface, (self.screen.get_rect().width - 5 - self.nexus2.nexus_surface.get_rect().width,  self.screen.get_rect().height - self.path.get_rect().height - self.nexus1.nexus_surface.get_rect().height + self.path.get_rect().height // 3)) 
        self.screen.blit(self.board, (-2,  -2))
        self.screen.blit(self.timer_text, self.timer_text_rect)
        self.screen.blit(self.gold_text, self.gold_text_rect)
        self.screen.blit(self.settings_button, self.play_pause_button)
            
        # else:
        #     self.screen.blit(self.play_button, self.play_pause_button)

    def draw_pause_pannel(self):
        self.set_fade()
        self.Pause_Pannel.update()

    def update(self):
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
        if self.curr_time - self.prev_gold_time >= 0.9965:
            self.curr_gold += 10
            self.prev_gold_time = self.curr_time
        if self.isPlay == False:
            self.curr_gold = self.tmp_gold
        
        self.timer_text = self.timer_font.render(curr_min + ':' + curr_sec, True, Black)
        self.timer_text_rect = self.timer_text.get_rect()
        self.timer_text_rect.center = (self.board.get_rect().width // 2, self.board.get_rect().height // 3 * 2)

        self.gold_text = self.gold_font.render(str(self.curr_gold), True, Yellow)
        self.gold_text_rect = self.gold_text.get_rect()
        self.gold_text_rect.center = (self.board.get_rect().width // 2, self.board.get_rect().height // 3)






        
