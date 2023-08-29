import pygame 
from pygame.locals import *
from straw_doll import *
from archer import *
from sword_man import *
from tanker import *
from wizard import *
from nexus_test import *

nexus = -1
straw_doll = 0
archer = 1
sword_man = 2
tanker = 3 
wizard = 4
def spawn(object_type,side,position,gameplay):
    if object_type == 0 :
        if side == 1 :
            gameplay.side1.append(straw_doll_class(side,position,gameplay))
        elif side == 2 :
            gameplay.side2.append(straw_doll_class(side,position,gameplay))
    elif object_type == 1 :
        if side == 1 :
            gameplay.side1.append(archerclass(side,position,gameplay))
        elif side == 2 :
            gameplay.side2.append(archerclass(side,position,gameplay))
    elif object_type == 2 :
        if side == 1 :
            gameplay.side1.append(sword_manclass(side,position,gameplay))
        elif side == 2 :
            gameplay.side2.append(sword_manclass(side,position,gameplay))
    elif object_type == 3 :
        if side == 1 :
            gameplay.side1.append(tankerclass(side,position,gameplay))
        elif side == 2 :
            gameplay.side2.append(tankerclass(side,position,gameplay))
    elif object_type == 4 :
        if side == 1 :
            gameplay.side1.append(wizardclass(side,position,gameplay))
        elif side == 2 :
            gameplay.side2.append(wizardclass(side,position,gameplay))
    elif object_type == -1 :
        if side == 1 :
            gameplay.side1.append(nexusclass(side,position,gameplay))
        elif side == 2 :
            gameplay.side2.append(nexusclass(side,position,gameplay))
        