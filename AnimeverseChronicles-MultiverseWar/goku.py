import pygame 
import math 
from pygame.locals import *
from color import *
from collide_checker import *
from object_function import *
from clock import *
from switch import *
from animation_player import *
from common_effect import *
from screen import *
   
class getting_hit_object():
    def __init__(self, object):
        self.object = object
        self.clock = timing_clock(0.1, object.gameplay)
        self.clock.start()

class kame_class():
    def __init__(self,goku):
        self.goku = goku
        self.gameplay = self.goku.gameplay
        self.side = self.goku.side
        if self.side == 1:
            self.start_point = goku_to_kame.imgbox_to_hitbox(goku.imgbox).topleft
            self.angle = -45
        elif self.side == -1:
            self.angle = -45 - 90
            self.start_point = goku_to_kame.reverse.imgbox_to_hitbox(goku.imgbox).topleft
        self.size = (self.goku.box.width * 20 ,self.goku.box.width )
        self.width = self.size[1] / 2
        self.radius = self.size[0] / 2

        self.status = True
        self.damage = 50
        self.damaged_list = []

        self.switch = N_time_switch(1)

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
        if self.switch.operation():
            self.time_marker = self.goku.gameplay.curr_time + 0.3
        self.img = pygame.transform.smoothscale(kame, (self.size[0], self.width))
        tmp = pygame.transform.rotate(self.img, self.angle)
        Center = (self.start_point[0] + math.cos(self.angle * math.pi/ 180) * self.radius, self.start_point[1] - math.sin(self.angle * math.pi / 180) * self.radius)
        tmp2 = tmp.get_rect(center = Center)
        screen.screen.blit(tmp, tmp2)
        self.angle += 25 * (self.goku.gameplay.curr_time - self.goku.gameplay.pre_curr_time) * self.side
        if  self.goku.gameplay.curr_time <= self.time_marker:
            self.width = self.size[1] / 5
        else:
            self.width += (self.goku.gameplay.curr_time - self.goku.gameplay.pre_curr_time) * self.size[1] * 3 / 0.5



    def collide_check(self):

        if self.side == 1:
            for enemy_object in self.gameplay.side2:
                if collide_check_special(self, enemy_object):
                    if not list_find_special(self.damaged_list, enemy_object):
                        self.damaged_list.append(getting_hit_object(enemy_object))
                        enemy_object.get_hit = True
                        enemy_object.get_damage = self.damage

        elif self.side == -1:
            for enemy_object in self.gameplay.side1:
                if collide_check_special(self, enemy_object):
                    if not list_find_special(self.damaged_list, enemy_object):
                        self.damaged_list.append(getting_hit_object(enemy_object))
                        enemy_object.get_hit = True
                        enemy_object.get_damage = self.damage
        for damaged_object in self.damaged_list:
            if damaged_object.clock.Return == False:
                self.damaged_list.remove(damaged_object)



    def operation(self):
        if self.status:
            self.collide_check()
            self.display()

                
            
