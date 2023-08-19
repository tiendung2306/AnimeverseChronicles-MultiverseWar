import random
import pygame 
from pygame.locals import *
from collide_checker import *
from fake_object import *
from clock import *
from switch import *
from list_function import *


xanh_nhat = (138,54,15)
trang = (255,255,255)
den = (0,0,0)
cam = (255,97,3)
xanh = (127,255,0)
xam = (193,205,205)
do = (255,64,64)
xam_dam = (131,139,139)
vang =(255,255,0)


class sword_manclass():
    def __init__(self,x,y,gameplay):
        self.gameplay = gameplay
        self.size = (self.gameplay.screen.get_rect().width / 15 , self.gameplay.screen.get_rect().height / 8)
        self.img1 = pygame.transform.smoothscale(pygame.image.load("GameplayAssets\\sword_man1.png"),self.size)
        self.img2 = pygame.transform.smoothscale(pygame.image.load("GameplayAssets\\sword_man2.png"),self.size)
        self.img3 = pygame.transform.smoothscale(pygame.image.load("GameplayAssets\\sword_man3.png"),(self.size[0] * 333 / 396, self.size[1] * 7 / 6 ))
        self.img4 = pygame.transform.smoothscale(pygame.image.load("GameplayAssets\\sword_man4.png"),(self.size[0] * 530 / 390, self.size[1] ))
        self.x = x
        self.y = y
        self.box = self.img1.get_rect(topleft = (self.x,self.y))
        self.speed = 5 # 5/100 map per second 
        self.attack_scope = 1 * self.gameplay.screen.get_rect().width / 15 # 4/15 map width
        self.attack_speed = 1 # attack(s) pers second
        self.attack_damage = 50
        self.health = 100
        self.get_hit = False
        self.get_damage = 0 
        self.mana = 0 #mana max = 100
        self.special_status = False
        self.attack_countdowner = repeated_clock(self.gameplay.FPS, 1 / self.attack_speed)
        self.switcher1 = N_time_switch(1)
        self.attack_display_counter = N_ValueReturn_repeated_clock(self.gameplay.FPS, 1 / (3 * self.attack_speed), 3)



    def status_bar(self):
        pygame.draw.rect(self.gameplay.screen,do,pygame.Rect(self.box.left + self.size[0] / 4 ,self.box.top - self.size[1] / 20 ,(self.size[0] - self.size[0] / 2) / 100 *self.health,self.size[1] / 20))
        pygame.draw.rect(self.gameplay.screen,xanh,pygame.Rect(self.box.left + self.size[0] / 4 ,self.box.top - self.size[1] / 10 - self.size[1] / 30 ,(self.size[0] - self.size[0] / 2) / 100 *self.mana,self.size[1] / 20))
    def display(self):
        if self.box.left % 100 > 50 :
            self.gameplay.screen.blit(self.img1,self.box)
        else:
            self.gameplay.screen.blit(self.img2,self.box)
        self.status_bar()
    def check_forward(self):
        checker = fake_object_class(self)
        # pygame.draw.rect(self.gameplay.screen,cam,checker.box)
        for enemy_object in self.gameplay.side2:
            if collide_checker(checker,enemy_object):
                return False
        return True
    def move(self):
        self.box.centerx += (self.speed * self.gameplay.screen.get_rect().width / 100) / self.gameplay.FPS  


    def Geting_hit(self):
        self.get_hit = False
        self.health -= self.get_damage 
        self.get_damage = 0
        if self.special_status == False:
            self.mana += 10
    
    def attack(self):
        self.status_bar()
        self.attack_display_counter.start()
        self.attack_display_counter.operation()
        if self.attack_display_counter.Return == 2 :
            self.gameplay.screen.blit(self.img1,self.box)
        elif self.attack_display_counter.Return == 3 :
            self.gameplay.screen.blit(self.img3,(self.box.left,self.box.bottom - self.size[1] * 7 / 6))
        elif self.attack_display_counter.Return == 1 :
            self.gameplay.screen.blit(self.img4,self.box)
        self.attack_countdowner.operation()
        self.attack_countdowner.start()
        if  self.attack_countdowner.Return:
            if self.mana >= 100:
                self.special_status = True
                self.mana = 0
            else:
                 if not self.special_status:
                    self.mana += 10
            if self.special_status :
                self.special_skill()

            checker = fake_object_class(self)
            checker.box.width += self.attack_scope
            for enemy_object in self.gameplay.side2:
                if collide_checker(checker,enemy_object):
                        enemy_object.get_hit = True
                        enemy_object.get_damage = self.attack_damage
            


    def special_skill(self):
        if self.switcher1.operation():
            self.attack_damage = 150
            self.health += (100 - self.health) / 5
        else:
            self.attack_damage = 50
            self.special_status = False
            self.switcher1 = N_time_switch(1)   
    def operation(self):
        if self.check_forward():
            self.display()
            self.move()
        else:
            self.attack()
        if self.get_hit :
            self.Geting_hit()


