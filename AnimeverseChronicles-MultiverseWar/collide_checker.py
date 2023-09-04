import math
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
        

def collide_check_special(special_object, object):
    if special_object.side == -1:
        special_object.topleft = special_object.topright
    tan1 =  (special_object.topleft[1] - object.box.centery ) / (object.box.centerx - special_object.topleft[0])
    alpha = math.atan(tan1)
    # print(alpha)
    beta = alpha - special_object.angle * math.pi / 180
    # print(beta)
    distance = abs(math.sin(beta) * math.sqrt((special_object.topleft[0] - object.box.centerx)**2 +(special_object.topleft[1] - object.box.centery)**2  ))
    # print(math.sin(beta))
    # print(special_object.topleft[0] - object.box.centerx)
    # print(special_object.topleft[1] - object.box.centery)
    if distance < special_object.size[0] / 2 + object.box.width / 2:
        return True
    else:
        return False