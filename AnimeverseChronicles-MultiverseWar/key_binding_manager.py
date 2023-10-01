import pygame
from pygame.locals import *
class keybindingmanager():  
    default_key_map = {
        'Slot 1' : pygame.K_1,
        'Slot 2' : pygame.K_2,
        'Slot 3' : pygame.K_3,
        'Slot 4' : pygame.K_4,
        'Slot 5' : pygame.K_5,
        'Slot 6' : pygame.K_6,
        'Slot 7' : pygame.K_7,
        'Player_2_level_up' : pygame.K_p,
        'Character_level_up_key1' : pygame.K_LCTRL,
        'Character_level_up_key2' : pygame.K_RCTRL,
    }

    key_map = default_key_map.copy()