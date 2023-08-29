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

        self.spam_pointX = ( self.imgbox.left + self.imgbox.right) / 2
        self.time_flag = self.archer.gameplay.curr_time 

        self.piercing = self.archer.piercing
        self.speed = 10.0  # 10/100 map per second
        self.damage = self.archer.attack_damage
        self.special = self.archer.special_status 
        self.status = True

        self.damaged_object = []
        if self.piercing :
            self.x_limit = self.archer.box.right + self.archer.attack_scope * 2
            if self.side == 1:
                self.img = special_arrow
            elif self.side == -1:
                self.img = reverse(special_arrow)


    def move(self):
        self.imgbox.centerx = self.spam_pointX + (self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.time_flag)  * self.side


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


    def operation(self):
        self.collide_check()
        # if self.special :
        #     pygame.draw.rect(screen.screen,Yellow,self.box)          
        # if self.piercing :
        #     pygame.draw.rect(screen.screen,Black,self.box)  

        screen.screen.blit(pygame.transform.smoothscale(self.img.img,(self.imgbox.width,self.imgbox.height)),self.imgbox)
        self.box = self.img.imgbox_to_hitbox(self.imgbox)

        if self.status:
            if self.piercing :
                self.limit_check()
            self.move()
        elif self.special == False :
            return True
        
