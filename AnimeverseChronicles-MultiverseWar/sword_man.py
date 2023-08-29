import pygame 
from pygame.locals import *
from color import *
from collide_checker import *
from fake_object import *
from clock import *
from switch import *
from list_function import *
from animation_player import *
from screen import *


class sword_manclass():
    def __init__(self,side,box_number,gameplay):
        self.gameplay = gameplay
        self.box = pygame.Rect(box_number * self.gameplay.box_size[0],self.gameplay.path_height - self.gameplay.box_size[1], self.gameplay.box_size[0], self.gameplay.box_size[1])

        if side == 1 :
            self.side = 1
            self.imgbox = sword_man1.hitbox_to_imgbox(self.box)        
        elif side == 2:
            self.side = -1
            self.imgbox = reverse(sword_man1).hitbox_to_imgbox(self.box)    
            
        self.speed = 5.0 # 5/100 map per second 
        self.attack_scope = 1 * self.gameplay.box_size[0] # 4/15 map width
        self.attack_speed = 1/3 # attack(s) pers second
        self.attack_damage = 30.0
        self.attack_damage_orginal = self.attack_damage
        self.health_max = 100.0
        self.health = self.health_max 
        self.mana_max =100.0
        self.mana = 0.0

        self.effect_list = []

        self.alive = True
        self.get_hit = False
        self.special_status = False

        self.moving_animation = animation_player([sword_man1,sword_man2,sword_man3,sword_man4,sword_man5,sword_man6,sword_man7,sword_man8,sword_man9,sword_man10], self.side,1, self.imgbox , self.gameplay)
        tmp_lib = [sword_man31,sword_man32,sword_man33,sword_man34,sword_man35,sword_man36,sword_man37,sword_man38]
        for i in range(2):
            for img in [sword_man11,sword_man12,sword_man13,sword_man14,sword_man15,sword_man16,sword_man17,sword_man18]:
                for counter in range(2):
                    tmp_lib.append(img)
    
        self.attacking_animation = animation_player(tmp_lib, self.side, 1 / self.attack_speed, self.imgbox, self.gameplay)
        self.special_skill_animation = one_time_animation_player([sword_man19,sword_man20,sword_man21,sword_man22,sword_man23,sword_man24,sword_man25,sword_man26,sword_man27,sword_man28,sword_man29,sword_man30], self.side, 1, self.imgbox, self.gameplay)
        self.standstill_animation = animation_player([sword_man11,sword_man12,sword_man13,sword_man14,sword_man15,sword_man16,sword_man17,sword_man18],self.side, 1, self.imgbox, self.gameplay)

        self.switcher1 = N_time_switch(1)
        self.switcher2 = N_time_switch(1)
        self.switcher3 = N_time_switch(1)
        self.direct = False


    def status_bar(self):
        pygame.draw.rect(screen.screen,Red,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 10 ,(self.box.width - self.box.width / 2) / self.health_max *self.health,self.box.height / 20))
        pygame.draw.rect(screen.screen,Blue,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 5 - self.box.height / 30 ,(self.box.width - self.box.width / 2) / self.mana_max *self.mana,self.box.height / 20))
        

    def move(self):
        if self.switcher3.operation():
            self.time_flag = self.gameplay.curr_time
            self.spam_pointX = ( self.imgbox.left + self.imgbox.right) / 2

        else:
            self.box = self.moving_animation.play()
            self.imgbox.centerx = self.spam_pointX + (self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.time_flag)  * self.side
        self.standstill_animation.reset()
        self.attacking_animation.reset()


    def standstill(self):
        self.box = self.standstill_animation.play()
        self.moving_animation.reset()
        self.attacking_animation.reset()
        self.switcher3.reset()

    
    
    def check_forward(self):
        checker = fake_object_class(self)
        if self.side == 1:
            checker.box = sword_man1.imgbox_to_hitbox(self.imgbox)
            checker.box.width *= 2
            # pygame.draw.rect(screen.screen,Red,checker.box)
            for object in self.gameplay.side2 :
                if collide_checker(checker,object):
                    self.status = 1
                    return None
            checker.box.width *= 1 / 2
            for object in self.gameplay.side1:
                if collide_checker(checker,object):
                        if (not (object == self)) and (object.box.left >= self.box.left):
                            self.status = 2
                            return None

        elif self.side == -1:
            checker.box = reverse(sword_man1).imgbox_to_hitbox(self.imgbox)
            checker.box.width *= 2
            checker.box.centerx -= checker.box.width / 2
            # pygame.draw.rect(self.gameplay.screen,White,checker.box)
            for object in self.gameplay.side1 :
                if collide_checker(checker,object):
                    self.status = 1
                    return None            
            checker.box.centerx += checker.box.width / 2
            checker.box.width *= 1/ 2
            for object in self.gameplay.side2:
                if collide_checker(checker,object):
                    if (not (object == self)) and (object.box.left <= self.box.left) :
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
        if self.side == 1:
            self.gameplay.side1.remove(self)
        elif self.side == -1:
            self.gameplay.side2.remove(self)
        self.moving_animation.remove()
        self.attacking_animation.remove()
        self.standstill_animation.remove()
        self.alive = False

    
    def attack(self):
        if self.special_status:
            self.special_skill()
            self.box = self.special_skill_animation.play()
            if self.special_skill_animation.clock.Return == 4 or self.special_skill_animation.clock.Return == 9 :     
                if self.switcher1.operation():
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
            elif self.special_skill_animation.clock.Return == 5:
                self.switcher1.reset()

            elif self.special_skill_animation.clock.Return == 12:
                self.switcher1.reset()
                self.special_skill_reset()
                self.attacking_animation.reset()

        else:
            self.box = self.attacking_animation.play()
            if self.attacking_animation.clock.Return == 4:     
                if self.switcher1.operation():
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
            elif self.attacking_animation.clock.Return == 1:             
                self.switcher1.reset()
                if self.mana >= self.mana_max:
                    self.mana = 0
                    self.special_status = True
                            
            self.standstill_animation.reset()
            self.moving_animation.reset()
            self.switcher3.reset()


    def special_skill(self):
            if self.switcher2.operation():
                self.attack_damage += 3 
                self.health += (self.health_max - self.health) / 5

    def special_skill_reset(self):
            self.switcher2.reset()
            self.attack_damage = self.attack_damage
            self.special_status = False


    def operation(self):
        if self.alive:
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

            if self.health <= 0:
                self.die()
            # pygame.draw.rect(screen.screen,White,self.box,1)
            # pygame.draw.rect(screen.screen,White,self.imgbox,1)



