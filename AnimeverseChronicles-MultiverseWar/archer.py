import random
import pygame 
from pygame.locals import *

pygame.init()


fpsclock = pygame.time.Clock()
FPS = 60



xanh_nhat = (138,54,15)
trang = (255,255,255)
den = (0,0,0)
cam = (255,97,3)
xanh = (127,255,0)
xam = (193,205,205)
do = (255,64,64)
xam_dam = (131,139,139)
vang =(255,255,0)

text_font = pygame.font.Font("Fonts\\Minecraft.ttf",20)


def collide_checker(object1,object2):
    box1 = object1
    box2 = object2
    if ((box1.left < box2.left)and(box2.left < box1.right)) or ((box1.left < box2.right)and(box2.right < box1.right)):
        # print("jjj")
        if ((box1.top < box2.top)and(box2.top < box1.bottom)) or ((box1.top < box2.bottom)and(box2.bottom < box1.bottom)):
            return True
    (box1, box2) = (box2, box1)
    if ((box1.left < box2.left)and(box2.left < box1.right)) or ((box1.left < box2.right)and(box2.right < box1.right)):
    # print("jjj")
        if ((box1.top < box2.top)and(box2.top < box1.bottom)) or ((box1.top < box2.bottom)and(box2.bottom < box1.bottom)):
            return True    
    

# collide_checker(pygame.Rect(954, 255, 50, 7),straw_doll.get_rect(topleft = (900,220)))
# print(straw_doll.get_rect(topleft = (900,220)))
class arrowclass():
    def __init__(self,archer):
        self.img = pygame.transform.smoothscale(pygame.image.load("GameplayAssets\\arrow.png"),(50,7))
        self.box = self.img.get_rect(topleft = (archer.box.left + 65,archer.y + 55))
        self.speed = 5
        self.damage = 0
        self.status = True
        self.archer = archer
    def move(self):
        self.box.centerx += self.speed
    def collide_check(self):
        for enemy_object in self.archer.gameplay.enemy_list:
            if collide_checker(self.box,enemy_object):
                print('')
                self.status = False
    def arrow_operation(self,surface):
        self.collide_check()
        if self.status:
            pygame.draw.rect(surface,cam,self.box)
            surface.blit(self.img,self.box)
            # print(self.box)
            self.move()
        else:
            return True
        
class archerclass():
    def __init__(self,x,y,size_list,speed):
        self.size = size_list
        self.img1 = pygame.transform.smoothscale(pygame.image.load("GameplayAssets\\archer1.png"),self.size)
        self.img2 = pygame.transform.smoothscale(pygame.image.load("GameplayAssets\\archer2.png"),self.size)
        self.img3 = pygame.transform.smoothscale(pygame.image.load("GameplayAssets\\archer3.png"),self.size)
        self.x = x
        self.y = y
        self.box = self.img1.get_rect(topleft = (self.x,self.y))
        self.speed = speed
        self.attack_scope = 500
        self.attack_speed = 1
        self.attack_countdowner = 0
        self.arrow_list = []
        self.health = 100
        self.mana = 0
        self.mana_max = 100
        

    def status_bar(self,surface):
        pygame.draw.rect(surface,do,pygame.Rect(self.box.left ,self.box.top -20,self.health,15))
        pygame.draw.rect(surface,xanh,pygame.Rect(self.box.left ,self.box.top -20 - 20,self.mana,15))
    def display(self,surface):
        if self.box.left%30 > 15 :
            surface.blit(self.img1,self.box)
        else:
            surface.blit(self.img2,self.box)
        self.status_bar(surface)
    def check_forward(self):
        check_box = self.img1.get_rect(center = (self.box.centerx + self.attack_scope,self.box.centery))
        for enemy_object in self.gameplay.enemy_list:
            if collide_checker(check_box,enemy_object):
                return False
        return True
    def move(self):
            self.box.centerx += 1
    def attack(self,surface):
        self.status_bar(surface)
        surface.blit(self.img3,self.box)
        if self.attack_countdown():
            self.arrow_list.append(arrowclass(self))
        for arrows in self.arrow_list:
            if arrows.arrow_operation(surface):
                self.mana += 10
                if self.mana > self.mana_max:
                    self.mana = self.mana_max
            if arrows.status == False :
                self.arrow_list.remove(arrows)
    def attack_countdown(self):
        if self.attack_countdowner == 0:
            self.attack_countdowner = self.attack_speed * FPS
            return True
        else:
            self.attack_countdowner -= 1
            return False
    # def special_skill(self):
    #     self.attack_speed += 


    def operation(self,surface):
        if self.check_forward():
            self.display(surface)
            self.move()
        else:
            self.attack(surface)
    






