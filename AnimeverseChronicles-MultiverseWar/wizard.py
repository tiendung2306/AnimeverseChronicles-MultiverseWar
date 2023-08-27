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

        self.spam_pointX = ( self.imgbox.left + self.imgbox.right) / 2
        self.time_flag = self.wizard.gameplay.curr_time 

        self.speed = 30  # 10/100 map per second
        self.damage = self.wizard.attack_damage
        self.status = True
        self.direct = True

        self.animation_player = animation_player([magic_ball1, magic_ball2, magic_ball3, magic_ball4,magic_ball5],self.side,1,self.imgbox,self.wizard.gameplay)
        self.switch = N_time_switch(1)


    def move(self):
        self.imgbox.centerx = self.spam_pointX+ (self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.time_flag)  * self.side
        self.box = self.animation_player.play()

    def explosive(self):
        if self.switch.operation():
            self.animation_player2 = animation_player([magic_ball6,magic_ball7, magic_ball8, magic_ball9],self.side,0.25,self.imgbox,self.wizard.gameplay)
        self.animation_player2.play()

    def collide_check(self):
        if self.direct:
            if self.side == 1:
                for enemy_object in self.wizard.gameplay.side2:
                    if collide_checker(self,enemy_object):
                        enemy_object.get_damage = self.damage
                        enemy_object.get_hit = True
                        return False
            elif self.side == -1:
                for enemy_object in self.wizard.gameplay.side1:
                    if collide_checker(self,enemy_object):
                        enemy_object.get_damage = self.damage
                        enemy_object.get_hit = True
                        return False
            return True
        else:
            return False
                    


    def operation(self):
        if self.status:
            if self.collide_check():
                self.move()
            else:
                self.direct = False
                self.explosive()
                if self.animation_player2.clock.gameplay.curr_time >= self.animation_player2.clock.counter:
                    if self.animation_player2.clock.Return == self.animation_player2.clock.times:
                        self.status = False
                        return True
            
