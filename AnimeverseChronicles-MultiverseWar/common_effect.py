import pygame 
from pygame.locals import *
from clock import *
from img_analyze import *
from animation_player import *

class dizzy():
    def __init__(self, object, lasted_time):
        self.imgbox = dizzy_effect1.hitbox_to_imgbox(pygame.Rect(object.box.left, object.box.top - object.box.height / 4, object.box.width, object.box.height / 2))
        self.animation = animation_player([dizzy_effect1,dizzy_effect2,dizzy_effect3,dizzy_effect4,dizzy_effect5,dizzy_effect6,dizzy_effect7,dizzy_effect8,dizzy_effect9], object.side ,1,self.imgbox, object.gameplay)
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

dizzy_effect = 1

def add_effect(object, effect,lasted_time):
    if effect == dizzy_effect:
        object.effect_list.append(dizzy(object, lasted_time))
