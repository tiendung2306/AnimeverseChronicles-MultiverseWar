import pygame 
from pygame.locals import *
from clock import*
from img_analyze import *
from screen import *

class animation_player():
    def __init__(self,img_lib,side,loop_time,imgbox,gameplay):
        self.img_lib = []
        if side == 1:
            self.img_lib =img_lib
        else:
            for img in img_lib:
                self.img_lib.append(reverse(img))
        self.frames = len(img_lib)
        self.loop_time = loop_time
        self.imgbox = imgbox
        self.gameplay = gameplay
        self.clock = N_ValueReturn_repeated_clock(self.loop_time / self.frames, self.frames,self.gameplay)
    
    def play(self):
        self.clock.start()
        screen.screen.blit(pygame.transform.scale(self.img_lib[self.clock.Return - 1].img, (self.imgbox.width,self.imgbox.height)), self.imgbox)
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


class one_time_animation_player():
    def __init__(self,img_lib,side,loop_time,imgbox,gameplay):
        self.img_lib = []
        if side == 1:
            self.img_lib =img_lib
        else:
            for img in img_lib:
                self.img_lib.append(reverse(img))
        self.frames = len(img_lib)
        self.loop_time = loop_time
        self.imgbox = imgbox
        self.gameplay = gameplay
        self.clock = N_ValueReturn_repeated_clock(self.loop_time / self.frames, self.frames,self.gameplay)
        self.status = True

    def play(self):
        if self.status:
            self.clock.start()
            if self.clock.Return == self.clock.times:
                if self.clock.gameplay.curr_time >= self.clock.counter:
                    self.remove()
            screen.screen.blit(pygame.transform.scale(self.img_lib[self.clock.Return - 1].img, (self.imgbox.width,self.imgbox.height)), self.imgbox)
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
        self.status = False