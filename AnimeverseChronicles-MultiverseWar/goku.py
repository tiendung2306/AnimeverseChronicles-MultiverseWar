import pygame 
import math 
from pygame.locals import *
from color import *
from collide_checker import *
from fake_object import *
from clock import *
from switch import *
from list_function import *
from animation_player import *
from screen import *
from common_effect import *
   

class kame_class():
    def __init__(self,goku):
        self.goku = goku
        self.gameplay = self.goku.gameplay
        self.side = self.goku.side

        self.status = True
        self.angle = -45 
        self.damage = 50
        self.width = 0

    def resize(self):
        a = float(screen.screen.get_width()) / self.gameplay.screen[0]
        b = float(screen.screen.get_height()) /  self.gameplay.screen[1]
        tmp_box = pygame.Rect(self.box.left * a, self.box.top *  b, self.box.width * a, self.box.height * b)
        tmp_imgbox = pygame.Rect(self.wizard.imgbox.left,self.wizard.imgbox.top,self.wizard.imgbox.width,self.wizard.imgbox.height)
        fake_imgbox = wizard_to_magic_ball.imgbox_to_hitbox(tmp_imgbox)
        self.imgbox.left *= a
        self.imgbox.top = fake_imgbox.top
        self.imgbox.width = fake_imgbox.width
        self.imgbox.height = fake_imgbox.height
        self.box.top = tmp_box.top
        self.box.left = tmp_box.left
        self.box.width = tmp_box.width
        self.box.height = tmp_box.height

    def display(self):
        if self.side == 1:
            tmp = pygame.transform.rotate(pygame.transform.smoothscale(kame, (self.size[1], self.size[0] + self.width)), self.angle)
        elif self.side == -1:
            tmp = pygame.transform.flip(pygame.transform.rotate(pygame.transform.smoothscale(kame, (self.size[1], self.size[0] + self.width)), self.angle), True, False)
        screen.screen.blit(tmp, self.topleft)
        self.angle += 60/120
        # self.width += 5


    def collide_check(self):
        self.size = (self.goku.box.width ,self.goku.box.width * 20 )
        if self.side == 1:
            self.topleft = (self.goku.box.left + self.goku.box.width / 4, self.goku.box.top + self.goku.box.height / 4)
        elif self.side == -1:
            self.topleft = (self.goku.box.right - self.goku.box.width / 4 , self.goku.box.top + self.goku.box.height / 4)
        if self.side == 1:
            for enemy_object in self.gameplay.side2:
                if collide_check_special(self, enemy_object):
                    enemy_object.get_damage = self.damage
                    enemy_object.get_hit = True
                    return False
        elif self.side == -1:
            for enemy_object in self.gameplay.side1:
                if collide_check_special(self, enemy_object):
                    enemy_object.get_damage = self.damage
                    enemy_object.get_hit = True
                    return False



    def operation(self):
        if self.status:
            self.collide_check()
            self.display()

                
            
