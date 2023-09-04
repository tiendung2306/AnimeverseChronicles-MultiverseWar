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


class tankerclass():
    def __init__(self,side,box_number,gameplay):
        self.gameplay = gameplay
        self.size = (self.gameplay.box_size[0] / 1.65, (self.gameplay.box_size[0] / 1.65 * tanker5.data[3] )/ tanker5.data[2] )
        self.box = pygame.Rect(box_number * self.gameplay.box_size[0],self.gameplay.path_height - self.size[1] * 4 / 5, self.size[0], self.size[1])
        if side == 1 :
            self.side = 1
            self.imgbox = tanker5.hitbox_to_imgbox(self.box)        
        elif side == 2:
            self.side = -1
            self.imgbox = reverse(tanker5).hitbox_to_imgbox(self.box)   

        self.speed = 5.0 # 1/100 map per second 
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

        self.moving_animation = animation_player([tanker13,tanker14,tanker15,tanker16,tanker17,tanker18,tanker19], self.side, 1, self.imgbox , self.gameplay)
        tmp_lib = [tanker23,tanker24,tanker25,tanker26,tanker27,tanker28,tanker29,tanker30,tanker31]
        for i in range(6):
            for img in [tanker20,tanker21,tanker22,tanker21]:
                for counter in range(2):
                    tmp_lib.append(img)
        
        self.attacking_animation = animation_player(tmp_lib,self.side, 1 / self.attack_speed, self.imgbox, self.gameplay)
        self.standstill_animation = animation_player([tanker1,tanker2,tanker3,tanker4],self.side, 1, self.imgbox, self.gameplay)
        self.dying_animation = one_time_animation_player([tanker32,tanker33,tanker34,tanker35,tanker36,tanker37,tanker38,tanker38,tanker38,tanker38], self.side, 0.8, self.imgbox, self.gameplay)

        self.switcher1 = N_time_switch(1)
        self.switcher2 = N_time_switch(1)
        self.switcher3 = N_time_switch(1)

        self.skill_countdowner = timing_clock(3,self.gameplay)

    def resize(self):
        a = float(screen.screen.get_width()) / self.gameplay.screen[0]
        b = float(screen.screen.get_height()) /  self.gameplay.screen[1]
        tmp_box = pygame.Rect(self.box.left * a, self.box.top *  b, self.box.width * a, self.box.height * b)
        self.size = (self.gameplay.box_size[0] / 1.65, (self.gameplay.box_size[0] / 1.65 * tanker5.data[3] )/ tanker5.data[2] )
        fake_box = pygame.Rect( self.gameplay.box_size[0],self.gameplay.path_height - self.size[1] * 4 / 5, self.size[0], self.size[1])
        fake_imgbox = tanker5.hitbox_to_imgbox(fake_box)
        self.imgbox.left *= a
        self.imgbox.top = fake_imgbox.top
        self.imgbox.width = fake_imgbox.width
        self.imgbox.height = fake_imgbox.height
        self.box.top = tmp_box.top
        self.box.left = tmp_box.left
        self.box.width = tmp_box.width
        self.box.height = tmp_box.height


    def status_bar(self):
        if self.mana >= self.mana_max:
            self.mana = 0
            self.special_status = True
        if self.special_status:
            self.special_skill()
            if self.skill_countdowner.Return == False:
                self.special_skill_reset()
   
        pygame.draw.rect(screen.screen,Red,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 10 ,(self.box.width - self.box.width / 2) / self.health_max *self.health,self.box.height / 20))
        pygame.draw.rect(screen.screen,Blue,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 5 - self.box.height / 30 ,(self.box.width - self.box.width / 2) / self.mana_max *self.mana,self.box.height / 20))
    
    
    def move(self):
        self.standstill_animation.reset()
        self.attacking_animation.reset()
        copy(self.box, self.moving_animation.play())
        self.imgbox.centerx += (self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  * self.side


    def standstill(self):
        copy(self.box, self.standstill_animation.play())
        self.moving_animation.reset()
        self.attacking_animation.reset()
    
    
    def check_forward(self):
        checker = fake_object_class(self)
        if self.side == 1:
            checker.box = tanker1.imgbox_to_hitbox(self.imgbox)
            checker.box.width *= 2
            # pygame.draw.rect(screen.screen,Red,checker.box)
            for object in self.gameplay.side2 :
                if collide_checker(checker,object):
                    self.status = 1
                    return None

            for object in self.gameplay.side1 + self.gameplay.side4:
                if collide_checker(checker ,object):
                    if (not (object == self)) and (object.box.right > checker.box.right):
                        self.status = 2
                        return None

        elif self.side == -1:
            checker.box = reverse(tanker1).imgbox_to_hitbox(self.imgbox)
            checker.box.width *= 2
            checker.box.centerx -= checker.box.width / 2
            # pygame.draw.rect(self.gameplay.screen,White,checker.box)
            for object in self.gameplay.side1 :
                if collide_checker(checker,object):
                    self.status = 1
                    return None

            for object in self.gameplay.side2 + self.gameplay.side4:
                if collide_checker(checker,object):
                    if (not (object == self)) and (object.box.left < checker.box.left) :
                        self.status = 2
                        return None
        self.status = 3


    def Geting_hit(self):
        self.get_hit = False
        self.health -= self.get_damage 
        self.get_damage = 0
        if not self.special_status:
            self.mana += 10


    def die(self):
        if not self.side == 0:
            if self.side == 1:
                self.gameplay.side1.remove(self)
            elif self.side == -1:
                self.gameplay.side2.remove(self)
            self.side = 0
            self.gameplay.side0.append(self)
            self.moving_animation.remove()
            self.attacking_animation.remove()
            self.standstill_animation.remove()      
            self.skill_countdowner.remove()         
        else:
            if self.dying_animation.play():
                self.alive = False
                self.gameplay.side0.remove(self)



    def attack(self):
        copy(self.box, self.attacking_animation.play())
        if self.attacking_animation.clock.Return == 5 or self.attacking_animation.clock.Return == 8:
            if self.switcher1.operation():

                if not self.special_status :
                    self.mana += 10 
                        
                checker = fake_object_class(self)
                checker.box.width += self.attack_scope 
                if self.side == 1:
                    for enemy_object in self.gameplay.side2:
                    # pygame.draw.rect(screen.screen,White,checker.box)
                        if collide_checker(checker,enemy_object):
                                enemy_object.get_hit = True
                                enemy_object.get_damage = self.attack_damage
                elif self.side == -1:
                    checker.box.centerx -= self.attack_scope 
                    # pygame.draw.rect(screen.screen,White,checker.box)
                    for enemy_object in self.gameplay.side1:
                        if collide_checker(checker,enemy_object):
                                enemy_object.get_hit = True
                                enemy_object.get_damage = self.attack_damage
        elif self.attacking_animation.clock.Return == 7:
            self.switcher1.reset()

        elif self.attacking_animation.clock.Return == 1:     
            self.switcher1.reset()
        self.standstill_animation.reset()
        self.moving_animation.reset()


    def special_skill(self):
            if self.switcher2.operation():
                self.damage_reduce = self.damage_reduce_special
                self.skill_countdowner.start()


    def special_skill_reset(self):
            self.damage_reduce = 0
            self.special_status = False
            self.switcher2.reset()
            self.skill_countdowner.reset()


    def operation(self):
            if self.alive:
                if self.health <= 0:
                    self.die()
                    return None
                self.status_bar()
                self.check_forward()

                for effect in self.effect_list:
                    effect.play()

                if self.status == 3:
                    self.move()

                elif self.status == 1:
                    self.attack()

                elif self.status == 2 :
                    self.standstill()

                if self.get_hit :
                    self.Geting_hit()

                # pygame.draw.rect(screen.screen,White,self.box,1)
                # pygame.draw.rect(screen.screen,White,self.imgbox,1)

