import pygame
from pygame.locals import *
from object_function import *
from Random import *
class PvC_mode():
    def __init__(self, gameplay):
        self.gameplay = gameplay
        self.rand = Random()
        self.character_control = []
        self.start_spawn_time = -1
        self.spawn_queue = []

    def get_random_number(self):
        return self.rand.get_truly_random_seed_through_os()

    def get_character(self, index): #lay nhan vat vi tri index(index tinh tu 0)
        return self.character_control[index]

    def spawn_state(self, idx):
        if self.gameplay.curr_gold_2 >= self.gameplay.get_character_cost(idx, 2) and len(self.spawn_queue) < 3:
            return True
        return False
    
    def insert_in_spawn_queue(self, idx):
        if len(self.spawn_queue) < 3:
            self.spawn_queue.append(idx)
            self.gameplay.gold_outcome_2 += self.gameplay.get_character_cost(idx, 2)

    def level_up_routines(self):
        #up level
        if self.gameplay.curr_gold_2 >= self.gameplay.level_up_cost[self.gameplay.curr_level2 - 1]:
            self.gameplay.level_up(2)
            if self.gameplay.character_level2[3] < 3 and self.gameplay.character_level_up(3, 2) == False:
                if self.gameplay.character_level2[1] < 3 and self.gameplay.character_level_up(1, 2) == False:
                    if self.gameplay.character_level_up(3, 2) == False:
                        if self.gameplay.character_level2[2] < 3 and self.gameplay.character_level_up(2, 2) == False:
                            if self.gameplay.character_level2[4] < 3 and self.gameplay.character_level_up(4, 2) == False:
                                if self.gameplay.character_level_up(1, 2) == False:
                                    if self.gameplay.character_level_up(4, 2) == False:
                                        if self.gameplay.character_level_up(2, 2) == False:
                                            if self.gameplay.character_level2[5] < 2 and self.gameplay.character_level_up(5, 2) == False:
                                                if self.gameplay.character_level_up(6, 2) == False:
                                                    if self.gameplay.character_level_up(5, 2) == False:
                                                        pass

    def update(self):
        self.character_control = []
        for i in range(1, len(self.gameplay.side2)):
            try:
                self.character_control.append(list(self.gameplay.character_slot_idx.values()).index(self.gameplay.side2[i].__class__))
            except:
                pass
        for x in self.spawn_queue:
            self.character_control.append(x)

        # print(self.character_control)
        if len(self.character_control) == 0 or (len(self.character_control) == 1 and self.character_control[-1] != 0):
            if self.spawn_state(0):
                self.insert_in_spawn_queue(0)
                self.character_control.append(0)
        elif self.character_control[-1] == 0 and len(self.character_control) <= 5:
            if self.spawn_state(1):
                self.insert_in_spawn_queue(1)
                self.character_control.append(1)
        elif self.character_control[-1] == 1 and len(self.character_control) <= 5:
            if self.spawn_state(2):
                self.insert_in_spawn_queue(2)
                self.character_control.append(2)
        elif self.character_control[-1] == 2 and len(self.character_control) <= 5:
            if self.spawn_state(3):
                self.insert_in_spawn_queue(3)
                self.character_control.append(3)
        elif len(self.character_control) <= 6:
            if len(self.gameplay.side2) + len(self.spawn_queue) - len(self.gameplay.side1) < 2 and self.spawn_state(5):
                rand_num = self.get_random_number() % 2 + 4
                if self.spawn_state(rand_num):
                    self.insert_in_spawn_queue(rand_num)
                    self.character_control.append(rand_num)
            else:
                self.level_up_routines()
        else:
            self.level_up_routines()


        if self.start_spawn_time != -1 and self.gameplay.curr_time - self.start_spawn_time >= self.gameplay.spawn_time:
            spawn(self.gameplay.character_slot_idx[self.spawn_queue[0]], 2, self.gameplay.number_of_box - 5, self.gameplay)
            del self.spawn_queue[0]
            self.start_spawn_time = -1
        
        if len(self.spawn_queue) != 0 and self.start_spawn_time == -1:
            self.start_spawn_time = self.gameplay.curr_time

