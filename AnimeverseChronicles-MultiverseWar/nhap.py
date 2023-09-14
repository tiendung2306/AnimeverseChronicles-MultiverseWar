import pygame 
import math
from pygame.locals import *
# from clock import*
# from list_function import *
from color import *
# from switch import *
# from img_analyze import *
# from animation_player import *
# from collide_checker import*
import time

pygame.init()
# img_lib = [tanker3, sword_man15, archer15, goku1, wizard1,nexus, naruto18]

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
        size = ( 585 / 100 , 1131 / 100 )
        center_vector = ( -18 / 100 , -516 / 100 )
    elif object_type == "narutoclass":
        size = ( 685 / 100 , 585 / 100 )
        center_vector = ( 21 / 100 , -216 / 100 )

    size = (size[0] * spawn_box.width, size[1] * spawn_box.width)
    center_vector = (center_vector[0] * spawn_box.width , center_vector[1] * spawn_box.width)
    tmp = pygame.Rect(0,0,size[0], size[1])
    tmp.center = (spawn_box.centerx + center_vector[0], spawn_box.bottom + center_vector[1])
    return tmp
WIN = pygame.display.set_mode((600,300))

screen = WIN.get_rect()
panel = pygame.Rect(0,0,600,300)
panel.center = screen.center
boder = 20
board = pygame.Rect(0,0,panel.width - boder * 2, panel.height - boder * 2)
board.center = screen.center
character_box = pygame.Rect(0 , 0 , 155 , 235)
character_box.center = board.center
character_blit_box = pygame.Rect(0, 0 , 114 , 197)
character_blit_box.center = board.center
img  = pygame.image.load("GameplayAssets\\tanker(3).png ")
Rect = get_spawn_imgbox( "tankerclass", character_blit_box)

#bar
# def static_panel(object):


#class name (name, 31, (385, ...), win)
topleft = (0,0)
font_size = 10
width = 50
height = 10
boder = 5
radius = 10
data = 20
center = (10,10)
def class_display(class_name):
    tmp = pygame.font.Font('Fonts\\AznKnucklesTrial-z85pa.otf', 31).render(class_name,True,White) #co chu phair ngi=uyennnnnn
    WIN.blit(tmp, ((board.left + character_box.left) / 2.0 - tmp.get_width() / 2.0, character_box.top))

def text_display(text, font_size, topleft, color):
    tmp = pygame.font.Font('Fonts\\AznKnucklesTrial-z85pa.otf', font_size).render(text,True,color) #co chu phair ngi=uyennnnnn
    WIN.blit(tmp, topleft)
def bar_display(data, center, color):
    hcn1 = pygame.Rect(0,0,167,11)
    hcn2 = pygame.Rect(0,0,167 - 2 * 1, 11 - 2 * 1)
    hcn1.center = hcn2.center = center
    pygame.draw.rect(WIN, Gray, hcn1,border_radius = 12)
    if data >= 100:
        hcn3 = hcn2
        hcn3.topleft = hcn2.topleft
        pygame.draw.rect(WIN, Black, hcn2,border_radius = 12)
        pygame.draw.rect(WIN, color, hcn3, border_radius = 12)
    else:
        hcn3 = pygame.Rect(0,0,hcn2.width * data / 100, 11 - 2 * 1)
        hcn3.topleft = hcn2.topleft
        pygame.draw.rect(WIN, Black, hcn2,border_radius = 12)
        pygame.draw.rect(WIN, color, hcn3, border_top_left_radius = 12, border_bottom_left_radius = 12)

# class properties():
#     def __init__(self, name, data):
#         self.name = name
#         self.font_size = 15
#         self.text_topleft_coordinate = (233 , 425)
#         self.text = pygame.font.Font('Fonts\\AznKnucklesTrial-z85pa.otf', self.font_size).render(self.name,True,White)
#         self.data = data

#     def display(self, surface):
#         surface.blit(self.text, self.text_topleft_coordinate)
#         panel = pygame.Rect



#     text_topleft_coordinate = 




# Health = properties("Health")
direct = True
flagg = 49
while direct:
    WIN.fill(White)
    pygame.draw.rect(WIN,Gray, panel, border_radius= 10)
    pygame.draw.rect(WIN,Black, board,border_radius= 10)    
    #character box
    WIN.blit(pygame.transform.smoothscale(img, (Rect.width, Rect.height)), Rect)

    #type
    class_display("TANKER")
    text_display("Bacsic statics :", 16, (35 , 72), White)
    text_display("Health :", 14, (35 , 93), White)
    bar_display(data, (117, 121), Red)
    text_display("Mana :", 14, (35 , 138), White)
    bar_display(data, (117, 121 + 45), Blue)
    text_display("Damage :", 14, (35 , 93 + 45 * 2), White)
    bar_display(data, (117, 121 + 45 * 2), Green)
    text_display("Attack speed :", 14, (35 , 93 + 45 * 3), White)
    bar_display(data, (117, 121 + 45 * 3), Yellow)

    text_display("Status :",  16, (394, 72), White)
    text_display("Effect :",  16, (394, 158), White)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            flagg = event.key
            if event.key == 9:
                direct = False
                print(width,height,boder,radius,center)
                print()
        if event.type == MOUSEWHEEL:
            if flagg == 49 :
                width += event.y
            if flagg == 50 :
                height += event.y
            if flagg == 51 :
                boder += event.y
            if flagg == 52 :
                radius += event.y
            if flagg == 53 :
                data += event.y

    (a,b) = pygame.mouse.get_pos()
    # line1 = pygame.Rect(0,b,WIN.get_size()[0],1)
    # line2 = pygame.Rect(a,0,1,WIN.get_size()[1])
    # pygame.draw.rect(WIN,Yellow,line1)
    # pygame.draw.rect(WIN,Yellow,line2)


    center = (a,b)
    pygame.draw.rect(WIN, Yellow, character_box, 1)

    
    pygame.display.update()

