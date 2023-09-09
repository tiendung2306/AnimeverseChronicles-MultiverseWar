import pygame 
from pygame.locals import *
from collide_checker import *
from object_function import *
from clock import *
from switch import *
from list_function import *
from animation_player import *
from screen import *


class sword_manclass():
    def __init__(self,side,gameplay):
        self.pre_status = None
        self.status  = None
        self.box = pygame.Rect(0,0,0,0)
        self.imgbox = pygame.Rect(0,0,0,0)
        self.gameplay = gameplay
        if side == 1 :
            self.side = 1
        elif side == 2:
            self.side = -1   
        
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
        self.check = False
        self.collide = None
        self.special_status = False

        self.moving_animation = animation_player([sword_man1,sword_man2,sword_man3,sword_man4,sword_man5,sword_man6,sword_man7,sword_man8,sword_man9,sword_man10], self.side,1, self.imgbox , self.gameplay)
        self.attacking_animation = one_time_animation_player([sword_man31,sword_man32,sword_man33,sword_man34,sword_man35,sword_man36,sword_man37,sword_man38], self.side, 0.5 , self.imgbox, self.gameplay)
        self.special_skill_animation = one_time_animation_player([sword_man19,sword_man20,sword_man21,sword_man22,sword_man23,sword_man24,sword_man25,sword_man26,sword_man27,sword_man28,sword_man29,sword_man30], self.side, 1, self.imgbox, self.gameplay)
        self.standstill_animation = one_time_animation_player([sword_man11,sword_man12,sword_man13,sword_man14,sword_man15,sword_man16,sword_man17,sword_man18],self.side, 1, self.imgbox, self.gameplay)  
        self.dying_animation = one_time_animation_player([sword_man50], self.side, 0.8, self.imgbox, self.gameplay)
        self.knock_back_animation = animation_player([sword_man39], self.side, 1, self.imgbox, self.gameplay)
        self.flying_animation = animation_player([sword_man41], self.side, 1, self.imgbox, self.gameplay)
        self.falling_animation = animation_player([sword_man40], self.side, 1, self.imgbox, self.gameplay)

        self.switcher1 = N_time_switch(1)
        self.switcher2 = N_time_switch(1)

        self.attack_coundowner = timing_clock(1 / self.attack_speed, self.gameplay)


    def resize(self):
        a = float(screen.screen.get_width()) / self.gameplay.screen[0]
        b = float(screen.screen.get_height()) /  self.gameplay.screen[1]
        tmp = pygame.Rect(self.imgbox.left * a, self.imgbox.top * b, self.imgbox.width * a, self.imgbox.height * b)
        copy(self.imgbox, tmp)
        self.operation()

 
    def status_update(self):
        if self.mana >= self.mana_max:
            self.mana = 0
            self.special_status = True
        pygame.draw.rect(screen.screen,Red,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 10 ,(self.box.width - self.box.width / 2) / self.health_max *self.health,self.box.height / 20))
        pygame.draw.rect(screen.screen,Blue,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 5 - self.box.height / 30 ,(self.box.width - self.box.width / 2) / self.mana_max *self.mana,self.box.height / 20))
        

    def move(self):
        if not self.status == self.pre_status:
            self.moving_animation.reset()
        copy(self.box, self.moving_animation.play())
        self.imgbox.centerx += (self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  * self.side




    def standstill(self):
        if not self.status == self.pre_status:
            self.standstill_animation.reset()
        copy(self.box, self.standstill_animation.play())
        if self.standstill_animation.status == True:
            self.check = False
        elif self.standstill_animation.status == False:
            self.check = True
            self.standstill_animation.reset()

    
    
    def check_collide(self):
        if self.collide == None:
            for object in self.gameplay.side(self.side) + self.gameplay.side4 + self.gameplay.side(- self.side):
                if (object.box.centerx - self.box.centerx) * self.side >= 0:
                    if same_line_checker(self, object):
                        if not (self == object):
                            if collide_checker(self ,object):
                                if self.side == object.side:
                                    self.collide = 1
                                    object.collide = 1
                                else:
                                    self.collide = 2
                                    object.collide = 2

                                if not (self.box.centerx == object.box.centerx and self.index < object.index and self.side == object.side ):
                                    self.collide = True
                                    self.imgbox.centerx -= ( 5.0 * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time) * self.side
                                    self.box.centerx -= ( 5.0 * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  *self.side
                                    return
            self.collide = False


    def check_forward(self): #always after check_collide
        flag = False
        if self.collide == 2:
            self.status = 1
            flag = True

        elif self.collide == 1:
            for object in self.gameplay.side(- self.side) :
                if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2 :
                    if (object.box.centerx - self.box.centerx) * self.side >= 0:
                        if same_line_checker(self, object):
                            self.status = 1
                            flag = True
                            break
            self.status = 2
            flag = True
        else:
            for object in self.gameplay.side(self.side) + self.gameplay.side4 :
                if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 2 + (self.box.width + object.box.width) / 2:
                    if (object.box.centerx - self.box.centerx) * self.side >= 0:
                        if same_line_checker(self, object):
                            if not (self == object):
                                self.status = 2
                                flag = True
                                break

            for object in self.gameplay.side( - self.side) :
                if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2 :
                    if (object.box.centerx - self.box.centerx) * self.side >= 0:
                        if same_line_checker(self, object):
                            self.status = 1
                            flag = True
                            break          
        if not flag:
            self.status = 3
        
        if self.status == 1 :
            if self.attack_coundowner.Return == True:
                self.status = 2
            elif self.special_status:
                self.status = 4
            

        

    def Geting_hit(self):
        self.get_hit = False
        self.health -= self.get_damage 
        self.get_damage = 0
        if not self.special_status:
            self.mana += 10


    def die(self):
        self.alive = False
        self.moving_animation.remove()
        self.attacking_animation.remove()
        self.standstill_animation.remove()      
        self.falling_animation.remove()
        self.flying_animation.remove()
        self.knock_back_animation.remove()

        self.gameplay.side(self.side).remove(self)
        self.side = 0
        self.gameplay.side0.append(self)

    
    def attack(self):
        if (not self.status == self.pre_status) or (not self.attack_coundowner.Return == True ) :
            self.attacking_animation.reset() 
            self.attack_coundowner.reset()
            self.attack_coundowner.start()
            
        copy(self.box, self.attacking_animation.play())
        if self.attacking_animation.clock.Return == 4:
            if self.switcher1.operation():
                self.mana += 10 
                for object in self.gameplay.side(- self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                object.get_hit = True
                                object.get_damage = self.attack_damage
        elif self.attacking_animation.clock.Return == 3:
            self.switcher1.reset()

        if self.attacking_animation.status == True:
            self.check = False
        elif self.attacking_animation.status == False:
            self.check = True
            self.attacking_animation.reset() 

    

    def special_skill(self):
        if not self.status == self.pre_status:
            self.attacking_animation.reset() 
            
        copy(self.box, self.special_skill_animation.play())
        self.attack_damage = 2 * self.attack_damage_orginal
        if self.special_skill_animation.clock.Return == 3 or self.special_skill_animation.clock.Return == 8:
            if self.switcher1.operation():
                for object in self.gameplay.side(- self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                self.health += (self.health_max - self.health) / 5
                                object.get_hit = True
                                object.get_damage = self.attack_damage
        elif self.special_skill_animation.clock.Return == 2 or self.special_skill_animation.clock.Return == 7:
            self.switcher1.reset()

        if self.special_skill_animation.status == True:
            self.check = False
        elif self.special_skill_animation.status == False:
            self.special_skill_animation.reset() 
            self.special_status = False
            self.check = True
        self.attack_damage = self.attack_damage_orginal


    def operation(self):
        if self.alive:
            for effect in self.effect_list:
                effect.play()
            if self.get_hit :
                self.Geting_hit()
            self.status_update()
            if self.health <= 0:
                self.die()
                return
            
            elif self.status > 0:
                self.check = True
                self.collide = False
                if self.status == 3:
                    self.move()

                elif self.status == 1:
                    self.attack()

                elif self.status == 2 :
                    self.standstill()

                elif self.status == 4:
                    self.special_skill()

                self.pre_status = self.status

            if self.status > 0:
                if self.check:
                    self.check_forward()
                self.check_collide()
                self.collide = None

            # pygame.draw.rect(screen.screen,White,self.box,1)
            # pygame.draw.rect(screen.screen,White,self.imgbox,1)
        else:
            self.dying_animation.play()
            if self.dying_animation.status == False:
                self.dying_animation.remove()
                self.gameplay.side0.remove(self)


