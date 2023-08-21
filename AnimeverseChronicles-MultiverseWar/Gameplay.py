import pygame
import time
from pygame.locals import *
from color import *
from object_manager import * 
from nexus import *

class gameplay():
    def __init__(self):
        pygame.init()


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
        self.tmp_time = 0.0
        self.pause_time = 0.0
        self.start_pause_time = 0.0
        self.time = 0.0

        self.gold_font = pygame.font.Font('Fonts\\joystix_monospace.otf', 20)
        self.curr_gold = 0
        self.tmp_gold = 0
        self.prev_gold_time = 0.0

        self.isPlay = True

        self.FPS = 60
        self.box_size = (self.screen.get_rect().width / 20 , self.screen.get_rect().height / 10)
        self.path_height = self.screen.get_rect().height - self.path.get_rect().height + 20
    #Object import:
        self.side1 = []
        self.side2 = []
        self.side3 = []

        # spawn(straw_doll,2,8,self)
        # spawn(archer,1,1,self)
        spawn(sword_man,1,5,self)
        spawn(tanker,1,3,self)

        # spawn(archer,2,15,self)
        # spawn(sword_man,2,14,self)

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

    def screen_resize(self):
        self.load_all_gameplay_image()
        self.nexus1.screen_resize('GameplayAssets\\nexus1.png')
        self.nexus2.screen_resize('GameplayAssets\\nexus2.png')

    def check_click(self, play_pause_button, mouse):
        if play_pause_button[0] <= mouse[0] <= play_pause_button[0] + self.pause_button.get_rect().width and play_pause_button[1] <= mouse[1] <= play_pause_button[1] + self.pause_button.get_rect().height:
            self.SwitchPlayPauseState()
            self.isPlay = 1 - self.isPlay
            return

    def SwitchPlayPauseState(self):
        if self.isPlay == True:
            self.tmp_gold = self.curr_gold

            self.tmp_time = self.curr_time
            self.start_pause_time = self.time
        else:
            self.pause_time += self.time - self.start_pause_time

    def draw_gameplay_ui(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.path, (0, self.screen.get_rect().height - self.path.get_rect().height))
        self.screen.blit(self.nexus1.nexus_surface, (5,  self.screen.get_rect().height - self.path.get_rect().height - self.nexus1.nexus_surface.get_rect().height + self.path.get_rect().height // 3))
        self.screen.blit(self.nexus2.nexus_surface, (self.screen.get_rect().width - 5 - self.nexus2.nexus_surface.get_rect().width,  self.screen.get_rect().height - self.path.get_rect().height - self.nexus1.nexus_surface.get_rect().height + self.path.get_rect().height // 3)) 
        self.screen.blit(self.board, (-2,  -2))
        self.screen.blit(self.timer_text, self.timer_text_rect)
        self.screen.blit(self.gold_text, self.gold_text_rect)
        self.screen.blit(self.settings_button, self.play_pause_button)
        # if self.isPlay == True:
        #     self.screen.blit(self.pause_button, self.play_pause_button)
        # else:
        #     self.screen.blit(self.play_button, self.play_pause_button)

    def update(self):
        #timer process
        if self.isPlay == False:
            self.curr_time = self.tmp_time
        else:
            self.curr_time = self.time - self.start_time - self.pause_time
        curr_tmp_min = int(self.curr_time//60)
        curr_tmp_sec = int(self.curr_time - curr_tmp_min * 60)
        if curr_tmp_min < 10:
            curr_min = '0' + str(curr_tmp_min)
        else:
            curr_min = str(curr_tmp_min)
        if curr_tmp_sec < 10:
            curr_sec = '0' + str(curr_tmp_sec)
        else:
            curr_sec = str(curr_tmp_sec)
        self.timer_text = self.timer_font.render(curr_min + ':' + curr_sec, True, Black)
        self.timer_text_rect = self.timer_text.get_rect()
        self.timer_text_rect.center = (self.board.get_rect().width // 2, self.board.get_rect().height // 3 * 2)

        #gold process
        if self.curr_time - self.prev_gold_time >= 0.999:
            self.curr_gold += 10
            self.prev_gold_time = self.curr_time
        if self.isPlay == False:
            self.curr_gold = self.tmp_gold
        self.gold_text = self.gold_font.render(str(self.curr_gold), True, Yellow)
        self.gold_text_rect = self.gold_text.get_rect()
        self.gold_text_rect.center = (self.board.get_rect().width // 2, self.board.get_rect().height // 3)

    def object_operation(self):
        for object in self.side1 + self.side2 + self.side3:
            object.operation()




        
