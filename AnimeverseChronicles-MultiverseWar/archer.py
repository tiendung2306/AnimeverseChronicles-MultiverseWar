import pygame 
from pygame.locals import *
from collide_checker import *
from object_function import *
from clock import *
from switch import *
from list_function import *
from animation_player import *
from screen import *

   

class arrowclass():
    def __init__(self,archer):
        self.archer = archer
        self.gameplay = self.archer.gameplay
        self.side = self.archer.side

        self.imgbox = pygame.Rect(self.archer.imgbox.left,self.archer.imgbox.top,self.archer.imgbox.width,self.archer.imgbox.height)
        if self.side == 1:
            self.box = arrow.imgbox_to_hitbox(self.imgbox)
            self.img = arrow
        elif self.side == -1:
            self.box = reverse(arrow).imgbox_to_hitbox(self.imgbox)
            self.img = reverse(arrow)

        self.time_flag = self.archer.gameplay.curr_time 

        self.piercing = self.archer.piercing
        self.speed = 30.0  # 10/100 map per second
        self.damage = self.archer.attack_damage
        self.special = self.archer.special_status 

        self.damaged_object = []
        if self.piercing :
            if self.side == 1:
                self.x_limit = self.archer.box.right + self.archer.attack_scope * 2
                self.img = special_arrow
            elif self.side == -1:
                self.img = reverse(special_arrow)
                self.x_limit = self.archer.box.left - self.archer.attack_scope * 2

    def resize(self):
        a = float(screen.screen.get_width()) / self.gameplay.screen[0]
        b = float(screen.screen.get_height()) /  self.gameplay.screen[1]
        tmp = pygame.Rect(self.imgbox.left * a, self.imgbox.top * b, self.imgbox.width * a, self.imgbox.height * b)
        copy(self.imgbox, tmp)
        self.operation()


    def move(self):
        self.imgbox.centerx += (self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  * self.side

    def remove(self):
        self.archer.arrow_list.remove(self)

    def collide_check(self):
        for enemy_object in self.archer.gameplay.side( - self.side):
            if collide_checker(self,enemy_object):
                if list_find(self.damaged_object,enemy_object) == -1:
                    self.damaged_object.append(enemy_object)
                    enemy_object.get_damage = self.damage
                    enemy_object.get_hit = True
                    return True
        return False
        


    def limit_check(self):
        if (len(self.damaged_object) == 3) or ((self.x_limit - self.box.centerx) * self.side <= self.box.width / 2):
            return True

    def operation(self):
        screen.screen.blit(pygame.transform.smoothscale(self.img.img,(self.imgbox.width,self.imgbox.height)),self.imgbox)
        copy(self.box, self.img.imgbox_to_hitbox(self.imgbox))
        self.move()
        if self.piercing == True:
            if self.limit_check():
                self.remove
            else:
                self.collide_check()

        else:
            if self.collide_check():
                if not self.special:
                    self.archer.mana += 10
                self.remove()



class archerclass():
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
            
        self.skill_lasting_time = 4.0
        self.speed = 5.0 # 5/100 map per second 
        self.attack_scope = 4 * self.gameplay.box_size[0] # 4/15 map width
        self.attack_scope_orginal = self.attack_scope
        self.attack_speed = 1/2 # arrow(s) pers second
        self.attack_speed_orginal = self.attack_speed
        self.attack_damage = 10.0
        self.attack_damage_orginal = self.attack_damage
        self.health_max = 100.0
        self.health = self.health_max
        self.mana_max =100.0
        self.mana = 0.0

        self.arrow_list = []
        self.effect_list = []

        self.alive = True
        self.get_hit = False
        self.check = False
        self.collide = None
        self.special_status = False
        self.piercing = False


        self.moving_animation = animation_player([archer1,archer2,archer3,archer4,archer5,archer6,archer7,archer8,archer9,archer10],self.side, 1, self.imgbox , self.gameplay)
        self.attacking_animation = one_time_animation_player([archer17,archer18,archer19,archer20,archer21,archer22,archer23,archer24,archer25,archer26,archer27,archer28,archer29,archer30],self.side, 1 , self.imgbox, self.gameplay)
        self.standstill_animation = one_time_animation_player([archer11,archer12,archer13,archer14,archer15,archer16],self.side, 1, self.imgbox, self.gameplay)
        self.dying_animation = one_time_animation_player([archer40], self.side, 0.8, self.imgbox, self.gameplay)
        self.knock_back_animation = animation_player([archer31], self.side, 1, self.imgbox, self.gameplay)
        self.flying_animation = animation_player([archer32], self.side, 1, self.imgbox, self.gameplay)
        self.falling_animation = animation_player([archer33], self.side, 1, self.imgbox, self.gameplay)

        self.switcher1 = N_time_switch(1)
        self.switcher2 = N_time_switch(1)
        self.switcher3 = N_time_switch(1)


        self.skill_countdowner = timing_clock(self.skill_lasting_time,self.gameplay)
        self.attack_coundowner = timing_clock(1 / self.attack_speed, self.gameplay)


    def resize(self):
        a = float(screen.screen.get_width()) / self.gameplay.screen[0]
        b = float(screen.screen.get_height()) /  self.gameplay.screen[1]
        tmp = pygame.Rect(self.imgbox.left * a, self.imgbox.top * b, self.imgbox.width * a, self.imgbox.height * b)
        copy(self.imgbox, tmp)
        self.operation()

        for arrows in self.arrow_list:
            arrows.resize()


    def status_update(self):
        if self.mana >= self.mana_max:
            self.mana = 0
            self.special_status = True
        if self.special_status:
            self.special_skill()        
        
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
        if self.attacking_animation.clock.Return == 9:
            if self.switcher1.operation():
                self.arrow_list.append(arrowclass(self))  

        elif self.attacking_animation.clock.Return == 8:
            self.switcher1.reset()

        if self.attacking_animation.status == True:
            self.check = False
        elif self.attacking_animation.status == False:
            self.check = True
            self.attacking_animation.reset() 


    
    def special_skill(self):
        if self.switcher2.operation():
            self.piercing = True
            self.attack_damage *= 2 
            self.attack_scope = 7 * self.gameplay.box_size[0]
            self.flag = len(self.arrow_list)

        if len(self.arrow_list) == self.flag + 1:
            if self.switcher3.operation():
                self.piercing = False
                self.attack_damage = self.attack_damage_orginal
                self.attack_scope = self.attack_scope_orginal
                self.attack_speed = self.attack_speed * 2
                self.attack_coundowner.update_lasting_time(1 / self.attack_speed)
                if 1 / self.attack_speed <= 1 :
                    self.attacking_animation.update_looptime( 1 / self.attack_speed )
                self.skill_countdowner.start()

            if self.skill_countdowner.Return == False:
                self.special_status = False
                self.switcher2.reset()
                self.switcher3.reset()
                self.attack_speed = self.attack_speed_orginal
                self.attacking_animation.update_looptime(1)
                self.attack_coundowner.update_lasting_time(1 / self.attack_speed)
                self.skill_countdowner.reset()



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
                if self.status == 3:
                    self.move()

                elif self.status == 1:
                    self.attack()

                elif self.status == 2 :
                    self.standstill()

                for arrows in self.arrow_list:
                    arrows.operation()

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


    






