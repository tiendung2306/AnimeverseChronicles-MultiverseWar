import pygame 
from pygame.locals import *
from color import *
from collide_checker import *
from fake_object import *
from clock import *
from switch import *
from list_function import *
from animation_player import *


   

class arrowclass():
    def __init__(self,archer):
        self.archer = archer
        self.gameplay = self.archer.gameplay
        self.side = self.archer.side

        if self.side == 1:
            self.img_lib = [arrow1]
        elif self.side == -1:
            self.img_lib = [arrow2] 

        self.imgbox = pygame.Rect(self.archer.imgbox.left,self.archer.imgbox.top,self.archer.imgbox.width,self.archer.imgbox.height)
        self.box = self.img_lib[0].imgbox_to_hitbox(self.imgbox)

        self.spam_pointX = ( self.imgbox.left + self.imgbox.right) / 2
        self.time_flag = self.archer.gameplay.curr_time 

        self.piercing = self.archer.piercing
        self.speed = 10  # 10/100 map per second
        self.damage = self.archer.attack_damage
        self.special = self.archer.special_status 
        self.status = True

        self.damaged_object = []
        if self.piercing :
            self.x_limit = self.archer.box.right + self.archer.attack_scope


    def move(self):
        self.imgbox.centerx = self.spam_pointX+ (self.speed * self.gameplay.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.time_flag)  * self.side
    

    def collide_check(self):
        if self.side == 1:
            for enemy_object in self.archer.gameplay.side2:
                if collide_checker(self,enemy_object):
                    if list_find(self.damaged_object,enemy_object) == -1:
                        self.damaged_object.append(enemy_object)
                        enemy_object.get_damage = self.damage
                        enemy_object.get_hit = True
                        if not self.piercing:
                            self.status = False
        elif self.side == -1:
            for enemy_object in self.archer.gameplay.side1:
                if collide_checker(self,enemy_object):
                    if list_find(self.damaged_object,enemy_object) == -1:
                        self.damaged_object.append(enemy_object)
                        enemy_object.get_damage = self.damage
                        enemy_object.get_hit = True
                        if not self.piercing:
                            self.status = False


    def limit_check(self):
        if (len(self.damaged_object) == 3) or (self.box.right >= self.x_limit):
            self.status = False


    def arrow_operation(self):
        self.collide_check()
        if self.special :
            pygame.draw.rect(self.gameplay.screen,Yellow,self.box)          
        if self.piercing :
            pygame.draw.rect(self.gameplay.screen,Black,self.box)  

        self.gameplay.screen.blit(pygame.transform.smoothscale(self.img_lib[0].img,(self.imgbox.width,self.imgbox.height)),self.imgbox)
        self.box = self.img_lib[0].imgbox_to_hitbox(self.imgbox)

        if self.status:
            if self.piercing :
                self.limit_check()
            self.move()
        elif self.special == False :
            return True
        
