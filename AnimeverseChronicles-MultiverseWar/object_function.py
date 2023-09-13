import pygame 
from pygame.locals import *
from img_analyze import *
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

def spawn(object,side,position,gameplay):
    tmp = object(side, gameplay)
    tmp.index = len(gameplay.side(tmp.side)) 
    gameplay.side(tmp.side).append(tmp)
    tmp2 = pygame.Rect(position * gameplay.box_size[0], gameplay.path_height - gameplay.box_size[1], gameplay.box_size[0], gameplay.box_size[1])
    get_spawn_display(tmp, tmp2)

img_lib = [tanker3, sword_man15, archer15, goku1, wizard1,nexus, naruto18]

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
    elif object.__class__ == object.gameplay.nexusclass:
        size = ( 585 / 100 , 1131 / 100 )
        center_vector = ( -18 / 100 , -516 / 100 )
    elif object.__class__ == object.gameplay.narutoclass:
        size = ( 685 / 100 , 585 / 100 )
        center_vector = ( 21 / 100 , -216 / 100 )
    elif object.__class__ == object.gameplay.cloneclass:
        size = ( 685 / 100 , 585 / 100 )
        center_vector = ( 21 / 100 , -216 / 100 )

    size = (size[0] * spawn_box.width, size[1] * spawn_box.width)
    center_vector = (center_vector[0] * object.side * spawn_box.width , center_vector[1] * spawn_box.width)
    tmp = pygame.Rect(0,0,size[0], size[1])
    tmp.center = (spawn_box.centerx + center_vector[0], spawn_box.bottom + center_vector[1])
    return tmp

def get_spawn_display(object, spawn_box):
    if object.__class__ == object.gameplay.sword_manclass:
        size = ( 398 / 100 , 396 / 100 )
        center_vector = ( 2 / 100 , -194 / 100 ) 
        img = sword_man15
    elif object.__class__ == object.gameplay.archerclass:
        size = ( 413 / 100 , 411 / 100 )
        center_vector = ( 11 / 100 , -201 / 100 )  
        img = archer15
    elif object.__class__ == object.gameplay.tankerclass:
        size = ( 508 / 100 , 254 / 100 )
        center_vector = ( 24 / 100 , -112 / 100 )
        img = tanker3
    elif object.__class__ == object.gameplay.gokuclass:
        size = ( 507 / 100 , 338 / 100 )
        center_vector = ( 89 / 100 , -99 / 100 )
        img = goku1
    elif object.__class__ == object.gameplay.wizardclass:
        size = ( 388 / 100 , 201 / 100 )
        center_vector = ( 35 / 100 , -83 / 100 )
        img = wizard1
    elif object.__class__ == object.gameplay.nexusclass:
        size = ( 585 / 100 , 1131 / 100 )
        center_vector = ( -18 / 100 , -516 / 100 )
        img = nexus
    elif object.__class__ == object.gameplay.narutoclass:
        size = ( 685 / 100 , 585 / 100 )
        center_vector = ( 21 / 100 , -216 / 100 )
        img = naruto18

    size = (size[0] * spawn_box.width, size[1] * spawn_box.width)
    center_vector = (center_vector[0] * object.side * spawn_box.width , center_vector[1] * spawn_box.width)
    tmp = pygame.Rect(0,0,size[0], size[1])
    tmp.center = (spawn_box.centerx + center_vector[0], spawn_box.bottom + center_vector[1])
    copy(object.imgbox, tmp)
    copy(object.box, img.imgbox_to_hitbox(object.imgbox))



