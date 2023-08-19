import random
import pygame 
from pygame.locals import *
from collide_checker import *


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


class straw_doll_class():
    def __init__(self,x,y,gameplay):
        self.gameplay = gameplay
        self.size = (self.gameplay.screen.get_rect().width / 15 , self.gameplay.screen.get_rect().height / 8)
        self.img = pygame.transform.smoothscale(pygame.image.load("GameplayAssets\\straw_doll.png"),self.size)
        self.x = x
        self.y = y
        self.box = self.img.get_rect(topleft = (self.x,self.y))
        self.health = 200
        self.status = True
        self.get_damage = 0
        self.alive = True
        self.get_hit = False

    def status_bar(self):
        pygame.draw.rect(self.gameplay.screen,do,pygame.Rect(self.box.left + self.size[0] / 4 ,self.box.top - self.size[1] / 20 ,(self.size[0] - self.size[0] / 2) / 500 *self.health,self.size[1] / 20))
    
    def display(self):
        self.gameplay.screen.blit(self.img,self.box)
        self.status_bar()

    def Geting_hit(self):
        self.get_hit = False
        self.health -= self.get_damage 
        self.get_damage = 0

    def die(self):
        self.gameplay.side2.remove(self)
        self.alive = False

    def operation(self):
        if self.alive :
            self.display()
            self.Geting_hit()
            if self.health <= 0:
                self.die()