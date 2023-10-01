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
from character_properties import *

goku1 = analyzed_img("GameplayAssets\\goku\\goku(1).png ",139 , 90 , 110 , 226)
goku2 = analyzed_img("GameplayAssets\\goku\\goku(2).png ",139 , 90 , 110 , 226)
goku3 = analyzed_img("GameplayAssets\\goku\\goku(3).png ",139 , 90 , 110 , 226)
goku4 = analyzed_img("GameplayAssets\\goku\\goku(4).png ",139 , 90 , 110 , 226)
goku5 = analyzed_img("GameplayAssets\\goku\\goku(5).png ",102 , 137 , 201 , 136)
goku6 = analyzed_img("GameplayAssets\\goku\\goku(6).png ",102 , 137 , 201 , 136)
goku7 = analyzed_img("GameplayAssets\\goku\\goku(7).png ",102 , 137 , 201 , 136)
goku8 = analyzed_img("GameplayAssets\\goku\\goku(8).png ",102 , 137 , 201 , 136)
goku9 = analyzed_img("GameplayAssets\\goku\\goku(9).png ",135 , 166 , 99 , 151)
goku10 = analyzed_img("GameplayAssets\\goku\\goku(10).png", 179 , 131 , 97 , 175)
goku11 = analyzed_img("GameplayAssets\\goku\\goku(11).png", 161 , 126 , 85 , 198)
goku12 = analyzed_img("GameplayAssets\\goku\\goku(12).png", 161 , 126 , 85 , 198)
goku13 = analyzed_img("GameplayAssets\\goku\\goku(13).png", 161 , 126 , 85 , 198)
goku14 = analyzed_img("GameplayAssets\\goku\\goku(14).png", 161 , 126 , 85 , 198)
goku15 = analyzed_img("GameplayAssets\\goku\\goku(15).png", 208 , 137 , 116 , 203)
goku16 = analyzed_img("GameplayAssets\\goku\\goku(16).png", 224 , 120 , 130 , 211)
goku17 = analyzed_img("GameplayAssets\\goku\\goku(17).png", 224 , 120 , 130 , 211)
goku18 = analyzed_img("GameplayAssets\\goku\\goku(18).png", 224 , 120 , 130 , 211)
goku19 = analyzed_img("GameplayAssets\\goku\\goku(19).png", 224 , 120 , 130 , 211)
goku20 = analyzed_img("GameplayAssets\\goku\\goku(20).png", 224 , 120 , 130 , 211)
goku21 = analyzed_img("GameplayAssets\\goku\\goku(21).png", 224 , 120 , 130 , 211)
goku22 = analyzed_img("GameplayAssets\\goku\\goku(22).png", 224 , 120 , 130 , 211)
goku23 = analyzed_img("GameplayAssets\\goku\\goku(23).png", 224 , 120 , 130 , 211)
goku24 = analyzed_img("GameplayAssets\\goku\\goku(24).png", 224 , 120 , 130 , 211)
goku25 = analyzed_img("GameplayAssets\\goku\\goku(25).png", 224 , 120 , 130 , 211)
goku50 = analyzed_img("GameplayAssets\\goku\\goku(50).png", 224 , 120 , 130 , 211)
goku51 = analyzed_img("GameplayAssets\\goku\\goku(51).png", 224 , 120 , 130 , 211)
goku52 = analyzed_img("GameplayAssets\\goku\\goku(52).png", 224 , 120 , 130 , 211)
goku53 = analyzed_img("GameplayAssets\\goku\\goku(53).png", 224 , 120 , 130 , 211)
goku54 = analyzed_img("GameplayAssets\\goku\\goku(54).png" , 145 , 125 , 101 , 186 )
goku55 = analyzed_img("GameplayAssets\\goku\\goku(55).png" , 145 , 125 , 101 , 186 )
goku56 = analyzed_img("GameplayAssets\\goku\\goku(56).png" , 145 , 125 , 101 , 186 )
goku57 = analyzed_img("GameplayAssets\\goku\\goku(57).png" , 185 , 113 , 89 , 211 )
goku58 = analyzed_img("GameplayAssets\\goku\\goku(58).png" , 185 , 113 , 89 , 211 )
goku59 = analyzed_img("GameplayAssets\\goku\\goku(59).png" , 185 , 113 , 89 , 211 )

