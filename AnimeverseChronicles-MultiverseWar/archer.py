import pygame 
from pygame.locals import *
from collide_checker import *
from object_function import *
from clock import *
from switch import *
from list_function import *
from animation_player import *
from screen import *
from character_properties import *


archer1 = analyzed_img("GameplayAssets\\archer\\archer(1).png", 166 , 285 , 113 , 212)
archer2 = analyzed_img("GameplayAssets\\archer\\archer(2).png", 166 , 285 , 113 , 212)
archer3 = analyzed_img("GameplayAssets\\archer\\archer(3).png", 166 , 285 , 113 , 212)
archer4 = analyzed_img("GameplayAssets\\archer\\archer(4).png", 166 , 285 , 113 , 212)
archer5 = analyzed_img("GameplayAssets\\archer\\archer(5).png", 166 , 285 , 113 , 212)
archer6 = analyzed_img("GameplayAssets\\archer\\archer(6).png", 166 , 285 , 113 , 212)
archer7 = analyzed_img("GameplayAssets\\archer\\archer(7).png", 166 , 285 , 113 , 212)
archer8 = analyzed_img("GameplayAssets\\archer\\archer(8).png", 166 , 285 , 113 , 212)
archer9 = analyzed_img("GameplayAssets\\archer\\archer(9).png", 166 , 285 , 113 , 212)
archer10 = analyzed_img("GameplayAssets\\archer\\archer(10).png", 166 , 285 , 113 , 212)
archer11 = analyzed_img("GameplayAssets\\archer\\archer(11).png", 194 , 285 , 81 , 206)
archer12 = analyzed_img("GameplayAssets\\archer\\archer(12).png", 194 , 288 , 82 , 203)
archer13 = analyzed_img("GameplayAssets\\archer\\archer(13).png", 195 , 294 , 81 , 198)
archer14 = analyzed_img("GameplayAssets\\archer\\archer(14).png", 195 , 294 , 81 , 198)
archer15 = analyzed_img("GameplayAssets\\archer\\archer(15).png", 195 , 294 , 81 , 198)
archer16 = analyzed_img("GameplayAssets\\archer\\archer(16).png", 195 , 284 , 79 , 206)
archer17 = analyzed_img("GameplayAssets\\archer\\archer(17).png", 195 , 284 , 79 , 206)
archer18 = analyzed_img("GameplayAssets\\archer\\archer(18).png", 195 , 284 , 79 , 206)
archer19 = analyzed_img("GameplayAssets\\archer\\archer(19).png", 195 , 284 , 79 , 206)
archer20 = analyzed_img("GameplayAssets\\archer\\archer(20).png", 206 , 275 , 73 , 216)
archer21 = analyzed_img("GameplayAssets\\archer\\archer(21).png", 206 , 275 , 73 , 216)
archer22 = analyzed_img("GameplayAssets\\archer\\archer(22).png", 199 , 294 , 71 , 197)
archer23 = analyzed_img("GameplayAssets\\archer\\archer(23).png", 199 , 298 , 69 , 192)
archer24 = analyzed_img("GameplayAssets\\archer\\archer(24).png", 199 , 298 , 69 , 192)
archer25 = analyzed_img("GameplayAssets\\archer\\archer(25).png", 199 , 298 , 69 , 192)
archer26 = analyzed_img("GameplayAssets\\archer\\archer(26).png", 199 , 298 , 69 , 192)
archer27 = analyzed_img("GameplayAssets\\archer\\archer(27).png", 199 , 298 , 69 , 192)
archer28 = analyzed_img("GameplayAssets\\archer\\archer(28).png", 199 , 298 , 69 , 192)
archer29 = analyzed_img("GameplayAssets\\archer\\archer(29).png", 199 , 298 , 69 , 192)
archer30 = analyzed_img("GameplayAssets\\archer\\archer(30).png", 199 , 298 , 69 , 192)
archer31 = analyzed_img("GameplayAssets\\archer\\archer(31).png", 199 , 298 , 69 , 192)
archer32 = analyzed_img("GameplayAssets\\archer\\archer(32).png", 199 , 298 , 69 , 192)
archer33 = analyzed_img("GameplayAssets\\archer\\archer(33).png", 199 , 298 , 69 , 192)
archer40 = analyzed_img("GameplayAssets\\archer\\archer(40).png", 199 , 298 , 69 , 192)


