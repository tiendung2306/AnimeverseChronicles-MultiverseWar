import pygame
from img_analyze import *
from screen import *

class Nexusclass():
    def __init__(self, side , gameplay):
        # self.screen = pygame.display.get_surface()
        # self.nexus_surface_original = pygame.image.load(filename)
        # self.nexus_surface = self.nexus_surface_original.copy()

        # pre_nexus_height = self.nexus_surface.get_rect().height
        # pre_nexus_width = self.nexus_surface.get_rect().width
        # new_nexus_width = self.screen.get_rect().width // 10
        # self.nexus_surface = pygame.transform.smoothscale(self.nexus_surface, (new_nexus_width, new_nexus_width / pre_nexus_width * pre_nexus_height))
        self.gameplay = gameplay
        self.size = (self.gameplay.box_size[0] * 2, self.gameplay.box_size[0] * 2 * nexus.data[3] / nexus.data[2] )
        if side == 1 :
            self.gameplay.side1.append(self)
            self.box = pygame.Rect(self.size[0] / 2, self.gameplay.path_height - self.size[1] * 9 / 10, self.size[0], self.size[1])     
            self.side = 1
            self.imgbox = nexus.hitbox_to_imgbox(self.box)        
            self.img = nexus

        elif side == 2:
            self.gameplay.side2.append(self)
            self.box = pygame.Rect(screen.screen.get_size()[0] - self.size[0], self.gameplay.path_height - self.size[1] * 9 / 10, self.size[0], self.size[1])     
            self.side = -1
            self.imgbox = reverse(nexus).hitbox_to_imgbox(self.box)
            self.img = nexus.reverse


        self.health_max = 500.0
        self.health =  self.health_max
        self.mana_max = 100.0
        self.mana = 0
        self.damage_reduce =  0 #0%

        self.effect_list = []

        self.alive = True
        self.get_hit = False

    def resize(self):  
        self.size = (self.gameplay.box_size[0] * 2, self.gameplay.box_size[0] * 2 * nexus.data[3] / nexus.data[2] )
        if self.side == 1 :
            self.box = pygame.Rect(self.size[0] / 2, self.gameplay.path_height - self.size[1] * 9 / 10, self.size[0], self.size[1])     
            self.imgbox = nexus.hitbox_to_imgbox(self.box)        

        elif self.side == -1:
            self.box = pygame.Rect(screen.screen.get_size()[0] - self.size[0] * 3 / 2, self.gameplay.path_height - self.size[1] * 9 / 10, self.size[0], self.size[1])     
            self.imgbox = reverse(nexus).hitbox_to_imgbox(self.box)   
        self.display()

    def status_bar(self):
        if self.mana >= self.mana_max:
            self.mana = 0
            self.special_status = True
        pygame.draw.rect(screen.screen,Red,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 10 ,(self.box.width - self.box.width / 2) / self.health_max *self.health,self.box.height / 20))
        pygame.draw.rect(screen.screen,Blue,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 5 - self.box.height / 30 ,(self.box.width - self.box.width / 2) / self.mana_max *self.mana,self.box.height / 20))
    
    def display(self):
        self.status_bar()
        self.gameplay.bg.blit(pygame.transform.smoothscale(self.img.img , (self.imgbox.width, self.imgbox.height)), self.imgbox)

 
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
                #     return None
                # self.check_forward()
                # for effect in self.effect_list:
                #     effect.play()

                # if self.status == 3:
                #     self.move()

                # elif self.status == 1:
                #     self.attack()

                # elif self.status == 2 :
                #     self.standstill()s



                pygame.draw.rect(screen.screen,White,self.box,1)
                pygame.draw.rect(screen.screen,Red,self.imgbox,1)