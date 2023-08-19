import pygame 
from pygame.locals import *
from clock import*
from list_function import *

a = N_ValueReturn_repeated_clock(60,3,3)

flag = True
while True:
    pygame.time.Clock().tick(60)     
    a.start()
    a.operation()
    print(a.Return,a.counter)