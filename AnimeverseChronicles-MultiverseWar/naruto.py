import pygame 
from pygame.locals import *
from collide_checker import *
from object_function import *
from clock import *
from switch import *
from list_function import *
from animation_player import *
from screen import *
from common_effect import *
from character_properties import *


naruto1 = analyzed_img( "GameplayAssets\\naruto\\naruto(1).png " , 296 , 346 , 74 , 176 )
naruto2 = analyzed_img( "GameplayAssets\\naruto\\naruto(2).png " , 296 , 346 , 74 , 176 )
naruto3 = analyzed_img( "GameplayAssets\\naruto\\naruto(3).png " , 296 , 346 , 74 , 176 )
naruto4 = analyzed_img( "GameplayAssets\\naruto\\naruto(4).png " , 296 , 346 , 74 , 176 )
naruto5 = analyzed_img( "GameplayAssets\\naruto\\naruto(5).png " , 296 , 346 , 74 , 176 )
naruto6 = analyzed_img( "GameplayAssets\\naruto\\naruto(6).png " , 268 , 369 , 110 , 156 )
naruto7 = analyzed_img( "GameplayAssets\\naruto\\naruto(7).png " , 295 , 341 , 78 , 177 )
naruto8 = analyzed_img( "GameplayAssets\\naruto\\naruto(8).png " , 281 , 425 , 148 , 102 )
naruto9 = analyzed_img( "GameplayAssets\\naruto\\naruto(9).png " , 281 , 425 , 148 , 102 )
naruto10 = analyzed_img( "GameplayAssets\\naruto\\naruto(10).png " , 289 , 386 , 118 , 137 )
naruto11 = analyzed_img( "GameplayAssets\\naruto\\naruto(11).png " , 324 , 335 , 93 , 185 )
naruto12 = analyzed_img( "GameplayAssets\\naruto\\naruto(12).png " , 324 , 335 , 93 , 185 )
naruto13 = analyzed_img( "GameplayAssets\\naruto\\naruto(13).png " , 292 , 349 , 96 , 178 )
naruto14 = analyzed_img( "GameplayAssets\\naruto\\naruto(14).png " , 303 , 352 , 97 , 169 )
naruto15 = analyzed_img( "GameplayAssets\\naruto\\naruto(15).png " , 306 , 340 , 97 , 183 )
naruto16 = analyzed_img( "GameplayAssets\\naruto\\naruto(16).png " , 306 , 340 , 97 , 183 )
naruto17 = analyzed_img( "GameplayAssets\\naruto\\naruto(17).png " , 322 , 361 , 102 , 164 )
naruto18 = analyzed_img( "GameplayAssets\\naruto\\naruto(18).png " , 278 , 354 , 98 , 167 )
naruto19 = analyzed_img( "GameplayAssets\\naruto\\naruto(19).png " , 295 , 362 , 77 , 158 )
naruto20 = analyzed_img( "GameplayAssets\\naruto\\naruto(20).png " , 295 , 362 , 77 , 158 )
naruto21 = analyzed_img( "GameplayAssets\\naruto\\naruto(21).png " , 295 , 362 , 77 , 158 )
naruto22 = analyzed_img( "GameplayAssets\\naruto\\naruto(22).png " , 295 , 362 , 77 , 158 )
naruto23 = analyzed_img( "GameplayAssets\\naruto\\naruto(23).png " , 295 , 362 , 77 , 158 )
naruto24 = analyzed_img( "GameplayAssets\\naruto\\naruto(24).png " , 295 , 362 , 77 , 158 )
naruto25 = analyzed_img( "GameplayAssets\\naruto\\naruto(25).png " , 295 , 362 , 77 , 158 )
naruto26 = analyzed_img( "GameplayAssets\\naruto\\naruto(26).png " , 295 , 362 , 77 , 158 )
naruto27 = analyzed_img( "GameplayAssets\\naruto\\naruto(27).png " , 162 , 339 , 331 , 187 )
naruto28 = analyzed_img( "GameplayAssets\\naruto\\naruto(28).png " , 162 , 339 , 331 , 187 )
naruto29 = analyzed_img( "GameplayAssets\\naruto\\naruto(29).png " , 162 , 339 , 331 , 187 )
naruto30 = analyzed_img( "GameplayAssets\\naruto\\naruto(30).png " , 194 , 338 , 234 , 191 )
naruto31 = analyzed_img( "GameplayAssets\\naruto\\naruto(31).png " , 194 , 338 , 234 , 191 )
naruto32 = analyzed_img( "GameplayAssets\\naruto\\naruto(32).png " , 194 , 338 , 234 , 191 )
naruto33 = analyzed_img( "GameplayAssets\\naruto\\naruto(33).png " , 194 , 338 , 234 , 191 )
naruto34 = analyzed_img( "GameplayAssets\\naruto\\naruto(34).png " , 194 , 338 , 234 , 191 )
naruto35 = analyzed_img( "GameplayAssets\\naruto\\naruto(35).png " , 165 , 337 , 326 , 191 )
naruto36 = analyzed_img( "GameplayAssets\\naruto\\naruto(36).png " , 165 , 337 , 326 , 191 )
naruto37 = analyzed_img( "GameplayAssets\\naruto\\naruto(37).png " , 165 , 337 , 326 , 191 )
naruto38 = analyzed_img( "GameplayAssets\\naruto\\naruto(38).png " , 165 , 337 , 326 , 191 )
naruto39 = analyzed_img( "GameplayAssets\\naruto\\naruto(39).png " , 278 , 310 , 112 , 222 )
naruto40 = analyzed_img( "GameplayAssets\\naruto\\naruto(40).png " , 278 , 310 , 112 , 222 )
naruto41 = analyzed_img( "GameplayAssets\\naruto\\naruto(41).png " , 278 , 310 , 112 , 222 )
naruto42 = analyzed_img( "GameplayAssets\\naruto\\naruto(42).png " , 289 , 314 , 112 , 221 )
naruto43 = analyzed_img( "GameplayAssets\\naruto\\naruto(43).png " , 289 , 314 , 112 , 221 )
naruto44 = analyzed_img( "GameplayAssets\\naruto\\naruto(44).png " , 265 , 332 , 106 , 194 )
naruto45 = analyzed_img( "GameplayAssets\\naruto\\naruto(45).png " , 265 , 332 , 106 , 194 )
naruto46 = analyzed_img( "GameplayAssets\\naruto\\naruto(46).png " , 272 , 385 , 94 , 135 )
naruto47 = analyzed_img( "GameplayAssets\\naruto\\naruto(47).png " , 276 , 371 , 106 , 154 )
naruto48 = analyzed_img( "GameplayAssets\\naruto\\naruto(48).png " , 276 , 371 , 106 , 154 )
naruto49 = analyzed_img( "GameplayAssets\\naruto\\naruto(49).png " , 276 , 371 , 106 , 154 )
naruto50 = analyzed_img( "GameplayAssets\\naruto\\naruto(50).png " , 275 , 350 , 95 , 164 )
naruto51 = analyzed_img( "GameplayAssets\\naruto\\naruto(51).png " , 284 , 315 , 90 , 202 )
naruto52 = analyzed_img( "GameplayAssets\\naruto\\naruto(52).png " , 260 , 410 , 129 , 121 )
naruto53 = analyzed_img( "GameplayAssets\\naruto\\naruto(53).png " , 263 , 326 , 121 , 195 )
naruto54 = analyzed_img( "GameplayAssets\\naruto\\naruto(54).png " , 263 , 326 , 121 , 195 )
naruto55 = analyzed_img( "GameplayAssets\\naruto\\naruto(55).png " , 263 , 326 , 121 , 195 )
naruto56 = analyzed_img( "GameplayAssets\\naruto\\naruto(56).png " , 263 , 326 , 121 , 195 )
naruto57 = analyzed_img( "GameplayAssets\\naruto\\naruto(57).png " , 260 , 432 , 132 , 99 )
naruto58 = analyzed_img( "GameplayAssets\\naruto\\naruto(58).png " , 268 , 337 , 115 , 192 )
naruto59 = analyzed_img( "GameplayAssets\\naruto\\naruto(59).png " , 267 , 309 , 120 , 215 )
naruto60 = analyzed_img( "GameplayAssets\\naruto\\naruto(60).png " , 267 , 309 , 120 , 215 )
naruto61 = analyzed_img( "GameplayAssets\\naruto\\naruto(61).png " , 267 , 309 , 120 , 215 )
naruto62 = analyzed_img( "GameplayAssets\\naruto\\naruto(62).png " , 253 , 373 , 159 , 150 )
naruto63 = analyzed_img( "GameplayAssets\\naruto\\naruto(63).png " , 253 , 373 , 159 , 150 )
naruto64 = analyzed_img( "GameplayAssets\\naruto\\naruto(64).png " , 253 , 373 , 159 , 150 )
naruto65 = analyzed_img( "GameplayAssets\\naruto\\naruto(65).png " , 253 , 373 , 159 , 150 )
naruto66 = analyzed_img( "GameplayAssets\\naruto\\naruto(66).png " , 253 , 373 , 159 , 150 )
naruto67 = analyzed_img( "GameplayAssets\\naruto\\naruto(67).png " , 253 , 373 , 159 , 150 )
naruto68 = analyzed_img( "GameplayAssets\\naruto\\naruto(68).png " , 278 , 353 , 102 , 167 )
naruto69 = analyzed_img( "GameplayAssets\\naruto\\naruto(69).png " , 278 , 353 , 102 , 167 )
naruto70 = analyzed_img( "GameplayAssets\\naruto\\naruto(70).png " , 278 , 353 , 102 , 167 )
naruto71 = analyzed_img( "GameplayAssets\\naruto\\naruto(71).png " , 259 , 353 , 90 , 172 )
naruto72 = analyzed_img( "GameplayAssets\\naruto\\naruto(72).png " , 249 , 429 , 128 , 93 )
naruto73 = analyzed_img( "GameplayAssets\\naruto\\naruto(73).png " , 239 , 464 , 176 , 102 )
naruto74 = analyzed_img( "GameplayAssets\\naruto\\naruto(74).png " , 249 , 354 , 136 , 170 )
naruto75 = analyzed_img( "GameplayAssets\\naruto\\naruto(75).png " , 194 , 338 , 234 , 191 )
naruto76 = analyzed_img( "GameplayAssets\\naruto\\naruto(76).png " , 194 , 338 , 234 , 191 )
naruto77 = analyzed_img( "GameplayAssets\\naruto\\naruto(77).png " , 194 , 338 , 234 , 191 )
naruto78 = analyzed_img( "GameplayAssets\\naruto\\naruto(35).png " , 165 , 337 , 326 , 191 )
naruto79 = analyzed_img( "GameplayAssets\\naruto\\naruto(79).png " , 165 , 337 , 326 , 191 )
naruto80 = analyzed_img( "GameplayAssets\\naruto\\naruto(80).png " , 165 , 337 , 326 , 191 )
naruto81 = analyzed_img( "GameplayAssets\\naruto\\naruto(81).png " , 165 , 337 , 326 , 191 )
naruto82 = analyzed_img( "GameplayAssets\\naruto\\naruto(82).png " , 289 , 314 , 112 , 221 )
naruto89 = analyzed_img("GameplayAssets\\naruto\\naruto(89).png" , 281 , 343 , 109 , 175 )
naruto90 = analyzed_img("GameplayAssets\\naruto\\naruto(90).png" , 281 , 343 , 109 , 175 )
naruto91 = analyzed_img("GameplayAssets\\naruto\\naruto(91).png" , 281 , 343 , 109 , 175 )
naruto92 = analyzed_img("GameplayAssets\\naruto\\naruto(92).png" , 281 , 343 , 109 , 175 )
naruto93 = analyzed_img("GameplayAssets\\naruto\\naruto(93).png" , 281 , 343 , 109 , 175 )
naruto94 = analyzed_img("GameplayAssets\\naruto\\naruto(94).png" , 281 , 343 , 109 , 175 )

