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
# hcn = pygame.Rect(100,100,100,200)
img = pygame.image.load("GameplayAssets\\tanker2(1).png")
img.get_size()[0]

class oc ():
    def __init__(self):
        self.box = None
a = oc()
b = oc()

hcn = pygame.Rect(100,50,50,50)
hcn2 = pygame.Rect(100,0,50,50)
hcn2.width += 100
hcn2.centerx -= 100
flag = 1
counter = 100
while flag:
    flag += 1
    WIN.fill(Black)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            flag = False

    pygame.draw.rect(WIN, Yellow,hcn) 
    pygame.draw.rect(WIN, Blue, hcn2) 


    pygame.display.update()

