import pygame
from img_analyze import *
from screen import *
from object_function import *

class Nexusclass():
    def __init__(self, side , gameplay):
        self.gameplay = gameplay
        if side == 1:
            self.side = 1
            self.img = nexus
        elif side == 2:
            self.side = -1
            self.img = nexus.reverse
        self.index = 0
        self.gameplay.side(self.side).append(self)
        rect = pygame.Rect(0,0,self.gameplay.box_size[0], self.gameplay.box_size[1])
        rect.center = (screen.screen.get_rect().centerx - self.side * self.gameplay.box_size[0] * 20, self.gameplay.path_height - self.gameplay.box_size[1] / 2)
        self.box = pygame.Rect(0,0,0,0)
        self.imgbox = pygame.Rect(0,0,0,0)
        get_spawn_display(self, rect)
        self.health_max = 500.0
        self.health =  self.health_max
        self.mana_max = 100.0
        self.mana = 0
        self.damage_reduce =  0 #0%
        self.effect_list = []

        self.alive = True
        self.status = True
        self.get_hit = False

    def resize(self):  
        a = float(screen.screen.get_width()) / self.gameplay.screen[0]
        b = float(screen.screen.get_height()) /  self.gameplay.screen[1]
        tmp = pygame.Rect(self.imgbox.left * a, self.imgbox.top * b, self.imgbox.width * a, self.imgbox.height * b)
        copy(self.imgbox, tmp)
        self.box = self.img.imgbox_to_hitbox(self.imgbox)
        self.operation()  

    def status_bar(self):
        if self.mana >= self.mana_max:
            self.mana = 0
            self.special_status = True
        pygame.draw.rect(screen.screen,Red,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 10 ,(self.box.width - self.box.width / 2) / self.health_max *self.health,self.box.height / 20))
        pygame.draw.rect(screen.screen,Blue,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 5 - self.box.height / 30 ,(self.box.width - self.box.width / 2) / self.mana_max *self.mana,self.box.height / 20))
    
    def display(self):
        self.status_bar()
        self.gameplay.bg.blit(pygame.transform.smoothscale(self.img.img , (self.imgbox.width, self.imgbox.height)), self.imgbox)
        pygame.draw.rect(screen.screen,White,self.box,1)
        pygame.draw.rect(screen.screen,Red,self.imgbox,1)

 
    def Geting_hit(self):
        self.get_hit = False
        self.health -= self.get_damage 
        self.get_damage = 0



    def die(self):
        if self.side == 1:
            self.gameplay.side1.remove(self)
        elif self.side == -1:
            self.gameplay.side2.remove(self)
        self.alive = False

    def check_gameover(self):
        return not(self.alive)

    def operation(self):
            if self.alive:
                if self.health <= 0:
                    self.die()
                if self.get_hit :
                    self.Geting_hit()
                self.display()
            else:
                self.gameplay.end = True
