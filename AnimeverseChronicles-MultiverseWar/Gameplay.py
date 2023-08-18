import pygame
import time
from pygame.locals import *
from color import *
from archer import *
from nexus import *

class gameplay():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.get_surface()

        self.load_all_gameplay_image()
        self.nexus1 = Nexus('GameplayAssets\\nexus1.png')
        self.nexus2 = Nexus('GameplayAssets\\nexus2.png')

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

        self.straw_doll = pygame.image.load("GameplayAssets\\straw_doll.png")
        self.enemy = self.straw_doll.get_rect(topleft = (900,560))
        self.enemy_list = []
        self.enemy_list.append(self.enemy)
        self.archer = archerclass(100, 560, (100, 170), 2)
        self.archer.gameplay = self

    def load_all_gameplay_image(self):
        self.bg = pygame.image.load('GameplayAssets\\bg1.jpg')
        self.path = pygame.image.load('GameplayAssets\\path1.png')
        self.board = pygame.image.load('GameplayAssets\\board.png')
        self.play_button = pygame.image.load('GameplayAssets\\play_button.png')
        self.pause_button = pygame.image.load('GameplayAssets\\pause_button.png')

        info = pygame.display.Info()
        self.bg = pygame.transform.smoothscale(self.bg, (info.current_w, info.current_h))
        self.path = pygame.transform.smoothscale(self.path, (self.bg.get_rect().width, self.screen.get_rect().height // 7))
        self.board = pygame.transform.smoothscale(self.board, (self.screen.get_rect().width / 7, self.screen.get_rect().width / 7 / 2.4))
        self.play_button = pygame.transform.smoothscale(self.play_button, (self.board.get_rect().width // 6, self.board.get_rect().width // 6))
        self.pause_button = pygame.transform.smoothscale(self.pause_button, (self.board.get_rect().width // 6, self.board.get_rect().width // 6))

    def screen_resize(self):
        self.load_all_gameplay_image()
        self.nexus1.screen_resize('GameplayAssets\\nexus1.png')
        self.nexus2.screen_resize('GameplayAssets\\nexus2.png')

    def SwitchPlayPauseState(self):
        if self.isPlay == True:
            self.tmp_gold = self.curr_gold

            self.tmp_time = self.curr_time
            self.start_pause_time = self.time
        else:
            self.pause_time += self.time - self.start_pause_time

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






        
