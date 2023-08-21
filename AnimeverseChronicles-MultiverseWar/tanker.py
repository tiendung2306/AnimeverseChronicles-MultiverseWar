import random
import pygame 
from pygame.locals import *
from collide_checker import *
from fake_object import *
from clock import *
from switch import *
from list_function import *
from animation_player import *


class tankerclass():
    def __init__(self,side,box_number,gameplay):
        if side == 1 :
            self.side = 1
        elif side == 2:
            self.side = -1   
        
        self.gameplay = gameplay
        
        self.size = self.gameplay.box_size
        if self.side == 1:
            self.img_lib = [tanker1_1, tanker1_2, tanker1_3, tanker1_4]
        elif self.side == -1:
            self.img_lib = [tanker2_1, tanker2_2, tanker2_3, tanker2_4]
        self.imgbox = self.img_lib[0].hitbox_to_imgbox(pygame.Rect(box_number * self.gameplay.box_size[0],self.gameplay.path_height - self.gameplay.box_size[1], self.gameplay.box_size[0], self.gameplay.box_size[1]))        
        self.box = self.img_lib[0].imgbox_to_hitbox(self.imgbox)
        self.speed = 20 # 5/100 map per second 
        self.attack_scope = 0 * self.gameplay.box_size[0] + 1  # 4/15 map width
        self.attack_speed = 1/5 # attack(s) pers second
        self.attack_damage = 20
        self.health_max = 500
        self.health = self.health_max
        self.mana_max =100
        self.mana = 0
        self.damage_reduce =  0 #0%
        self.damage_reduce_special =  40 #%


        self.alive = True
        self.get_hit = False
        self.alive = True
        self.get_damage = 0
        self.special_status = False

        self.moving_animation = animation_player([self.img_lib[0], self.img_lib[1]], 1, self.imgbox , self.gameplay)
        self.attacking_animation = animation_player([self.img_lib[2], self.img_lib[3]], 1 / self.attack_speed, self.imgbox, self.gameplay)
        self.standstill_animation = animation_player([self.img_lib[0], self.img_lib[0]], 1, self.imgbox, self.gameplay)

        self.switcher1 = N_time_switch(1)
        self.switcher2 = N_time_switch(1)
        self.skill_countdowner = timing_clock(3,self.gameplay)


    def status_bar(self):
        if self.mana >= self.mana_max:
            self.mana = 0
            self.special_status = True
        pygame.draw.rect(self.gameplay.screen,Red,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 10 ,(self.box.width - self.box.width / 2) / self.health_max *self.health,self.box.height / 20))
        pygame.draw.rect(self.gameplay.screen,Blue,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 5 - self.box.height / 30 ,(self.box.width - self.box.width / 2) / self.mana_max *self.mana,self.box.height / 20))
    
    
    def move(self):
        self.box = self.moving_animation.play()
        self.imgbox.centerx += (self.speed * self.gameplay.screen.get_rect().width / 100) / self.gameplay.FPS  * self.side
        self.attacking_animation.reset()


    def standstill(self):
        self.box = self.standstill_animation.play()
    
    
    
    def check_forward(self):
        checker = fake_object_class(self)
        for tmp_img in self.img_lib:
            checker.box = tmp_img.imgbox_to_hitbox(self.imgbox)
            # checker.box.width += self.attack_scope 
            if self.side == 1:
                # pygame.draw.rect(self.gameplay.screen,Red,checker.box)
                for object in self.gameplay.side2 :
                    if collide_checker(checker,object):
                        return 1
                
                for object in self.gameplay.side1:
                    if collide_checker(self,object):
                         if (not (object == self)) and (object.box.left >= self.box.left):
                            return 2

            elif self.side == -1:
                # checker.box.centerx -= self.attack_scope 
                # pygame.draw.rect(self.gameplay.screen,White,checker.box)
                for object in self.gameplay.side1 :
                    if collide_checker(checker,object):
                        return 1
                for object in self.gameplay.side2:
                    if collide_checker(self,object):
                        if (not (object == self)) and (object.box.left <= self.box.left) :
                            return 2
        return 0


    def Geting_hit(self):
        self.get_hit = False
        self.health -= self.get_damage 
        self.get_damage = 0
        if not self.special_status:
            self.mana += 10


    def die(self):
        if self.side == 1:
            self.gameplay.side1.remove(self)
        elif self.side == -1:
            self.gameplay.side2.remove(self)
        self.moving_animation.remove()
        self.attacking_animation.remove()
        self.standstill_animation.remove()      
        self.skill_countdowner.remove()         
        self.alive = False
    

    def attack(self):
        self.box = self.attacking_animation.play()
        if self.attacking_animation.clock.Return == 2:
            if self.switcher1.operation():

                if self.special_status :
                    self.skill_countdowner.start()
                    if self.skill_countdowner.Return:
                        self.special_skill()
                    else:
                        self.special_skill_reset()
                else:
                    self.mana += 10 
                        
                checker = fake_object_class(self)
                checker.box.width += self.attack_scope 
                if self.side == 1:
                    for enemy_object in self.gameplay.side2:
                    # pygame.draw.rect(self.gameplay.screen,White,checker.box)
                        if collide_checker(checker,enemy_object):
                                # print("kk")
                                enemy_object.get_hit = True
                                enemy_object.get_damage = self.attack_damage
                elif self.side == -1:
                    checker.box.centerx -= self.attack_scope 
                    # pygame.draw.rect(self.gameplay.screen,White,checker.box)
                    for enemy_object in self.gameplay.side1:
                        if collide_checker(checker,enemy_object):
                                enemy_object.get_hit = True
                                enemy_object.get_damage = self.attack_damage
        elif self.attacking_animation.clock.Return == 1:     
            self.switcher1.reset()


    def special_skill(self):
            self.damage_reduce = self.damage_reduce_special


    def special_skill_reset(self):
            self.damage_reduce = 0
            self.special_status = False
            self.skill_countdowner.reset()


    def operation(self):
            if self.alive:
                self.status_bar()
                tmp = self.check_forward()
                if tmp == 0:
                    self.move()

                elif tmp == 1:
                    self.attack()

                elif tmp == 2 :
                    self.standstill()

                if self.get_hit :
                    self.Geting_hit()

                if self.health <= 0:
                    self.die()
                pygame.draw.rect(self.gameplay.screen,White,self.box,1)
                pygame.draw.rect(self.gameplay.screen,White,self.imgbox,1)

