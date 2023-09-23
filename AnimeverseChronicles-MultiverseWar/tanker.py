import pygame 
from pygame.locals import *
from collide_checker import *
from object_function import *
from clock import *
from switch import *
from animation_player import *
from screen import *
from list_function import*
from common_effect import*


tanker1 = analyzed_img("GameplayAssets\\tanker\\tanker(1).png", 229 , 60 , 85 , 222)
tanker2 = analyzed_img("GameplayAssets\\tanker\\tanker(2).png", 229 , 60 , 85 , 222)
tanker3 = analyzed_img("GameplayAssets\\tanker\\tanker(3).png", 229 , 60 , 85 , 222)
tanker4 = analyzed_img("GameplayAssets\\tanker\\tanker(4).png", 229 , 60 , 85 , 222)
tanker5 = analyzed_img("GameplayAssets\\tanker\\tanker(5).png", 223 , 59 , 76 , 220)
tanker6 = analyzed_img("GameplayAssets\\tanker\\tanker(6).png", 223 , 59 , 76 , 220)
tanker7 = analyzed_img("GameplayAssets\\tanker\\tanker(7).png", 223 , 59 , 76 , 220)
tanker8 = analyzed_img("GameplayAssets\\tanker\\tanker(8).png", 236 , 60 , 73 , 222)
tanker9 = analyzed_img("GameplayAssets\\tanker\\tanker(9).png", 224 , 62 , 69 , 216)
tanker10 = analyzed_img("GameplayAssets\\tanker\\tanker(10).png", 218 , 62 , 84 , 221)
tanker11 = analyzed_img("GameplayAssets\\tanker\\tanker(11).png", 221 , 61 , 96 , 220)
tanker12 = analyzed_img("GameplayAssets\\tanker\\tanker(12).png", 219 , 62 , 76 , 216)
tanker13 = analyzed_img("GameplayAssets\\tanker\\tanker(13).png", 261 , 72 , 70 , 205)
tanker14 = analyzed_img("GameplayAssets\\tanker\\tanker(14).png", 261 , 72 , 70 , 205)
tanker15 = analyzed_img("GameplayAssets\\tanker\\tanker(15).png", 257 , 66 , 65 , 215)
tanker16 = analyzed_img("GameplayAssets\\tanker\\tanker(16).png", 243 , 65 , 56 , 210)
tanker17 = analyzed_img("GameplayAssets\\tanker\\tanker(17).png", 262 , 75 , 60 , 204)
tanker18 = analyzed_img("GameplayAssets\\tanker\\tanker(18).png", 266 , 77 , 70 , 201)
tanker19 = analyzed_img("GameplayAssets\\tanker\\tanker(19).png", 249 , 71 , 71 , 207)
tanker20 = analyzed_img("GameplayAssets\\tanker\\tanker(20).png" , 260 , 73 , 98 , 207 )
tanker21 = analyzed_img("GameplayAssets\\tanker\\tanker(21).png" , 260 , 73 , 98 , 207 )
tanker22 = analyzed_img("GameplayAssets\\tanker\\tanker(22).png" , 260 , 73 , 98 , 207 )
tanker23 = analyzed_img("GameplayAssets\\tanker\\tanker(23).png", 240 , 62 , 56 , 219)
tanker24 = analyzed_img("GameplayAssets\\tanker\\tanker(24).png" , 211 , 62 , 89 , 216 )
tanker25 = analyzed_img("GameplayAssets\\tanker\\tanker(25).png" , 211 , 62 , 89 , 216 )
tanker26 = analyzed_img("GameplayAssets\\tanker\\tanker(26).png" , 211 , 62 , 89 , 216 )
tanker27 = analyzed_img("GameplayAssets\\tanker\\tanker(27).png" , 263 , 60 , 67 , 218 )
tanker28 = analyzed_img("GameplayAssets\\tanker\\tanker(28).png" , 263 , 60 , 67 , 218 )
tanker29 = analyzed_img("GameplayAssets\\tanker\\tanker(29).png" , 263 , 60 , 67 , 218 )
tanker30 = analyzed_img("GameplayAssets\\tanker\\tanker(30).png" , 214 , 61 , 102 , 220 )
tanker31 = analyzed_img("GameplayAssets\\tanker\\tanker(31).png" , 214 , 61 , 102 , 220 )
tanker32 = analyzed_img("GameplayAssets\\tanker\\tanker(32).png", 217 , 77 , 94 , 203)
tanker33 = analyzed_img("GameplayAssets\\tanker\\tanker(33).png", 410 , 186 , 0 , 0)
tanker34 = analyzed_img("GameplayAssets\\tanker\\tanker(34).png", 256 , 80 , 75 , 199)
tanker35 = analyzed_img("GameplayAssets\\tanker\\tanker(35).png", 410 , 186 , 0 , 0)
tanker36 = analyzed_img("GameplayAssets\\tanker\\tanker(36).png", 410 , 186 , 0 , 0)
tanker37 = analyzed_img("GameplayAssets\\tanker\\tanker(37).png", 410 , 186 , 0 , 0)
tanker38 = analyzed_img("GameplayAssets\\tanker\\tanker(38).png", 410 , 186 , 0 , 0)