class gokuclass():
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
        self.attack_scope = 1 * self.gameplay.box_size[0] # 4/15 map width
        self.attack_scope_orginal = self.attack_scope
        self.attack_speed = 1/2 # arrow(s) pers second
        self.attack_speed_orginal = self.attack_speed
        self.attack_damage = 30.0
        self.attack_damage_orginal = self.attack_damage
        self.health_max = 1000.0
        self.health = self.health_max
        self.mana_max =100.0
        self.mana = 0.0

        self.effect_list = []

        self.alive = True
        self.get_hit = False
        self.check = False
        self.collide = None
        self.special_status = False

        self.moving_animation = animation_player([goku5,goku6,goku7,goku8],self.side, 0.5, self.imgbox , self.gameplay)
        self.attacking_animation = one_time_animation_player([goku9,goku9,goku9,goku10,goku11,goku12,goku13,goku14],self.side, 0.5 , self.imgbox, self.gameplay)
        self.standstill_animation = one_time_animation_player([goku1, goku2, goku3, goku4], self.side, 1, self.imgbox, self.gameplay)
        self.special_skill_animation = one_time_animation_player([goku9,goku10,goku11,goku12,goku13,goku14,goku15,goku18,goku16,goku16,goku16,goku17,goku17,goku17,goku18,goku19,goku20,goku21,goku21,goku21,goku22,goku22,goku22,goku23,goku23,goku23,goku24,goku24,goku24,goku25,goku25,goku25,goku25,goku25,goku18,goku18], self.side, 2.25, self.imgbox, self.gameplay)
        self.dying_animation = one_time_animation_player([goku51], self.side, 0.8, self.imgbox, self.gameplay)
        self.knock_back_animation = animation_player([goku53], self.side, 1, self.imgbox, self.gameplay)
        self.flying_animation = animation_player([goku52], self.side, 1, self.imgbox, self.gameplay)
        self.falling_animation = animation_player([goku50], self.side, 1, self.imgbox, self.gameplay)


        self.switcher1 = N_time_switch(1)
        self.switcher2 = N_time_switch(1)
        self.switcher3 = N_time_switch(1)

        self.attack_coundowner = timing_clock(1 / self.attack_speed, self.gameplay)



    def resize(self):
        a = float(screen.screen.get_width()) / self.gameplay.screen[0]
        b = float(screen.screen.get_height()) /  self.gameplay.screen[1]
        tmp = pygame.Rect(self.imgbox.left * a, self.imgbox.top * b, self.imgbox.width * a, self.imgbox.height * b)
        copy(self.imgbox, tmp)
        self.operation()


    def status_update(self):
        if self.mana >= self.mana_max:
            self.mana = 0
            self.special_status = True
            self.status = 4

        pygame.draw.rect(screen.screen,Red,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 10 ,(self.box.width - self.box.width / 2) / self.health_max *self.health,self.box.height / 20))
        pygame.draw.rect(screen.screen,Blue,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 5 - self.box.height / 30 ,(self.box.width - self.box.width / 2) / self.mana_max *self.mana,self.box.height / 20))
     
    
    def move(self):
        if not self.status == self.pre_status:
            self.moving_animation.reset()
        copy(self.box, self.moving_animation.play())
        self.imgbox.centerx += (self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  * self.side
        self.check = True


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
        if self.attacking_animation.clock.Return == 6:
            if self.switcher1.operation():
                if not self.special_status :
                    self.mana += 10 
                for object in self.gameplay.side(- self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                object.get_hit = True
                                object.get_damage = self.attack_damage
        elif self.attacking_animation.clock.Return == 5 :
            self.switcher1.reset()
        if self.attacking_animation.status == True:
            self.check = False
        elif self.attacking_animation.status == False:
            self.check = True
            self.attacking_animation.reset() 


    def special_skill(self):
        copy(self.box, self.special_skill_animation.play())
        if self.special_skill_animation.clock.Return == 4:
            if self.switcher2.operation():
                for object in self.gameplay.side(- self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope * 1.5 + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                self.target = object
                                add_effect(object, knock_back(object,self.special_skill_animation.clock.repeat_time * 3, 40))
                                object.get_hit = True
                                object.get_damage = self.attack_damage
                                return
                self.special_skill_reset()

        elif self.special_skill_animation.clock.Return == 5:
            self.switcher2.reset()

        elif self.special_skill_animation.clock.Return == 8:
            if self.switcher2.operation():
                self.tmp = fake_object_class(self)
                self.gameplay.side4.append(self.tmp)
                tmp = (self.box.centerx - self.imgbox.centerx, self.box.centery - self.imgbox.centery)
                self.imgbox.centerx = self.target.imgbox.centerx - self.gameplay.box_size[0] / 3 * self.side
                self.box.center = (self.imgbox.centerx + tmp[0], self.imgbox.centery + tmp[1])

        elif self.special_skill_animation.clock.Return == 9:
            self.switcher2.reset()

        elif self.special_skill_animation.clock.Return == 10:
            if self.switcher2.operation():
                if self.target.alive == True:
                    add_effect(self.target, flying(self.target, 20))
                    self.target.get_hit = True
                    self.target.get_damage = self.attack_damage
                

        elif self.special_skill_animation.clock.Return == 11:
            self.switcher2.reset()

        elif self.special_skill_animation.clock.Return == 15:
            if self.switcher2.operation():
                tmp = (self.box.centerx - self.imgbox.centerx, self.box.centery - self.imgbox.centery)
                self.imgbox.centery -= 4.5 * self.gameplay.box_size[1]
                self.imgbox.centerx -= self.gameplay.box_size[0] * self.side
                self.box.center = (self.imgbox.centerx + tmp[0], self.imgbox.centery + tmp[1])
                self.kame = kame_class(self)

        elif self.special_skill_animation.clock.Return >= 24 and self.special_skill_animation.clock.Return < 33:
            self.kame.operation()

        elif self.special_skill_animation.clock.Return == 33 :
            self.kame.operation()
            self.switcher2.reset()

        elif self.special_skill_animation.clock.Return == 34 :
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
            for effect in self.effect_list:
                effect.play()
            if self.get_hit :
                self.Geting_hit()
            self.status_update()
            if self.health <= 0:
                self.die()
                return
            
            elif self.special_status:
                self.special_skill()
            elif self.status > 0:
                self.check = True
                if self.status == 3:
                    self.move()

                elif self.status == 1:
                    self.attack()

                elif self.status == 2 :
                    self.standstill()

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



    





