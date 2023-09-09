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
    if object.box.centerx - special_object.start_point[0] == 0:
        alpha = - math.pi / 2
    else:
        tan1 =  (special_object.start_point[1] - object.box.centery ) / (object.box.centerx - special_object.start_point[0])
        alpha = math.atan(tan1)
    beta = alpha - special_object.angle * math.pi / 180
    distance = abs(math.sin(beta) * math.sqrt((special_object.start_point[0] - object.box.centerx)**2 +(special_object.start_point[1] - object.box.centery)**2  ))

    if distance < special_object.size[1] / 2 + object.box.width / 2:
        return True
    else:
        return False
    

def same_line_checker(object1, object2):
    box1 = object1.box
    box2 = object2.box
    if ((box1.top <= box2.top)and(box2.top <= box1.bottom)) or ((box1.top <= box2.bottom)and(box2.bottom <= box1.bottom)):
        return True
    else:
        (box1, box2) = (box2, box1)
        if ((box1.top <= box2.top)and(box2.top <= box1.bottom)) or ((box1.top <= box2.bottom)and(box2.bottom <= box1.bottom)):
            return True
    return False