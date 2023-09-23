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


sword_man1 = analyzed_img("GameplayAssets\\sword_man\\sword_man(1).png", 254 , 352 , 108 , 239)
sword_man2 = analyzed_img("GameplayAssets\\sword_man\\sword_man(2).png", 254 , 352 , 108 , 239)
sword_man3 = analyzed_img("GameplayAssets\\sword_man\\sword_man(3).png", 254 , 352 , 108 , 239)
sword_man4 = analyzed_img("GameplayAssets\\sword_man\\sword_man(4).png", 254 , 352 , 108 , 239)
sword_man5 = analyzed_img("GameplayAssets\\sword_man\\sword_man(5).png", 254 , 352 , 108 , 239)
sword_man6 = analyzed_img("GameplayAssets\\sword_man\\sword_man(6).png", 254 , 352 , 108 , 239)
sword_man7 = analyzed_img("GameplayAssets\\sword_man\\sword_man(7).png", 254 , 352 , 108 , 239)
sword_man8 = analyzed_img("GameplayAssets\\sword_man\\sword_man(8).png", 254 , 352 , 108 , 239)
sword_man9 = analyzed_img("GameplayAssets\\sword_man\\sword_man(9).png", 252 , 340 , 116 , 249)
sword_man10 = analyzed_img("GameplayAssets\\sword_man\\sword_man(10).png", 250 , 347 , 113 , 246)
sword_man11 = analyzed_img("GameplayAssets\\sword_man\\sword_man(11).png", 249 , 348 , 122 , 247)
sword_man12 = analyzed_img("GameplayAssets\\sword_man\\sword_man(12).png", 249 , 348 , 122 , 247)
sword_man13 = analyzed_img("GameplayAssets\\sword_man\\sword_man(13).png", 231 , 350 , 131 , 242)
sword_man14 = analyzed_img("GameplayAssets\\sword_man\\sword_man(14).png", 231 , 350 , 131 , 242)
sword_man15 = analyzed_img("GameplayAssets\\sword_man\\sword_man(15).png", 231 , 350 , 131 , 242)
sword_man16 = analyzed_img("GameplayAssets\\sword_man\\sword_man(16).png", 240 , 348 , 125 , 244)
sword_man17 = analyzed_img("GameplayAssets\\sword_man\\sword_man(17).png", 244 , 353 , 127 , 238)
sword_man18 = analyzed_img("GameplayAssets\\sword_man\\sword_man(18).png", 244 , 353 , 127 , 238)
sword_man19 = analyzed_img("GameplayAssets\\sword_man\\sword_man(19).png", 253 , 346 , 121 , 246)
sword_man20 = analyzed_img("GameplayAssets\\sword_man\\sword_man(20).png", 247 , 355 , 117 , 236)
sword_man21 = analyzed_img("GameplayAssets\\sword_man\\sword_man(21).png", 247 , 355 , 117 , 236)
sword_man22 = analyzed_img("GameplayAssets\\sword_man\\sword_man(22).png", 250 , 352 , 123 , 238)
sword_man23 = analyzed_img("GameplayAssets\\sword_man\\sword_man(23).png", 251 , 355 , 113 , 236)
sword_man24 = analyzed_img("GameplayAssets\\sword_man\\sword_man(24).png", 251 , 355 , 113 , 236)
sword_man25 = analyzed_img("GameplayAssets\\sword_man\\sword_man(25).png", 251 , 355 , 113 , 236)
sword_man26 = analyzed_img("GameplayAssets\\sword_man\\sword_man(26).png", 258 , 392 , 109 , 203)
sword_man27 = analyzed_img("GameplayAssets\\sword_man\\sword_man(27).png", 253 , 394 , 108 , 203)
sword_man28 = analyzed_img("GameplayAssets\\sword_man\\sword_man(28).png", 253 , 394 , 108 , 203)
sword_man29 = analyzed_img("GameplayAssets\\sword_man\\sword_man(29).png", 250 , 382 , 117 , 208)
sword_man30 = analyzed_img("GameplayAssets\\sword_man\\sword_man(30).png", 232 , 386 , 129 , 208)
sword_man31 = analyzed_img("GameplayAssets\\sword_man\\sword_man(31).png", 249 , 362 , 124 , 229)
sword_man32 = analyzed_img("GameplayAssets\\sword_man\\sword_man(32).png", 257 , 352 , 107 , 239)
sword_man33 = analyzed_img("GameplayAssets\\sword_man\\sword_man(33).png", 259 , 385 , 124 , 209)
sword_man34 = analyzed_img("GameplayAssets\\sword_man\\sword_man(34).png", 259 , 385 , 124 , 209)
sword_man35 = analyzed_img("GameplayAssets\\sword_man\\sword_man(35).png", 259 , 385 , 124 , 209)
sword_man36 = analyzed_img("GameplayAssets\\sword_man\\sword_man(36).png", 259 , 385 , 124 , 209)
sword_man37 = analyzed_img("GameplayAssets\\sword_man\\sword_man(37).png", 251 , 377 , 88 , 214)
sword_man38 = analyzed_img("GameplayAssets\\sword_man\\sword_man(38).png", 249 , 348 , 122 , 247)
sword_man39 = analyzed_img("GameplayAssets\\sword_man\\sword_man(39).png", 249 , 348 , 122 , 247)
sword_man40 = analyzed_img("GameplayAssets\\sword_man\\sword_man(40).png", 249 , 348 , 122 , 247)
sword_man41 = analyzed_img("GameplayAssets\\sword_man\\sword_man(41).png", 249 , 348 , 122 , 247)
sword_man50 = analyzed_img("GameplayAssets\\sword_man\\sword_man(50).png", 249 , 348 , 122 , 247)