class wizardclass():
    def __init__(self, side, box_number, gameplay):
        self.gameplay = gameplay
        self.box = pygame.Rect(box_number * self.gameplay.box_size[0],self.gameplay.path_height - self.gameplay.box_size[1], self.gameplay.box_size[0], self.gameplay.box_size[1])
        if side == 1 :
            self.side = 1
            self.imgbox = wizard1.hitbox_to_imgbox(self.box)        
        elif side == 2:
            self.side = -1
            self.imgbox = reverse(wizard1).hitbox_to_imgbox(self.box)        

        self.skill_lasting_time = 1.5
        self.speed = 5.0 # 5/100 map per second 
        self.attack_scope = 7 * self.gameplay.box_size[0] # 4/15 map width
        self.attack_scope_orginal = self.attack_scope
        self.attack_speed = 1/5 # arrow(s) pers second
        self.attack_speed_orginal = self.attack_speed
        self.attack_damage = 10.0
        self.attack_damage_orginal = self.attack_damage
        self.health_max = 100.0
        self.health = self.health_max
        self.mana_max =100.0
        self.mana = 0

        self.magicball_list = []
        self.effect_list = []

        self.alive = True
        self.get_hit = False
        self.special_status = False

        self.moving_animation = animation_player([wizard1,wizard2,wizard3,wizard2],self.side, 1, self.imgbox , self.gameplay)
        tmp_lib = [wizard4,wizard5,wizard6,wizard7,wizard8,wizard9,wizard10,wizard11]
        for i in range(3):
            for img in [wizard1,wizard2,wizard3,wizard2,wizard1]:
                for counter in range(2):
                    tmp_lib.append(img)
    
        self.attacking_animation = animation_player(tmp_lib,self.side, 1 / self.attack_speed, self.imgbox, self.gameplay)
        self.standstill_animation = animation_player([wizard1,wizard2,wizard3,wizard2], self.side, 1, self.imgbox, self.gameplay)

        self.switcher1 = N_time_switch(1)
        self.switcher2 = N_time_switch(1)
        self.switcher3 = N_time_switch(1)
        self.skill_countdowner = timing_clock(self.skill_lasting_time,self.gameplay)



    def status_bar(self):
        if self.mana >= self.mana_max:
            self.mana = 0
            self.special_status = True

        pygame.draw.rect(screen.screen,Red,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 10 ,(self.box.width - self.box.width / 2) / self.health_max *self.health,self.box.height / 20))
        pygame.draw.rect(screen.screen,Blue,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 5 - self.box.height / 30 ,(self.box.width - self.box.width / 2) / self.mana_max *self.mana,self.box.height / 20))
     
    
    def move(self):
        if self.switcher3.operation():
            self.time_flag = self.gameplay.curr_time
            self.spam_pointX = ( self.imgbox.left + self.imgbox.right) / 2

        else:
            self.box = self.moving_animation.play()
            self.imgbox.centerx = self.spam_pointX+ (self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.time_flag)  * self.side
        self.standstill_animation.reset()
        self.attacking_animation.reset()

    def standstill(self):
        self.box = self.standstill_animation.play()
        self.moving_animation.reset()
        self.attacking_animation.reset()
        self.switcher3.reset()
    

    def check_forward(self):
        checker = fake_object_class(self)
        if self.side == 1:
            checker.box = wizard1.imgbox_to_hitbox(self.imgbox)
            checker.box.width += self.attack_scope
            # pygame.draw.rect(self.gameplay.screen,Red,checker.box)
            for object in self.gameplay.side2 :
                if collide_checker(checker,object):
                    self.status = 1
                    return None
            
            for object in self.gameplay.side1:
                if collide_checker(self,object):
                    if (not (object == self)) and (object.box.left >= self.box.left):
                        self.status = 2
                        return None


        elif self.side == -1:
            checker.box =reverse(wizard1).imgbox_to_hitbox(self.imgbox)
            checker.box.width += self.attack_scope
            checker.box.centerx -= self.attack_scope 
            pygame.draw.rect(screen.screen,White,checker.box,1)
            for object in self.gameplay.side1 :
                if collide_checker(checker,object):
                    self.status = 1
                    return None

            for object in self.gameplay.side2:
                if collide_checker(self,object):
                    if (not (object == self)) and (object.box.left <= self.box.left) :
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
        self.box = self.attacking_animation.play()
        if self.attacking_animation.clock.Return == 3:
            if self.switcher1.operation():
                self.magicball_list.append(magic_ball_class(self))  
        elif self.attacking_animation.clock.Return == 1:     
            self.switcher1.reset()

        self.standstill_animation.reset()
        self.moving_animation.reset()
        self.switcher3.reset()

    
    def special_skill(self):
        if self.switcher2.operation():
            self.skill_countdowner.start()
            self.special_skill_animation = one_time_animation_player([wizard11,wizard12,wizard13,wizard14,wizard15,wizard16,wizard17,wizard18,wizard19,wizard20,wizard21,wizard22,wizard23,wizard24,wizard25,wizard26,wizard27,wizard28], self.side, 2, self.imgbox, self.gameplay)
            checker = fake_object_class(self)
            checker.box.width += self.attack_scope * 1.5
            if self.side == 1:
                for enemy in self.gameplay.side2:
                    if collide_checker(checker,enemy):
                        add_effect(enemy, dizzy_effect, 5)
                        self.special_effect_animation = one_time_animation_player([soul1, soul2, soul3, soul4, soul5, soul6, soul6, soul6, soul7, soul8], self.side, 1,soul1.hitbox_to_imgbox(pygame.Rect(enemy.box.left - enemy.box.width * 3 / 4, enemy.box.top - enemy.box.height /2, enemy.box.width, enemy.box.height )),  self.gameplay)
                        break
                    else:
                        self.special_skill_reset()

            elif self.side == -1:
                checker.box.centerx -= self.attack_scope * 1.5
                for enemy in self.gameplay.side1:
                    print(checker.box, enemy.box)
                    if collide_checker(checker,enemy):
                        add_effect(enemy, dizzy_effect, 5)
                        print("okok")
                        self.special_effect_animation = one_time_animation_player([soul1, soul2, soul3, soul4, soul5, soul6, soul6, soul6, soul7, soul8], self.side, 1,soul1.hitbox_to_imgbox(pygame.Rect(enemy.box.right - enemy.box.width / 4, enemy.box.top - enemy.box.height /2, enemy.box.width, enemy.box.height )),  self.gameplay)
                        break
                    else:
                        self.special_skill_reset()
        else:
            self.box = self.special_skill_animation.play()
            if self.special_skill_animation.clock.Return >= 5:
                self.special_effect_animation.play()
            if self.special_skill_animation.status == False:
                self.special_skill_reset()
            


    def special_skill_reset(self):
        self.special_status = False
        self.skill_countdowner.reset()
        self.switcher2.reset()


    def operation(self):
        if self.alive: 
            self.status_bar()
            self.check_forward()
            for effect in self.effect_list:
                effect.play()

            if self.status == 3:
                self.move()

            elif self.status == 1:
                if self.special_status:
                    self.special_skill()
                else:
                    self.attack()

            elif self.status == 2 :
                self.standstill()
            
            if self.get_hit:
               self.Geting_hit()

            if self.health <= 0:
                self.die()
            
            for magic_ball in self.magicball_list:
                if magic_ball.operation():
                    self.mana += 10
                if magic_ball.status == False :
                    self.magicball_list.remove(magic_ball)

            pygame.draw.rect(screen.screen,White,self.box,1)
            pygame.draw.rect(screen.screen,White,self.imgbox,1)

    






