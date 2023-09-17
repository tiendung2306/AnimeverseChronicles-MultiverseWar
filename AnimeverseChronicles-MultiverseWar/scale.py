import pygame 
import math
from pygame.locals import *
from color import *
from img_analyze import *


pygame.init()

WIN = pygame.display.set_mode((1000,1000))


def get_spawn_imgbox(object_type, spawn_box):
    if object_type == "sword_manclass":
        size = ( 398 / 100 , 396 / 100 )
        center_vector = ( 2 / 100 , -194 / 100 ) 
    elif object_type =="archerclass" :
        size = ( 413 / 100 , 411 / 100 )
        center_vector = ( 11 / 100 , -201 / 100 )  
    elif object_type == "tankerclass":
        size = ( 508 / 100 , 254 / 100 )
        center_vector = ( 24 / 100 , -112 / 100 )
    elif object_type == "gokuclass":
        size = ( 507 / 100 , 338 / 100 )
        center_vector = ( 89 / 100 , -99 / 100 )
    elif object_type == "wizardclass":
        size = ( 388 / 100 , 201 / 100 )
        center_vector = ( 35 / 100 , -83 / 100 )
    elif object_type == "nexus":
        size = ( 1683 / 100 , 1683 / 100 )
        center_vector = ( -29 / 100 , -571 / 100 )
    elif object_type == "narutoclass":
        size = ( 685 / 100 , 585 / 100 )
        center_vector = ( 21 / 100 , -216 / 100 )

    size = (size[0] * spawn_box.width, size[1] * spawn_box.width)
    center_vector = (center_vector[0] * spawn_box.width , center_vector[1] * spawn_box.width)
    tmp = pygame.Rect(0,0,size[0], size[1])
    tmp.center = (spawn_box.centerx + center_vector[0], spawn_box.bottom + center_vector[1])
    return tmp


img = shield_animation1
img_lib = [tanker3, sword_man15, archer15, goku1, wizard1,nexus, naruto18]
type_lib = ["tankerclass", "sword_manclass", "archerclass", "gokuclass" ,"wizardclass", "nexus","narutoclass"]
x1 = 300
y1 = 500 - 100 * 54 / 32
bottom_box = pygame.Rect( x1, 500 - 100 * 54 / 32, 100 ,100 * 54 / 32)
split_box = pygame.Rect( 500, 150 , 1, 700)
width = bottom_box.width

x2 =  225 + 500
bottom_box2 = pygame.Rect( x2, 500 - 100 * 54 / 32, 100 ,100 * 54 / 32)
counter = 0


flag = 1
while flag:
    WIN.fill(Black)
    (a,b) = pygame.mouse.get_pos()
    bottom_box = pygame.Rect( x1, y1, 100 ,100 * 54 / 32)
    bottom_box2 = pygame.Rect( x2, 500 - 100 * 54 / 32, 100 ,100 * 54 / 32)
    bottom_box3 = pygame.Rect( x1 + 500, y1 , 100 ,100 * 54 / 32)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == 32:
                print("size = (",imgbox_rect.width, "/", bottom_box.width, "," ,imgbox_rect.height, "/", bottom_box.width,")")
                print("center_vector = (",imgbox_rect.centerx - bottom_box.centerx, "/", bottom_box.width, "," ,imgbox_rect.centery - bottom_box.bottom, "/", bottom_box.width,")") 

            elif event.key == 9:
                flag = False

        if event.type == MOUSEWHEEL:
            if a <= 500:
                width += event.y
            else:
                if counter < len(img_lib) - 1 and counter > 0:
                    counter += event.y
                elif counter == len(img_lib) - 1: 
                    if event.y > 0:
                        counter = 0
                    else:
                        counter -= 1
                elif counter == 0 :
                    if event.y < 0:
                        counter = len(img_lib) - 1
                    else:
                        counter += 1
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if a < 500:
                    (x1,y1) = (a,b)
                else:
                    x2 = a
                
    #display
    pygame.draw.rect(WIN, White, bottom_box2, 1)
    tmp = get_spawn_imgbox(type_lib[counter], bottom_box2)
    WIN.blit(pygame.transform.smoothscale(img_lib[counter].img, (tmp.width, tmp.height)), tmp)

    pygame.draw.rect(WIN, White, split_box)

    pygame.draw.rect(WIN, White, bottom_box3, 2)            
    height = width * img.data[3] / img.data[2]
    box_rect = pygame.Rect(0, 0, width, height)
    box_rect.centerx = bottom_box3.centerx
    box_rect.centery = bottom_box3.bottom - height / 2
    imgbox_rect = img.hitbox_to_imgbox(box_rect)
    WIN.blit(pygame.transform.smoothscale(img.img, (imgbox_rect.width, imgbox_rect.height)), imgbox_rect)
    pygame.draw.rect(WIN, Red, box_rect, 1)




    pygame.display.update()

