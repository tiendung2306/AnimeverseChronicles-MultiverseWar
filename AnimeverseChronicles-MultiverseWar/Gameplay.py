import pygame
from pygame.locals import *

class gameplay():
    def __init__(self):
        self.bg = pygame.image.load('GameplaySprites\\bg0.jpg')
    
    def update(self):
        info = pygame.display.Info()
        self.bg = pygame.transform.smoothscale(self.bg, (info.current_w, info.current_h))