attack_damage = [10.0 , 20.0, 45.0 , 50.0,  70.0]
health = [500.0, 600.0, 1200.0, 1500.0, 3000.0]
damage_reduce = [40.0, 45.0, 70.0, 65.0, 90.0]

class tankerclass():
    def __init__(self, side, gameplay):
        self.pre_status = None
        self.status  = None
        self.box = pygame.Rect(0,0,0,0)
        self.imgbox = pygame.Rect(0,0,0,0)
        self.gameplay = gameplay
        if side == 1 :
            self.side = 1
            self.level = self.gameplay.character_level1[0]
        elif side == 2:
            self.side = -1
            self.level = self.gameplay.character_level2[0]

        self.speed = 5.0 # 1/100 map per second 
        self.attack_scope = 1 * self.gameplay.box_size[0]   # 4/15 map width
        self.attack_speed = 1/6 # attack(s) pers second
        self.attack_damage = attack_damage[self.level - 1]
        self.health_max = health[self.level - 1]
        self.health =  self.health_max
        self.mana_max = 100.0
        self.mana = 0.0
        self.damage_reduce =  0 #0%
        self.skill_lasting_time = 3

        self.effect_list = []

        self.alive = True
        self.get_hit = False
        self.ischeck = True
        self.iscollide_check = True
        self.collide = None
        self.special_status = False

        self.moving_animation = animation_player([tanker13,tanker14,tanker15,tanker16,tanker17,tanker18,tanker19], self.side, 1, self.imgbox , self.gameplay)
        self.attacking_animation = one_time_animation_player([tanker23,tanker24,tanker25,tanker26,tanker27,tanker28,tanker29,tanker30,tanker31],self.side, 1 , self.imgbox, self.gameplay)
        self.defending_animation = one_time_animation_player( [tanker20,tanker21,tanker22,tanker21], self.side, 1, self.imgbox, self.gameplay)
        self.walking_animation = animation_player( [tanker20,tanker21,tanker22,tanker21], self.side, 1, self.imgbox, self.gameplay)
        self.walking_animation2 = animation_player([tanker1,tanker2,tanker3,tanker4],self.side, 1, self.imgbox, self.gameplay)
        self.standstill_animation = one_time_animation_player([tanker1,tanker2,tanker3,tanker4],self.side, 1, self.imgbox, self.gameplay)
        self.dying_animation = one_time_animation_player([tanker32,tanker33,tanker34,tanker35,tanker36,tanker37,tanker38,tanker38,tanker38,tanker38], self.side, 0.8, self.imgbox, self.gameplay)
        self.knock_back_animation = animation_player([tanker34], self.side, 1, self.imgbox, self.gameplay)
        self.flying_animation = animation_player([tanker32,tanker32], self.side, 1, self.imgbox, self.gameplay)
        self.falling_animation = animation_player([tanker34], self.side, 1, self.imgbox, self.gameplay)

        self.switcher1 = N_time_switch(1)
        self.switcher2 = N_time_switch(1)
        self.switcher3 = N_time_switch(1)
        self.switcher4 = N_time_switch(1)
        self.switcher5 = N_time_switch(1)
        self.attack_coundowner = timing_clock(1 / self.attack_speed, self.gameplay)

        self.skill_countdowner = timing_clock(3, self.gameplay)


    def resize(self):
        a = float(screen.screen.get_width()) / self.gameplay.screen[0]
        b = float(screen.screen.get_height()) /  self.gameplay.screen[1]
        tmp = pygame.Rect(self.imgbox.left * a, self.imgbox.top * b, self.imgbox.width * a, self.imgbox.height * b)
        copy(self.imgbox, tmp)
        self.operation()

        
    def status_update(self):
        if not self.level == self.gameplay.character_level(self.side, 0):
            self.attack_damage = attack_damage[self.level - 1]
            self.health_max = health[self.level - 1]
            self.damage_reduce_special =  damage_reduce[self.level - 1]


        self.attack_damage = attack_damage[self.level - 1]
        self.health_max = health[self.level - 1]
        self.damage_reduce_special =  damage_reduce[self.level - 1]

        self.pre_status = self.status

        if self.pre_status == 1:
            if self.attacking_animation.status == True:
                self.ischeck = False
            elif self.attacking_animation.status == False:
                self.ischeck = True
                self.attack_reset()
        elif self.pre_status == 2:
            if self.standstill_animation.status == True:
                self.ischeck = False
            elif self.standstill_animation.status == False:
                self.ischeck = True           
                self.standsill_reset()
        if self.pre_status == 6:
            if self.defending_animation.status == True:
                self.ischeck = False
            elif self.defending_animation.status == False:
                self.ischeck = True
                self.defend_reset()


    def display(self):
        copy(self.box, self.animation_player.play())
        pygame.draw.rect(screen.screen,Red,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 10 ,(self.box.width - self.box.width / 2) / self.health_max *self.health,self.box.height / 20))
        pygame.draw.rect(screen.screen,Blue,pygame.Rect(self.box.left + self.box.width / 4 ,self.box.top - self.box.height / 5 - self.box.height / 30 ,(self.box.width - self.box.width / 2) / self.mana_max *self.mana,self.box.height / 20))
        
    
    def move(self):
        self.animation_player = self.moving_animation
        self.imgbox.centerx += (self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  * self.side

    def walk(self):
        self.animation_player = self.walking_animation
        self.imgbox.centerx += (2 * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  * self.side

    def walk2(self):
        self.animation_player = self.walking_animation2
        self.imgbox.centerx += (2 * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  * self.side

    def standstill(self):
        self.animation_player = self.standstill_animation

    def standsill_reset(self):
        self.standstill_animation.reset()
    
    
    def check_collide(self):
        if self.iscollide_check:
            for object in self.gameplay.side(self.side) + self.gameplay.side4 + self.gameplay.side(- self.side):
                if abs(object.box.centerx - self.box.centerx) <= self.gameplay.box_size[0] / 3:
                    if same_line_checker(self, object):
                        if not (self == object):
                            if collide_checker(self ,object):
                                self.collide = True
                                if self.side == object.side:
                                    if self.index > object.index :
                                        self.collide = 1
                                        if self.box.right < self.gameplay.nexus2.box.left and self.box.left > self.gameplay.nexus1.box.right:
                                            self.imgbox.centerx -= ( 5.0 * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time) * self.side
                                            self.box.centerx -= ( 5.0 * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time) * self.side
                                        return

                                else:
                                    self.collide = 2
                                    if self.box.right < self.gameplay.nexus2.box.left and self.box.left > self.gameplay.nexus1.box.right:
                                        self.imgbox.centerx -= ( 5.0 * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time) * self.side
                                        self.box.centerx -= ( 5.0 * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time) * self.side
                                    return
                self.collide = False


    def check_forward(self): #always after check_collide
        if self.ischeck :

            flag = False
            if self.collide == 2:
                self.status = 1
                flag = True

            elif self.collide == 1:
                ispass = False
                for object in self.gameplay.side(- self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 3 + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side > 0:
                            if same_line_checker(self, object):
                                self.status = 1
                                flag = True
                                ispass = True
                                break
                if not ispass:
                    self.status = 2
                    flag = True
            else:
                ispass = False
                for object in self.gameplay.side( - self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 3 + (self.box.width + object.box.width) / 2:
                        if (object.box.centerx - self.box.centerx) * self.side > 0:
                            if same_line_checker(self, object):
                                self.status = 1
                                flag = True
                                ispass = True
                                break
                if not ispass:
                    for object in self.gameplay.side(self.side) + self.gameplay.side4 :
                        if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 2 + (self.box.width + object.box.width) / 2 :
                            if (object.box.centerx - self.box.centerx) * self.side > 0:
                                if same_line_checker(self, object):
                                    if (not (self == object)) and (self.index > object.index):
                                        self.status = 2
                                        flag = True
                                        break         
            if not flag:
                self.status = 3

            if self.status == 3 and (not self.pre_status == 3):
                ispass = False
                for object in self.gameplay.side( - self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 3 + (self.speed * screen.screen.get_rect().width / 100) * 0.5  + (self.box.width + object.box.width) / 2:
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                self.status = 5.5
                                ispass = True
                                break
                if not ispass:
                    for object in self.gameplay.side(self.side) + self.gameplay.side4 :
                        if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 2 + (self.speed * screen.screen.get_rect().width / 100) * 0.5  + (self.box.width + object.box.width) / 2 :
                            if (object.box.centerx - self.box.centerx) * self.side >= 0:
                                if same_line_checker(self, object):
                                    if not (self == object):
                                        if not  object.status == 3:
                                            self.status = 5
                                            break     
            
            
            if self.status == 1 :
                if self.attack_coundowner.Return == True:
                    self.status = 6

        if self.mana >= self.mana_max:
            self.mana = 0
            self.special_status = True

        if self.status > 0:
            if not self.pre_status == None:
                if self.pre_status > 0:
                    if not self.pre_status == self.status:            
                        if self.pre_status == 1:
                            self.attack_reset()
                        elif self.pre_status == 2:
                            self.standsill_reset()
                        elif self.pre_status == 4:
                            self.defend_reset()




    def Geting_hit(self):
        self.get_hit = False
        self.health -= self.get_damage - self.get_damage * self.damage_reduce / 100
        self.get_damage = 0
        if not self.special_status:
            self.mana += 10


    def dying(self):
        if self.switcher4.operation():
            self.moving_animation.remove()
            self.attacking_animation.remove()
            self.standstill_animation.remove()      
            self.falling_animation.remove()
            self.flying_animation.remove()
            self.knock_back_animation.remove()

            self.gameplay.side(self.side).remove(self)
            self.side = 0
            self.gameplay.side0.append(self)
            
        self.dying_animation.play()
        if self.dying_animation.status == False:
            self.dying_animation.remove()
            self.gameplay.side0.remove(self)



    def attack(self):
        if self.switcher5.operation():
            self.attack_coundowner.reset()
            self.attack_coundowner.start()
            
        self.animation_player = self.attacking_animation
        if self.attacking_animation.clock.Return == 5 or self.attacking_animation.clock.Return == 8 :
            if self.switcher1.operation():
                if not self.special_status :
                    self.mana += 10     
                for object in self.gameplay.side(- self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                object.get_hit = True
                                object.get_damage = self.attack_damage
        elif self.attacking_animation.clock.Return == 4 or self.attacking_animation.clock.Return == 7 :
            self.switcher1.reset()
            

    def attack_reset(self):
        self.attacking_animation.reset() 
        self.switcher5.reset()


    def defend(self):
        self.animation_player = self.defending_animation

    def defend_reset(self):
        self.defending_animation.reset()

    def special_skill(self):
        if self.switcher2.operation():
            self.skill_countdowner.start()
            self.effect = shield(self, 10, damage_reduce[self.level - 1])
            add_effect(self,self.effect)

        if self.skill_countdowner.Return == False:
            self.special_skill_reset()

    def special_skill_reset(self):
        self.damage_reduce = 0
        self.special_status = False
        self.switcher2.reset()
        self.skill_countdowner.reset()            


    def operation(self):
        if self.alive:
            def play(effect):
                effect.play()
            list_browser(self.effect_list, play)
            
            self.check_collide()
            self.check_forward()
            
            if self.status == 3:
                self.move()
            elif self.status == 5:
                self.walk2()

            elif self.status == 5.5:
                self.walk()


            elif self.status == 1:
                self.attack()

            elif self.status == 2 :
                self.standstill()

            elif self.status == 6:
                self.defend()

            if self.special_status:
                self.special_skill()

            if self.get_hit :
                self.Geting_hit()

            if self.health <= 0:
                self.alive = False
                

            self.display()
            self.status_update()


            # pygame.draw.rect(screen.screen,White,self.box,1)
            # pygame.draw.rect(screen.screen,White,self.imgbox,1)
        else:
            self.dying()


