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
   

class magic_ball_class():
    def __init__(self,wizard):
        self.wizard = wizard
        self.gameplay = self.wizard.gameplay
        self.side = self.wizard.side

        self.imgbox = pygame.Rect(self.wizard.imgbox.left,self.wizard.imgbox.top,self.wizard.imgbox.width,self.wizard.imgbox.height)
        if self.side == 1:
            self.imgbox = wizard_to_magic_ball.imgbox_to_hitbox(self.imgbox)
            self.box = magic_ball1.imgbox_to_hitbox(self.imgbox)
        else:
            self.imgbox = reverse(wizard_to_magic_ball).imgbox_to_hitbox(self.imgbox)
            self.box = reverse(magic_ball1).imgbox_to_hitbox(self.imgbox)

        self.speed = 30  # 10/100 map per second
        self.damage = self.wizard.attack_damage
        self.direct = True
 

        self.moving_animation = animation_player([magic_ball1, magic_ball2, magic_ball3, magic_ball4,magic_ball5],self.side,1,self.imgbox,self.wizard.gameplay)
        self.explosion_animation = one_time_animation_player([magic_ball6,magic_ball7, magic_ball8, magic_ball9],self.side,0.25,self.imgbox,self.wizard.gameplay)

    def resize(self):
        a = float(screen.screen.get_width()) / self.gameplay.screen[0]
        b = float(screen.screen.get_height()) /  self.gameplay.screen[1]
        tmp = pygame.Rect(self.imgbox.left * a, self.imgbox.top * b, self.imgbox.width * a, self.imgbox.height * b)
        copy(self.imgbox, tmp)
        self.operation()

    def move(self):
        self.imgbox.centerx += (self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  * self.side
        copy(self.box, self.moving_animation.play())

    def explosive(self):
        copy(self.box, self.explosion_animation.play())
        if self.explosion_animation.status ==  False:
            self.remove()

    def collide_check(self):
        for enemy_object in self.wizard.gameplay.side( - self.side):
            if collide_checker(self,enemy_object):
                enemy_object.get_damage = self.damage
                enemy_object.get_hit = True
                self.wizard.mana += 10
                return True
        return False


    def remove(self):
        self.moving_animation.remove()
        self.explosion_animation.remove()
        self.wizard.magicbullet_list.remove(self)
                    


    def operation(self):
        if self.direct :
            if self.collide_check():
                self.direct = False
            else:
                self.move()
        else:
            self.explosive()


            
class wizardclass():
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

        self.speed = 5.0 # 5/100 map per second 
        self.attack_scope = 7 * self.gameplay.box_size[0] # 4/15 map width
        self.attack_scope_orginal = self.attack_scope
        self.attack_speed = 1/5 # arrow(s) pers second
        self.attack_speed_orginal = self.attack_speed
        self.attack_damage = 0.0
        self.attack_damage_orginal = self.attack_damage
        self.health_max = 100000.0
        self.health = self.health_max
        self.mana_max =100.0
        self.mana = 0.0

        self.magicbullet_list = []
        self.effect_list = []

        self.alive = True
        self.get_hit = False
        self.ischeck = True
        self.iscollide_check = True        
        self.collide = None        
        self.special_status = False

        self.moving_animation = animation_player([wizard1,wizard2,wizard3,wizard2],self.side, 1, self.imgbox , self.gameplay)
        self.walking_animation = animation_player([wizard1,wizard2,wizard3,wizard2], self.side, 1, self.imgbox, self.gameplay)
        self.attacking_animation = one_time_animation_player([wizard4,wizard5,wizard6,wizard7,wizard8,wizard9,wizard10,wizard11],self.side, 1 , self.imgbox, self.gameplay)
        self.standstill_animation = one_time_animation_player([wizard1,wizard2,wizard3,wizard2], self.side, 1, self.imgbox, self.gameplay)
        self.special_skill_animation = one_time_animation_player([wizard11,wizard12,wizard13,wizard14,wizard15,wizard16,wizard17,wizard18,wizard19,wizard20,wizard21,wizard22,wizard23,wizard24,wizard25,wizard26,wizard27,wizard28], self.side, 2, self.imgbox, self.gameplay)
        self.dying_animation = one_time_animation_player([wizard31], self.side, 0.8, self.imgbox, self.gameplay)
        self.knock_back_animation = animation_player([wizard29], self.side, 1, self.imgbox, self.gameplay)
        self.flying_animation = animation_player([wizard32], self.side, 1, self.imgbox, self.gameplay)
        self.falling_animation = animation_player([wizard30], self.side, 1, self.imgbox, self.gameplay)

        self.switcher1 = N_time_switch(1)
        self.switcher2 = N_time_switch(1)
        self.switcher3 = N_time_switch(1)
        self.switcher4 = N_time_switch(1)
        self.switcher5 = N_time_switch(1)

        self.attack_coundowner = timing_clock(1 / self.attack_speed, self.gameplay)


    def resize(self):
        a = float(screen.screen.get_width()) / self.gameplay.screen[0]
        b = float(screen.screen.get_height()) /  self.gameplay.screen[1]
        tmp = pygame.Rect(self.imgbox.left * a, self.imgbox.top * b, self.imgbox.width * a, self.imgbox.height * b)
        copy(self.imgbox, tmp)
        self.operation()

        for magicbullet in self.magicbullet_list:
            magicbullet.resize()

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

    def display(self):
        copy(self.box, self.animation_player.play())
        pygame.draw.rect(screen.screen,Red,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 10 ,(self.box.width - self.box.width / 2) / self.health_max *self.health,self.box.height / 20))
        pygame.draw.rect(screen.screen,Blue,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 5 - self.box.height / 30 ,(self.box.width - self.box.width / 2) / self.mana_max *self.mana,self.box.height / 20))


    
    def move(self):
        self.animation_player = self.moving_animation
        self.imgbox.centerx += (self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  * self.side
        
    def walk(self):
        self.animation_player = self.walking_animation
        self.imgbox.centerx += (5.0 * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  * self.side
   
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
                            self.special_status = False
        

        

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
        if self.attacking_animation.clock.Return == 3:
            if self.switcher1.operation():
                self.magicbullet_list.append(magic_ball_class(self))  

        elif self.attacking_animation.clock.Return == 2:
            self.switcher1.reset()


    def attack_reset(self):
        self.attacking_animation.reset() 
        self.switcher5.reset()
    
    def special_skill(self):
        self.animation_player = self.special_skill_animation
        if self.special_skill_animation.clock.Return == 3:
            if self.switcher2.operation():
                for object in self.gameplay.side(- self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope * 2 + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                add_effect(object, dizzy(object, 5))
                                add_effect(object, soul_sucking(object))                        
                                return
                self.special_skill_animation.status = False

        elif self.special_skill_animation.clock.Return == 2 or self.special_skill_animation.clock.Return == 9:
            self.switcher2.reset()

        elif self.special_skill_animation.clock.Return == 10:
            if self.switcher2.operation():
                for object in self.gameplay.side(- self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] * 5  + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                add_effect(object, knock_back(object, 0.5, 20))




    def special_skill_reset(self):
        self.special_skill_animation.reset()

    def operation(self):
        if self.alive:
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

            if self.special_status:
                self.special_skill()

            if self.get_hit :
                self.Geting_hit()

            if self.health <= 0:
                self.alive = False
                

            self.display()
            self.status_update()

            for magicbullet in self.magicbullet_list:
                magicbullet.operation()
            

            # pygame.draw.rect(screen.screen,White,self.box,1)
            # pygame.draw.rect(screen.screen,White,self.imgbox,1)
        else:
            self.dying()   
    
               






