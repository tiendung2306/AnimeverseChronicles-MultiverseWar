import pygame 
from pygame.locals import *
from clock import *
from img_analyze import *
from animation_player import *

class dizzy():
    def __init__(self, object, lasted_time):
        self.animation = animation_player_special([dizzy_effect1,dizzy_effect2,dizzy_effect3,dizzy_effect4,dizzy_effect5,dizzy_effect6,dizzy_effect7,dizzy_effect8,dizzy_effect9], object.side ,1, object.box, (0, -1/4, 1,  1/2), object.gameplay)
        self.clock = timing_clock(lasted_time ,object.gameplay)
        self.object = object

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
        self.animation = one_time_animation_player_special([soul1, soul2, soul3, soul4, soul5, soul6, soul6, soul6, soul7, soul8], - object.side, 1, object.box, (- 3 / 4, -1 / 2, 1, 1), object.gameplay)
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


dizzy_effect = 1
soul_sucking_effect = 2

def add_effect(object, effect,lasted_time):
    if effect == dizzy_effect:
        object.effect_list.append(dizzy(object, lasted_time))
    if effect == soul_sucking_effect:
        object.effect_list.append(soul_sucking(object))