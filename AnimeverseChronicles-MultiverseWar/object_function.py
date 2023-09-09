import pygame 
from pygame.locals import *

class fake_object_class():
    def __init__(self,object):
        self.box = pygame.Rect(object.box.left,object.box.top,object.box.width,object.box.height)
        self.imgbox = pygame.Rect(object.imgbox.left,object.imgbox.top,object.imgbox.width,object.imgbox.height)
        self.status = True
        self.side = 0


def copy( rect1, rect2 ):
    rect1.left = rect2.left
    rect1.top = rect2.top
    rect1.width = rect2.width
    rect1.height = rect2.height

def spawn(object_type,side,position,gameplay):
    tmp = object_type(side, gameplay)
    tmp.index = len(gameplay.side(tmp.side)) 
    gameplay.side(tmp.side).append(tmp)
    tmp2 = pygame.Rect(position * gameplay.box_size[0], gameplay.path_height - gameplay.box_size[1], gameplay.box_size[0], gameplay.box_size[1])
    copy(tmp.imgbox, get_spawn_imgbox(tmp,tmp2))
    tmp.status = 2



def get_spawn_imgbox(object, spawn_box):
    if object.__class__ == object.gameplay.sword_manclass:
        size = ( 398 / 100 , 396 / 100 )
        center_vector = ( 2 / 100 , -194 / 100 ) 
    elif object.__class__ == object.gameplay.archerclass:
        size = ( 413 / 100 , 411 / 100 )
        center_vector = ( 11 / 100 , -201 / 100 )  
    elif object.__class__ == object.gameplay.tankerclass:
        size = ( 508 / 100 , 254 / 100 )
        center_vector = ( 24 / 100 , -112 / 100 )
    elif object.__class__ == object.gameplay.gokuclass:
        size = ( 507 / 100 , 338 / 100 )
        center_vector = ( 89 / 100 , -99 / 100 )
    elif object.__class__ == object.gameplay.wizardclass:
        size = ( 388 / 100 , 201 / 100 )
        center_vector = ( 35 / 100 , -83 / 100 )

    size = (size[0] * spawn_box.width, size[1] * spawn_box.width)
    center_vector = (center_vector[0] * object.side * spawn_box.width , center_vector[1] * spawn_box.width)
    tmp = pygame.Rect(0,0,size[0], size[1])
    tmp.center = (spawn_box.centerx + center_vector[0], spawn_box.bottom + center_vector[1])
    return tmp



