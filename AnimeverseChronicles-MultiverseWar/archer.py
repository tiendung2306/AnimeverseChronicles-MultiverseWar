import random
import pygame 
from pygame.locals import *
from collide_checker import *
from fake_object import *
from clock import *
from switch import *
from list_function import *

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
vang = (255,255,0)


   

class arrowclass():
    def __init__(self,archer):
        self.archer = archer
        self.img = pygame.transform.smoothscale(pygame.image.load("GameplayAssets\\arrow.png"),(50, 7))
        self.box = self.img.get_rect(topleft = (self.archer.box.left + 3.25 * self.archer.box.width / 5, self.archer.box.top + 0.85 * self.archer.box.height / 3))
        self.piercing = self.archer.piercing
        self.speed = 20  # 10/100 map per second
        self.damage = self.archer.attack_damage
        self.damaged_object = []
        self.status = True
        self.special = self.archer.special_status 
        if self.special :
            self.x_limit = self.archer.box.right + self.archer.attack_scope
    def move(self):
        self.box.centerx += (self.speed * self.archer.gameplay.screen.get_rect().width / 100) / self.archer.gameplay.FPS
    def collide_check(self):
        for enemy_object in self.archer.gameplay.side2:
            if collide_checker(self,enemy_object):
                if list_find(self.damaged_object,enemy_object) == -1:
                    self.damaged_object.append(enemy_object)
                    # print("kkkkkkkkkkkkkkkkkk")
                    enemy_object.get_damage = self.damage
                    enemy_object.get_hit = True
                    if not self.piercing:
                        self.status = False

    def limit_check(self):
        if (len(self.damaged_object) == 3) or (self.box.right >= self.x_limit):
            self.status = False
    def arrow_operation(self):
        self.collide_check()
        if self.status:
            if self.piercing :
                self.limit_check()
                pygame.draw.rect(self.archer.gameplay.screen,den,self.box)
            self.archer.gameplay.screen.blit(self.img,self.box.topleft)
            self.move()
        elif self.special == False :
            return True
        
class archerclass():
    def __init__(self,x,y,gameplay):
        self.gameplay = gameplay
        self.size = (self.gameplay.screen.get_rect().width / 15 , self.gameplay.screen.get_rect().height / 8)
        self.img1 = pygame.transform.smoothscale(pygame.image.load("GameplayAssets\\archer1.png"),self.size)
        self.img2 = pygame.transform.smoothscale(pygame.image.load("GameplayAssets\\archer2.png"),self.size)
        self.img3 = pygame.transform.smoothscale(pygame.image.load("GameplayAssets\\archer3.png"),self.size)
        self.x = x
        self.y = y
        self.box = self.img1.get_rect(topleft = (self.x,self.y))
        self.piercing = False
        self.speed = 20 # 5/100 map per second 
        self.attack_scope = 4 * self.gameplay.screen.get_rect().width / 15 # 4/15 map width
        # print(self.gameplay.screen.get_rect().width)

        self.attack_speed = 1 # arrow(s) pers second
        self.attack_damage = 10
        self.arrow_list = []
        self.health = 100
        self.get_hit = False
        self.get_damage = 0
        self.mana = 0 #mana max = 100
        self.special_status = False
        self.attack_countdowner = repeated_clock(self.gameplay.FPS, 1 / self.attack_speed)
        self.skill_countdowner = timing_clock(self.gameplay.FPS, 1.5)
        self.special_arrow_switcher = N_time_switch(1)
        self.special_arrow_switcher2 = N_time_switch(1)

    # def update(gameplay):  


        

    def status_bar(self):
        pygame.draw.rect(self.gameplay.screen,do,pygame.Rect(self.box.left + self.size[0] / 4 ,self.box.top - self.size[1] / 20 ,(self.size[0] - self.size[0] / 2) / 100 *self.health,self.size[1] / 20))
        pygame.draw.rect(self.gameplay.screen,xanh,pygame.Rect(self.box.left + self.size[0] / 4 ,self.box.top - self.size[1] / 10 - self.size[1] / 30 ,(self.size[0] - self.size[0] / 2) / 100 *self.mana,self.size[1] / 20))
    def display(self):
        if self.box.left % 30 > 15 :
            self.gameplay.screen.blit(self.img1,self.box)
        else:
            self.gameplay.screen.blit(self.img2,self.box)
        self.status_bar()
    def check_forward(self):
        checker = fake_object_class(self)
        checker.box.width += self.attack_scope
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
        self.gameplay.screen.blit(self.img3,self.box)
        self.attack_countdowner.operation()
        self.attack_countdowner.start()
        self.skill_countdowner.operation()
        if  self.attack_countdowner.Return:
            # print("hooh")
            if self.mana >= 100:
                self.special_status = True
                self.mana = 0
            if self.special_status :
                # print("pow")
                self.skill_countdowner.start()
                if self.skill_countdowner.Return:
                    # print("hehe")
                    self.special_skill()
                else:
                    # print("ehheahhea")
                    self.special_skill_reset()
            
            self.arrow_list.append(arrowclass(self))            
        

    def special_skill(self):
        if self.special_arrow_switcher.operation():
            self.piercing = True
            self.attack_damage = 20
            self.attack_scope = 7 * self.gameplay.screen.get_rect().width / 15
        elif self.special_arrow_switcher2.operation():
            self.attack_speed = 3
            self.attack_countdowner = repeated_clock(self.gameplay.FPS, 1 / self.attack_speed)
            self.piercing = False
            self.attack_damage = 10
            self.attack_scope = 4 * self.gameplay.screen.get_rect().width / 15

    def special_skill_reset(self):
        self.special_status = False
        self.attack_speed = 1
        self.attack_countdowner = repeated_clock(self.gameplay.FPS, 1 / self.attack_speed)
        self.skill_countdowner.reset()
        self.special_arrow_switcher.reset()
        self.special_arrow_switcher2.reset()
    def operation(self):
        if self.check_forward():
            self.display()
            self.move()
        else:
            self.attack()
        for arrows in self.arrow_list:
            if arrows.arrow_operation():
                self.mana += 10
            if arrows.status == False :
                self.arrow_list.remove(arrows)
        if self.get_hit:
            self.Geting_hit()

    