goku_to_kame = analyzed_img("GameplayAssets\\goku\\goku(23).png", 315 , 251 , 5 , 4)
goku_to_kame2 = analyzed_img("GameplayAssets\\goku\\goku(57).png",  353 , 177 , 6 , 4)
kame = pygame.image.load("GameplayAssets\\goku\\kame.png")

attack_damage = gk_attack_damage
health = gk_health
kame_dame = gk_kame_dame

class getting_hit_object():
    def __init__(self, object):
        self.object = object
        self.clock = timing_clock(0.1, object.gameplay)
        self.clock.start()

class kame_class():
    def __init__(self,goku, rotation, angle):
        self.goku = goku
        self.gameplay = self.goku.gameplay
        self.side = self.goku.side
        if self.side == 1:
            if rotation:
                self.start_point = goku_to_kame.imgbox_to_hitbox(goku.imgbox).topleft
            else:
                self.start_point = goku_to_kame2.imgbox_to_hitbox(goku.imgbox).topleft
            self.angle = angle
        elif self.side == -1:
            if rotation:
                self.start_point = goku_to_kame.reverse.imgbox_to_hitbox(goku.imgbox).topleft
            else:
                self.start_point = goku_to_kame2.reverse.imgbox_to_hitbox(goku.imgbox).topleft
            self.angle = 180 - angle
        self.size = (self.goku.box.width * 20 ,self.goku.box.width )
        self.width = self.size[1] / 2
        self.radius = self.size[0] / 2
        self.is_rotation = rotation

        self.status = True
        self.damage = kame_dame[self.goku.level - 1]
        self.damaged_list = []

        self.switch = N_time_switch(1)

    def resize(self):
        a = float(screen.screen.get_width()) / self.gameplay.screen[0]
        b = float(screen.screen.get_height()) /  self.gameplay.screen[1]
        tmp = pygame.Rect(self.imgbox.left * a, self.imgbox.top * b, self.imgbox.width * a, self.imgbox.height * b)
        copy(self.imgbox, tmp)
        self.operation()


    def display(self):
        if self.switch.operation():
            self.time_marker = self.goku.gameplay.curr_time + 0.3
        self.img = pygame.transform.smoothscale(kame, (self.size[0], self.width))
        tmp = pygame.transform.rotate(self.img, self.angle)
        Center = (self.start_point[0] + math.cos(self.angle * math.pi/ 180) * self.radius, self.start_point[1] - math.sin(self.angle * math.pi / 180) * self.radius)
        tmp2 = tmp.get_rect(center = Center)
        screen.screen.blit(tmp, tmp2)
        if self.is_rotation:
            self.angle += 25 * (self.goku.gameplay.curr_time - self.goku.gameplay.pre_curr_time) * self.side
        if  self.goku.gameplay.curr_time <= self.time_marker:
            self.width = self.size[1] / 5
        else:
            if self.width < self.size[1] * 2:
                self.width += (self.goku.gameplay.curr_time - self.goku.gameplay.pre_curr_time) * self.size[1] * 3



    def collide_check(self):
        for enemy_object in self.gameplay.side( - self.side):
            if collide_check_special(self, enemy_object):
                if not list_find_special(self.damaged_list, enemy_object):
                    self.damaged_list.append(getting_hit_object(enemy_object))
                    enemy_object.health -= self.damage


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
            self.level = self.gameplay.character_level1[4]
        elif side == 2:
            self.side = -1
            self.level = self.gameplay.character_level2[4]

        self.speed = 5.0 # 5/100 map per second 
        self.attack_scope = 1 * self.gameplay.box_size[0] # 4/15 map width
        self.attack_scope_orginal = self.attack_scope
        self.attack_speed = 1/2 # arrow(s) pers second
        self.attack_speed_orginal = self.attack_speed
        self.attack_damage = attack_damage[self.level - 1]
        self.attack_damage_orginal = self.attack_damage
        self.health_max = health[self.level - 1]
        self.health = self.health_max
        self.mana_max = 100.0
        self.mana = 90.0

        self.effect_list = []

        self.alive = True
        self.get_hit = False
        self.ischeck = True
        self.iscollide_check = True
        self.collide = None
        self.special_status = False

        self.moving_animation = animation_player([goku5,goku6,goku7,goku8],self.side, 0.5, self.imgbox , self.gameplay)
        self.walking_animation = animation_player([goku1, goku2, goku3, goku4], self.side, 1, self.imgbox, self.gameplay)
        self.attacking_animation = one_time_animation_player([goku9,goku9,goku9,goku10,goku11,goku12,goku13,goku14],self.side, 0.5 , self.imgbox, self.gameplay)
        self.standstill_animation = one_time_animation_player([goku1, goku2, goku3, goku4], self.side, 1, self.imgbox, self.gameplay)
        self.special_skill_animation1 = one_time_animation_player([goku9,goku10,goku11,goku12,goku13,goku14,goku54, goku55, goku56, goku57,goku57, goku57, goku57, goku57, goku57, goku57, goku57, goku57, goku57, goku57, goku57, goku57, goku57, goku57,goku58, goku59], self.side, 1.75, self.imgbox, self.gameplay)
        self.special_skill_animation2 = one_time_animation_player([goku9,goku10,goku11,goku12,goku13,goku14,goku15,goku18,goku16,goku16,goku16,goku17,goku17,goku17,goku18,goku19,goku20,goku21,goku21,goku21,goku22,goku22,goku22,goku23,goku23,goku23,goku24,goku24,goku24,goku25,goku25,goku25,goku25,goku25,goku18,goku18], self.side, 2.25, self.imgbox, self.gameplay)
        self.special_skill_animation3 = one_time_animation_player([goku9,goku10,goku11,goku12,goku13,goku14,goku54, goku55, goku56, goku57,goku57, goku57, goku57, goku57, goku57, goku57, goku57, goku57, goku57, goku57, goku57, goku57, goku57, goku57,goku58, goku59,goku15,goku18,goku16,goku16,goku16,goku17,goku17,goku17,goku18,goku19,goku20,goku21,goku21,goku21,goku22,goku22,goku22,goku23, goku23, goku23, goku23, goku23, goku23, goku24, goku24, goku24, goku24, goku24, goku24, goku25, goku25, goku25, goku25, goku25, goku25,goku18,goku18], self.side, 5.0 , self.imgbox, self.gameplay)
        
        self.dying_animation = one_time_animation_player([goku51], self.side, 0.8, self.imgbox, self.gameplay)
        self.knock_back_animation = animation_player([goku53], self.side, 1, self.imgbox, self.gameplay)
        self.flying_animation = animation_player([goku52], self.side, 1, self.imgbox, self.gameplay)
        self.falling_animation = animation_player([goku50], self.side, 1, self.imgbox, self.gameplay)


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
        if not self.special_status:
            if not self.level == self.gameplay.character_level(self.side, 4):
                self.level = self.gameplay.character_level(self.side, 4)
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
            self.mana = 0
            self.special_status = True
            if self.level == 1: 
                self.special_skill_animation = self.special_skill_animation1
            elif self.level == 2 :
                self.special_skill_animation = self.special_skill_animation2
            elif self.level == 3:
                self.special_skill_animation = self.special_skill_animation3
            add_effect(self, iron_body(self, self.special_skill_animation.loop_time + 1 / self.attack_speed))


        if self.ischeck :

            flag = False
            if self.collide == 2:
                self.status = 1
                flag = True

            elif self.collide == 1:
                ispass = False
                for object in self.gameplay.side(- self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 3 + (self.box.width + object.box.width) / 2 :
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
                    if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 3 + (self.box.width + object.box.width) / 2:
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
        if self.attacking_animation.clock.Return == 6:
            if self.switcher1.operation():
                for object in self.gameplay.side(- self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                if not self.special_status :
                                    self.mana += 10 
                                object.get_hit = True
                                object.get_damage = self.attack_damage
        elif self.attacking_animation.clock.Return == 5 :
            self.switcher1.reset()


    def attack_reset(self):
        self.attacking_animation.reset() 
        self.switcher5.reset()

    def special_skill(self):
        if self.switcher3.operation():
            self.attack_coundowner.reset()
            self.attack_coundowner.start()
        
        if self.level == 1:
            self.animation_player = self.special_skill_animation
            if self.special_skill_animation.clock.Return == 3: 
                self.switcher2.reset()
            elif self.special_skill_animation.clock.Return == 4:
                if self.switcher2.operation():
                    for object in self.gameplay.side(- self.side) :
                        if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope *1.5 + (self.box.width + object.box.width) / 2 :
                            if (object.box.centerx - self.box.centerx) * self.side >= 0:
                                if same_line_checker(self, object):
                                    if not object.__class__ == self.gameplay.nexusclass:
                                        self.target = object
                                        add_effect(object, knock_back(object,self.special_skill_animation.clock.repeat_time * 3, 40))
                                        object.get_hit = True
                                        object.get_damage = self.attack_damage
                                        return
                    self.target = None
            
            elif self.special_skill_animation.clock.Return == 9:
                self.switcher2.reset()

            elif self.special_skill_animation.clock.Return == 10:
                if self.switcher2.operation():
                    self.kame = kame_class(self, False, 0)
            elif self.special_skill_animation.clock.Return > 10 :
                self.kame.operation()



        elif self.level == 2:
            self.animation_player = self.special_skill_animation
            if self.special_skill_animation.clock.Return == 3:
                self.switcher2.reset()
            elif self.special_skill_animation.clock.Return == 4:
                if self.switcher2.operation():
                    for object in self.gameplay.side(- self.side) :
                        if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope *1.5 + (self.box.width + object.box.width) / 2 :
                            if (object.box.centerx - self.box.centerx) * self.side >= 0:
                                if same_line_checker(self, object):
                                    if not object.__class__ == self.gameplay.nexusclass:
                                        self.target = object
                                        add_effect(object, knock_back(object,self.special_skill_animation.clock.repeat_time * 3, 40))
                                        object.get_hit = True
                                        object.get_damage = self.attack_damage
                                        return
                    self.target = None

            elif self.special_skill_animation.clock.Return == 5:
                self.switcher2.reset()

            elif self.special_skill_animation.clock.Return == 8:
                if self.switcher2.operation():
                    tmp = (self.box.centerx - self.imgbox.centerx, self.box.centery - self.imgbox.centery)
                    if self.target == None:
                        if self.box.right + 10 * self.gameplay.box_size[0] < self.gameplay.nexus2.box.left and self.box.left > self.gameplay.nexus1.box.right + 10 * self.gameplay.box_size[0]:   
                            self.imgbox.centerx += 10 * self.gameplay.box_size[0] *  self.side
                            self.box.center = (self.imgbox.centerx + tmp[0], self.imgbox.centery + tmp[1])
                        else:
                            self.imgbox.center  = self.gameplay.side(- self.side)[0].box.center
                            self.imgbox.centerx -= (self.gameplay.side(- self.side)[0].box.width  / 2 + self.attack_scope * 1.5) * self.side
                            self.box.center = (self.imgbox.centerx + tmp[0], self.imgbox.centery + tmp[1])
                    else:  
                        if self.target.alive == False:
                            if self.box.right + 10 * self.gameplay.box_size[0] < self.gameplay.nexus2.box.left and self.box.left > self.gameplay.nexus1.box.right + 10 * self.gameplay.box_size[0]:   
                                self.imgbox.centerx += 10 * self.gameplay.box_size[0] *  self.side
                                self.box.center = (self.imgbox.centerx + tmp[0], self.imgbox.centery + tmp[1])
                            else:
                                self.imgbox.center  = self.gameplay.side(- self.side)[0].box.center
                                self.imgbox.centerx -= (self.gameplay.side(- self.side)[0].box.width  / 2 + self.attack_scope * 1.5) * self.side
                                self.box.center = (self.imgbox.centerx + tmp[0], self.imgbox.centery + tmp[1])
                        else:
                            self.box.centerx = self.target.box.centerx - self.gameplay.box_size[0] / 3 * self.side
                            self.imgbox.center = (self.box.centerx - tmp[0], self.box.centery - tmp[1])

            elif self.special_skill_animation.clock.Return == 9:
                self.switcher2.reset()

            elif self.special_skill_animation.clock.Return == 10:
                if self.switcher2.operation():
                    if self.target == None:
                        for object in self.gameplay.side(- self.side) :
                            if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope *1.5 + (self.box.width + object.box.width) / 2 :
                                if (object.box.centerx - self.box.centerx) * self.side >= 0:
                                    if same_line_checker(self, object):
                                        if not object.__class__ == self.gameplay.nexusclass:
                                            self.target = object
                                            add_effect(self.target, flying(self.target, 20))
                                            self.target.get_hit = True
                                            self.target.get_damage = self.attack_damage
                                            return
                    else:
                        if self.target.alive == False:
                            for object in self.gameplay.side(- self.side) :
                                if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope *1.5 + (self.box.width + object.box.width) / 2 :
                                    if (object.box.centerx - self.box.centerx) * self.side >= 0:
                                        if same_line_checker(self, object):
                                            if not object.__class__ == self.gameplay.nexusclass:
                                                self.target = object
                                                add_effect(self.target, flying(self.target, 20))
                                                self.target.get_hit = True
                                                self.target.get_damage = self.attack_damage
                                                return
                        else:
                            add_effect(self.target, flying(self.target, 20))
                            self.target.get_hit = True
                            self.target.get_damage = self.attack_damage
                    

            elif self.special_skill_animation.clock.Return == 11:
                self.switcher2.reset()

            elif self.special_skill_animation.clock.Return == 15:
                if self.switcher2.operation():
                    tmp = (self.box.centerx - self.imgbox.centerx, self.box.centery - self.imgbox.centery)
                    self.imgbox.centery -= 4.5 * self.gameplay.box_size[1]
                    self.imgbox.centerx -=  5.0 * self.gameplay.box_size[0] * self.side
                    self.box.center = (self.imgbox.centerx + tmp[0], self.imgbox.centery + tmp[1])
                    self.kame = kame_class(self, True, -45)

            elif self.special_skill_animation.clock.Return >= 24 and self.special_skill_animation.clock.Return < 33:
                self.kame.operation()

            elif self.special_skill_animation.clock.Return == 33 :
                self.kame.operation()
                self.switcher2.reset()

            elif self.special_skill_animation.clock.Return == 34 :
                if self.switcher2.operation():
                    index = self.index
                    while True:
                        if(( self.side == 1) and (index + 2 <= self.gameplay.side1_heros)) or (( self.side == -1) and (index + 2 <= self.gameplay.side2_heros)):
                            if not self.gameplay.side(self.side)[index + 1] ==  None:
                                object = self.gameplay.side(self.side)[index + 1]
                                Rect = pygame.Rect(0,0, self.gameplay.box_size[0], self.gameplay.box_size[1])
                                Rect.center = (object.box.centerx + (self.gameplay.box_size[0] / 2) * self.side ,  self.gameplay.path_height - self.gameplay.box_size[1] / 2)
                                get_spawn_display(self, Rect)
                                break

                            else:
                                index += 1
                        else:
                                object = self.gameplay.side(self.side)[0]
                                Rect = pygame.Rect(0,0, self.gameplay.box_size[0], self.gameplay.box_size[1])
                                Rect.center = (object.box.centerx + (self.gameplay.box_size[0] / 2) * self.side ,  self.gameplay.path_height - self.gameplay.box_size[1] / 2)
                                get_spawn_display(self, Rect)
                                break
                            
        
        elif self.level == 3:    
            self.animation_player = self.special_skill_animation
            if self.special_skill_animation.clock.Return == 3: 
                self.switcher2.reset()
            elif self.special_skill_animation.clock.Return == 4:
                if self.switcher2.operation():
                    for object in self.gameplay.side(- self.side) :
                        if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope *1.5 + (self.box.width + object.box.width) / 2 :
                            if (object.box.centerx - self.box.centerx) * self.side >= 0:
                                if same_line_checker(self, object):
                                    if not object.__class__ == self.gameplay.nexusclass:
                                        self.target = object
                                        add_effect(object, knock_back(object,self.special_skill_animation.clock.repeat_time * 3, 40))
                                        object.get_hit = True
                                        object.get_damage = self.attack_damage
                                        return
                    self.target = None
            
            elif self.special_skill_animation.clock.Return == 9:
                self.switcher2.reset()

            elif self.special_skill_animation.clock.Return == 10:
                if self.switcher2.operation():
                    self.kame = kame_class(self, False, 0)
            elif self.special_skill_animation.clock.Return > 10  and self.special_skill_animation.clock.Return <  25:
                self.kame.operation()            

            elif self.special_skill_animation.clock.Return == 28:
                self.switcher2.reset()

            elif self.special_skill_animation.clock.Return == 29:
                if self.switcher2.operation():
                    tmp = (self.box.centerx - self.imgbox.centerx, self.box.centery - self.imgbox.centery)
                    if self.target == None:
                        if self.box.right + 10 * self.gameplay.box_size[0] < self.gameplay.nexus2.box.left and self.box.left > self.gameplay.nexus1.box.right + 10 * self.gameplay.box_size[0]:   
                            self.imgbox.centerx += 10 * self.gameplay.box_size[0] *  self.side
                            self.box.center = (self.imgbox.centerx + tmp[0], self.imgbox.centery + tmp[1])
                        else:
                            self.imgbox.center  = self.gameplay.side(- self.side)[0].box.center
                            self.imgbox.centerx -= (self.gameplay.side(- self.side)[0].box.width  / 2 + self.attack_scope * 1.5) * self.side
                            self.box.center = (self.imgbox.centerx + tmp[0], self.imgbox.centery + tmp[1])
                    else:  
                        if self.target.alive == False:
                            if self.box.right + 10 * self.gameplay.box_size[0] < self.gameplay.nexus2.box.left and self.box.left > self.gameplay.nexus1.box.right + 10 * self.gameplay.box_size[0]:   
                                self.imgbox.centerx += 10 * self.gameplay.box_size[0] *  self.side
                                self.box.center = (self.imgbox.centerx + tmp[0], self.imgbox.centery + tmp[1])
                            else:
                                self.imgbox.center  = self.gameplay.side(- self.side)[0].box.center
                                self.imgbox.centerx -= (self.gameplay.side(- self.side)[0].box.width  / 2 + self.attack_scope * 1.5) * self.side
                                self.box.center = (self.imgbox.centerx + tmp[0], self.imgbox.centery + tmp[1])
                        else:
                            self.box.centerx = self.target.box.centerx - self.gameplay.box_size[0] / 3 * self.side
                            self.imgbox.center = (self.box.centerx - tmp[0], self.box.centery - tmp[1])

            elif self.special_skill_animation.clock.Return == 30:
                self.switcher2.reset()

            elif self.special_skill_animation.clock.Return == 31:
                if self.switcher2.operation():
                    if self.target == None:
                        for object in self.gameplay.side(- self.side) :
                            if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope *1.5 + (self.box.width + object.box.width) / 2 :
                                if (object.box.centerx - self.box.centerx) * self.side >= 0:
                                    if same_line_checker(self, object):
                                        if not object.__class__ == self.gameplay.nexusclass:
                                            self.target = object
                                            add_effect(self.target, flying(self.target, 20))
                                            self.target.get_hit = True
                                            self.target.get_damage = self.attack_damage
                                            return
                    else:
                        if self.target.alive == False:
                            for object in self.gameplay.side(- self.side) :
                                if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope *1.5 + (self.box.width + object.box.width) / 2 :
                                    if (object.box.centerx - self.box.centerx) * self.side >= 0:
                                        if same_line_checker(self, object):
                                            if not object.__class__ == self.gameplay.nexusclass:
                                                self.target = object
                                                add_effect(self.target, flying(self.target, 20))
                                                self.target.get_hit = True
                                                self.target.get_damage = self.attack_damage
                                                return
                        else:
                            add_effect(self.target, flying(self.target, 20))
                            self.target.get_hit = True
                            self.target.get_damage = self.attack_damage
                    

            elif self.special_skill_animation.clock.Return == 32:
                self.switcher2.reset()

            elif self.special_skill_animation.clock.Return == 36:
                if self.switcher2.operation():
                    tmp = (self.box.centerx - self.imgbox.centerx, self.box.centery - self.imgbox.centery)
                    self.imgbox.centery -= 4.5 * self.gameplay.box_size[1]
                    self.imgbox.centerx -=  5.0 * self.gameplay.box_size[0] * self.side
                    self.box.center = (self.imgbox.centerx + tmp[0], self.imgbox.centery + tmp[1])
                    self.kame = kame_class(self, True, -45)

            elif self.special_skill_animation.clock.Return >= 44 and self.special_skill_animation.clock.Return < 61:
                self.kame.operation()

            elif self.special_skill_animation.clock.Return == 61 :
                self.kame.operation()
                self.switcher2.reset()

            elif self.special_skill_animation.clock.Return == 62 :
                if self.switcher2.operation():
                    index = self.index
                    while True:
                        if(( self.side == 1) and (index + 2 <= self.gameplay.side1_heros)) or (( self.side == -1) and (index + 2 <= self.gameplay.side2_heros)):
                            if not self.gameplay.side(self.side)[index + 1] ==  None:
                                object = self.gameplay.side(self.side)[index + 1]
                                Rect = pygame.Rect(0,0, self.gameplay.box_size[0], self.gameplay.box_size[1])
                                Rect.center = (object.box.centerx + (self.gameplay.box_size[0] / 2) * self.side ,  self.gameplay.path_height - self.gameplay.box_size[1] / 2)
                                get_spawn_display(self, Rect)
                                break

                            else:
                                index += 1
                        else:
                                object = self.gameplay.side(self.side)[0]
                                Rect = pygame.Rect(0,0, self.gameplay.box_size[0], self.gameplay.box_size[1])
                                Rect.center = (object.box.centerx + (self.gameplay.box_size[0] / 2) * self.side ,  self.gameplay.path_height - self.gameplay.box_size[1] / 2)
                                get_spawn_display(self, Rect)
                                break



    def special_skill_reset(self):
        self.switcher3.reset()
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

            elif self.status == 4:
                self.special_skill()

            if self.get_hit :
                self.Geting_hit()

            if self.health <= 0:
                self.alive = False
                if self.side == 1:
                    self.gameplay.gold_income_1 += self.gameplay.character_cost[self.__class__][self.level - 1] * 10.0 / 100
                else:
                    self.gameplay.gold_income_2 += self.gameplay.character_cost[self.__class__][self.level - 1] * 10.0 / 100

            self.display()
            self.status_update()

            # pygame.draw.rect(screen.screen,White,self.box,1)
            # pygame.draw.rect(screen.screen,White,self.imgbox,1)
        else:
            self.dying()
   



    






