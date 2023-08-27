import random
import pygame 
from pygame.locals import *

def collide_checker(object1,object2):
    box1 = object1.box
    box2 = object2.box
    if ((box1.left <= box2.left)and(box2.left <= box1.right)) or ((box1.left <= box2.right)and(box2.right <= box1.right)):
        if ((box1.top <= box2.top)and(box2.top <= box1.bottom)) or ((box1.top <= box2.bottom)and(box2.bottom <= box1.bottom)):
            return True
        else:
            (box1, box2) = (box2, box1)
            if ((box1.top <= box2.top)and(box2.top <= box1.bottom)) or ((box1.top <= box2.bottom)and(box2.bottom <= box1.bottom)):
                return True
        
    (box1, box2) = (box2, box1)
    if ((box1.left <= box2.left)and(box2.left <= box1.right)) or ((box1.left <= box2.right)and(box2.right <= box1.right)):
        if ((box1.top <= box2.top)and(box2.top <= box1.bottom)) or ((box1.top <= box2.bottom)and(box2.bottom <= box1.bottom)):
            return True   
        else:
            (box1, box2) = (box2, box1)
            if ((box1.top <= box2.top)and(box2.top <= box1.bottom)) or ((box1.top <= box2.bottom)and(box2.bottom <= box1.bottom)):
                return True
        