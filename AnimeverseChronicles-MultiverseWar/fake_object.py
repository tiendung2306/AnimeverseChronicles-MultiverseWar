import random
import pygame 
from pygame.locals import *

class fake_object_class():
    def __init__(self,object):
        self.box = pygame.Rect(object.box.left,object.box.top,object.box.width,object.box.height)
        self.status = True