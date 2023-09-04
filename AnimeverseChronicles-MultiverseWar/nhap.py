import pygame 
from pygame.locals import *
# from clock import*
# from list_function import *
from color import *
# from switch import *
from img_analyze import *
# from animation_player import *
# from collide_checker import*

pygame.init()

WIN = pygame.display.set_mode((1000,1000))


anh = pygame.image.load("GameplayAssets\\tanker(1).png")
angle = 0

flag = 1
while flag:
    flag += 1
    # pygame.draw.rect(WIN, Yellow, hcn)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            flag = False
    tmp = pygame.transform.rotate(anh, angle)
    # pygame.draw.rect(WIN, Red ,tmp.get_rect())
    WIN.blit(tmp,(0,0))
    angle += 1


    pygame.display.update()

