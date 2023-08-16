import pygame
import time
from pygame.locals import *
from color import *

class gameplay():
    def __init__(self):
        pygame.init()
        self.bg = pygame.image.load('GameplayAssets\\bg0.jpg')
        self.nexus1 = pygame.image.load('GameplayAssets\\nexus1.png')
        self.nexus2 = pygame.image.load('GameplayAssets\\nexus2.png')
        self.board = pygame.image.load('GameplayAssets\\board.png')
        self.timer_font = pygame.font.Font('Fonts\\joystix_monospace.otf', 16)
        self.start_time = time.time()
        self.gold_font = pygame.font.Font('Fonts\\joystix_monospace.otf', 20)
        self.curr_gold = 0
        self.gold_count_time = time.time()
    
    def update(self):
        info = pygame.display.Info()
        self.bg = pygame.transform.smoothscale(self.bg, (info.current_w, info.current_h))
        pre_nexus_height = self.nexus1.get_rect().height
        pre_nexus_width = self.nexus1.get_rect().width
        new_nexus_width = info.current_w//10
        self.nexus1 = pygame.transform.smoothscale(self.nexus1, (new_nexus_width, new_nexus_width / pre_nexus_width * pre_nexus_height))
        self.nexus2 = pygame.transform.smoothscale(self.nexus2, (new_nexus_width, new_nexus_width / pre_nexus_width * pre_nexus_height))
        self.board = pygame.transform.smoothscale(self.board, (240, 100))

        if time.time() - self.gold_count_time > 1:
            self.curr_gold += 10
            self.gold_count_time = time.time()
        self.gold_text = self.gold_font.render(str(self.curr_gold), True, Yellow)
        self.gold_text_rect = self.gold_text.get_rect()
        self.gold_text_rect.center = (self.board.get_rect().width // 2, self.board.get_rect().height // 3)

        curr_time = time.time() - self.start_time
        curr_tmp_min = int(curr_time//60)
        curr_tmp_sec = int(curr_time - (curr_time//60) * 60)
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

        