attack_damage = [50.0, 55.0 , 100.0, 110.0 , 200.0]
health = [150.0, 200.0, 300.0, 400.0, 600.0]

class sword_manclass():
    def __init__(self,side,gameplay):
        self.pre_status = None
        self.status  = None
        self.box = pygame.Rect(0,0,0,0)
        self.imgbox = pygame.Rect(0,0,0,0)
        self.gameplay = gameplay
        if side == 1 :
            self.side = 1
            self.level = self.gameplay.character_level1[1]
        elif side == 2:
            self.side = -1   
            self.level = self.gameplay.character_level2[1]
        
        self.speed = 5.0 # 5/100 map per second 
        self.attack_scope = 2.5 * self.gameplay.box_size[0] # 4/15 map width
        self.attack_speed = 1/3 # attack(s) pers second
        self.attack_damage = attack_damage[self.level - 1]
        self.attack_damage_orginal = self.attack_damage
        self.health_max = health[self.level - 1]
        self.health = self.health_max 
        self.mana_max = 100.0
        self.mana = 0.0

        self.effect_list = []

        self.alive = True
        self.get_hit = False
        self.ischeck = True
        self.iscollide_check = True        
        self.collide = None
        self.special_status = False

        self.moving_animation = animation_player([sword_man1,sword_man2,sword_man3,sword_man4,sword_man5,sword_man6,sword_man7,sword_man8,sword_man9,sword_man10], self.side,1, self.imgbox , self.gameplay)
        self.walking_animation = animation_player([sword_man11,sword_man12,sword_man13,sword_man14,sword_man15,sword_man16,sword_man17,sword_man18],self.side, 1, self.imgbox, self.gameplay)  
        self.attacking_animation = one_time_animation_player([sword_man31,sword_man32,sword_man33,sword_man34,sword_man35,sword_man36,sword_man37,sword_man38], self.side, 0.5 , self.imgbox, self.gameplay)
        self.special_skill_animation = one_time_animation_player([sword_man19,sword_man20,sword_man21,sword_man22,sword_man23,sword_man24,sword_man25,sword_man26,sword_man27,sword_man28,sword_man29,sword_man30], self.side, 1, self.imgbox, self.gameplay)
        self.standstill_animation = one_time_animation_player([sword_man11,sword_man12,sword_man13,sword_man14,sword_man15,sword_man16,sword_man17,sword_man18],self.side, 1, self.imgbox, self.gameplay)  
        self.dying_animation = one_time_animation_player([sword_man50], self.side, 0.8, self.imgbox, self.gameplay)
        self.knock_back_animation = animation_player([sword_man39], self.side, 1, self.imgbox, self.gameplay)
        self.flying_animation = animation_player([sword_man41], self.side, 1, self.imgbox, self.gameplay)
        self.falling_animation = animation_player([sword_man40], self.side, 1, self.imgbox, self.gameplay)

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

 
    def status_update(self):
        if not self.level == self.gameplay.character_level(self.side, 2):
            self.level = self.gameplay.character_level(self.side, 2)
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
        pygame.draw.rect(screen.screen,Red,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 10 ,(self.box.width - self.box.width / 2) / self.health_max *self.health,self.box.height / 20))
        pygame.draw.rect(screen.screen,Blue,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 5 - self.box.height / 30 ,(self.box.width - self.box.width / 2) / self.mana_max *self.mana,self.box.height / 20))


    def move(self):
        self.animation_player = self.moving_animation
        self.imgbox.centerx += (self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  * self.side

    def walk(self):
        self.animation_player = self.walking_animation
        self.imgbox.centerx += (5 * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  * self.side

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
            self.mana = 0
            self.special_status = True

        if self.ischeck :

            flag = False
            if self.collide == 2:
                self.status = 1
                flag = True

            elif self.collide == 1:
                ispass = False
                for object in self.gameplay.side(- self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side > 0:
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
                for object in self.gameplay.side(self.side) + self.gameplay.side4 :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 2 + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side > 0:
                            if same_line_checker(self, object):
                                if (not (self == object)) and (self.index > object.index):
                                    self.status = 2
                                    flag = True
                                    break         
                if flag == True:
                    check = self.attack_scope
                else:
                    check = self.gameplay.box_size[0] / 2
                for object in self.gameplay.side( - self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= check + (self.box.width + object.box.width) / 2:
                        if (object.box.centerx - self.box.centerx) * self.side > 0:
                            if same_line_checker(self, object):
                                self.status = 1
                                flag = True
                                ispass = True
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
                elif self.special_status:
                    self.status = 4
            

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
        if self.special_status and self.status < 0:
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
        if self.attacking_animation.clock.Return == 4:
            if self.switcher1.operation():
                for object in self.gameplay.side(- self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                self.mana += 10  
                                object.get_hit = True
                                object.get_damage = self.attack_damage
        elif self.attacking_animation.clock.Return == 3:
            self.switcher1.reset()



    def attack_reset(self):
        self.attacking_animation.reset() 
        self.switcher5.reset()


    def special_skill(self):
        if self.switcher3.operation():
            self.attack_coundowner.reset()
            self.attack_coundowner.start()

        self.animation_player = self.special_skill_animation
        if self.special_skill_animation.clock.Return == 3 or self.special_skill_animation.clock.Return == 8:
            if self.switcher1.operation():
                for object in self.gameplay.side(- self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                add_effect(self, heal(self, self.health * 20.0 / 100))
                                object.get_hit = True
                                object.get_damage = self.attack_damage
        elif self.special_skill_animation.clock.Return == 2 or self.special_skill_animation.clock.Return == 7:
            self.switcher1.reset()



    def special_skill_reset(self):
        self.special_skill_animation.reset() 
        self.switcher3.reset()



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

            elif self.status == 4:
                self.special_skill()

            if self.get_hit :
                self.Geting_hit()

            if self.health <= 0:
                self.alive = False
                

            self.display()
            self.status_update()

            # pygame.draw.rect(screen.screen,White,self.box,1)
            # pygame.draw.rect(screen.screen,White,self.imgbox,1)
        else:
            self.dying()