class gokuclass():
    def __init__(self, side, box_number, gameplay):
        self.gameplay = gameplay
        self.size = (self.gameplay.box_size[0] , (self.gameplay.box_size[0]  * goku1.data[3] )/ goku1.data[2] )
        self.box = pygame.Rect(box_number * self.gameplay.box_size[0],self.gameplay.path_height - self.size[1] * 4 / 5, self.size[0], self.size[1])
        if side == 1 :
            self.side = 1
            self.imgbox = goku1.hitbox_to_imgbox(self.box)        
        elif side == 2:
            self.side = -1
            self.imgbox = reverse(goku1).hitbox_to_imgbox(self.box)        

        self.skill_lasting_time = 1.5
        self.speed = 15.0 # 5/100 map per second 
        self.attack_scope = 1 * self.gameplay.box_size[0] # 4/15 map width
        self.attack_scope_orginal = self.attack_scope
        self.attack_speed = 1/2 # arrow(s) pers second
        self.attack_speed_orginal = self.attack_speed
        self.attack_damage = 10.0
        self.attack_damage_orginal = self.attack_damage
        self.health_max = 100.0
        self.health = self.health_max
        self.mana_max =100.0
        self.mana = 80

        self.effect_list = []

        self.alive = True
        self.get_hit = False
        self.special_status = False

        self.moving_animation = animation_player([goku5,goku6,goku7,goku8],self.side, 0.5, self.imgbox , self.gameplay)
        tmp_lib = [goku9,goku9,goku9,goku10,goku11,goku12,goku13,goku14]
        for i in range(3):
            for img in [goku1, goku2, goku3, goku4]:
                for counter in range(2):
                    tmp_lib.append(img)
    
        self.attacking_animation = animation_player(tmp_lib,self.side, 1 / self.attack_speed, self.imgbox, self.gameplay)
        self.standstill_animation = animation_player([goku1, goku2, goku3, goku4], self.side, 1, self.imgbox, self.gameplay)
        self.special_skill_animation = one_time_animation_player([goku9,goku10,goku11,goku12,goku13,goku14,goku15,goku18,goku16,goku16,goku16,goku17,goku17,goku17,goku18,goku19,goku20,goku21,goku22,goku23,goku23,goku23,goku24,goku24,goku24,goku25,goku25,goku25,goku25,goku25,goku18,goku18], self.side, 2.25, self.imgbox, self.gameplay)

        self.switcher1 = N_time_switch(1)
        self.switcher2 = N_time_switch(1)
        self.switcher3 = N_time_switch(1)


    def resize(self):
        a = float(screen.screen.get_width()) / self.gameplay.screen[0]
        b = float(screen.screen.get_height()) /  self.gameplay.screen[1]
        tmp_box = pygame.Rect(self.box.left * a, self.box.top *  b, self.box.width * a, self.box.height * b)
        self.size = (self.gameplay.box_size[0] / 2, (self.gameplay.box_size[0] / 2 * goku1.data[3] )/ goku1.data[2] )
        fake_box = pygame.Rect( self.gameplay.box_size[0],self.gameplay.path_height - self.size[1] * 4 / 5, self.size[0], self.size[1])
        fake_imgbox = wizard1.hitbox_to_imgbox(fake_box)
        self.imgbox.left *= a
        self.imgbox.top = fake_imgbox.top
        self.imgbox.width = fake_imgbox.width
        self.imgbox.height = fake_imgbox.height
        self.box.top = tmp_box.top
        self.box.left = tmp_box.left
        self.box.width = tmp_box.width
        self.box.height = tmp_box.height



    def status_bar(self):
        if self.mana >= self.mana_max:
            self.mana = 0
            self.special_status = True
        pygame.draw.rect(screen.screen,Red,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 10 ,(self.box.width - self.box.width / 2) / self.health_max *self.health,self.box.height / 20))
        pygame.draw.rect(screen.screen,Blue,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 5 - self.box.height / 30 ,(self.box.width - self.box.width / 2) / self.mana_max *self.mana,self.box.height / 20))
     
    
    def move(self):
        copy(self.box, self.moving_animation.play())
        self.imgbox.centerx += (self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  * self.side
        self.standstill_animation.reset()
        self.attacking_animation.reset()



    def standstill(self):
        copy(self.box, self.standstill_animation.play())
        self.moving_animation.reset()
        self.attacking_animation.reset()


    def check_forward(self):
        checker = fake_object_class(self)
        if self.side == 1:
            checker.box = tanker1.imgbox_to_hitbox(self.imgbox)
            checker.box.width *= 2
            # pygame.draw.rect(screen.screen,Red,checker.box)
            for object in self.gameplay.side2 :
                if collide_checker(checker,object):
                    self.status = 1
                    return None

            for object in self.gameplay.side1 + self.gameplay.side4:
                if collide_checker(checker ,object):
                    if (not (object == self)) and (object.box.right > checker.box.right):
                        self.status = 2
                        return None

        elif self.side == -1:
            checker.box = reverse(tanker1).imgbox_to_hitbox(self.imgbox)
            checker.box.width *= 2
            checker.box.centerx -= checker.box.width / 2
            # pygame.draw.rect(self.gameplay.screen,White,checker.box)
            for object in self.gameplay.side1 :
                if collide_checker(checker,object):
                    self.status = 1
                    return None

            for object in self.gameplay.side2 + self.gameplay.side4:
                if collide_checker(checker,object):
                    if (not (object == self)) and (object.box.left < checker.box.left) :
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
        self.alive = False
    
    
    def attack(self):
        copy(self.box, self.attacking_animation.play())
        if self.attacking_animation.clock.Return == 4 :
            if self.switcher1.operation():

                if not self.special_status :
                    self.mana += 10 
                        
                checker = fake_object_class(self)
                checker.box.width += self.attack_scope 
                if self.side == 1:
                    for enemy_object in self.gameplay.side2:
                    # pygame.draw.rect(screen.screen,White,checker.box)
                        if collide_checker(checker,enemy_object):
                                enemy_object.get_hit = True
                                enemy_object.get_damage = self.attack_damage
                elif self.side == -1:
                    checker.box.centerx -= self.attack_scope 
                    # pygame.draw.rect(screen.screen,White,checker.box)
                    for enemy_object in self.gameplay.side1:
                        if collide_checker(checker,enemy_object):
                                enemy_object.get_hit = True
                                enemy_object.get_damage = self.attack_damage
        elif self.attacking_animation.clock.Return == 1:
            self.switcher1.reset()

        self.standstill_animation.reset()
        self.moving_animation.reset()

    
    def special_skill(self):
        copy(self.box, self.special_skill_animation.play())
        if self.special_skill_animation.clock.Return == 4:
            if self.switcher2.operation():
                checker = fake_object_class(self)
                checker.box.width += self.attack_scope 
                if self.side == 1:
                    for enemy_object in self.gameplay.side2:
                    # pygame.draw.rect(screen.screen,White,checker.box)
                        if collide_checker(checker,enemy_object):
                            self.target = enemy_object
                            add_effect(enemy_object, knock_back_effect, None, 4)
                            enemy_object.get_hit = True
                            enemy_object.get_damage = self.attack_damage
                            return
                    self.special_skill_reset()
                    
                elif self.side == -1:
                    checker.box.centerx -= self.attack_scope 
                    # pygame.draw.rect(screen.screen,White,checker.box)
                    for enemy_object in self.gameplay.side1:
                        if collide_checker(checker,enemy_object):
                            self.target = enemy_object
                            add_effect(enemy_object, knock_back_effect, None, 4)
                            enemy_object.get_hit = True
                            enemy_object.get_damage = self.attack_damage   
                            return
                    self.special_skill_reset()
                    
    
        elif self.special_skill_animation.clock.Return == 5:
            self.switcher2.reset()
        elif self.special_skill_animation.clock.Return == 8:
            if self.switcher2.operation():
                self.tmp = fake_object_class(self)
                self.gameplay.side4.append(self.tmp)
                self.imgbox.centerx = self.target.imgbox.centerx - self.gameplay.box_size[0] * self.side
        elif self.special_skill_animation.clock.Return == 9:
            self.switcher2.reset()
        elif self.special_skill_animation.clock.Return == 10:
            if self.switcher2.operation():
                add_effect(self.target, flying_effect, None, 3)
        elif self.special_skill_animation.clock.Return == 11:
            self.switcher2.reset()
        elif self.special_skill_animation.clock.Return == 15:
            if self.switcher2.operation():
                self.imgbox.centery -= 4 * self.gameplay.box_size[1]
                self.imgbox.centerx -= self.gameplay.box_size[0]
                self.kame = kame_class(self)
        elif self.special_skill_animation.clock.Return >= 20 and self.special_skill_animation.clock.Return < 30:
            self.kame.operation()
            self.switcher2.reset()

        elif self.special_skill_animation.clock.Return == 30 :
            if self.switcher2.operation():
                copy(self.imgbox, self.tmp.imgbox)
                self.gameplay.side4.remove(self.tmp)

        if self.special_skill_animation.status == False:
            self.special_skill_reset()

            


    def special_skill_reset(self):
        self.special_status = False
        self.switcher2.reset()
        self.special_skill_animation.reset()

    def operation(self):
        if self.alive: 
            if self.special_status:
                self.special_skill()
            else:
                self.check_forward()
                for effect in self.effect_list:
                    effect.play()

                if self.status == 3:
                    self.move()

                elif self.status == 1:
                    self.attack()

                elif self.status == 2 :
                    self.standstill()
            
            self.status_bar()
            if self.get_hit:
               self.Geting_hit()

            if self.health <= 0:
                self.die()
            

            pygame.draw.rect(screen.screen,Red,self.box,1)
            pygame.draw.rect(screen.screen,White,self.imgbox,1)

    