class archerclass():
    def __init__(self, side, box_number, gameplay):
        self.gameplay = gameplay
        self.box = pygame.Rect(box_number * self.gameplay.box_size[0],self.gameplay.path_height - self.gameplay.box_size[1], self.gameplay.box_size[0], self.gameplay.box_size[1])
        if side == 1 :
            self.side = 1
            self.imgbox = archer1.hitbox_to_imgbox(self.box)        

        elif side == 2:
            self.side = -1
            self.imgbox = reverse(archer1).hitbox_to_imgbox(self.box)        
        
        self.skill_lasting_time = 5
        self.piercing = False
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
        self.special_status = False

        self.moving_animation = animation_player([archer1,archer2,archer3,archer4,archer5,archer6,archer7,archer8,archer9,archer10],self.side, 1, self.imgbox , self.gameplay)
        self.attacking_animation = animation_player([archer17,archer18,archer19,archer20,archer21,archer22,archer23,archer24,archer25,archer26,archer27,archer28,archer29,archer30,archer11,archer12,archer13,archer14,archer15,archer16],self.side, 1 / self.attack_speed, self.imgbox, self.gameplay)
        self.standstill_animation = animation_player([archer11,archer12,archer13,archer14,archer15,archer16],self.side, 1, self.imgbox, self.gameplay)

        self.switcher1 = N_time_switch(1)
        self.switcher2 = N_time_switch(1)
        self.switcher3 = N_time_switch(1)
        self.switcher4 = N_time_switch(1)
        self.switcher5 = N_time_switch(1)

        self.skill_countdowner = timing_clock(self.skill_lasting_time,self.gameplay)

        self.special_arrow_switcher = N_time_switch(1)


    def status_bar(self):
        if self.mana >= self.mana_max:
            self.mana = 0
            self.special_status = True
        if self.special_status :
            if self.skill_countdowner.Return == False:
                self.special_skill_reset() 
        pygame.draw.rect(screen.screen,Red,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 10 ,(self.box.width - self.box.width / 2) / self.health_max *self.health,self.box.height / 20))
        pygame.draw.rect(screen.screen,Blue,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 5 - self.box.height / 30 ,(self.box.width - self.box.width / 2) / self.mana_max *self.mana,self.box.height / 20))
     
    
    def move(self):
        if self.switcher3.operation():
            if self.side == 1 :
                tmp = archer1.hitbox_to_imgbox(self.box) 
                self.imgbox.left =  tmp.left  
                self.imgbox.top = tmp.top
                self.imgbox.width = tmp.width
                self.imgbox.height = tmp.height

            elif self.side == -1:
                tmp = reverse(archer1).hitbox_to_imgbox(self.box)    
                self.imgbox.left =  tmp.left  
                self.imgbox.top = tmp.top
                self.imgbox.width = tmp.width
                self.imgbox.height = tmp.height

            self.time_flag = self.gameplay.curr_time
            self.spam_pointX = ( self.imgbox.left + self.imgbox.right) / 2
            self.standstill_animation.reset()
            self.attacking_animation.reset()
            self.switcher4.reset()
            self.switcher5.reset()

        else:
            self.imgbox.centerx = self.spam_pointX + (self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.time_flag)  * self.side
            self.box = self.moving_animation.play()

    def standstill(self):
        if self.switcher5.operation():
            if self.side == 1 :
                tmp = archer11.hitbox_to_imgbox(self.box) 
                self.imgbox.left =  tmp.left  
                self.imgbox.top = tmp.top
                self.imgbox.width = tmp.width
                self.imgbox.height = tmp.height

            elif self.side == -1:
                tmp = reverse(archer11).hitbox_to_imgbox(self.box)    
                self.imgbox.left =  tmp.left  
                self.imgbox.top = tmp.top
                self.imgbox.width = tmp.width
                self.imgbox.height = tmp.height
        self.box = self.standstill_animation.play()
        self.moving_animation.reset()
        self.attacking_animation.reset()
        self.switcher3.reset()
        self.switcher4.reset()
    

    def check_forward(self):
        checker = fake_object_class(self)
        if self.side == 1:
            checker.box = archer1.imgbox_to_hitbox(self.imgbox)
            checker.box.width += self.attack_scope 
            # pygame.draw.rect(screen.screen,Red,checker.box)
            for object in self.gameplay.side2 :
                if collide_checker(checker,object):
                    self.status = 1
                    return None
            checker.box.width -= self.attack_scope 
            for object in self.gameplay.side1:
                if collide_checker(checker,object):
                        if (not (object == self)) and (object.box.left >= checker.box.left):
                            self.status = 2
                            return None

        elif self.side == -1:
            checker.box = reverse(archer1).imgbox_to_hitbox(self.imgbox)
            checker.box.width += self.attack_scope
            checker.box.centerx -= self.attack_scope 
            # pygame.draw.rect(self.gameplay.screen,White,checker.box)
            for object in self.gameplay.side1 :
                if collide_checker(checker,object):
                    self.status = 1
                    return None
            checker.box.centerx += self.attack_scope 
            checker.box.width -= self.attack_scope 
            for object in self.gameplay.side2:
                if collide_checker(checker,object):
                    if (not (object == self)) and (object.box.left <= checker.box.left) :
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
        self.skill_countdowner.remove()  
        self.alive = False
    
    
    def attack(self):
        if self.switcher4.operation():
            if self.side == 1 :
                tmp = archer11.hitbox_to_imgbox(self.box) 
                self.imgbox.left =  tmp.left  
                self.imgbox.top = tmp.top
                self.imgbox.width = tmp.width
                self.imgbox.height = tmp.height

            elif self.side == -1:
                tmp = reverse(archer11).hitbox_to_imgbox(self.box)    
                self.imgbox.left =  tmp.left  
                self.imgbox.top = tmp.top
                self.imgbox.width = tmp.width
                self.imgbox.height = tmp.height
            self.standstill_animation.reset()
            self.moving_animation.reset()
            self.switcher3.reset()
            self.switcher5.reset()

        self.box = self.attacking_animation.play()
        if self.attacking_animation.clock.Return == 9:
            if self.switcher1.operation():

                if self.special_status :
                    self.special_skill()

                    
                else:
                    self.arrow_list.append(arrowclass(self))  
        elif self.attacking_animation.clock.Return == 1:     
            self.switcher1.reset()


    
    def special_skill(self):
        if self.special_arrow_switcher.operation():
            self.piercing = True
            self.attack_damage = 20
            self.attack_scope = 7 * self.gameplay.box_size[0]
            self.arrow_list.append(arrowclass(self))  

            self.piercing = False
            self.attack_damage = self.attack_damage_orginal
            self.attack_scope = self.attack_scope_orginal
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
            self.check_forward()
            for effect in self.effect_list:
                effect.play()
            if self.status == 3:
                self.move()

            elif self.status == 1:
                self.attack()

            elif self.status == 2 :
                self.standstill()
            
            if self.get_hit:
               self.Geting_hit()

            if self.health <= 0:
                self.die()
            
            for arrows in self.arrow_list:
                if arrows.operation():
                    self.mana += 10
                if arrows.status == False :
                    self.arrow_list.remove(arrows)
            pygame.draw.rect(screen.screen,White,self.box,1)
            pygame.draw.rect(screen.screen,White,self.imgbox,1)

    






