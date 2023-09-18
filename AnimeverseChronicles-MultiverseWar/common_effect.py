from typing import Any
import pygame 
from pygame.locals import *
from clock import *
from img_analyze import *
from animation_player import *
from object_function import *
from list_function import *
from collide_checker import *

healling_effect1 = analyzed_img("GameplayAssets\\effect\\healling_effect(1).png" , 31 , 33 , 202 , 222 )
healling_effect2 = analyzed_img("GameplayAssets\\effect\\healling_effect(2).png" , 31 , 33 , 202 , 222 )
healling_effect3 = analyzed_img("GameplayAssets\\effect\\healling_effect(3).png" , 31 , 33 , 202 , 222 )
healling_effect4 = analyzed_img("GameplayAssets\\effect\\healling_effect(4).png" , 31 , 33 , 202 , 222 )

shield_animation1 = analyzed_img("GameplayAssets\\effect\\shield_animation(1).png" , 151 , 267 , 311 , 150 )
shield_animation2 = analyzed_img("GameplayAssets\\effect\\shield_animation(2).png" , 151 , 267 , 311 , 150 )
shield_animation3 = analyzed_img("GameplayAssets\\effect\\shield_animation(3).png" , 151 , 267 , 311 , 150 )
shield_animation4 = analyzed_img("GameplayAssets\\effect\\shield_animation(4).png" , 151 , 267 , 311 , 150 )
shield_animation5 = analyzed_img("GameplayAssets\\effect\\shield_animation(5).png" , 151 , 267 , 311 , 150 )
shield_animation6 = analyzed_img("GameplayAssets\\effect\\shield_animation(6).png" , 151 , 267 , 311 , 150 )
shield_animation7 = analyzed_img("GameplayAssets\\effect\\shield_animation(7).png" , 151 , 267 , 311 , 150 )

dizzy_effect1 = analyzed_img("GameplayAssets\\effect\\dizzy_effect(1).png", 27 , 58 , 522 , 290)
dizzy_effect2 = analyzed_img("GameplayAssets\\effect\\dizzy_effect(2).png", 27 , 58 , 522 , 290)
dizzy_effect3 = analyzed_img("GameplayAssets\\effect\\dizzy_effect(3).png", 27 , 58 , 522 , 290)
dizzy_effect4 = analyzed_img("GameplayAssets\\effect\\dizzy_effect(4).png", 27 , 58 , 522 , 290)
dizzy_effect5 = analyzed_img("GameplayAssets\\effect\\dizzy_effect(5).png", 27 , 58 , 522 , 290)
dizzy_effect6 = analyzed_img("GameplayAssets\\effect\\dizzy_effect(6).png", 27 , 58 , 522 , 290)
dizzy_effect7 = analyzed_img("GameplayAssets\\effect\\dizzy_effect(7).png", 27 , 58 , 522 , 290)
dizzy_effect8 = analyzed_img("GameplayAssets\\effect\\dizzy_effect(8).png", 27 , 58 , 522 , 290)
dizzy_effect9 = analyzed_img("GameplayAssets\\effect\\dizzy_effect(9).png", 27 , 58 , 522 , 290)

knock_back1 = analyzed_img("GameplayAssets\\effect\knock_back(1).png", 283 , 198 , 143 , 84)
knock_back2 = analyzed_img("GameplayAssets\\effect\knock_back(2).png", 287 , 180 , 195 , 101)
knock_back3 = analyzed_img("GameplayAssets\\effect\knock_back(3).png", 291 , 160 , 189 , 120)
knock_back4 = analyzed_img("GameplayAssets\\effect\knock_back(4).png", 291 , 160 , 189 , 120)
knock_back5 = analyzed_img("GameplayAssets\\effect\knock_back(5).png", 291 , 160 , 189 , 120)
knock_back6 = analyzed_img("GameplayAssets\\effect\knock_back(6).png", 378 , 147 , 83 , 115)