shuriken = analyzed_img("GameplayAssets\\naruto\\shuriken.png" , 447 , 406 , 75 , 37 )

rasenshuriken1 = analyzed_img( "GameplayAssets\\naruto\\rasenshuriken(1).png " , 363 , 351 , 320 , 135 )
rasenshuriken2 = analyzed_img( "GameplayAssets\\naruto\\rasenshuriken(2).png " , 363 , 351 , 320 , 135 )
rasenshuriken3 = analyzed_img( "GameplayAssets\\naruto\\rasenshuriken(3).png " , 363 , 351 , 320 , 135 )
rasenshuriken4 = analyzed_img( "GameplayAssets\\naruto\\rasenshuriken(4).png " , 363 , 351 , 320 , 135 )
rasenshuriken5 = analyzed_img( "GameplayAssets\\naruto\\rasenshuriken(5).png " , 363 , 351 , 320 , 135 )
rasenshuriken6 = analyzed_img( "GameplayAssets\\naruto\\rasenshuriken(6).png " , 363 , 351 , 320 , 135 )

explosion_stage_1_1 = analyzed_img( "GameplayAssets\\naruto\\explosion_stage_1(1).png " , 289 , 397 , 88 , 72 )
explosion_stage_1_2 = analyzed_img( "GameplayAssets\\naruto\\explosion_stage_1(2).png " , 264 , 359 , 130 , 110 )
explosion_stage_1_3 = analyzed_img( "GameplayAssets\\naruto\\explosion_stage_1(3).png " , 237 , 315 , 177 , 152 )
explosion_stage_1_4 = analyzed_img( "GameplayAssets\\naruto\\explosion_stage_1(4).png " , 176 , 214 , 303 , 257 )

