import random
import pygame 
from pygame.locals import *
from switch import *

class repeated_clock():
    def __init__(self,FPS,repeat_time):
        self.repeat_time = repeat_time #second(s)
        self.counter = repeat_time
        self.FPS = FPS
        self.Return = None
        self.status = False
        self.switch = N_time_switch(1)
    def start(self):
        if self.switch.operation():
            self.status = True  
            self.operation()
    def reset(self):
        self.counter = self.repeat_time
        self.Return = None
        self.status = False
        self.switch = N_time_switch(1)

    def operation(self):
        if self.status:
            if self.counter == self.repeat_time:
                self.counter -= 1 / self.FPS
                self.Return = True
            else:
                if self.counter < 0:
                    self.counter = self.repeat_time
                else :
                    self.counter -= 1 / self.FPS
                self.Return = False

class N_ValueReturn_repeated_clock():
    def __init__(self,FPS,repeat_time,times):
        self.repeat_time = repeat_time #second(s)
        self.counter = 0
        self.FPS = FPS
        self.times = times
        self.times_counter = 1
        self.Return = 1
        self.status = False
        self.switch = N_time_switch(1)
    def start(self):
        if self.switch.operation():
            self.status = True  
            self.operation()
    def reset(self):
        self.counter = 0
        self.Return = 1
        self.status = False
        self.switch = N_time_switch(1)

    def operation(self):
        if self.status:
            if self.Return > self.times:
                self.Return = 1
            if self.counter >= self.repeat_time:
                self.Return += 1
                self.counter = 0
            else:
                self.counter += 1 / self.FPS
        # print(self.counter)


class timing_clock():
    def __init__(self,FPS,time):
        self.time = time
        self.counter = time
        self.FPS = FPS
        self.Return = None
        self.status = False
        self.switch = N_time_switch(1)

    def start(self):
        if self.switch.operation():
            self.status = True  
            self.operation()
    def reset(self):
        self.counter = self.time 
        self.Return = None
        self.status = False
        self.switch = N_time_switch(1)

    def operation(self):
        if self.status:
            if self.counter > 0:
                self.counter -= 1 / self.FPS
                self.Return = True
            else:
                self.Return = False
