import pygame 
from pygame.locals import *
from clock import*
from list_function import *
from color import *
from switch import *
from img_analyze import *
from animation_player import *
from collide_checker import*

pygame.init()

WIN = pygame.display.set_mode((1000,1000))

print(WIN.get_rect())

flag = 1
while flag:
    flag += 1
    WIN.fill(Black)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            flag = False


    pygame.display.update()