arrow = analyzed_img("GameplayAssets\\archer\\arrow.png", 279 , 332 , 132 , 20)
special_arrow = analyzed_img("GameplayAssets\\archer\\special_arrow.png", 279 , 332 , 132 , 20)

attack_damage = ac_attack_damage
attack_speed = ac_attack_speed
health = ac_health

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


        self.piercing = self.archer.piercing
        self.speed = 30.0  # 10/100 map per second
        self.damage = self.archer.attack_damage
        self.special = self.archer.special_status 

        self.damaged_object = []
        if self.piercing :
            self.x_limit = self.archer.box.centerx + (self.archer.attack_scope + self.gameplay.box_size[0] * 3 + self.archer.box.width / 2) * self.side
            if self.side == 1:
                self.img = special_arrow
            elif self.side == -1:
                self.img = reverse(special_arrow)
        else:
            self.x_limit = self.archer.box.centerx + (self.archer.attack_scope + self.gameplay.box_size[0] + self.archer.box.width / 2) * self.side

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
        if (self.x_limit - self.box.centerx) * self.side <= self.box.width / 2 :
            return True

        if self.piercing == True:
            if (len(self.damaged_object) == 3) :
                return True
        
        return False

    def operation(self):
        screen.screen.blit(pygame.transform.smoothscale(self.img.img,(self.imgbox.width,self.imgbox.height)),self.imgbox)
        copy(self.box, self.img.imgbox_to_hitbox(self.imgbox))
        self.move()
        if self.limit_check():
            self.remove()
        else:
            if self.collide_check():
                if not self.special :
                    self.archer.mana += 10

                if self.piercing == False:
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
            self.level = self.gameplay.character_level1[2]
        elif side == 2:
            self.side = -1          
            self.level = self.gameplay.character_level2[2]
            
        self.skill_lasting_time = 4.0
        self.speed = 5.0 # 5/100 map per second 
        self.attack_scope = 7 * self.gameplay.box_size[0] # 4/15 map width
        self.attack_scope_orginal = self.attack_scope
        self.attack_speed = attack_speed[self.level - 1]
        self.attack_speed_orginal = self.attack_speed
        self.attack_damage = attack_damage[self.level - 1]
        self.attack_damage_orginal = self.attack_damage
        self.health_max = health[self.level - 1]
        self.health = self.health_max
        self.mana_max =100.0
        self.mana = 0.0

        self.arrow_list = []
        self.effect_list = []

        self.alive = True
        self.get_hit = False
        self.ischeck = True
        self.iscollide_check = True
        self.collide = None
        self.special_status = False
        self.piercing = False


        self.animation_player = None
        self.moving_animation = animation_player([archer1,archer2,archer3,archer4,archer5,archer6,archer7,archer8,archer9,archer10],self.side, 1, self.imgbox , self.gameplay)
        self.walking_animation = animation_player([archer11,archer12,archer13,archer14,archer15,archer16],self.side, 1, self.imgbox, self.gameplay)
        self.attacking_animation = one_time_animation_player([archer17,archer19,archer20,archer21,archer22,archer23,archer24,archer25,archer26,archer27,archer30],self.side, 0.5 , self.imgbox, self.gameplay)
        self.standstill_animation = one_time_animation_player([archer11,archer12,archer13,archer14,archer15,archer16],self.side, 1, self.imgbox, self.gameplay)
        self.dying_animation = one_time_animation_player([archer40], self.side, 0.8, self.imgbox, self.gameplay)
        self.knock_back_animation = animation_player([archer31], self.side, 1, self.imgbox, self.gameplay)
        self.flying_animation = animation_player([archer32], self.side, 1, self.imgbox, self.gameplay)
        self.falling_animation = animation_player([archer33], self.side, 1, self.imgbox, self.gameplay)

        self.switcher1 = N_time_switch(1)
        self.switcher2 = N_time_switch(1)
        self.switcher3 = N_time_switch(1)
        self.switcher4 = N_time_switch(1)
        self.switcher5 = N_time_switch(1)

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
        if not self.level == self.gameplay.character_level(self.side, 2):
            self.level = self.gameplay.character_level(self.side, 2)
            self.attack_damage = attack_damage[self.level - 1]
            self.attack_damage_orginal = self.attack_damage
            self.health_max = health[self.level - 1]
            self.attack_speed = attack_speed[self.level - 1]
            self.attack_speed_orginal = self.attack_speed
            if self.special_status:
                if len(self.arrow_list) >= self.flag + 1:
                    self.attack_speed *= 2
                    self.attack_coundowner.update_lasting_time(1 / self.attack_speed)
                else:
                    self.attack_damage *= 2


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
                for object in self.gameplay.side( - self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2:
                        if (object.box.centerx - self.box.centerx) * self.side > 0:
                            if same_line_checker(self, object):
                                self.status = 1
                                flag = True
                                ispass = True
                                break
                if not ispass:
                    for object in self.gameplay.side(self.side) + self.gameplay.side4 :
                        if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 2 + (self.box.width + object.box.width) / 2 :
                            if (object.box.centerx - self.box.centerx) * self.side > 0:
                                if same_line_checker(self, object):
                                    if (not (self == object)) and (self.index > object.index):
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
                        if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.speed * screen.screen.get_rect().width / 100) * 0.5  + (self.box.width + object.box.width) / 2 :
                            if (object.box.centerx - self.box.centerx) * self.side >= 0:
                                if same_line_checker(self, object):
                                    if not (self == object):
                                        if not  object.status == 3:
                                            self.status = 5
                                            break           
            
            
            if self.status == 1 :
                if self.attack_coundowner.Return == True:
                    self.status = 2            

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
        if self.attacking_animation.clock.Return == 9:
            if self.switcher1.operation():
                if self.level < 3:
                    self.arrow_list.append(arrowclass(self))  
                elif self.level >= 3 and self.level < 5:
                    self.arrow_list.append(arrowclass(self))  
                    self.imgbox.centery += self.gameplay.box_size[1] / 5
                    self.arrow_list.append(arrowclass(self))  
                    self.imgbox.centery -= self.gameplay.box_size[1] / 5
                elif self.level == 5:
                    tmp = self.imgbox.centery
                    self.arrow_list.append(arrowclass(self))  
                    self.imgbox.centery += self.gameplay.box_size[1] / 5
                    self.arrow_list.append(arrowclass(self))  
                    self.imgbox.centery -= 2 * self.gameplay.box_size[1] / 5
                    self.arrow_list.append(arrowclass(self))  
                    self.imgbox.centery += self.gameplay.box_size[1] / 5
                    self.imgbox.centery = tmp


                    
        elif self.attacking_animation.clock.Return == 8:
            self.switcher1.reset()



    def attack_reset(self):
        self.attacking_animation.reset() 
        self.switcher5.reset()

    
    def special_skill(self):
        if self.switcher2.operation():
            self.piercing = True
            if self.level <= 2:
                self.attack_damage *= 2 
            self.attack_scope = 7 * self.gameplay.box_size[0]
            self.flag = len(self.arrow_list)

        if len(self.arrow_list) >= self.flag + 1:
            if self.switcher3.operation():
                self.piercing = False
                self.attack_damage = self.attack_damage_orginal
                self.attack_scope = self.attack_scope_orginal
                self.attack_speed = self.attack_speed * 2
                self.attack_coundowner.update_lasting_time(1 / self.attack_speed)
                self.skill_countdowner.start()

            if self.skill_countdowner.Return == False:
                self.special_skill_reset()

    def special_skill_reset(self):
        self.special_status = False
        self.piercing = False
        self.switcher2.reset()
        self.switcher3.reset()
        self.attack_damage = self.attack_damage_orginal
        self.attack_speed = self.attack_speed_orginal
        self.attack_coundowner.update_lasting_time(1 / self.attack_speed)
        self.skill_countdowner.reset()



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
                    self.gameplay.gold_income_1 += self.gameplay.character_cost[self.__class__] / 2
                else:
                    self.gameplay.gold_income_2 += self.gameplay.character_cost[self.__class__] / 2
                

            self.display()
            self.status_update()

            for arrows in self.arrow_list:
                arrows.operation()


            # pygame.draw.rect(screen.screen,White,self.box,1)
            # pygame.draw.rect(screen.screen,White,self.imgbox,1)
        else:
            self.dying()


    






