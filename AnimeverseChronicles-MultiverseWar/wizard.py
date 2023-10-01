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
from character_properties import *


wizard1 = analyzed_img("GameplayAssets\\wizard\\wizard(1).png", 170 , 56 , 68 , 179)
wizard2 = analyzed_img("GameplayAssets\\wizard\\wizard(2).png", 170 , 56 , 68 , 179)
wizard3 = analyzed_img("GameplayAssets\\wizard\\wizard(3).png", 170 , 56 , 68 , 179)
wizard4 = analyzed_img("GameplayAssets\\wizard\\wizard(4).png", 175 , 96 , 53 , 127)
wizard5 = analyzed_img("GameplayAssets\\wizard\\wizard(5).png", 157 , 98 , 91 , 143)
wizard6 = analyzed_img("GameplayAssets\\wizard\\wizard(6).png", 137 , 74 , 59 , 161)
wizard7 = analyzed_img("GameplayAssets\\wizard\\wizard(7).png", 136 , 67 , 56 , 160)
wizard8 = analyzed_img("GameplayAssets\\wizard\\wizard(8).png", 138 , 67 , 63 , 160)
wizard9 = analyzed_img("GameplayAssets\\wizard\\wizard(9).png", 136 , 70 , 67 , 158)
wizard10 = analyzed_img("GameplayAssets\\wizard\\wizard(10).png", 136 , 70 , 67 , 158)
wizard11 = analyzed_img("GameplayAssets\\wizard\\wizard(11).png", 164 , 79 , 65 , 152)
wizard12 = analyzed_img("GameplayAssets\\wizard\\wizard(12).png", 164 , 79 , 65 , 152)
wizard13 = analyzed_img("GameplayAssets\\wizard\\wizard(13).png", 167 , 98 , 86 , 146)
wizard14 = analyzed_img("GameplayAssets\\wizard\\wizard(14).png", 192 , 96 , 69 , 144)
wizard15 = analyzed_img("GameplayAssets\\wizard\\wizard(15).png", 192 , 96 , 69 , 144)
wizard16 = analyzed_img("GameplayAssets\\wizard\\wizard(16).png", 192 , 96 , 69 , 144)
wizard17 = analyzed_img("GameplayAssets\\wizard\\wizard(17).png", 192 , 96 , 69 , 144)
wizard18 = analyzed_img("GameplayAssets\\wizard\\wizard(18).png", 163 , 94 , 85 , 159)
wizard19 = analyzed_img("GameplayAssets\\wizard\\wizard(19).png", 164 , 80 , 94 , 150)
wizard20 = analyzed_img("GameplayAssets\\wizard\\wizard(20).png", 135 , 71 , 88 , 160)
wizard21 = analyzed_img("GameplayAssets\\wizard\\wizard(21).png", 183 , 77 , 72 , 162)
wizard22 = analyzed_img("GameplayAssets\\wizard\\wizard(22).png", 183 , 77 , 72 , 162)
wizard23 = analyzed_img("GameplayAssets\\wizard\\wizard(23).png", 177 , 65 , 73 , 187)
wizard24 = analyzed_img("GameplayAssets\\wizard\\wizard(24).png", 177 , 65 , 73 , 187)
wizard25 = analyzed_img("GameplayAssets\\wizard\\wizard(25).png", 163 , 59 , 70 , 160)
wizard26 = analyzed_img("GameplayAssets\\wizard\\wizard(26).png", 141 , 64 , 76 , 150)
wizard27 = analyzed_img("GameplayAssets\\wizard\\wizard(27).png", 132 , 87 , 75 , 155)
wizard28 = analyzed_img("GameplayAssets\\wizard\\wizard(28).png", 149 , 84 , 73 , 158)
wizard29 = analyzed_img("GameplayAssets\\wizard\\wizard(29).png", 170 , 56 , 68 , 179)
wizard30 = analyzed_img("GameplayAssets\\wizard\\wizard(30).png", 149 , 84 , 73 , 158)
wizard31 = analyzed_img("GameplayAssets\\wizard\\wizard(31).png", 149 , 84 , 73 , 158)
wizard32 = analyzed_img("GameplayAssets\\wizard\\wizard(32).png", 149 , 84 , 73 , 158)

wizard_to_magic_ball = analyzed_img("GameplayAssets\\wizard\\wizard_to_magicball.png",   332 , 104 , 57 , 39)


magic_ball1= analyzed_img("GameplayAssets\\wizard\\magic_ball(1).png", 261 , 42 , 137 , 154)
magic_ball2 = analyzed_img("GameplayAssets\\wizard\\magic_ball(2).png", 261 , 42 , 137 , 154)
magic_ball3 = analyzed_img("GameplayAssets\\wizard\\magic_ball(3).png", 261 , 42 , 137 , 154)
magic_ball4 = analyzed_img("GameplayAssets\\wizard\\magic_ball(4).png", 261 , 42 , 137 , 154)
magic_ball5 = analyzed_img("GameplayAssets\\wizard\\magic_ball(5).png", 261 , 42 , 137 , 154)
magic_ball6 = analyzed_img("GameplayAssets\\wizard\\magic_ball(6).png" , 251 , 45 , 143 , 145)
magic_ball7 = analyzed_img("GameplayAssets\\wizard\\magic_ball(7).png" , 294 , 85 , 105 , 86)
magic_ball8 = analyzed_img("GameplayAssets\\wizard\\magic_ball(8).png" , 339 , 94 , 62 , 72)
magic_ball9 = analyzed_img("GameplayAssets\\wizard\\magic_ball(9).png" , 369 , 101 , 40 , 40)
   
