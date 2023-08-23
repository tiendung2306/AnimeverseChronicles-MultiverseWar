import pygame
from pygame.locals import *

class screen():
    pygame.init()
    curr_monitor_resolution = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    screen = pygame.display.set_mode((curr_monitor_resolution), FULLSCREEN)