explosion_stage_2_1 = analyzed_img( "GameplayAssets\\naruto\\explosion_stage_2(1).png " , 90 , 170 , 484 , 300 )
explosion_stage_2_2 = analyzed_img( "GameplayAssets\\naruto\\explosion_stage_2(2).png " , 90 , 170 , 484 , 300 )
explosion_stage_2_3 = analyzed_img( "GameplayAssets\\naruto\\explosion_stage_2(3).png " , 90 , 170 , 484 , 300 )

explosion_stage_3_1 = analyzed_img( "GameplayAssets\\naruto\\explosion_stage_3(1).png " , 77 , 111 , 538 , 361 )
explosion_stage_3_2 = analyzed_img( "GameplayAssets\\naruto\\explosion_stage_3(2).png " , 77 , 111 , 538 , 361 )

breaking_ground1 = analyzed_img("GameplayAssets\\naruto\\breaking_ground(1).png" , 38 , 357 , 629 , 135 )
breaking_ground2 = analyzed_img("GameplayAssets\\naruto\\breaking_ground(2).png" , 5 , 230 , 685 , 256 )
breaking_ground3 = analyzed_img("GameplayAssets\\naruto\\breaking_ground(3).png" , 9 , 120 , 645 , 367 )

shuriken_explosion = analyzed_img("GameplayAssets\\naruto\\shuriken_explosion.png ", 195 , 307 , 184 , 184 )

health = na_health
attack_damage = na_attack_damage

class getting_hit_object():
    def __init__(self, object):
        self.object = object
        self.clock = timing_clock(0.1, object.gameplay)
        self.clock.start()

