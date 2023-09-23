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
    if side == 1:
        tmp.index = gameplay.side1_heros
        gameplay.side1_heros += 1
    else:
        tmp.index = gameplay.side2_heros
        gameplay.side2_heros += 1
    gameplay.side(tmp.side).append(tmp)
    tmp2 = pygame.Rect(position * gameplay.box_size[0], gameplay.path_height - gameplay.box_size[1], gameplay.box_size[0], gameplay.box_size[1])
    get_spawn_display(tmp, tmp2)

tanker3 = analyzed_img("GameplayAssets\\tanker\\tanker(3).png", 229 , 60 , 85 , 222)
sword_man15 = analyzed_img("GameplayAssets\\sword_man\\sword_man(15).png", 231 , 350 , 131 , 242)
archer15 = analyzed_img("GameplayAssets\\archer\\archer(15).png", 195 , 294 , 81 , 198)
goku1 = analyzed_img("GameplayAssets\\goku\\goku(1).png ",139 , 90 , 110 , 226)
wizard1 = analyzed_img("GameplayAssets\\wizard\\wizard(1).png", 170 , 56 , 68 , 179)
nexus = analyzed_img("GameplayAssets\\nexus.png", 309 , 15 , 106 , 572)
naruto18 = analyzed_img( "GameplayAssets\\naruto\\naruto(18).png " , 278 , 354 , 98 , 167 )


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
        size = ( 1683 / 100 , 1683 / 100 )
        center_vector = ( -29 / 100 , -571 / 100 )
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
        object.name = "Sword Man"
    elif object.__class__ == object.gameplay.archerclass:
        size = ( 413 / 100 , 411 / 100 )
        center_vector = ( 11 / 100 , -201 / 100 )  
        img = archer15
        object.name = "Archer"
    elif object.__class__ == object.gameplay.tankerclass:
        size = ( 508 / 100 , 254 / 100 )
        center_vector = ( 24 / 100 , -112 / 100 )
        img = tanker3
        object.name = "Tanker"
    elif object.__class__ == object.gameplay.gokuclass:
        size = ( 507 / 100 , 338 / 100 )
        center_vector = ( 89 / 100 , -99 / 100 )
        img = goku1
        object.name = "Goku"
    elif object.__class__ == object.gameplay.wizardclass:
        size = ( 388 / 100 , 201 / 100 )
        center_vector = ( 35 / 100 , -83 / 100 )
        img = wizard1
        object.name = "Wizard"
    elif object.__class__ == object.gameplay.nexusclass:
        size = ( 1683 / 100 , 1683 / 100 )
        center_vector = ( -29 / 100 , -571 / 100 )
        img = nexus
    elif object.__class__ == object.gameplay.narutoclass:
        size = ( 685 / 100 , 585 / 100 )
        center_vector = ( 21 / 100 , -216 / 100 )
        img = naruto18
        object.name = "Naruto"

    size = (size[0] * spawn_box.width, size[1] * spawn_box.width)
    center_vector = (center_vector[0] * object.side * spawn_box.width , center_vector[1] * spawn_box.width)
    tmp = pygame.Rect(0,0,size[0], size[1])
    tmp.center = (spawn_box.centerx + center_vector[0], spawn_box.bottom + center_vector[1])
    copy(object.imgbox, tmp)
    copy(object.box, img.imgbox_to_hitbox(object.imgbox))



