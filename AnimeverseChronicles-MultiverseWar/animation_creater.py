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
a = time.time()

WIN = pygame.display.set_mode((1000,1000))
img_iib = []
flag = 0
for i in range(19,28):
    img = pygame.image.load("GameplayAssets\\naruto({}).png".format(i))
    img_iib.append(img)
for i in range(28,35):
    img = pygame.image.load("GameplayAssets\\naruto({}).png".format(i))
    img_iib.append(img)
for j in range(1,8):
    for i in range(75, 78):
        img = pygame.image.load("GameplayAssets\\naruto({}).png".format(i))
        img_iib.append(img)
for i in [35, 78,79,80,81]:
    img = pygame.image.load("GameplayAssets\\naruto({}).png".format(i))
    img_iib.append(img)
for i in range(36,43):
    img = pygame.image.load("GameplayAssets\\naruto({}).png".format(i))
    img_iib.append(img)
for j in range(1,8):
    for i in [43, 82]:
        img = pygame.image.load("GameplayAssets\\naruto({}).png".format(i))
        img_iib.append(img)
for i in range(44,51):
    img = pygame.image.load("GameplayAssets\\naruto({}).png".format(i))
    img_iib.append(img)
# 5.52

# for i in range(1,5):
#     img = pygame.image.load("GameplayAssets\\explosion_stage_1({}).png".format(i))
#     img_iib.append(img)
# for j in range(1,7):
#     for i in range(1,4):
#         img = pygame.image.load("GameplayAssets\\explosion_stage_2({}).png".format(i))
#         img_iib.append(img)

# for i in range(1,3):
#     for j in range(1,2):
#         img = pygame.image.load("GameplayAssets\\explosion_stage_3({}).png".format(i))
#         img_iib.append(img)

#1.61

# for i in [71, 73 ,74]:
#     img = pygame.image.load("GameplayAssets\\naruto({}).png".format(i))
#     img_iib.append(img)

# for i in range(53,57):
#     img = pygame.image.load("GameplayAssets\\naruto({}).png".format(i))
#     img_iib.append(img)
time_gap = 1000
direct = True
while direct:
    b = time.time()
    WIN.fill(White)
    WIN.blit(img_iib[flag], (0,0))
    print(flag + 1)
    (a,b) = pygame.mouse.get_pos()
    pygame.time.wait(time_gap)
    if flag == len(img_iib) - 1:
        flag = 0
    else:
         flag += 1
    for event in pygame.event.get():
        if event.type == KEYDOWN:
                direct = False
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

    #att 1 - 19 : 1.26
    #move 62 - 67 : 0.6
    #stan 68 - 70 : 0.58
    #spe 2.88
        #19-27: 0.88
        #

