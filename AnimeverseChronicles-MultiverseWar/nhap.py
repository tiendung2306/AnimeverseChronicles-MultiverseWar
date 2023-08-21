import pygame 
from pygame.locals import *
from clock import*
from list_function import *
from color import *
from switch import *
from img_analyze import *

pygame.init()

hcn = pygame.Rect(100,100,100,100)
hcn2 = arrow1.imgbox_to_hitbox(hcn)
WIN = pygame.display.set_mode((1000,1000))
Flag = True
while Flag:
    # WIN.fill(Black)
    # WIN.blit(anh_sau_scale,img_box)
    # pygame.draw.rect(WIN,White,hcn2,5)

    # pygame.draw.rect(WIN,White,img_box,5)
    # pygame.draw.rect(WIN,White,hcn,5)
    # WIN.blit(arrow1.img,hcn2)
    # WIN.blit(pygame.transform.smoothscale(archer1_3.img,(hcn.width,hcn.height)),hcn)
    pygame.draw.rect(WIN,Yellow,hcn,4)
    pygame.draw.rect(WIN,Red,hcn2,4)


    for event in pygame.event.get():
        if event.type == KEYDOWN:
            Flag = False

    pygame.display.update()



