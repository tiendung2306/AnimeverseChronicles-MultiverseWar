import random
import pygame 
from pygame.locals import *
from clock import*

def list_find(list,object):
    if not (len(list) == 0):
        for i in list:
            if i == object:
                return list.index(i)
        return -1
    else:
        return -1
    

def list_find_special(list, object,):
    if not (len(list) == 0):
        for i in list:
            if i.object == object:
                return True
        return False
    else:
        return False

def list_operation(list):
    tmp_list = []
    for object in list:
        tmp_list.append(object)
    for object in tmp_list:
        if list_find(list,object):
            object.operation()
    


def list_browser(list, method):
    tmp_list = []
    for element in list:
        tmp_list.append(element)
    for element in tmp_list:
        if not list_find(list,element) == -1 :
            method(element)


def list_browser_reverse(list, method):
    tmp_list = []
    for element in list:
        tmp_list.append(element)

    i = len(tmp_list) - 1
    while i >= 0 :
        if not list_find(list,tmp_list[i]) == -1 :
            method(tmp_list[i])
        i -= 1

