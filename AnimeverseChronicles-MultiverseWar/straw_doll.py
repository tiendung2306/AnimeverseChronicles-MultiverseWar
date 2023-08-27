import random
import pygame 
from pygame.locals import *
from collide_checker import *
from common_effect import *
from color import *
from screen import *

fpsclock = pygame.time.Clock()
FPS = 60



class straw_doll_class():
    def __init__(self,side,box_number,gameplay):
        if side == 1 :
            self.side = 1
        elif side == 2:
            self.side = -1

        self.gameplay = gameplay 

        self.size = self.gameplay.box_size
        self.imgbox = straw_doll.hitbox_to_imgbox(pygame.Rect(box_number * self.gameplay.box_size[0],self.gameplay.path_height - self.gameplay.box_size[1], self.gameplay.box_size[0], self.gameplay.box_size[1]))        
        self.box = straw_doll.imgbox_to_hitbox(self.imgbox)
        self.effect_list = []

        self.health_max = 1000
        self.health = self.health_max
        self.mana_max =100
        self.mana = 0        
        
        self.alive = True
        self.get_hit = False

    def status_bar(self):
        if self.mana >= self.mana_max:
            self.mana = 0
        pygame.draw.rect(screen.screen,Red,pygame.Rect(self.box.left + self.size[0] / 4 ,self.box.top - self.size[1] / 20 ,(self.size[0] - self.size[0] / 2) / self.health_max *self.health,self.size[1] / 20))
        pygame.draw.rect(screen.screen,Blue,pygame.Rect(self.box.left + self.size[0] / 4 ,self.box.top - self.size[1] / 10 - self.size[1] / 30 ,(self.size[0] - self.size[0] / 2) / self.mana_max *self.mana,self.size[1] / 20))
    
    def display(self):
        screen.screen.blit(pygame.transform.smoothscale(straw_doll.img,(self.imgbox.width, self.imgbox.height)),self.imgbox)

    def Geting_hit(self):
        self.get_hit = False
        self.health -= self.get_damage 
        self.get_damage = 0
        self.mana += 10


    def die(self):
        if self.side == 1:
            self.gameplay.side1.remove(self)
        elif self.side == -1:
            self.gameplay.side2.remove(self)
        self.alive = False

    def operation(self):
        if self.alive :
            self.display()
            self.status_bar()
            for effect in self.effect_list:
                effect.play()
            if self.get_hit:
                self.Geting_hit()
            if self.health <= 0:
                self.die()
            pygame.draw.rect(screen.screen,White,self.box,1)
            pygame.draw.rect(screen.screen,White,self.imgbox,1)