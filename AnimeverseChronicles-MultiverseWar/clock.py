import pygame 
from pygame.locals import *
from switch import *



class repeated_clock():
    def __init__(self,repeat_time,gameplay):
        self.gameplay = gameplay
        self.repeat_time = + repeat_time #second(s)
        self.counter = None
        self.Return = None
        self.status = False
        self.switch = N_time_switch(1)
        gameplay.side3.append(self)

    def start(self):
        if self.switch.operation():
            self.counter = self.gameplay.curr_time + self.repeat_time #second(s)
            self.status = True  
            self.operation()

    def reset(self):
        self.counter =  self.gameplay.curr_time + self.repeat_time
        self.Return = None
        self.status = False
        self.switch = N_time_switch(1)

    def operation(self):
        if self.status:
            if self.gameplay.curr_time >= self.counter:
                self.counter += self.repeat_time
                self.Return = True
            else:
                self.Return = False

    def remove(self):
        self.gameplay.side3.remove(self)



class N_ValueReturn_repeated_clock():
    def __init__(self,repeat_time,loop_times,gameplay):
        self.gameplay = gameplay
        self.repeat_time = repeat_time #second(s)
        self.counter = None
        self.times = loop_times
        self.Return = 1
        self.status = None
        self.switch = N_time_switch(1)
        self.gameplay.side3.append(self)

    def start(self):
        if self.switch.operation():
            self.counter = self.gameplay.curr_time + self.repeat_time
            self.status = True  
            self.operation()

    def reset(self):
        self.counter = 0
        self.Return = 1
        self.status = None
        self.switch = N_time_switch(1)

    def operation(self):
        if self.status:
            if self.gameplay.curr_time >= self.counter:
                self.counter += self.repeat_time
                if self.Return == self.times:
                    self.Return = 1
                else:
                    self.Return += 1

    def remove(self):
        self.gameplay.side3.remove(self)


class timing_clock():
    def __init__(self,lasted_time,gameplay):
        self.gameplay = gameplay
        self.lasted_time = lasted_time
        self.counter = None
        self.Return = None
        self.status = False
        self.switch = N_time_switch(1)
        gameplay.side3.append(self)

    def start(self):
        if self.switch.operation():
            self.counter = self.gameplay.curr_time + self.lasted_time
            self.status = True  
            self.operation()

    def operation(self):
        if self.status:
            if self.gameplay.curr_time <= self.counter :
                self.Return = True
            else:
                self.Return = False

    def reset(self):
        self.counter = None
        self.Return = None
        self.status = False
        self.switch.reset()

    def update_lasting_time(self, new_lasting_time):
        tmp = (self.counter - self.gameplay.curr_time) / self.lasted_time
        self.lasted_time = new_lasting_time
        self.counter = tmp * self.lasted_time + self.gameplay.curr_time

    def remove(self):
        self.gameplay.side3.remove(self)