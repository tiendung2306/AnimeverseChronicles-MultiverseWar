import pygame 
from pygame.locals import *
from clock import*
from list_function import *
from color import *
from switch import *
from img_analyze import *
from animation_player import *

pygame.init()

WIN = pygame.display.set_mode((1000,1000))
# hcn = pygame.Rect(100,100,100,200)
img = pygame.image.load("GameplayAssets\\tanker2(1).png")

flag = 1
counter = 100
while flag:
    flag += 1
    WIN.fill(Black)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            flag = False
    if flag % 7 == 0 :
        counter -= 1
    if counter == 63 :
        counter = 0
    # print(counter)
    WIN.blit(img,(100,100))
    pygame.display.update()
    img_rect = img.get_rect()
    print(img_rect.top)



