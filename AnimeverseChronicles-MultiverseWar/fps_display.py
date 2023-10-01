import pygame
import sys
from color import *
from screen import *

class FPS:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Fonts\\AznKnucklesTrialBold-6YB6o.otf", 28)
        self.text = self.font.render(str(self.clock.get_fps()), True, Green)

    def render(self, display):
        self.text = self.font.render(str(round(self.clock.get_fps(),2)), True, Green)
        display.blit(self.text, (5, 5))