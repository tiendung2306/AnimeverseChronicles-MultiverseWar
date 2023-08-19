import random
import pygame 
from pygame.locals import *


class N_time_switch():
    def __init__(self,N):
        self.N = N
        self.counter = N
    def operation(self):
        if not (self.counter == 0):
            self.counter -= 1
            return True
        else:
            return False

    def reset(self):
        self.counter = self.N