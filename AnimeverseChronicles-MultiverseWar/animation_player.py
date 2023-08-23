import pygame 
from pygame.locals import *
from clock import*
from img_analyze import *


class animation_player():
    def __init__(self,img_lib,loop_time,imgbox,gameplay):
        self.img_lib = img_lib
        self.frames = len(img_lib)
        self.loop_time = loop_time
        self.imgbox = imgbox
        self.gameplay = gameplay
        self.clock = N_ValueReturn_repeated_clock(self.loop_time / self.frames, self.frames,self.gameplay)
    
    def play(self):
        self.clock.start()
        self.gameplay.screen.blit(pygame.transform.smoothscale(self.img_lib[self.clock.Return - 1].img, (self.imgbox.width,self.imgbox.height)), self.imgbox)
        return self.img_lib[self.clock.Return - 1].imgbox_to_hitbox(self.imgbox)
    
    def update_looptime(self, new_loop_time):
        self.loop_time = new_loop_time
        tmp = self.clock.Return
        self.clock = N_ValueReturn_repeated_clock(self.loop_time / self.frames, self.frames,self.gameplay)
        self.clock.Return = tmp
            
    def reset(self):
        self.clock.reset

    def remove(self):
        self.clock.remove()