class archerclass():
    def __init__(self, side, box_number, gameplay):
        if side == 1 :
            self.side = 1
        elif side == 2:
            self.side = -1

        self.gameplay = gameplay

        self.size = self.gameplay.box_size
        if self.side == 1:
            self.img_lib = [archer1_1, archer1_2, archer1_3]
        elif self.side == -1:
            self.img_lib = [archer2_1, archer2_2, archer2_3]
        self.imgbox = self.img_lib[0].hitbox_to_imgbox(pygame.Rect(box_number * self.gameplay.box_size[0],self.gameplay.path_height - self.gameplay.box_size[1], self.gameplay.box_size[0], self.gameplay.box_size[1]))        
        self.box = self.img_lib[0].imgbox_to_hitbox(self.imgbox)
        
        self.spam_pointX = None
        self.time_flag = self.gameplay.curr_time 
        
        self.skill_lasting_time = 1.5
        self.piercing = False
        self.speed = 5 # 5/100 map per second 
        self.attack_scope = 4 * self.gameplay.box_size[0] # 4/15 map width
        self.attack_scope_orginal = self.attack_scope
        self.attack_speed = 1 # arrow(s) pers second
        self.attack_speed_orginal = self.attack_speed
        self.attack_damage = 10 
        self.attack_damage_orginal = self.attack_damage
        self.health_max = 100
        self.health = self.health_max
        self.mana_max =100
        self.mana = 0

        self.arrow_list = []

        self.alive = True
        self.get_hit = False
        self.get_damage = 0
        self.special_status = False

        self.moving_animation = animation_player([self.img_lib[0], self.img_lib[1]], 1, self.imgbox , self.gameplay)
        self.attacking_animation = animation_player([self.img_lib[0], self.img_lib[2]], 1 / self.attack_speed, self.imgbox, self.gameplay)
        self.standstill_animation = animation_player([self.img_lib[0], self.img_lib[0]], 1, self.imgbox, self.gameplay)

        self.switcher1 = N_time_switch(1)
        self.switcher2 = N_time_switch(1)
        self.switcher3 = N_time_switch(1)
        self.skill_countdowner = timing_clock(self.skill_lasting_time,self.gameplay)

        self.special_arrow_switcher = N_time_switch(1)


    def status_bar(self):
        if self.mana >= self.mana_max:
            self.mana = 0
            self.special_status = True
        if self.special_status :
            if self.skill_countdowner.Return == False:
                self.special_skill_reset() 
        pygame.draw.rect(self.gameplay.screen,Red,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 10 ,(self.box.width - self.box.width / 2) / self.health_max *self.health,self.box.height / 20))
        pygame.draw.rect(self.gameplay.screen,Blue,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 5 - self.box.height / 30 ,(self.box.width - self.box.width / 2) / self.mana_max *self.mana,self.box.height / 20))
     
    
    def move(self):
        if self.switcher3.operation():
            self.time_flag = self.gameplay.curr_time
            self.spam_pointX = ( self.imgbox.left + self.imgbox.right) / 2

        else:
            self.box = self.moving_animation.play()
            self.imgbox.centerx = self.spam_pointX+ (self.speed * self.gameplay.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.time_flag)  * self.side
        self.standstill_animation.reset()
        self.attacking_animation.reset()

    def standstill(self):
        self.box = self.standstill_animation.play()
        self.moving_animation.reset()
        self.attacking_animation.reset()
        self.switcher3.reset()
    

    def check_forward(self):
        checker = fake_object_class(self)
        for tmp_img in self.img_lib:
            checker.box = tmp_img.imgbox_to_hitbox(self.imgbox)
            checker.box.width += self.attack_scope 
            if self.side == 1:
                # pygame.draw.rect(self.gameplay.screen,Red,checker.box)
                for object in self.gameplay.side2 :
                    if collide_checker(checker,object):
                        return 1
                
                for object in self.gameplay.side1:
                    if collide_checker(self,object):
                         if (not (object == self)) and (object.box.left >= self.box.left):
                            return 2

            elif self.side == -1:
                checker.box.centerx -= self.attack_scope 
                # pygame.draw.rect(self.gameplay.screen,White,checker.box)
                for object in self.gameplay.side1 :
                    if collide_checker(checker,object):
                        return 1
                for object in self.gameplay.side2:
                    if collide_checker(self,object):
                        if (not (object == self)) and (object.box.left <= self.box.left) :
                            return 2
        return 0
        

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
        self.skill_countdowner.remove()  
        self.alive = False
    
    
    def attack(self):
        self.box = self.attacking_animation.play()
        if self.attacking_animation.clock.Return == 2:
            if self.switcher1.operation():

                if self.special_status :
                    self.special_skill()

                    
                else:
                    self.arrow_list.append(arrowclass(self))  
        elif self.attacking_animation.clock.Return == 1:     
            self.switcher1.reset()

        self.standstill_animation.reset()
        self.moving_animation.reset()
        self.switcher3.reset()

    
    def special_skill(self):
        if self.special_arrow_switcher.operation():
            self.piercing = True
            self.attack_damage = 20
            self.attack_scope = 7 * self.gameplay.box_size[0]
            self.arrow_list.append(arrowclass(self))  

            self.piercing = False
            self.attack_damage = self.attack_damage_orginal
            self.attack_scope = 4 * self.attack_scope_orginal
            self.attack_speed = self.attack_speed * 2
            self.attacking_animation.update_looptime( 1 / self.attack_speed )
            self.skill_countdowner.start()
        else:
            self.arrow_list.append(arrowclass(self))    


    def special_skill_reset(self):
        self.special_status = False
        self.attack_speed = self.attack_speed_orginal
        self.attacking_animation.update_looptime(1 / self.attack_speed)
        self.skill_countdowner.reset()
        self.special_arrow_switcher.reset()


    def operation(self):
        if self.alive: 
            self.status_bar()
            tmp = self.check_forward()
            if tmp == 0:
                self.move()

            elif tmp == 1:
                self.attack()

            elif tmp == 2 :
                self.standstill()
            
            if self.get_hit:
               self.Geting_hit()

            if self.health <= 0:
                self.die()
            
            for arrows in self.arrow_list:
                if arrows.arrow_operation():
                    self.mana += 10
                if arrows.status == False :
                    self.arrow_list.remove(arrows)

            pygame.draw.rect(self.gameplay.screen,White,self.box,1)
            pygame.draw.rect(self.gameplay.screen,White,self.imgbox,1)

    






