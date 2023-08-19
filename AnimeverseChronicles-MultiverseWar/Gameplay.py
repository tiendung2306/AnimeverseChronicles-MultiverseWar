import pygame
import time
from pygame.locals import *
from color import *
from archer import *
from straw_doll import *
from sword_man import *
from tanker import *

class gameplay():
    def __init__(self,screen):
        pygame.init()

        self.FPS = 120
        self.screen = screen

        self.bg = pygame.image.load('GameplayAssets\\bg0.png')
        self.path = pygame.image.load('GameplayAssets\\path1.png')
        self.nexus1 = pygame.image.load('GameplayAssets\\nexus1.png')
        self.nexus2 = pygame.image.load('GameplayAssets\\nexus2.png')
        self.board = pygame.image.load('GameplayAssets\\board.png')

        self.timer_font = pygame.font.Font('Fonts\\joystix_monospace.otf', 16)
        self.start_time = time.time()
        self.curr_time = 0
        self.tmp_time = 0
        self.pause_time = 0
        self.start_pause_time = 0

        self.gold_font = pygame.font.Font('Fonts\\joystix_monospace.otf', 20)
        self.curr_gold = 0
        self.tmp_gold = 0
        self.prev_gold_time = 0

        self.play_button = pygame.image.load('GameplayAssets\\play_button.png')
        self.pause_button = pygame.image.load('GameplayAssets\\pause_button.png')
        self.isPlay = True

        # self.straw_doll = straw_doll_class(1000, 560,self)
        # self.straw_doll2 = straw_doll_class(800, 560,self)
        # self.straw_doll3 = straw_doll_class(600, 560,self)
        self.tanker = tankerclass(900,560,self)

        self.side2 = []
        # self.side2.append(self.straw_doll)
        # self.side2.append(self.straw_doll2)
        # self.side2.append(self.straw_doll3)
        self.side2.append(self.tanker)


        self.archer = archerclass(100, 560,self)
        self.sword_man = sword_manclass(100, 567,self)
        self.side1 = []
        self.side1.append(self.archer)
        self.side1.append(self.sword_man)


    def screen_resize(self):
        self.bg = pygame.image.load('GameplayAssets\\bg1.jpg')
        self.path = pygame.image.load('GameplayAssets\\path1.png')
        self.nexus1 = pygame.image.load('GameplayAssets\\nexus1.png')
        self.nexus2 = pygame.image.load('GameplayAssets\\nexus2.png')
        self.board = pygame.image.load('GameplayAssets\\board.png')
        self.play_button = pygame.image.load('GameplayAssets\\play_button.png')
        self.pause_button = pygame.image.load('GameplayAssets\\pause_button.png')

    def SwitchPlayPauseState(self):
        if self.isPlay == True:
            self.tmp_gold = self.curr_gold

            self.tmp_time = self.curr_time
            self.start_pause_time = time.time()
        else:
            self.pause_time += time.time() - self.start_pause_time

    def update(self):
        info = pygame.display.Info()
        self.bg = pygame.transform.smoothscale(self.bg, (info.current_w, info.current_h))
        self.path = pygame.transform.smoothscale(self.path, (self.bg.get_rect().width, self.screen.get_rect().height // 7))
        pre_nexus_height = self.nexus1.get_rect().height
        pre_nexus_width = self.nexus1.get_rect().width
        new_nexus_width = info.current_w//10
        self.nexus1 = pygame.transform.smoothscale(self.nexus1, (new_nexus_width, new_nexus_width / pre_nexus_width * pre_nexus_height))
        self.nexus2 = pygame.transform.smoothscale(self.nexus2, (new_nexus_width, new_nexus_width / pre_nexus_width * pre_nexus_height))
        self.board = pygame.transform.smoothscale(self.board, (self.screen.get_rect().width / 7, self.screen.get_rect().width / 7 / 2.4))
        self.play_button = pygame.transform.smoothscale(self.play_button, (self.board.get_rect().width // 6, self.board.get_rect().width // 6))
        self.pause_button = pygame.transform.smoothscale(self.pause_button, (self.board.get_rect().width // 6, self.board.get_rect().width // 6))

        if self.isPlay == False:
            self.curr_time = self.tmp_time
        else:
            self.curr_time = time.time() - self.start_time - self.pause_time
        curr_tmp_min = int(self.curr_time//60)
        curr_tmp_sec = int(self.curr_time - (self.curr_time//60) * 60)
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

        if self.curr_time - self.prev_gold_time >= 1:
            self.curr_gold += 10
            self.prev_gold_time = self.curr_time
        if self.isPlay == False:
            self.curr_gold = self.tmp_gold
        self.gold_text = self.gold_font.render(str(self.curr_gold), True, Yellow)
        self.gold_text_rect = self.gold_text.get_rect()
        self.gold_text_rect.center = (self.board.get_rect().width // 2, self.board.get_rect().height // 3)






        