flying1 = analyzed_img("GameplayAssets\\effect\\flying(1).png",  199 , 259 , 270 , 105)
flying2 = analyzed_img("GameplayAssets\\effect\\flying(2).png",  199 , 259 , 270 , 105)
flying3 = analyzed_img("GameplayAssets\\effect\\flying(3).png",  199 , 259 , 270 , 105)
flying4 = analyzed_img("GameplayAssets\\effect\\flying(4).png",  199 , 259 , 270 , 105)
flying5 = analyzed_img("GameplayAssets\\effect\\flying(5).png",  199 , 259 , 270 , 105)
flying6 = analyzed_img("GameplayAssets\\effect\\flying(6).png",  199 , 259 , 270 , 105)
flying7 = analyzed_img("GameplayAssets\\effect\\flying(7).png",  199 , 259 , 270 , 105)
flying8 = analyzed_img("GameplayAssets\\effect\\flying(8).png",  199 , 259 , 270 , 105)

soul1 = analyzed_img("GameplayAssets\\effect\\soul(1).png", 241 , 109 , 221 , 201)
soul2 = analyzed_img("GameplayAssets\\effect\\soul(2).png", 241 , 109 , 221 , 201)
soul3 = analyzed_img("GameplayAssets\\effect\\soul(3).png", 241 , 109 , 221 , 201)
soul4 = analyzed_img("GameplayAssets\\effect\\soul(4).png", 241 , 109 , 221 , 201)
soul5 = analyzed_img("GameplayAssets\\effect\\soul(5).png", 241 , 109 , 221 , 201)
soul6 = analyzed_img("GameplayAssets\\effect\\soul(6).png", 241 , 109 , 221 , 201)
soul7 = analyzed_img("GameplayAssets\\effect\\soul(7).png", 241 , 109 , 221 , 201)
soul8 = analyzed_img("GameplayAssets\\effect\\soul(8).png", 241 , 109 , 221 , 201)


class dizzy():
    def __init__(self, object, lasted_time):
        self.object = object
        self.animation = animation_player_special([dizzy_effect1,dizzy_effect2,dizzy_effect3,dizzy_effect4,dizzy_effect5,dizzy_effect6,dizzy_effect7,dizzy_effect8,dizzy_effect9], object.side ,1, self.object.box, (0, -1/4, 1,  1/2), object.gameplay)
        self.clock = timing_clock(lasted_time ,object.gameplay)
        self.type = -1

    def play(self):
        self.clock.start()
        if self.clock.Return == True:
            self.animation.play()
            self.object.status = 2
            self.object.ischeck = False
            if self.object.special_status:
                self.object.special_skill_reset()
                self.object.special_status = False

        else:
            self.remove()

    def remove(self):
        self.clock.remove()
        remove(self)


class soul_sucking():
    def __init__(self, object):
        self.imgbox = object.box
        if object.side == 1:
            self.animation = one_time_animation_player_special([soul1, soul2, soul3, soul4, soul5, soul6, soul6, soul6, soul7, soul8], - object.side, 1, object.box, ( 3 / 4, -1 / 2, 1, 1), object.gameplay)
        else:
            self.animation = one_time_animation_player_special([soul1, soul2, soul3, soul4, soul5, soul6, soul6, soul6, soul7, soul8], - object.side, 1, object.box, ( - 3 / 4, -1 / 2, 1, 1), object.gameplay)
        self.clock = timing_clock(1 ,object.gameplay)
        self.object = object
        self.switch = N_time_switch(1)
        self.type = -1


    def play(self):
        self.clock.start()
        if self.switch.operation():
            self.object.get_hit = True
            self.object.get_damage = self.object.health * 20 / 100
        if self.clock.Return == True:
            self.animation.play()
        else:
            self.remove()

    def remove(self):
        self.clock.remove()
        self.object.effect_list.remove(self)



