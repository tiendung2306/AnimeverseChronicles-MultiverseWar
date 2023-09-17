import pygame 
from pygame.locals import *
from collide_checker import *
from object_function import *
from clock import *
from switch import *
from list_function import *
from animation_player import *
from screen import *
from common_effect import *

class getting_hit_object():
    def __init__(self, object):
        self.object = object
        self.clock = timing_clock(0.1, object.gameplay)
        self.clock.start()

class rasenshuriken():
    def __init__(self, naruto) :
        self.naruto = naruto
        self.pre_status = None
        self.status  = True
        self.imgbox = pygame.Rect(0,0,0,0)
        copy(self.imgbox, self.naruto.imgbox)
        self.box = rasenshuriken1.imgbox_to_hitbox(self.imgbox)
        self.gameplay = naruto.gameplay
        self.side = naruto.side
        
        self.speed = 15.0 # 5/100 map per second 
        self.x_limit = (self.naruto.box.centerx + (self.gameplay.box_size[0] * 20) * self.side )/ screen.screen.get_width()
        self.lasting_time = ( self.x_limit * screen.screen.get_width() - self.box.centerx ) * self.side / (self.speed * screen.screen.get_rect().width / 100) 
        self.damage = 3.0
        self.damaged_list = []
        self.effectted_list = []

        self.direct = True
        self.direct2 = True

        self.moving_animation = animation_player([rasenshuriken1, rasenshuriken2, rasenshuriken3, rasenshuriken4, rasenshuriken5, rasenshuriken6],self.side, 0.1, self.imgbox,self.gameplay)
        self.explosion_animation1 = one_time_animation_player([explosion_stage_1_1, explosion_stage_1_2, explosion_stage_1_3, explosion_stage_1_4],self.side,0.33,self.imgbox,self.gameplay)
        self.explosion_animation2 = one_time_animation_player([explosion_stage_2_1, explosion_stage_2_2, explosion_stage_2_1, explosion_stage_2_2, explosion_stage_2_1, explosion_stage_2_2, explosion_stage_2_1, explosion_stage_2_2, explosion_stage_2_1, explosion_stage_2_2, explosion_stage_2_1, explosion_stage_2_2, explosion_stage_2_1, explosion_stage_2_2, explosion_stage_2_1, explosion_stage_2_2, explosion_stage_2_1, explosion_stage_2_2, explosion_stage_3_1, explosion_stage_3_2],self.side,1.96,self.imgbox,self.gameplay)
        self.ground_animation = one_time_animation_player([breaking_ground1, breaking_ground2, breaking_ground3], self.side, 0.32, self.imgbox, self.gameplay)

        self.switcher1 = N_time_switch(1)

        self.gameplay.side0.append(self)

    def resize(self):
        a = float(screen.screen.get_width()) / self.gameplay.screen[0]
        b = float(screen.screen.get_height()) /  self.gameplay.screen[1]
        tmp = pygame.Rect(self.imgbox.left * a, self.imgbox.top * b, self.imgbox.width * a, self.imgbox.height * b)
        copy(self.imgbox, tmp)
        self.operation()

    def move(self):
        if self.box.right < self.gameplay.nexus2.box.left and self.box.left > self.gameplay.nexus1.box.right:
            self.imgbox.centerx += (self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  * self.side
        copy(self.box, self.moving_animation.play())

    def explosive(self):
        if self.switcher1.operation():
            if self.side == 1:
                copy(self.imgbox,shuriken_explosion.hitbox_to_imgbox(self.imgbox))
            else:
                copy(self.imgbox,shuriken_explosion.reverse.hitbox_to_imgbox(self.imgbox))
        if self.direct :
            copy(self.box, self.explosion_animation1.play())
            if self.explosion_animation1.status == False:
                self.direct = False
        else:
            copy(self.box , self.explosion_animation2.play())
            self.ground_animation.play()
            if self.explosion_animation2.status == False:
                self.remove()
                    

    def strike(self):    
        for enemy_object in self.gameplay.side( - self.side):
            if collide_checker(self, enemy_object):
                if not list_find_special(self.damaged_list, enemy_object) :
                    self.damaged_list.append(getting_hit_object(enemy_object))
                    enemy_object.get_hit = True
                    enemy_object.get_damage = self.damage


        for damaged_object in self.damaged_list:
            if damaged_object.clock.Return == False:
                self.damaged_list.remove(damaged_object)



    def remove(self):
        self.moving_animation.remove()
        self.explosion_animation1.remove()
        self.explosion_animation2.remove()
        self.gameplay.side0.remove(self)
                    


    def operation(self):
        self.strike()
        self.lasting_time -= (self.gameplay.curr_time - self.gameplay.pre_curr_time)
        if self.direct2:
            self.move()
            checker = fake_object_class(self)
            checker.box .width = checker.box.width / 2
            for enemy_object in self.gameplay.side( - self.side):
                if collide_checker(checker, enemy_object):
                    if not enemy_object.status == - 1:
                        if list_find(self.effectted_list, enemy_object) == -1 :
                            ispass = False
                            for effect in enemy_object.effect_list:
                                if effect.__class__ == knock_back:
                                    ispass = True
                                    break
                            if not ispass:
                                add_effect(enemy_object, knock_back(enemy_object,self.lasting_time, self.speed))
                                self.effectted_list.append(enemy_object)
            if self.lasting_time < 0:
                self.direct2 = False
        else:
            self.explosive()


class cloneclass():
    def __init__(self, naruto):
        naruto.clone_list.append(self)
        self.naruto = naruto
        self.pre_status = None
        self.status  = None
        self.box = pygame.Rect(0,0,0,0)
        self.imgbox = pygame.Rect(0,0,0,0)
        self.gameplay = naruto.gameplay
        self.side = naruto.side
        # self.__class__ = naruto.__class__

        self.speed = 5.0 # 5/100 map per second 
        self.attack_scope = 1 * self.gameplay.box_size[0] # 4/15 map width
        self.attack_speed = 1/3 # attack(s) pers second
        self.attack_damage = 1.0
        self.attack_damage_orginal = self.attack_damage
        self.health_max = 100.0
        self.health = self.health_max 
        self.mana_max = 100.0
        self.mana = 0

        self.effect_list = []

        self.alive = None
        self.get_hit = False
        self.ischeck = True
        self.iscollide_check = True        
        self.collide = None
        self.special_status = False

        self.animation_player = None
        self.spawn_animation = one_time_animation_player([naruto53, naruto54, naruto55, naruto56], self.side, 0.36, self.imgbox, self.gameplay)
        self.moving_animation = animation_player([naruto62,naruto63,naruto64,naruto65,naruto66,naruto67], self.side, 0.6, self.imgbox , self.gameplay)
        self.walking_animation = animation_player([naruto62,naruto63,naruto64,naruto65,naruto66,naruto67], self.side, 0.6, self.imgbox , self.gameplay)
        self.attacking_animation = one_time_animation_player([naruto1,naruto2,naruto3,naruto4,naruto5,naruto6,naruto7,naruto8,naruto9,naruto10,naruto11,naruto12,naruto13,naruto14,naruto15,naruto16,naruto17,naruto18,naruto19], self.side, 1.26 , self.imgbox, self.gameplay)
        self.standstill_animation = one_time_animation_player([naruto68, naruto69, naruto70],self.side, 0.58, self.imgbox, self.gameplay)  
        self.dying_animation = one_time_animation_player([naruto57, naruto58, naruto59, naruto60, naruto61], self.side, 0.56, self.imgbox, self.gameplay)
        self.knock_back_animation = animation_player([naruto71], self.side, 1, self.imgbox, self.gameplay)
        self.flying_animation = animation_player([naruto74], self.side, 1, self.imgbox, self.gameplay)
        self.falling_animation = animation_player([naruto72], self.side, 1, self.imgbox, self.gameplay)

        self.switcher1 = N_time_switch(1)
        self.switcher2 = N_time_switch(1)
        self.switcher3 = N_time_switch(1)
        self.switcher4 = N_time_switch(1)
        self.switcher5 = N_time_switch(1)

        self.attack_coundowner = timing_clock(1 / self.attack_speed, self.gameplay)

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

    def resize(self):
        a = float(screen.screen.get_width()) / self.gameplay.screen[0]
        b = float(screen.screen.get_height()) /  self.gameplay.screen[1]
        tmp = pygame.Rect(self.imgbox.left * a, self.imgbox.top * b, self.imgbox.width * a, self.imgbox.height * b)
        copy(self.imgbox, tmp)
        self.operation()

    def display(self):
        copy(self.box, self.animation_player.play())
        pygame.draw.rect(screen.screen,Red,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 10 ,(self.box.width - self.box.width / 2) / self.health_max *self.health,self.box.height / 20))
        pygame.draw.rect(screen.screen,Blue,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 5 - self.box.height / 30 ,(self.box.width - self.box.width / 2) / self.mana_max *self.mana,self.box.height / 20))


    def move(self):
        self.animation_player = self.moving_animation
        self.imgbox.centerx += (self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  * self.side

    def walk(self):
        self.animation_player = self.walking_animation
        self.imgbox.centerx += (2 * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  * self.side

    def standstill(self):
        self.animation_player = self.standstill_animation

    def standsill_reset(self):
        self.standstill_animation.reset()

    
    
    def check_collide(self):
        if self.iscollide_check:
            for object in self.gameplay.side(self.side) + self.gameplay.side4 + self.gameplay.side(- self.side):
                if (object.box.centerx - self.box.centerx) * self.side >= 0:
                    if same_line_checker(self, object):
                        if not (self == object):
                            if collide_checker(self ,object):
                                self.collide = True
                                if self.side == object.side:
                                    if self.index > object.index :
                                        self.collide = 1
                                        if self.box.right < self.gameplay.nexus2.box.left and self.box.left > self.gameplay.nexus1.box.right:
                                            self.imgbox.centerx -= ( 5.0 * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time) * self.side
                                            self.box.centerx -= ( 5.0 * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time) * self.side
                                        return

                                else:
                                    self.collide = 2
                                    if self.box.right < self.gameplay.nexus2.box.left and self.box.left > self.gameplay.nexus1.box.right:
                                        self.imgbox.centerx -= ( 5.0 * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time) * self.side
                                        self.box.centerx -= ( 5.0 * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time) * self.side
                                    return
                self.collide = False



    def check_forward(self): #always after check_collide
        if self.mana >= self.mana_max:
            self.mana = 0

        if self.ischeck :

            flag = False
            if self.collide == 2:
                self.status = 1
                flag = True

            elif self.collide == 1:
                ispass = False
                for object in self.gameplay.side(- self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 3 + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                self.status = 1
                                flag = True
                                ispass = True
                                break
                if not ispass:
                    self.status = 2
                    flag = True
            else:
                ispass = False
                for object in self.gameplay.side( - self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 3 + (self.box.width + object.box.width) / 2:
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                self.status = 1
                                flag = True
                                ispass = True
                                break
                if not ispass:
                    for object in self.gameplay.side(self.side) + self.gameplay.side4 :
                        if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 2 + (self.box.width + object.box.width) / 2 :
                            if (object.box.centerx - self.box.centerx) * self.side >= 0:
                                if same_line_checker(self, object):
                                    if not (self == object):
                                        self.status = 2
                                        flag = True
                                        break         
            if not flag:
                self.status = 3

            if self.status == 3 and (not self.pre_status == 3):
                ispass = False
                for object in self.gameplay.side( - self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 3 + (self.speed * screen.screen.get_rect().width / 100) * 0.5  + (self.box.width + object.box.width) / 2:
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                self.status = 5
                                ispass = True
                                break
                if not ispass:
                    for object in self.gameplay.side(self.side) + self.gameplay.side4 :
                        if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 2 + (self.speed * screen.screen.get_rect().width / 100) * 0.5  + (self.box.width + object.box.width) / 2 :
                            if (object.box.centerx - self.box.centerx) * self.side >= 0:
                                if same_line_checker(self, object):
                                    if not (self == object):
                                        if not  object.status == 3:
                                            self.status = 5
                                            break        
        
            
            if self.status == 1 :
                if self.attack_coundowner.Return == True:
                    self.status = 2            


        if self.status > 0:
            if not self.pre_status == None:
                if self.pre_status > 0:
                    if not self.pre_status == self.status:            
                        if self.pre_status == 1:
                            self.attack_reset()
                        elif self.pre_status == 2:
                            self.standsill_reset()


    def Geting_hit(self):
        self.get_hit = False
        self.health -= self.get_damage 
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
            self.naruto.clone_list.remove(self)
            self.side = 0
            self.gameplay.side0.append(self)
            self.img = self.animation_player.img_lib[self.animation_player.clock.Return - 1]
        
        self.dying_animation.play()
        if self.dying_animation.clock.Return < 3:
            screen.screen.blit(pygame.transform.scale(self.img.img, (self.imgbox.width, self.imgbox.height)), self.imgbox)

        if self.dying_animation.status == False:
            self.dying_animation.remove()
            self.gameplay.side0.remove(self)

    
    def attack(self):
        if self.switcher5.operation():
            self.attack_coundowner.reset()
            self.attack_coundowner.start()
            
        self.animation_player = self.attacking_animation
        if self.attacking_animation.clock.Return == 5 or self.attacking_animation.clock.Return == 10:
            if self.switcher1.operation():
                for object in self.gameplay.side(- self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                self.mana += 10 
                                object.get_hit = True
                                object.get_damage = self.attack_damage
        elif self.attacking_animation.clock.Return == 17:
            if self.switcher1.operation():
                for object in self.gameplay.side(- self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                self.mana += 10 
                                object.get_hit = True
                                object.get_damage = self.attack_damage

        elif self.attacking_animation.clock.Return == 4 or self.attacking_animation.clock.Return == 9 or self.attacking_animation.clock.Return == 16:
            self.switcher1.reset()



    def attack_reset(self):
        self.attacking_animation.reset() 
        self.switcher5.reset()

    def operation(self):
        if self.alive == None:
            self.spawn_animation.play()
            if self.spawn_animation.status == False:
                self.alive = True
                self.index = len(self.gameplay.side(self.side))
                self.gameplay.side0.remove(self)
                self.gameplay.side(self.side).append(self)

        elif self.alive == True:

            def play(effect):
                effect.play()
            list_browser(self.effect_list, play)        

            self.check_collide()
            self.check_forward()
            
            if self.status == 3:
                self.move()

            if self.status == 5:
                self.walk()

            elif self.status == 1:
                self.attack()

            elif self.status == 2 :
                self.standstill()


            if self.get_hit :
                self.Geting_hit()

            if self.health <= 0:
                self.alive = False
                

            self.display()
            self.status_update()

            # pygame.draw.rect(screen.screen,White,self.box,1)
            # pygame.draw.rect(screen.screen,White,self.imgbox,1)
        elif self.alive == False:
            if self.animation_player == None:
                self.animation_player = self.standstill_animation
            self.dying()


class narutoclass():
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
        self.attack_damage = 10.0
        self.attack_damage_orginal = self.attack_damage
        self.health_max = 100.0
        self.health = self.health_max 
        self.mana_max =100.0
        self.mana = 0.0

        self.effect_list = []
        self.clone_list = []

        self.alive = True
        self.get_hit = False
        self.ischeck = True
        self.iscollide_check = True        
        self.collide = None
        self.special_status = False

        self.moving_animation = animation_player([naruto62,naruto63,naruto64,naruto65,naruto66,naruto67], self.side, 0.6, self.imgbox , self.gameplay)
        self.walking_animation = animation_player([naruto68, naruto69, naruto70],self.side, 0.58, self.imgbox, self.gameplay)  
        self.attacking_animation = one_time_animation_player([naruto1,naruto2,naruto3,naruto4,naruto5,naruto6,naruto7,naruto8,naruto9,naruto10,naruto11,naruto12,naruto13,naruto14,naruto15,naruto16,naruto17,naruto18,naruto19], self.side, 1.26 , self.imgbox, self.gameplay)
        tmp_lib = []
        for i in [naruto19, naruto20, naruto21, naruto22, naruto23, naruto24, naruto25, naruto26, naruto27]:
            tmp_lib.append(i)
        for i in [naruto28, naruto29, naruto30, naruto31, naruto32, naruto33, naruto34]:
            tmp_lib.append(i)
        for j in range(1,8):
            for i in [naruto75, naruto76, naruto77]:
                    tmp_lib.append(i)
        for i in [naruto35, naruto78, naruto79, naruto80, naruto81]:
            tmp_lib.append(i)
        for i in [naruto36, naruto37, naruto38, naruto39, naruto40, naruto41, naruto42]:
            tmp_lib.append(i)
        for j in range(1,8):
            for i in naruto43, naruto82, :
                    tmp_lib.append(i)
        for i in naruto44, naruto45, naruto46, naruto47, naruto48, naruto49, naruto50, :
            tmp_lib.append(i)
        
        self.special_skill_animation = one_time_animation_player(tmp_lib, self.side, 5.52, self.imgbox, self.gameplay)
        self.standstill_animation = one_time_animation_player([naruto68, naruto69, naruto70],self.side, 0.58, self.imgbox, self.gameplay)  
        self.dying_animation = one_time_animation_player([naruto71,naruto73,naruto74], self.side, 0.3, self.imgbox, self.gameplay)
        self.knock_back_animation = animation_player([naruto71], self.side, 1, self.imgbox, self.gameplay)
        self.flying_animation = animation_player([naruto74], self.side, 1, self.imgbox, self.gameplay)
        self.falling_animation = animation_player([naruto72], self.side, 1, self.imgbox, self.gameplay)

        self.switcher1 = N_time_switch(1)
        self.switcher2 = N_time_switch(1)
        self.switcher3 = N_time_switch(1)
        self.switcher4 = N_time_switch(1)
        self.switcher5 = N_time_switch(1)

        self.switcher_list = []
        for i in range(0,8):
            self.switcher_list.append(N_time_switch(1))

        self.attack_coundowner = timing_clock(1 / self.attack_speed, self.gameplay)
        self.clock = N_ValueReturn_repeated_clock(0.1 , 5 , self.gameplay)

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
        elif self.pre_status == 4:
            if self.special_skill_animation.status == True:
                self.ischeck = False
            elif self.special_skill_animation.status == False:
                self.ischeck = True
                self.special_status = False
                self.special_skill_reset()



    def resize(self):
        a = float(screen.screen.get_width()) / self.gameplay.screen[0]
        b = float(screen.screen.get_height()) /  self.gameplay.screen[1]
        tmp = pygame.Rect(self.imgbox.left * a, self.imgbox.top * b, self.imgbox.width * a, self.imgbox.height * b)
        copy(self.imgbox, tmp)
        self.operation()

 
    def display(self):
        copy(self.box, self.animation_player.play())
        pygame.draw.rect(screen.screen,Red,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 10 ,(self.box.width - self.box.width / 2) / self.health_max *self.health,self.box.height / 20))
        pygame.draw.rect(screen.screen,Blue,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 5 - self.box.height / 30 ,(self.box.width - self.box.width / 2) / self.mana_max *self.mana,self.box.height / 20))


    def move(self):
        self.animation_player = self.moving_animation
        self.imgbox.centerx += (self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  * self.side

    def walk(self):
        self.animation_player = self.walking_animation
        self.imgbox.centerx += (2 * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  * self.side
        
    def standstill(self):
        self.animation_player = self.standstill_animation

    def standsill_reset(self):
        self.standstill_animation.reset()

    
    
    def check_collide(self):
        if self.iscollide_check:
            for object in self.gameplay.side(self.side) + self.gameplay.side4 + self.gameplay.side(- self.side):
                if (object.box.centerx - self.box.centerx) * self.side >= 0:
                    if same_line_checker(self, object):
                        if not (self == object):
                            if collide_checker(self ,object):
                                self.collide = True
                                if self.side == object.side:
                                    if self.index > object.index :
                                        self.collide = 1
                                        if self.box.right < self.gameplay.nexus2.box.left and self.box.left > self.gameplay.nexus1.box.right:
                                            self.imgbox.centerx -= ( 5.0 * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time) * self.side
                                            self.box.centerx -= ( 5.0 * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time) * self.side
                                        return

                                else:
                                    self.collide = 2
                                    if self.box.right < self.gameplay.nexus2.box.left and self.box.left > self.gameplay.nexus1.box.right:
                                        self.imgbox.centerx -= ( 5.0 * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time) * self.side
                                        self.box.centerx -= ( 5.0 * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time) * self.side
                                    return
                self.collide = False

    def check_forward(self): #always after check_collide
        if self.mana >= self.mana_max:
            self.mana = 0
            self.special_status = True
            self.status = 4
            ispass = True
        else:
            ispass = False

        if not ispass:
            if self.ischeck :

                flag = False
                if self.collide == 2:
                    self.status = 1
                    flag = True

                elif self.collide == 1:
                    ispass = False
                    for object in self.gameplay.side(- self.side) :
                        if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 3 + (self.box.width + object.box.width) / 2 :
                            if (object.box.centerx - self.box.centerx) * self.side >= 0:
                                if same_line_checker(self, object):
                                    self.status = 1
                                    flag = True
                                    ispass = True
                                    break
                    if not ispass:
                        self.status = 2
                        flag = True
                else:
                    ispass = False
                    for object in self.gameplay.side( - self.side) :
                        if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 3 + (self.box.width + object.box.width) / 2:
                            if (object.box.centerx - self.box.centerx) * self.side >= 0:
                                if same_line_checker(self, object):
                                    self.status = 1
                                    flag = True
                                    ispass = True
                                    break
                    if not ispass:
                        for object in self.gameplay.side(self.side) + self.gameplay.side4 :
                            if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 2 + (self.box.width + object.box.width) / 2 :
                                if (object.box.centerx - self.box.centerx) * self.side >= 0:
                                    if same_line_checker(self, object):
                                        if not (self == object):
                                            self.status = 2
                                            flag = True
                                            break         
                if not flag:
                    self.status = 3

                if self.status == 3 and (not self.pre_status == 3):
                    ispass = False
                    for object in self.gameplay.side( - self.side) :
                        if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 2 + (self.speed * screen.screen.get_rect().width / 100) * 0.5  + (self.box.width + object.box.width) / 2:
                            if (object.box.centerx - self.box.centerx) * self.side >= 0:
                                if same_line_checker(self, object):
                                    self.status = 5
                                    ispass = True
                                    break
                    if not ispass:
                        for object in self.gameplay.side(self.side) + self.gameplay.side4 :
                            if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 3 + (self.speed * screen.screen.get_rect().width / 100) * 0.5  + (self.box.width + object.box.width) / 2 :
                                if (object.box.centerx - self.box.centerx) * self.side >= 0:
                                    if same_line_checker(self, object):
                                        if not (self == object):
                                            if not  object.status == 3:
                                                self.status = 5
                                                break         
                    
                
                if self.status == 1 :
                    if self.attack_coundowner.Return == True:
                        self.status = 2            


        if self.status > 0:
            if not self.pre_status == None:
                if self.pre_status > 0:
                    if not self.pre_status == self.status:            
                        if self.pre_status == 1:
                            self.attack_reset()
                        elif self.pre_status == 2:
                            self.standsill_reset()
                        elif self.pre_status == 4:
                            self.special_skill_reset()


    def Geting_hit(self):
        self.get_hit = False
        self.health -= self.get_damage 
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
        if self.attacking_animation.clock.Return == 3 or self.attacking_animation.clock.Return == 8:
            if self.switcher1.operation():
                for object in self.gameplay.side(- self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                self.mana += 10 
                                object.get_hit = True
                                object.get_damage = self.attack_damage
        elif self.attacking_animation.clock.Return == 15:
            if self.switcher1.operation():
                for object in self.gameplay.side(- self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                self.mana += 10 
                                add_effect(object, flying(object, 5.0))
                                object.get_hit = True
                                object.get_damage = self.attack_damage

        elif self.attacking_animation.clock.Return == 2 or self.attacking_animation.clock.Return == 7 or self.attacking_animation.clock.Return == 14:
            self.switcher1.reset()



    def attack_reset(self):
        self.attacking_animation.reset() 
        self.switcher5.reset()


    def kagebusino_jutsu(self, position): 
        tmp = cloneclass(self)
        tmp.indexx = len(self.clone_list)
        self.gameplay.side0.append(tmp)
        copy(tmp.imgbox, self.imgbox)
        tmp.imgbox.centerx += position * self.gameplay.box_size[0]
        


    def special_skill(self):
        if self.switcher3.operation():
            add_effect(self, iron_body(self, 5.52))
        self.animation_player = self.special_skill_animation
        if self.special_skill_animation.clock.Return == 3 :
            self.switcher1.reset()

        if self.special_skill_animation.clock.Return == 4 :
            if self.switcher1.operation():
                self.clock.start()
                self.switcher1.reset()


        elif self.special_skill_animation.clock.Return > 4 : 
            if self.switcher_list[self.clock.Return - 1].operation():
                self.kagebusino_jutsu(self.clock.Return * self.side)

        if self.special_skill_animation.clock.Return == 65 :
            self.switcher2.reset()

        elif self.special_skill_animation.clock.Return == 66 :
            if self.switcher2.operation():
                for clone in self.clone_list:
                    clone.alive = False

        elif self.special_skill_animation.clock.Return == 67 :
            self.switcher2.reset()

        elif self.special_skill_animation.clock.Return == 68 :
            if self.switcher2.operation():
                tmp = rasenshuriken(self)
                for object in self.gameplay.side(- self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                add_effect(object, knock_back(object,tmp.lasting_time, tmp.speed))




    def special_skill_reset(self):
        self.special_skill_animation.reset() 
        self.switcher1.reset()
        self.switcher2.reset()
        self.switcher3.reset()
        for switch in self.switcher_list:
            switch.reset()



    def operation(self):
        if self.alive:
            def play(effect):
                effect.play()
            list_browser(self.effect_list, play)
            
            self.check_collide()
            self.check_forward()

            if self.status == 3:
                self.move()

            elif self.status == 5 :
                self.walk()

            elif self.status == 1:
                self.attack()

            elif self.status == 2 :
                self.standstill()


            elif self.status == 4:
                self.special_skill()

            if self.get_hit :
                self.Geting_hit()

            if self.health <= 0:
                self.alive = False
                for clone in self.clone_list:
                    clone.alive = False
                

            self.display()
            self.status_update()

            pygame.draw.rect(screen.screen,White,self.box,1)
            pygame.draw.rect(screen.screen,White,self.imgbox,1)
        else:
            self.dying()