attack_damage = wz_attack_damage
health = wz_health
mana_per_att = wz_mana_per_att
heal_per_skill = wz_heal_per_skill
level_effect = wz_level_effect

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
                self.wizard.mana += mana_per_att[self.wizard.level - 1]
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
            self.level = self.gameplay.character_level1[3]
        elif side == 2:
            self.side = -1          
            self.level = self.gameplay.character_level2[3]               

        self.speed = 5.0 # 5/100 map per second 
        self.attack_scope = 8 * self.gameplay.box_size[0] # 4/15 map width
        self.attack_scope_orginal = self.attack_scope
        self.attack_speed = 1/2 # arrow(s) pers second
        self.attack_speed_orginal = self.attack_speed
        self.attack_damage = attack_damage[self.level - 1]
        self.attack_damage_orginal = self.attack_damage
        self.health_max = health[self.level - 1]
        self.health = self.health_max
        self.mana_max = 100.0
        self.mana = 85.0

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
        if not self.level == self.gameplay.character_level(self.side, 3):
            self.level = self.gameplay.character_level(self.side, 3)
            self.attack_damage = attack_damage[self.level - 1]
            self.health_max = health[self.level - 1]


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
        # pygame.draw.rect(screen.screen,Red,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 10 ,(self.box.width - self.box.width / 2) / self.health_max *self.health,self.box.height / 20))
        # pygame.draw.rect(screen.screen,Blue,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 5 - self.box.height / 30 ,(self.box.width - self.box.width / 2) / self.mana_max *self.mana,self.box.height / 20))


    
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
                if abs(object.box.centerx - self.box.centerx) <= self.gameplay.box_size[0] / 3:
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
            self.mana = self.mana % 100
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
                            if (object.box.centerx - self.box.centerx) * self.side > 0:
                                if same_line_checker(self, object):
                                    self.status = 1
                                    flag = True
                                    break
                    self.status = 2
                    flag = True
                else:
                    for object in self.gameplay.side(self.side) + self.gameplay.side4 :
                        if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 2 + (self.box.width + object.box.width) / 2:
                            if (object.box.centerx - self.box.centerx) * self.side > 0:
                                if same_line_checker(self, object):
                                    if (not (self == object)) and (self.index > object.index):
                                        self.status = 2
                                        flag = True
                                        break

                    for object in self.gameplay.side( - self.side) :
                        if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2 :
                            if (object.box.centerx - self.box.centerx) * self.side > 0:
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
            self.mana += mana_per_att[self.level - 1]
    

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
                self.effected_list = []
                for object in self.gameplay.side(- self.side) :
                    if len(self.effected_list) < level_effect[self.level - 1]:
                        if abs(object.box.centerx  - self.box.centerx ) <= screen.screen.get_width() + (self.box.width + object.box.width) / 2 :
                            if (object.box.centerx - self.box.centerx) * self.side >= 0:
                                if same_line_checker(self, object):
                                    if not object.__class__ == self.gameplay.nexusclass:
                                        self.effected_list.append(object)
                    else:
                        break
                for object in self.effected_list:
                    add_effect(object, dizzy(object, 1))
                    add_effect(object, soul_sucking(object))                        
                    

        elif self.special_skill_animation.clock.Return == 2 or self.special_skill_animation.clock.Return == 9 or self.special_skill_animation.clock.Return == 11:
            self.switcher2.reset()

        elif self.special_skill_animation.clock.Return == 10:
            if self.switcher2.operation():
                for object in self.effected_list :
                    add_effect(object, knock_back(object, 0.5, 20))
                    

        elif self.special_skill_animation.clock.Return == 12:
            if self.switcher2.operation():
                for object in self.gameplay.side( self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= screen.screen.get_width() + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                if not object == self:
                                    add_effect(object, heal(object, heal_per_skill[self.level - 1]))


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
                if self.side == 1:
                    self.gameplay.gold_income_1 += int(self.gameplay.character_cost[self.__class__][self.level - 1] * 10.0 / 100)
                else:
                    self.gameplay.gold_income_2 += int(self.gameplay.character_cost[self.__class__][self.level - 1] * 10.0 / 100)
                

            self.display()
            self.status_update()

            for magicbullet in self.magicbullet_list:
                magicbullet.operation()
            

            # pygame.draw.rect(screen.screen,White,self.box,1)
            # pygame.draw.rect(screen.screen,White,self.imgbox,1)
        else:
            self.dying()   
    
               






