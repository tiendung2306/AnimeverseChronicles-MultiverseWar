import random
import pygame 
from pygame.locals import *
from collide_checker import *
from fake_object import *
from clock import *
from switch import *
from list_function import *
from animation_player import *
from screen import *


class nexusclass():
    def __init__(self,side,box_number,gameplay):
        self.gameplay = gameplay
        self.box = pygame.Rect(box_number * self.gameplay.box_size[0],self.gameplay.path_height - 2.5 * self.gameplay.box_size[1],3 * self.gameplay.box_size[0], 3 * self.gameplay.box_size[1])
        if side == 1 :
            self.side = 1
            self.imgbox = nexus_test.hitbox_to_imgbox(self.box)        

        elif side == 2:
            self.side = -1
            self.imgbox = reverse(nexus_test).hitbox_to_imgbox(self.box)   

        self.attack_scope = 1 * self.gameplay.box_size[0] + 1  # 4/15 map width
        self.attack_speed = 1/6 # attack(s) pers second
        self.attack_damage = 5.0
        self.health_max = 500.0
        self.health =  self.health_max
        self.mana_max = 100.0
        self.mana = 0
        self.damage_reduce =  0 #0%
        self.damage_reduce_special =  40 #%
        self.skill_lasting_time = 3

        self.effect_list = []

        self.alive = True
        self.get_hit = False
        self.special_status = False




    def status_bar(self):
        if self.mana >= self.mana_max:
            self.mana = 0
            self.special_status = True
        pygame.draw.rect(screen.screen,Red,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 10 ,(self.box.width - self.box.width / 2) / self.health_max *self.health,self.box.height / 20))
        pygame.draw.rect(screen.screen,Blue,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 5 - self.box.height / 30 ,(self.box.width - self.box.width / 2) / self.mana_max *self.mana,self.box.height / 20))
    
    def display(self):
        screen.screen.blit(pygame.transform.smoothscale(nexus_test.img, (self.imgbox.width, self.imgbox.height)), self.imgbox)

    # def check_forward(self):
    #     checker = fake_object_class(self)
    #     if self.side == 1:
    #         checker.box = tanker5.imgbox_to_hitbox(self.imgbox)
    #         checker.box.width *= 2
    #         # pygame.draw.rect(screen.screen,Red,checker.box)
    #         for object in self.gameplay.side2 :
    #             if collide_checker(checker,object):
    #                 self.status = 1
    #                 return None
    #         checker.box.width *= 1 / 2
    #         for object in self.gameplay.side1:
    #             if collide_checker(checker,object):
    #                     if (not (object == self)) and (object.box.left > checker.box.left):
    #                         self.status = 2
    #                         return None

    #     elif self.side == -1:
    #         checker.box = reverse(tanker5).imgbox_to_hitbox(self.imgbox)
    #         checker.box.width *= 2
    #         checker.box.centerx -= checker.box.width / 2
    #         # pygame.draw.rect(self.gameplay.screen,White,checker.box)
    #         for object in self.gameplay.side1 :
    #             if collide_checker(checker,object):
    #                 self.status = 1
    #                 return None
    #         checker.box.centerx += checker.box.width / 2
    #         checker.box.width *= 1 / 2
    #         for object in self.gameplay.side2:
    #             if collide_checker(checker,object):
    #                 if (not (object == self)) and (object.box.left <= checker.box.left) :
    #                     self.status = 2
    #                     return None
    #     self.status = 3

    def Geting_hit(self):
        self.get_hit = False
        self.health -= self.get_damage 
        self.get_damage = 0
        if not self.special_status:
            self.mana += 10


    # def die(self):
    #     if not self.side == 0:
    #         if self.side == 1:
    #             self.gameplay.side1.remove(self)
    #         elif self.side == -1:
    #             self.gameplay.side2.remove(self)
    #         self.side = 0
    #         self.gameplay.side0.append(self)
    #         self.moving_animation.remove()
    #         self.attacking_animation.remove()
    #         self.standstill_animation.remove()      
    #         self.skill_countdowner.remove()         
    #     else:
    #         if self.dying_animation.play():
    #             self.alive = False
    #             self.gameplay.side0.remove(self)



    # def attack(self):
    #     self.box = self.attacking_animation.play()
    #     if self.attacking_animation.clock.Return == 5 or self.attacking_animation.clock.Return == 8:
    #         if self.switcher1.operation():

    #             if not self.special_status :
    #                 self.mana += 10 
                        
    #             checker = fake_object_class(self)
    #             checker.box.width += self.attack_scope 
    #             if self.side == 1:
    #                 for enemy_object in self.gameplay.side2:
    #                 # pygame.draw.rect(screen.screen,White,checker.box)
    #                     if collide_checker(checker,enemy_object):
    #                             enemy_object.get_hit = True
    #                             enemy_object.get_damage = self.attack_damage
    #             elif self.side == -1:
    #                 checker.box.centerx -= self.attack_scope 
    #                 # pygame.draw.rect(screen.screen,White,checker.box)
    #                 for enemy_object in self.gameplay.side1:
    #                     if collide_checker(checker,enemy_object):
    #                             enemy_object.get_hit = True
    #                             enemy_object.get_damage = self.attack_damage
    #     elif self.attacking_animation.clock.Return == 7:
    #         self.switcher1.reset()

  


    def operation(self):
            if self.alive:
                self.display()
                # if self.health <= 0:
                #     self.die()
                #     return None
                self.status_bar()
                # self.check_forward()
                # for effect in self.effect_list:
                #     effect.play()

                # if self.status == 3:
                #     self.move()

                # elif self.status == 1:
                #     self.attack()

                # elif self.status == 2 :
                #     self.standstill()

                if self.get_hit :
                    self.Geting_hit()

                pygame.draw.rect(screen.screen,White,self.box,1)
                pygame.draw.rect(screen.screen,Red,self.imgbox,1)

