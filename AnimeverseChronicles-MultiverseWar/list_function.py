import random
import pygame 
from pygame.locals import *
from clock import*

def list_find(list,object):
    if not (len(list) == 0):
        for i in list:
            if i == object:
                return list.index(i)
        return -1
    else:
        return -1
    

def list_find_special(list, object,):
    if not (len(list) == 0):
        for i in list:
            if i.object == object:
                return True
        return False
    else:
        return False