class rasenshuriken():
    def __init__(self, naruto) :
        self.naruto = naruto
        self.pre_status = None
        self.status  = True
        self.imgbox = pygame.Rect(0,0,0,0)
        copy(self.imgbox, self.naruto.imgbox)
        self.box = rasenshuriken1.imgbox_to_hitbox(self.imgbox)
        self.gameplay = naruto.gameplay
        self.side = naruto.side
        
        self.speed = 15.0 # 5/100 map per second 
        self.x_limit = (self.naruto.box.centerx + (screen.screen.get_width() / 4.0) * self.side ) / screen.screen.get_width()
        self.lasting_time = ( self.x_limit * screen.screen.get_width() - self.box.centerx ) * self.side / (self.speed * screen.screen.get_rect().width / 100) 
        self.damage = 5.0
        self.damaged_list = []
        self.effectted_list = []

        self.direct = True
        self.direct2 = True

        self.moving_animation = animation_player([rasenshuriken1, rasenshuriken2, rasenshuriken3, rasenshuriken4, rasenshuriken5, rasenshuriken6],self.side, 0.1, self.imgbox,self.gameplay)
        self.explosion_animation1 = one_time_animation_player([explosion_stage_1_1, explosion_stage_1_2, explosion_stage_1_3, explosion_stage_1_4],self.side,0.33,self.imgbox,self.gameplay)
        self.explosion_animation2 = one_time_animation_player([explosion_stage_2_1, explosion_stage_2_2, explosion_stage_2_1, explosion_stage_2_2, explosion_stage_2_1, explosion_stage_2_2, explosion_stage_2_1, explosion_stage_2_2, explosion_stage_2_1, explosion_stage_2_2, explosion_stage_2_1, explosion_stage_2_2, explosion_stage_2_1, explosion_stage_2_2, explosion_stage_2_1, explosion_stage_2_2, explosion_stage_2_1, explosion_stage_2_2, explosion_stage_3_1, explosion_stage_3_2],self.side,1.96,self.imgbox,self.gameplay)
        self.ground_animation = one_time_animation_player([breaking_ground1, breaking_ground2, breaking_ground3], self.side, 0.32, self.imgbox, self.gameplay)

        self.switcher1 = N_time_switch(1)

        self.gameplay.side0.append(self)

    def resize(self):
        a = float(screen.screen.get_width()) / self.gameplay.screen[0]
        b = float(screen.screen.get_height()) /  self.gameplay.screen[1]
        tmp = pygame.Rect(self.imgbox.left * a, self.imgbox.top * b, self.imgbox.width * a, self.imgbox.height * b)
        copy(self.imgbox, tmp)
        self.operation()

    def move(self):
        if self.box.right < self.gameplay.nexus2.box.left and self.box.left > self.gameplay.nexus1.box.right:
            self.imgbox.centerx += (self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  * self.side
        copy(self.box, self.moving_animation.play())

    def explosive(self):
        if self.switcher1.operation():
            if self.side == 1:
                copy(self.imgbox,shuriken_explosion.hitbox_to_imgbox(self.imgbox))
            else:
                copy(self.imgbox,shuriken_explosion.reverse.hitbox_to_imgbox(self.imgbox))
        if self.direct :
            copy(self.box, self.explosion_animation1.play())
            if self.explosion_animation1.status == False:
                self.direct = False
        else:
            copy(self.box , self.explosion_animation2.play())
            self.ground_animation.play()
            if self.explosion_animation2.status == False:
                self.remove()
                    

    def strike(self):    
        for enemy_object in self.gameplay.side( - self.side):
            if collide_checker(self, enemy_object):
                if not list_find_special(self.damaged_list, enemy_object) :
                    self.damaged_list.append(getting_hit_object(enemy_object))
                    enemy_object.health -= self.damage


        for damaged_object in self.damaged_list:
            if damaged_object.clock.Return == False:
                self.damaged_list.remove(damaged_object)



    def remove(self):
        self.moving_animation.remove()
        self.explosion_animation1.remove()
        self.explosion_animation2.remove()
        self.gameplay.side0.remove(self)
                    


    def operation(self):
        self.strike()
        self.lasting_time -= (self.gameplay.curr_time - self.gameplay.pre_curr_time)
        if self.direct2:
            self.move()
            checker = fake_object_class(self)
            checker.box .width = checker.box.width / 2
            for enemy_object in self.gameplay.side( - self.side):
                if collide_checker(checker, enemy_object):
                    if not enemy_object.status == - 1:
                        if list_find(self.effectted_list, enemy_object) == -1 :
                            ispass = False
                            for effect in enemy_object.effect_list:
                                if effect.__class__ == knock_back:
                                    ispass = True
                                    break
                            if not ispass:
                                add_effect(enemy_object, knock_back(enemy_object,self.lasting_time, self.speed))
                                self.effectted_list.append(enemy_object)
            if self.lasting_time < 0:
                self.direct2 = False
        else:
            self.explosive()


class cloneclass():
    def __init__(self, naruto):
        naruto.clone_list.append(self)
        self.naruto = naruto
        self.pre_status = None
        self.status  = None
        self.box = pygame.Rect(0,0,0,0)
        self.imgbox = pygame.Rect(0,0,0,0)
        self.gameplay = naruto.gameplay
        self.side = naruto.side
        self.name = "Clone"
        self.level = naruto.level

        self.speed = 5.0 # 5/100 map per second 
        self.attack_scope = naruto.attack_scope 
        self.attack_speed = naruto.attack_speed
        self.attack_damage_orginal = naruto.attack_damage_orginal
        self.attack_damage = naruto.attack_damage
        self.health_max = 70.0
        self.health = self.health_max 
        self.mana_max = 100.0
        self.mana = 0

        self.effect_list = []

        self.alive = None
        self.get_hit = False
        self.ischeck = True
        self.iscollide_check = True        
        self.collide = None
        self.special_status = False

        self.animation_player = None
        self.spawn_animation = one_time_animation_player([naruto53, naruto54, naruto55, naruto56], self.side, 0.36, self.imgbox, self.gameplay)
        self.moving_animation = animation_player([naruto62,naruto63,naruto64,naruto65,naruto66,naruto67], self.side, 0.6, self.imgbox , self.gameplay)
        self.walking_animation = animation_player([naruto62,naruto63,naruto64,naruto65,naruto66,naruto67], self.side, 0.6, self.imgbox , self.gameplay)
        self.attacking_animation = one_time_animation_player([naruto1,naruto2,naruto3,naruto4,naruto5,naruto6,naruto7,naruto8,naruto9,naruto10,naruto11,naruto12,naruto13,naruto14,naruto15,naruto16,naruto17,naruto18,naruto19], self.side, 1.26 , self.imgbox, self.gameplay)
        self.standstill_animation = one_time_animation_player([naruto68, naruto69, naruto70],self.side, 0.58, self.imgbox, self.gameplay)  
        self.dying_animation = one_time_animation_player([naruto57, naruto58, naruto59, naruto60, naruto61], self.side, 0.56, self.imgbox, self.gameplay)
        self.knock_back_animation = animation_player([naruto71], self.side, 1, self.imgbox, self.gameplay)
        self.flying_animation = animation_player([naruto74], self.side, 1, self.imgbox, self.gameplay)
        self.falling_animation = animation_player([naruto72], self.side, 1, self.imgbox, self.gameplay)

        self.switcher1 = N_time_switch(1)
        self.switcher2 = N_time_switch(1)
        self.switcher3 = N_time_switch(1)
        self.switcher4 = N_time_switch(1)
        self.switcher5 = N_time_switch(1)

        self.attack_coundowner = timing_clock(1 / self.attack_speed, self.gameplay)

    def status_update(self):
        self.level = self.naruto.level
        self.health_max =  self.naruto.health_max
        self.attack_damage = self.naruto.attack_damage

        self.collide = None 
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

    def resize(self):
        a = float(screen.screen.get_width()) / self.gameplay.screen[0]
        b = float(screen.screen.get_height()) /  self.gameplay.screen[1]
        tmp = pygame.Rect(self.imgbox.left * a, self.imgbox.top * b, self.imgbox.width * a, self.imgbox.height * b)
        copy(self.imgbox, tmp)
        self.operation()

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
        if self.mana >= self.mana_max:
            self.mana = 0

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
                                self.Attack = 1
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
                                self.Attack = 1
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
                                self.status = 5
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
                    self.status = 2            


        if self.status > 0:
            if not self.pre_status == None:
                if self.pre_status > 0:
                    if not self.pre_status == self.status:            
                        if self.pre_status == 1:
                            self.attack_reset()
                        elif self.pre_status == 2:
                            self.standsill_reset()


    def Geting_hit(self):
        self.get_hit = False
        self.health -= self.get_damage 
        self.get_damage = 0
        if not self.special_status:
            self.mana += 10


    def dying(self):
        if self.switcher4.operation():
            self.spawn_animation.remove()
            self.moving_animation.remove()
            self.attacking_animation.remove()
            self.standstill_animation.remove()      
            self.falling_animation.remove()
            self.flying_animation.remove()
            self.knock_back_animation.remove()

            self.gameplay.side(self.side).remove(self)
            self.naruto.clone_list.remove(self)
            self.side = 0
            self.gameplay.side0.append(self)
            if self.animation_player == None:
                self.animation_player = self.standstill_animation

            self.img = self.animation_player.img_lib[self.animation_player.clock.Return - 1]
        
        self.dying_animation.play()
        if self.dying_animation.clock.Return < 3:
            self.gameplay.bg.blit(pygame.transform.scale(self.img.img, (self.imgbox.width, self.imgbox.height)), self.imgbox)

        if self.dying_animation.status == False:
            self.dying_animation.remove()
            self.gameplay.side0.remove(self)

    
    def attack(self):
        if self.switcher5.operation():
            self.attack_coundowner.reset()
            self.attack_coundowner.start()
            
        self.animation_player = self.attacking_animation
        if self.attacking_animation.clock.Return == 5 or self.attacking_animation.clock.Return == 10:
            if self.switcher1.operation():
                for object in self.gameplay.side(- self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                self.mana += 10 
                                object.get_hit = True
                                object.get_damage = self.attack_damage
        elif self.attacking_animation.clock.Return == 17:
            if self.switcher1.operation():
                for object in self.gameplay.side(- self.side) :
                    if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2 :
                        if (object.box.centerx - self.box.centerx) * self.side >= 0:
                            if same_line_checker(self, object):
                                self.mana += 10 
                                object.get_hit = True
                                object.get_damage = self.attack_damage

        elif self.attacking_animation.clock.Return == 4 or self.attacking_animation.clock.Return == 9 or self.attacking_animation.clock.Return == 16:
            self.switcher1.reset()



    def attack_reset(self):
        self.attacking_animation.reset() 
        self.switcher5.reset()

    def operation(self):
        if self.alive == None:
            self.spawn_animation.play()
            if self.spawn_animation.status == False:
                self.alive = True
                self.index = len(self.gameplay.side(self.side))
                self.gameplay.side0.remove(self)
                self.gameplay.side(self.side).append(self)

        elif self.alive == True:

            def play(effect):
                effect.play()
            list_browser(self.effect_list, play)        

            self.check_collide()
            self.check_forward()
            
            if self.status == 3:
                self.move()

            if self.status == 5:
                self.walk()

            elif self.status == 1:
                self.attack()

            elif self.status == 2 :
                self.standstill()


            if self.get_hit :
                self.Geting_hit()

            if self.health <= 0:
                self.alive = False
                

            self.display()
            self.status_update()

            # pygame.draw.rect(screen.screen,White,self.box,1)
            # pygame.draw.rect(screen.screen,White,self.imgbox,1)
        elif self.alive == False:
            if (not  self.spawn_animation.status == False) or self.spawn_animation.status == None :
                self.gameplay.side0.remove(self)
                self.animation_player = self.standstill_animation
                self.gameplay.side(self.side).append(self)
                self.animation_player = self.standstill_animation
            self.dying()


class shuriken_class():
    def __init__(self,naruto):
        self.naruto = naruto
        self.gameplay = self.naruto.gameplay
        self.side = self.naruto.side

        self.imgbox = pygame.Rect(self.naruto.imgbox.left,self.naruto.imgbox.top,self.naruto.imgbox.width,self.naruto.imgbox.height)
        if self.side == 1:
            self.box = shuriken.imgbox_to_hitbox(self.imgbox)
            self.img = shuriken
        elif self.side == -1:
            self.box = reverse(shuriken).imgbox_to_hitbox(self.imgbox)
            self.img = reverse(shuriken)


        self.speed = 30.0  # 10/100 map per second
        self.damage = self.naruto.attack_damage

        self.x_limit = self.naruto.box.centerx + (self.naruto.attack_scope2 * 1.5 + self.naruto.box.width / 2) * self.side
        self.damaged_object = []


    def resize(self):
        a = float(screen.screen.get_width()) / self.gameplay.screen[0]
        b = float(screen.screen.get_height()) /  self.gameplay.screen[1]
        tmp = pygame.Rect(self.imgbox.left * a, self.imgbox.top * b, self.imgbox.width * a, self.imgbox.height * b)
        copy(self.imgbox, tmp)
        self.operation()


    def move(self):
        self.imgbox.centerx += (self.speed * screen.screen.get_rect().width / 100) * (self.gameplay.curr_time - self.gameplay.pre_curr_time)  * self.side

    def remove(self):
        self.naruto.shuriken_list.remove(self)

    def collide_check(self):
        for enemy_object in self.naruto.gameplay.side( - self.side):
            if collide_checker(self,enemy_object):
                if list_find(self.damaged_object,enemy_object) == -1:
                    self.damaged_object.append(enemy_object)
                    enemy_object.get_damage = self.damage
                    enemy_object.get_hit = True
                    return True
        return False
        


    def limit_check(self):
        if (self.x_limit - self.box.centerx) * self.side <= self.box.width / 2 :
            return True
        
        return False

    def operation(self):
        screen.screen.blit(pygame.transform.smoothscale(self.img.img,(self.imgbox.width,self.imgbox.height)),self.imgbox)
        copy(self.box, self.img.imgbox_to_hitbox(self.imgbox))
        self.move()
        if self.limit_check():
            self.remove()
        else:
            if self.collide_check():
                self.naruto.mana += 10
                self.remove()
                



class narutoclass():
    def __init__(self,side,gameplay):
        self.pre_status = None
        self.status  = None
        self.box = pygame.Rect(0,0,0,0)
        self.imgbox = pygame.Rect(0,0,0,0)
        self.gameplay = gameplay
        if side == 1 :
            self.side = 1
            self.level = self.gameplay.character_level1[5]
        elif side == 2:
            self.side = -1   
            self.level = self.gameplay.character_level2[5]
        
        self.speed = 5.0 # 5/100 map per second 
        self.attack_scope = 1 * self.gameplay.box_size[0] # 4/15 map width
        self.attack_scope2 = 5 * self.gameplay.box_size[0] # 4/15 map width
        self.attack_speed = 1/1 # attack(s) pers second
        self.attack_damage = attack_damage[self.level - 1]
        self.attack_damage_orginal = self.attack_damage
        self.health_max = health[self.level - 1]
        self.health = self.health_max 
        self.mana_max = 100.0
        self.mana = 50.0

        self.effect_list = []
        self.clone_list = []
        self.shuriken_list = []

        self.alive = True
        self.get_hit = False
        self.ischeck = True
        self.iscollide_check = True        
        self.collide = None
        self.special_status = False

        self.moving_animation = animation_player([naruto62,naruto63,naruto64,naruto65,naruto66,naruto67], self.side, 0.6, self.imgbox , self.gameplay)
        self.walking_animation = animation_player([naruto68, naruto69, naruto70],self.side, 0.58, self.imgbox, self.gameplay)  
        self.attacking_animation = one_time_animation_player([naruto1,naruto2,naruto3,naruto4,naruto5,naruto6,naruto7,naruto8,naruto9,naruto10,naruto11,naruto12,naruto13,naruto14,naruto15,naruto16,naruto17,naruto18,naruto19], self.side, 1.26 , self.imgbox, self.gameplay)
        self.attacking_animation2 = one_time_animation_player([naruto89, naruto90, naruto91, naruto92, naruto93, naruto94,], self.side, 0.35 , self.imgbox, self.gameplay)

        tmp_lib = []
        for i in [naruto19, naruto20, naruto21, naruto22, naruto23, naruto24, naruto25, naruto26, naruto27]:
            tmp_lib.append(i)
        for i in [naruto28, naruto29, naruto30, naruto31, naruto32, naruto33, naruto34]:
            tmp_lib.append(i)
        for j in range(1,8):
            for i in [naruto75, naruto76, naruto77]:
                    tmp_lib.append(i)
        for i in [naruto35, naruto78, naruto79, naruto80, naruto81]:
            tmp_lib.append(i)
        for i in [naruto36, naruto37, naruto38, naruto39, naruto40, naruto41, naruto42]:
            tmp_lib.append(i)
        for j in range(1,8):
            for i in naruto43, naruto82, :
                    tmp_lib.append(i)
        for i in naruto44, naruto45, naruto46, naruto47, naruto48, naruto49, naruto50, :
            tmp_lib.append(i)
        
        self.special_skill_animation = one_time_animation_player(tmp_lib, self.side, 5.52, self.imgbox, self.gameplay)
        self.special_skill_animation2 = one_time_animation_player([naruto19,naruto20,naruto21,naruto22,naruto22,naruto22,naruto22,naruto22,naruto22,naruto22], self.side, 0.8, self.imgbox, self.gameplay)
        self.standstill_animation = one_time_animation_player([naruto68, naruto69, naruto70],self.side, 0.58, self.imgbox, self.gameplay)  
        self.dying_animation = one_time_animation_player([naruto71,naruto73,naruto74], self.side, 0.3, self.imgbox, self.gameplay)
        self.knock_back_animation = animation_player([naruto71], self.side, 1, self.imgbox, self.gameplay)
        self.flying_animation = animation_player([naruto74], self.side, 1, self.imgbox, self.gameplay)
        self.falling_animation = animation_player([naruto72], self.side, 1, self.imgbox, self.gameplay)

        self.switcher1 = N_time_switch(1)
        self.switcher2 = N_time_switch(1)
        self.switcher3 = N_time_switch(1)
        self.switcher4 = N_time_switch(1)
        self.switcher5 = N_time_switch(1)

        self.switcher_list = []
        for i in range(0,8):
            self.switcher_list.append(N_time_switch(1))

        self.attack_coundowner = timing_clock(1 / self.attack_speed, self.gameplay)
        self.clock = N_ValueReturn_repeated_clock(0.1 , 5 , self.gameplay)
        self.special_skill_countdowner = timing_clock(5.0 , self.gameplay)

    def status_update(self):
        if not self.special_status:
            if not self.level == self.gameplay.character_level(self.side, 5):
                self.level = self.gameplay.character_level(self.side, 5)
                self.attack_damage = attack_damage[self.level - 1]
                self.health_max = health[self.level - 1]
    
        self.collide = None 
        self.pre_status = self.status

        if self.pre_status == 1:
            if self.Attack == 1:
                if self.attacking_animation.status == True:
                    self.ischeck = False
                elif self.attacking_animation.status == False:
                    self.ischeck = True
                    self.attack_reset()
            elif self.Attack == 2:
                if self.attacking_animation2.status == True:
                    self.ischeck = False
                elif self.attacking_animation2.status == False:
                    self.ischeck = True
                    self.attack_reset()

        elif self.pre_status == 2:
            if self.standstill_animation.status == True:
                self.ischeck = False
            elif self.standstill_animation.status == False:
                self.ischeck = True           
                self.standsill_reset()
        elif self.pre_status == 4:
            if self.level == 1:
                if self.special_skill_animation2.status == True:
                    self.ischeck = False
                elif self.special_skill_animation2.status == False:
                    self.ischeck = True

            elif self.level == 2:
                if self.special_skill_animation.status == True:
                    self.ischeck = False
                elif self.special_skill_animation.status == False:
                    self.ischeck = True
                    self.special_status = False
                    self.special_skill_reset()




    def resize(self):
        a = float(screen.screen.get_width()) / self.gameplay.screen[0]
        b = float(screen.screen.get_height()) /  self.gameplay.screen[1]
        tmp = pygame.Rect(self.imgbox.left * a, self.imgbox.top * b, self.imgbox.width * a, self.imgbox.height * b)
        copy(self.imgbox, tmp)
        self.operation()

 
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
        if self.mana >= self.mana_max:
            self.mana = 0
            self.special_status = True
            self.status = 4
            if self.level == 1:
                add_effect(self, iron_body(self, self.special_skill_animation2.loop_time))
            elif self.level == 2:
                add_effect(self, iron_body(self, self.special_skill_animation.loop_time))
            ispass = True
        else:
            ispass = False

        if not ispass:
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
                                    self.Attack = 1
                                    flag = True
                                    ispass = True
                                    break
                        elif abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope2 + (self.box.width + object.box.width) / 2 :
                            if (object.box.centerx - self.box.centerx) * self.side > 0:
                                if same_line_checker(self, object):
                                    self.status = 1
                                    self.Attack = 2
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
                                    self.Attack = 1
                                    flag = True
                                    ispass = True
                                    break
                        elif abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope2 + (self.box.width + object.box.width) / 2 :
                            if (object.box.centerx - self.box.centerx) * self.side > 0:
                                if same_line_checker(self, object):
                                    self.status = 1
                                    self.Attack = 2
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
                        if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 2 + (self.speed * screen.screen.get_rect().width / 100) * 0.5  + (self.box.width + object.box.width) / 2:
                            if (object.box.centerx - self.box.centerx) * self.side >= 0:
                                if same_line_checker(self, object):
                                    self.status = 5
                                    ispass = True
                                    break

                        elif abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope2 + (self.speed * screen.screen.get_rect().width / 100) * 0.5 + (self.box.width + object.box.width) / 2 :
                            if (object.box.centerx - self.box.centerx) * self.side > 0:
                                if same_line_checker(self, object):
                                    self.status = 5
                                    ispass = True
                                    break

                    if not ispass:
                        for object in self.gameplay.side(self.side) + self.gameplay.side4 :
                            if abs(object.box.centerx  - self.box.centerx ) <= self.gameplay.box_size[0] / 3 + (self.speed * screen.screen.get_rect().width / 100) * 0.5  + (self.box.width + object.box.width) / 2 :
                                if (object.box.centerx - self.box.centerx) * self.side >= 0:
                                    if same_line_checker(self, object):
                                        if not (self == object):
                                            if not  object.status == 3:
                                                self.status = 5
                                                break         
                    
                
                if self.status == 1 :
                    if self.attack_coundowner.Return == True:
                        self.status = 2            


        if self.status > 0:
            if not self.pre_status == None:
                if self.pre_status > 0:
                    if not self.pre_status == self.status:            
                        if self.pre_status == 1:
                            self.attack_reset()
                        elif self.pre_status == 2:
                            self.standsill_reset()


    def Geting_hit(self):
        self.get_hit = False
        self.health -= self.get_damage 
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
        if self.Attack == 1:
            self.animation_player = self.attacking_animation
            if self.attacking_animation.clock.Return == 3 or self.attacking_animation.clock.Return == 8:
                if self.switcher1.operation():
                    for object in self.gameplay.side(- self.side) :
                        if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2 :
                            if (object.box.centerx - self.box.centerx) * self.side >= 0:
                                if same_line_checker(self, object):
                                    if not self.special_status:
                                        self.mana += 30
                                    object.get_hit = True
                                    object.get_damage = self.attack_damage
            elif self.attacking_animation.clock.Return == 15:
                if self.switcher1.operation():
                    for object in self.gameplay.side(- self.side) :
                        if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2 :
                            if (object.box.centerx - self.box.centerx) * self.side >= 0:
                                if same_line_checker(self, object):
                                    if not self.special_status:
                                        self.mana += 30                                    
                                    add_effect(object, flying(object, 5.0))
                                    object.get_hit = True
                                    object.get_damage = self.attack_damage

            elif self.attacking_animation.clock.Return == 2 or self.attacking_animation.clock.Return == 7 or self.attacking_animation.clock.Return == 14:
                self.switcher1.reset()
        
        elif self.Attack == 2:
            self.animation_player = self.attacking_animation2
            if self.attacking_animation2.clock.Return == 4:
                if self.switcher1.operation():
                    self.shuriken_list.append(shuriken_class(self))  

            elif self.attacking_animation2.clock.Return == 3:
                self.switcher1.reset()



    def attack_reset(self):
        self.attacking_animation.reset() 
        self.attacking_animation2.reset() 
        self.switcher5.reset()


    def kagebusino_jutsu(self, position): 
        tmp = cloneclass(self)
        if self.side == 1:
            tmp.index = self.gameplay.side1_heros
            self.gameplay.side1_heros += 1
        else:
            tmp.index = self.gameplay.side2_heros
            self.gameplay.side2_heros += 1

        self.gameplay.side0.append(tmp)
        copy(tmp.imgbox, self.imgbox)
        tmp.imgbox.centerx += position * self.gameplay.box_size[0]
        tmp.box = naruto18.imgbox_to_hitbox(tmp.imgbox)
        if tmp.box.right < tmp.gameplay.nexus2.box.left and tmp.box.left > tmp.gameplay.nexus1.box.right:
            pass
        else:
            tmp.imgbox.centerx -= position * self.gameplay.box_size[0]



    def special_skill(self):
        if self.level == 1:
            self.animation_player = self.special_skill_animation2
            if self.special_skill_animation2.clock.Return == 3 :
                self.switcher1.reset()

            if self.special_skill_animation2.clock.Return == 4 :
                if self.switcher1.operation():
                    self.clock.start()
                    self.switcher1.reset()
                    self.special_skill_countdowner.start()


            elif self.special_skill_animation2.clock.Return > 4 : 
                if self.switcher_list[self.clock.Return - 1].operation():
                    self.kagebusino_jutsu(self.clock.Return * self.side  * 2)



        elif self.level == 2:
            self.animation_player = self.special_skill_animation
            if self.special_skill_animation.clock.Return == 3 :
                self.switcher1.reset()

            if self.special_skill_animation.clock.Return == 4 :
                if self.switcher1.operation():
                    self.clock.start()
                    self.switcher1.reset()


            elif self.special_skill_animation.clock.Return > 4 : 
                if self.switcher_list[self.clock.Return - 1].operation():
                    self.kagebusino_jutsu(self.clock.Return * self.side  * 2)

            if self.special_skill_animation.clock.Return == 65 :
                self.switcher2.reset()

            elif self.special_skill_animation.clock.Return == 66 :
                if self.switcher2.operation():
                    for clone in self.clone_list:
                        clone.alive = False

            elif self.special_skill_animation.clock.Return == 67 :
                self.switcher2.reset()

            elif self.special_skill_animation.clock.Return == 68 :
                if self.switcher2.operation():
                    tmp = rasenshuriken(self)
                    for object in self.gameplay.side(- self.side) :
                        if abs(object.box.centerx  - self.box.centerx ) <= self.attack_scope + (self.box.width + object.box.width) / 2 :
                            if (object.box.centerx - self.box.centerx) * self.side >= 0:
                                if same_line_checker(self, object):
                                    add_effect(object, knock_back(object,tmp.lasting_time, tmp.speed))




    def special_skill_reset(self):
        self.special_skill_animation.reset() 
        self.special_skill_animation2.reset() 

        self.switcher1.reset()
        self.switcher2.reset()
        for switch in self.switcher_list:
            switch.reset()
        self.special_skill_countdowner.reset()

        for clone in self.clone_list:
            clone.alive = False


    def operation(self):
        if self.alive:
            def play(effect):
                effect.play()
            list_browser(self.effect_list, play)
            
            self.check_collide()
            self.check_forward()


            if self.status == 3:
                self.move()

            elif self.status == 5 :
                self.walk()

            elif self.status == 1:
                self.attack()

            elif self.status == 2 :
                self.standstill()


            elif self.status == 4:
                self.special_skill()

            if self.special_status and self.level == 1:
                if self.special_skill_countdowner.Return == False:
                    self.special_status = False
                    self.special_skill_reset()


            if self.get_hit :
                self.Geting_hit()

            if self.health <= 0:
                self.alive = False
                for clone in self.clone_list:
                    clone.alive = False
                if self.side == 1:
                    self.gameplay.gold_income_1 += self.gameplay.character_cost[self.__class__] * 10.0 / 100
                else:
                    self.gameplay.gold_income_2 += self.gameplay.character_cost[self.__class__] * 10.0 / 100

            
            for shuriken in self.shuriken_list:
                shuriken.operation()
                

            self.display()
            self.status_update()

            # pygame.draw.rect(screen.screen,White,self.box,1)
            # pygame.draw.rect(screen.screen,White,self.imgbox,1)
        else:
            self.dying()

