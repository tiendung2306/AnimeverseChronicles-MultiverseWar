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


# WIN = pygame.display.set_mode((1000,1000))

# time_gap = 100
# direct = True
# while direct:
#     b = time.time()
#     WIN.fill(White)
#     WIN.blit(img_iib[flag], (0,0))
#     (a,b) = pygame.mouse.get_pos()
#     pygame.time.wait(time_gap)
#     if flag == len(img_iib) - 1:
#         flag = 0
#     else:
#          flag += 1
#     for event in pygame.event.get():
#         if event.type == KEYDOWN:
#                 direct = False
#                 print(((len(img_iib) - 1) * time_gap / 1000))

#         if event.type == MOUSEWHEEL:
#             if event.y > 0:
#                   time_gap += 10
#             elif event.y < 0:
#                  time_gap -= 10
#     pygame.display.update()

class another_randomshit():
    def __init__(self):
        self.x = 1


class randomshit():
    def __init__(self,another_randomshit):
        self.y = 1

a = another_randomshit()
b = randomshit(a)
c = randomshit(a)
print(b,c)
list = [b, c]
list2 = list
list.remove(b)
print(list[0],list2[0])
print(list,list2)
# if b == c:
#     print("nahhhhhh")