class knock_back():
    def __init__(self, object, lasting_time, knock_back_speed):
        self.object = object
        self.box = pygame.Rect(object.box.left,object.box.top,object.box.width,object.box.height)        
        if object.side == 1:
            self.animation = one_time_animation_player_special([knock_back1,knock_back2,knock_back3,knock_back4,knock_back5,knock_back6], object.side, 0.5, self.box, (1 + object.gameplay.box_size[0] / (self.box.width), 1 - object.gameplay.box_size[1] / (self.box.height)  , object.gameplay.box_size[0] / (self.box.width) , object.gameplay.box_size[1] / (self.box.height)), object.gameplay)
        elif object.side == -1:
            self.animation = one_time_animation_player_special([knock_back1,knock_back2,knock_back3,knock_back4,knock_back5,knock_back6], object.side, 0.5, self.box, (- object.gameplay.box_size[0] / (self.box.width), 1 - object.gameplay.box_size[1] / (self.box.height)  , object.gameplay.box_size[0] / (self.box.width) , object.gameplay.box_size[1] / (self.box.height)), object.gameplay)
        self.clock = timing_clock(lasting_time, object.gameplay)
        self.speed = knock_back_speed
        self.type = -1
    
    def play(self):
        self.animation.play()
        self.clock.start()
        if self.clock.Return :
            self.object.animation_player = self.object.knock_back_animation
            self.object.ischeck = False
            if self.object.special_status:
                self.object.special_skill_reset()
                self.object.special_status = False     
            self.object.status = -1
            if self.object.box.right < self.object.gameplay.nexus2.box.left and self.object.box.left > self.object.gameplay.nexus1.box.right:
                self.object.imgbox.centerx -= (self.speed * screen.screen.get_rect().width / 100) * (self.object.gameplay.curr_time - self.object.gameplay.pre_curr_time)  * self.object.side
            for object in self.object.gameplay.side(self.object.side):
                if collide_checker(self.object,object):
                    if (not (object == self.object)) :
                        ispass = False
                        for effect in object.effect_list:
                            if effect.__class__ == knock_back:
                                ispass = True
                                break
                        if not ispass:
                            add_effect(object, knock_back(object, self.clock.counter - self.clock.gameplay.curr_time, self.speed))
            
        elif self.animation.status == False:
            self.remove()

    def remove(self):
        self.clock.remove()
        remove(self)


acceleration_original = 20.0

class flying():
    def __init__(self, object, flying_speed):
        self.object = object
        self.box = pygame.Rect(object.box.left,object.box.top,object.box.width,object.box.height)        
        if object.side == 1:
            self.animation = one_time_animation_player_special([flying1,flying2,flying3,flying4,flying5,flying6,flying7,flying8], object.side, 0.7, self.box, (1/2 - object.gameplay.box_size[0] * 3 / (self.box.width * 2), 1 - object.gameplay.box_size[1] / (self.box.height * 2)  , object.gameplay.box_size[0] * 3 / (self.box.width) , object.gameplay.box_size[1] / (self.box.height * 2)), object.gameplay)
        elif object.side == -1:
            self.animation = one_time_animation_player_special([flying1,flying2,flying3,flying4,flying5,flying6,flying7,flying8], object.side, 0.7, self.box, (1/2 - object.gameplay.box_size[0] * 3 / (self.box.width * 2), 1 - object.gameplay.box_size[1] / (self.box.height * 2)  , object.gameplay.box_size[0] * 3 / (self.box.width) , object.gameplay.box_size[1] / (self.box.height * 2)), object.gameplay)
        self.speed = flying_speed
        self.type = -1


    def play(self):
        self.animation.play()
        self.object.animation_player = self.object.flying_animation
        self.object.ischeck = False
        if self.object.special_status:
            self.object.special_skill_reset()
            self.object.special_status = False
        self.object.status = -2
        self.speed -= acceleration_original * (self.object.gameplay.curr_time - self.object.gameplay.pre_curr_time) 
        self.object.imgbox.centery -= (self.speed* screen.screen.get_rect().width / 100) * (self.object.gameplay.curr_time - self.object.gameplay.pre_curr_time)  
        if self.speed <= 0:
            self.remove()
            ispass = False
            for effect in self.object.effect_list:
                if effect.__class__ == flying or effect.__class__ == falling:
                    ispass = True
                    break
            if not ispass:
                add_effect(self.object, falling(self.object))

    def remove(self):
        remove(self)


