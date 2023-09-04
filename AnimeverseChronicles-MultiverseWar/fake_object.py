import random
import pygame 
from pygame.locals import *

class fake_object_class():
    def __init__(self,object):
        self.box = pygame.Rect(object.box.left,object.box.top,object.box.width,object.box.height)
        self.imgbox = pygame.Rect(object.imgbox.left,object.imgbox.top,object.imgbox.width,object.imgbox.height)
        self.status = True

def copy( rect1, rect2 ):
    rect1.left = rect2.left
    rect1.top = rect2.top
    rect1.width = rect2.width
    rect1.height = rect2.height
