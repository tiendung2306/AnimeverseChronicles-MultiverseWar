from typing import Any
import pygame 
from pygame.locals import *
from clock import *
from img_analyze import *
from animation_player import *
from fake_object import *

class dizzy():
    def __init__(self, object, lasted_time):
        self.object = object
        self.animation = animation_player_special([dizzy_effect1,dizzy_effect2,dizzy_effect3,dizzy_effect4,dizzy_effect5,dizzy_effect6,dizzy_effect7,dizzy_effect8,dizzy_effect9], object.side ,1, self.object.box, (0, -1/4, 1,  1/2), object.gameplay)
        self.clock = timing_clock(lasted_time ,object.gameplay)

    def play(self):
        self.clock.start()
        if self.clock.Return == True:
            self.animation.play()
            self.object.status = 2
        else:
            self.remove()

    def remove(self):
        self.clock.remove()
        self.object.effect_list.remove(self)

class soul_sucking():
    def __init__(self, object):
        self.imgbox = object.box
        if object.side == 1:
            self.animation = one_time_animation_player_special([soul1, soul2, soul3, soul4, soul5, soul6, soul6, soul6, soul7, soul8], - object.side, 1, object.box, ( 3 / 4, -1 / 2, 1, 1), object.gameplay)
        else:
            self.animation = one_time_animation_player_special([soul1, soul2, soul3, soul4, soul5, soul6, soul6, soul6, soul7, soul8], - object.side, 1, object.box, ( - 3 / 4, -1 / 2, 1, 1), object.gameplay)
        self.clock = timing_clock(1 ,object.gameplay)
        self.object = object
    
    def play(self):
        self.clock.start()
        if self.clock.Return == True:
            self.animation.play()
        else:
            self.remove()

    def remove(self):
        self.clock.remove()
        self.object.effect_list.remove(self)


class knock_back():
    def __init__(self, object, level):
        self.object = object
        self.box = pygame.Rect(object.box.left,object.box.top,object.box.width,object.box.height)        
        if object.side == 1:
            self.animation = one_time_animation_player_special([knock_back1,knock_back2,knock_back3,knock_back4,knock_back5,knock_back6], object.side, 0.7, self.box, (1, 0, 3, 1), object.gameplay)
        elif object.side == -1:
            self.animation = one_time_animation_player_special([knock_back1,knock_back2,knock_back3,knock_back4,knock_back5,knock_back6], object.side, 0.7, self.box, (-1, 0, 3, 1), object.gameplay)
        self.clock = timing_clock(0.2, object.gameplay)
        self.level = level
    
    def play(self):
        self.animation.play()
        self.clock.start()
        if self.clock.Return :
            self.object.imgbox.centerx -= (self.object.speed * self.level * screen.screen.get_rect().width / 50) * (self.object.gameplay.curr_time - self.object.gameplay.pre_curr_time)  * self.object.side
        else:
            self.remove()

    def remove(self):
        self.object.effect_list.remove(self)
        self.clock.remove()

class flying():
    def __init__(self, object, level):
        self.object = object
        self.level = level

    def play(self):
        self.object.imgbox.centery -= self.object.gameplay.box_size[1] * self.level 
        self.remove()

    def remove(self):
        self.object.effect_list.remove(self)

dizzy_effect = 1
soul_sucking_effect = 2
knock_back_effect = 3
flying_effect = 4

def add_effect(object, effect,lasted_time, level):
    if effect == dizzy_effect:
        object.effect_list.append(dizzy(object, lasted_time))
    elif effect == soul_sucking_effect:
        object.effect_list.append(soul_sucking(object))
    elif effect == knock_back_effect:
        object.effect_list.append(knock_back(object, level))
    elif effect == flying_effect:
        object.effect_list.append(flying(object, level))
