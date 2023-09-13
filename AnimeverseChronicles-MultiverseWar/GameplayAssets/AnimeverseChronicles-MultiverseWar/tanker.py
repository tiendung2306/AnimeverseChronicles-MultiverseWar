import pygame 
from pygame.locals import *
from collide_checker import *
from object_function import *
from clock import *
from switch import *
from animation_player import *
from screen import *


class tankerclass():
    def __init__(self, side, gameplay):
        self.pre_status = None
        self.status  = None
        self.box = pygame.Rect(0,0,0,0)
        self.imgbox = pygame.Rect(0,0,0,0)
        self.gameplay = gameplay
        if side == 1 :
            self.side = 1
        elif side == 2:
            self.side = -1

        self.speed = 5.0 # 1/100 map per second 
        self.attack_scope = 1 * self.gameplay.box_size[0]   # 4/15 map width
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
        self.ischeck = True
        self.iscollide_check = True
        self.collide = None
        self.special_status = False

        self.moving_animation = animation_player([tanker13,tanker14,tanker15,tanker16,tanker17,tanker18,tanker19], self.side, 1, self.imgbox , self.gameplay)
        self.attacking_animation = one_time_animation_player([tanker23,tanker24,tanker25,tanker26,tanker27,tanker28,tanker29,tanker30,tanker31],self.side, 1 , self.imgbox, self.gameplay)
        self.defending_animation = one_time_animation_player( [tanker20,tanker21,tanker22,tanker21], self.side, 1, self.imgbox, self.gameplay)
        self.standstill_animation = one_time_animation_player([tanker1,tanker2,tanker3,tanker4],self.side, 1, self.imgbox, self.gameplay)
        self.dying_animation = one_time_animation_player([tanker32,tanker33,tanker34,tanker35,tanker36,tanker37,tanker38,tanker38,tanker38,tanker38], self.side, 0.8, self.imgbox, self.gameplay)
        self.knock_back_animation = animation_player([tanker34], self.side, 1, self.imgbox, self.gameplay)
        self.flying_animation = animation_player([tanker32,tanker32], self.side, 1, self.imgbox, self.gameplay)
        self.falling_animation = animation_player([tanker34], self.side, 1, self.imgbox, self.gameplay)

        self.switcher1 = N_time_switch(1)
        self.switcher2 = N_time_switch(1)
        self.switcher3 = N_time_switch(1)
        self.switcher4 = N_time_switch(1)
        self.switcher5 = N_time_switch(1)
        self.attack_coundowner = timing_clock(1 / self.attack_speed, self.gameplay)

        self.skill_countdowner = timing_clock(3, self.gameplay)


    def resize(self):
        a = float(screen.screen.get_width()) / self.gameplay.screen[0]
        b = float(screen.screen.get_height()) /  self.gameplay.screen[1]
        tmp = pygame.Rect(self.imgbox.left * a, self.imgbox.top * b, self.imgbox.width * a, self.imgbox.height * b)
        copy(self.imgbox, tmp)
        self.operation()

        
    def status_update(self):
        self.collide = None 
        self.pre_status = self.status

        if self.pre_status == 1:
            if self.attacking_animation.status == True:
                self.ischeck = False
            elif self.attacking_animation.status == False:
                self.ischeck = True
                self.attack_reset()
        elif self.pre_status == 2:
            if self.standstill_animation.status == True:
                self.ischeck = False
            elif self.standstill_animation.status == False:
                self.ischeck = True           
                self.standsill_reset()


    def display(self):
        copy(self.box, self.animation_player.play())
        pygame.draw.rect(screen.screen,Red,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 10 ,(self.box.width - self.box.width / 2) / self.health_max *self.health,self.box.height / 20))
        pygame.draw.rect(screen.screen,Blue,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 5 - self.box.height / 30 ,(self.box.width - self.box.width / 2) / self.mana_max *self.mana,self.box.height / 20))
        
    
    def move(self):
        self.animation_player = self.moving_animation
        self.imgbox.centerx += (self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  * self.side

    def move_reset(self):
        self.moving_animation.reset()

    def standstill(self):
        self.animation_player = self.standstill_animation


    def standsill_reset(self):
        self.standstill_animation.reset()
    
    
    def check_collide(self):
        if self.iscollide_check:
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
        if self.ischeck :
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
                    if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 2  + 5 *(self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time) + (self.box.width + object.box.width) / 2:
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                if abs(object.box.centerx  - self.box.centerx ) >= self.gameplay.box_size[0] / 2  + (self.box.width + object.box.width) / 2:
                                        self.imgbox.centerx += 5 *(self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time) * self.side
                                        self.box.centerx += 5 *(self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  *self.side
                                        self.status = 2
                                        flag = True
                                elif not (self == object):
                                    self.status = 2
                                    flag = True
                                    break

                for object in self.gameplay.side( - self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 2  + 5 *(self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time) + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                if abs(object.box.centerx  - self.box.centerx ) >= self.gameplay.box_size[0] / 2  + (self.box.width + object.box.width) / 2:
                                        self.imgbox.centerx += 5 *(self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time) * self.side
                                        self.box.centerx += 5 *(self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time) * self.side 
                                        self.status = 4
                                        flag = True
                                else:
                                    self.status = 1
                                    flag = True
                                    break          
            if not flag:
                self.status = 3

            
            if self.status == 1 :
                if self.attack_coundowner.Return == True:
                    self.status = 4

        if self.mana >= self.mana_max:
            self.mana = 0
            self.special_status = True

        if self.status > 0:
            if not self.pre_status == None:
                if self.pre_status > 0:
                    if not self.pre_status == self.status:            
                        if self.pre_status == 1:
                            self.attack_reset()
                        elif self.pre_status == 2:
                            self.standsill_reset()
                        elif self.pre_status == 3:
                            self.move_reset()
                        elif self.pre_status == 4:
                            self.defend_reset()

                



    def Geting_hit(self):
        self.get_hit = False
        self.health -= self.get_damage - self.get_damage * self.damage_reduce / 100
        self.get_damage = 0
        if not self.special_status:
            self.mana += 10


    def dying(self):
        if self.switcher4.operation():
            self.moving_animation.remove()
            self.attacking_animation.remove()
            self.standstill_animation.remove()      
            self.falling_animation.remove()
            self.flying_animation.remove()
            self.knock_back_animation.remove()

            self.gameplay.side(self.side).remove(self)
            self.side = 0
            self.gameplay.side0.append(self)
            
        self.dying_animation.play()
        if self.dying_animation.status == False:
            self.dying_animation.remove()
            self.gameplay.side0.remove(self)



    def attack(self):
        if self.switcher5.operation():
            self.attack_coundowner.reset()
            self.attack_coundowner.start()
            
        self.animation_player = self.attacking_animation
        if self.attacking_animation.clock.Return == 5 or self.attacking_animation.clock.Return == 8 :
            if self.switcher1.operation():
                if not self.special_status :
                    self.mana += 10     
                for object in self.gameplay.side(- self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                object.get_hit = True
                                object.get_damage = self.attack_damage
        elif self.attacking_animation.clock.Return == 4 or self.attacking_animation.clock.Return == 7 :
            self.switcher1.reset()


            

    def attack_reset(self):
        self.attacking_animation.reset() 
        self.switcher5.reset()


    def defend(self):
        if not self.status == self.pre_status:
            self.defending_animation.reset()
        self.animation_player = self.defending_animation
        if self.defending_animation.status == True:
            self.ischeck = False
        elif self.defending_animation.status == False:
            self.ischeck = True
            self.defend_reset()

    def defend_reset(self):
        self.defending_animation.reset()

    def special_skill(self):
        if self.switcher2.operation():
            self.damage_reduce = self.damage_reduce_special
            self.skill_countdowner.start()
        if self.skill_countdowner.Return == False:
            self.special_skill_reset()

    def special_skill_reset(self):
        self.damage_reduce = 0
        self.special_status = False
        self.switcher2.reset()
        self.skill_countdowner.reset()            


    def operation(self):
        if self.alive:
            for effect in self.effect_list:
                effect.play()
            
            self.check_collide()
            self.check_forward()
            
            if self.status == 3:
                self.move()

            elif self.status == 1:
                self.attack()

            elif self.status == 2 :
                self.standstill()

            elif self.status == 4:
                self.defend()

            if self.special_status:
                self.special_skill()

            if self.get_hit :
                self.Geting_hit()

            if self.health <= 0:
                self.alive = False
                

            self.display()
            self.status_update()


            pygame.draw.rect(screen.screen,White,self.box,1)
            pygame.draw.rect(screen.screen,White,self.imgbox,1)
        else:
            self.dying()


