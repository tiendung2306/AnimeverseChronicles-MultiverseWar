import pygame 
import math
from pygame.locals import *
# from clock import*
# from list_function import *
from color import *
# from switch import *
# from img_analyze import *
# from animation_player import *
# from collide_checker import*
import time

# pygame.init()


# class randomshit():
#     def __init__(self) -> None:
#         self.x = 0
#     def add(self):
#         print("vpa")
    
# a = randomshit()
# b = randomshit()

# c = a
# c.add()

WIN = pygame.display.set_mode((1000,1000))
img_iib = []
for i in range(1,4):
    img = pygame.image.load("GameplayAssets\\breaking_ground({}).png".format(i))
    img_iib.append(img)



flag = 0
time_gap = 100
direct = True
while direct:
    WIN.fill(White)
    WIN.blit(img_iib[flag], (0,0))
    print(flag + 1)
    if flag == len(img_iib) - 1:
        flag = 0
    else:
         flag += 1
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            direct = False
            if time_gap < 20:
                print("error")
            else:
                print(time_gap)
                print(((len(img_iib) - 1) * time_gap / 1000))

        if event.type == MOUSEWHEEL:
            if event.y > 0:
                  time_gap += 10
            elif event.y < 0:
                 time_gap -= 10
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                print(flag + 1)

    pygame.display.update()
    pygame.time.wait(time_gap)

    #att 1 - 19 : 1.26
    #move 62 - 67 : 0.6
    #stan 68 - 70 : 0.58
    #spe 2.88
        #19-27: 0.88
        #