class falling():
    def __init__(self, object):
        self.object = object
        self.box = pygame.Rect(object.box.left,object.box.top,object.box.width,object.box.height)        
        self.speed = 0
        self.type = -1


    def play(self):
        self.object.animation_player = self.object.falling_animation
        self.object.ischeck = False
        if self.object.special_status:
            self.object.special_skill_reset()
            self.object.special_status = False
        self.object.status = -3
        self.speed += acceleration_original * (self.object.gameplay.curr_time - self.object.gameplay.pre_curr_time) 
        self.object.imgbox.centery += (self.speed* screen.screen.get_rect().width / 100) * (self.object.gameplay.curr_time - self.object.gameplay.pre_curr_time)  
        if self.object.box.bottom >= self.object.gameplay.path_height :
            self.remove()


    def remove(self):
        tmp = get_spawn_imgbox(self.object, pygame.Rect( 0, self.object.gameplay.path_height - self.object.gameplay.box_size[1], self.object.gameplay.box_size[0], self.object.gameplay.box_size[1]))
        self.object.box.centery += tmp.centery - self.object.imgbox.centery
        self.object.imgbox.centery += tmp.centery - self.object.imgbox.centery
        remove(self)

class shield():
    def __init__(self, object, lasted_time, damage_reduce_percent):
        self.object = object
        self.animation = animation_player_special([shield_animation1,shield_animation2,shield_animation3,shield_animation4,shield_animation5,shield_animation6,shield_animation7], object.side ,0.6, self.object.box, ( - 1 , 1/4, 3,  1/2), object.gameplay)
        self.clock = timing_clock(lasted_time ,object.gameplay)
        self.reduce = damage_reduce_percent
        self.type = 1

    def play(self):
        self.clock.start()
        if self.clock.Return == True:
            self.animation.play()
            self.object.damage_reduce = self.reduce
        else:
            self.remove()

    def remove(self):
        self.clock.remove()
        remove(self)

class heal():
    def __init__(self, object, health):
        self.object = object
        self.animation = one_time_animation_player_special([healling_effect1, healling_effect2, healling_effect3, healling_effect4], object.side , 0.8, self.object.box, ( - 1 / 2 , 0, 2,  1), object.gameplay)
        self.heal = health
        self.type = 1
        self.switcher = N_time_switch(1)

    def play(self):
        self.animation.play()
        if self.switcher.operation():
            self.object.health += self.heal
            if self.object.health > self.object.health_max:
                self.object.health -= self.heal
                
        if self.animation.status == False:
            self.remove()

    def remove(self):
        remove(self)

class iron_body():
    def __init__(self, object, lasted_time):
        self.object = object
        self.clock = timing_clock(lasted_time ,object.gameplay)
        self.type = 1
        self.play()

    def play(self):
        self.clock.start()
        if self.clock.Return == True:
            def remove(effect):
                if effect.type < 0: 
                    effect.remove()
            list_browser(self.object.effect_list, remove)
                    
        else:
            self.remove()

    def remove(self):
        self.clock.remove()
        self.object.effect_list.remove(self)
        

def add_effect(object, effect):
    object.effect_list.append(effect)




def remove(effect):
    effect.object.effect_list.remove(effect)
    if effect.object.pre_status < 0 :
        effect.object.ischeck = True
        effect.object.check_forward()    
