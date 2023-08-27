import pygame 
from pygame.locals import *
from color import *

class  analyzed_img():
    def __init__(self,img,a,b,c,d):
        self.img_name = img
        self.img = pygame.image.load(img)
        self.data = (a,b,c,d)
    def hitbox_to_imgbox(self,hitbox):
        (m, n) = self.img.get_size()
        (a, b, c, d ) = self.data
        x = hitbox.width * a / c
        y = hitbox.height * b / d
        rong = hitbox.width * m / c
        dai = hitbox.height * n / d

        return pygame.Rect(hitbox.left - x, hitbox.top - y,rong,dai)


    def imgbox_to_hitbox(self,imgbox):
        (m, n) = self.img.get_size()
        (a, b, c, d ) = self.data
        x = imgbox.width * a / m
        y = imgbox.height * b / n
        rong = imgbox.width * c / m
        dai = imgbox.height * d / n

        return pygame.Rect(imgbox.left + x, imgbox.top + y,rong,dai)
    
def reverse(analyzed_IMG):
    (a, b, c, d ) = analyzed_IMG.data
    tmp = analyzed_img(analyzed_IMG.img_name, analyzed_IMG.img.get_size()[0] - a - c, b, c, d)
    tmp.img = pygame.transform.flip(tmp.img, True, False)
    return tmp




sword_man1_1  = analyzed_img("GameplayAssets\\sword_man1(1).png", 77 , 153 , 163 , 464)
sword_man1_2  = analyzed_img("GameplayAssets\\sword_man1(2).png", 88 , 154 , 156 , 477)
sword_man1_3  = analyzed_img("GameplayAssets\\sword_man1(3).png", 79 , 123 , 131 , 495)
sword_man1_4  = analyzed_img("GameplayAssets\\sword_man1(4).png", 93 , 133 , 158 , 484)

sword_man2_1  = analyzed_img("GameplayAssets\\sword_man2(1).png",700 - 77 - 163, 153 , 163 , 464)   
sword_man2_2  = analyzed_img("GameplayAssets\\sword_man2(2).png",700 - 88 - 156, 154 , 156 , 477)
sword_man2_3  = analyzed_img("GameplayAssets\\sword_man2(3).png",700 - 79 - 131, 123 , 131 , 495)
sword_man2_4  = analyzed_img("GameplayAssets\\sword_man2(4).png",700 - 93 - 158, 133 , 158 , 484)


archer1_1 = analyzed_img("GameplayAssets\\archer1(1).png", 66 , 40 , 60 , 164)
archer1_2 = analyzed_img("GameplayAssets\\archer1(2).png", 67 , 40 , 58 , 170)
archer1_3 = analyzed_img("GameplayAssets\\archer1(3).png", 70 , 40 , 54 , 162)

archer2_1 = analyzed_img("GameplayAssets\\archer2(1).png", 200 - 66 - 60, 40 , 60 , 164)
archer2_2 = analyzed_img("GameplayAssets\\archer2(2).png", 200 - 67 - 58, 40 , 58 , 170)
archer2_3 = analyzed_img("GameplayAssets\\archer2(3).png", 200 - 70 - 54, 40 , 54 , 162)

archer1 = analyzed_img("GameplayAssets\\archer(1).png", 255 , 371 , 85 , 221)
archer2 = analyzed_img("GameplayAssets\\archer(2).png", 263 , 356 , 87 , 235)
archer3 = analyzed_img("GameplayAssets\\archer(3).png", 248 , 383 , 99 , 208)
archer4 = analyzed_img("GameplayAssets\\archer(4).png", 249 , 377 , 94 , 213)
archer5 = analyzed_img("GameplayAssets\\archer(5).png", 259 , 373 , 90 , 216)
archer6 = analyzed_img("GameplayAssets\\archer(6).png", 259 , 373 , 90 , 216)
archer7 = analyzed_img("GameplayAssets\\archer(7).png", 258 , 364 , 91 , 224)
archer8 = analyzed_img("GameplayAssets\\archer(8).png", 264 , 372 , 88 , 220)
archer9 = analyzed_img("GameplayAssets\\archer(9).png", 275 , 372 , 85 , 217)
archer10 = analyzed_img("GameplayAssets\\archer(10).png", 268 , 381 , 87 , 210)
archer11 = analyzed_img("GameplayAssets\\archer(11).png", 194 , 285 , 81 , 206)
archer12 = analyzed_img("GameplayAssets\\archer(12).png", 194 , 288 , 82 , 203)
archer13 = analyzed_img("GameplayAssets\\archer(13).png", 195 , 294 , 81 , 198)
archer14 = analyzed_img("GameplayAssets\\archer(14).png", 195 , 294 , 81 , 198)
archer15 = analyzed_img("GameplayAssets\\archer(15).png", 195 , 294 , 81 , 198)
archer16 = analyzed_img("GameplayAssets\\archer(16).png", 195 , 284 , 79 , 206)
archer17 = analyzed_img("GameplayAssets\\archer(17).png", 195 , 284 , 79 , 206)
archer18 = analyzed_img("GameplayAssets\\archer(18).png", 195 , 284 , 79 , 206)
archer19 = analyzed_img("GameplayAssets\\archer(19).png", 195 , 284 , 79 , 206)
archer20 = analyzed_img("GameplayAssets\\archer(20).png", 206 , 275 , 73 , 216)
archer21 = analyzed_img("GameplayAssets\\archer(21).png", 206 , 275 , 73 , 216)
archer22 = analyzed_img("GameplayAssets\\archer(22).png", 199 , 294 , 71 , 197)
archer23 = analyzed_img("GameplayAssets\\archer(23).png", 199 , 298 , 69 , 192)
archer24 = analyzed_img("GameplayAssets\\archer(24).png", 199 , 298 , 69 , 192)
archer25 = analyzed_img("GameplayAssets\\archer(25).png", 199 , 298 , 69 , 192)
archer26 = analyzed_img("GameplayAssets\\archer(26).png", 199 , 298 , 69 , 192)
archer27 = analyzed_img("GameplayAssets\\archer(27).png", 199 , 298 , 69 , 192)
archer28 = analyzed_img("GameplayAssets\\archer(28).png", 199 , 298 , 69 , 192)
archer29 = analyzed_img("GameplayAssets\\archer(29).png", 199 , 298 , 69 , 192)
archer30 = analyzed_img("GameplayAssets\\archer(30).png", 199 , 298 , 69 , 192)

arrow = analyzed_img("GameplayAssets\\arrow.png", 279 , 332 , 132 , 20)
special_arrow = analyzed_img("GameplayAssets\\special_arrow.png", 279 , 332 , 132 , 20)

arrow1 =  analyzed_img("GameplayAssets\\arrow1.png", 142 , 79 , 65 , 10)
arrow2 =  analyzed_img("GameplayAssets\\arrow2.png",200 - 142 - 65, 79 , 65 , 10)

tanker1_1 = analyzed_img("GameplayAssets\\tanker1(1).png", 107 , 68 , 187 , 390)
tanker1_2 = analyzed_img("GameplayAssets\\tanker1(2).png", 107 , 67 , 191 , 390)
tanker1_3 = analyzed_img("GameplayAssets\\tanker1(3).png", 137 , 66 , 159 , 391)
tanker1_4 = analyzed_img("GameplayAssets\\tanker1(4).png", 138 , 66 , 160 , 393)

tanker2_1 = analyzed_img("GameplayAssets\\tanker2(1).png", 451 - 107 - 187 , 68 , 187 , 390)
tanker2_2 = analyzed_img("GameplayAssets\\tanker2(2).png", 451 - 107 - 191 , 67 , 191 , 390)
tanker2_3 = analyzed_img("GameplayAssets\\tanker2(3).png", 451 - 137 - 159 , 66 , 159 , 391)
tanker2_4 = analyzed_img("GameplayAssets\\tanker2(4).png", 451 - 138 - 160 , 66 , 160 , 393)

nexus1 = analyzed_img("GameplayAssets\\nexus1.png", 111 , 328 , 517 , 582)
nexus2 = analyzed_img("GameplayAssets\\nexus2.png", 186 , 209 , 457 , 769)


wizard1 = analyzed_img("GameplayAssets\\wizard(1).png", 180 , 74 , 58 , 157)
wizard2 = analyzed_img("GameplayAssets\\wizard(2).png", 187 , 83 , 51 , 157)
wizard3 = analyzed_img("GameplayAssets\\wizard(3).png", 191 , 91 , 51 , 154)
wizard4 = analyzed_img("GameplayAssets\\wizard(4).png", 175 , 96 , 53 , 127)
wizard5 = analyzed_img("GameplayAssets\\wizard(5).png", 157 , 98 , 91 , 143)
wizard6 = analyzed_img("GameplayAssets\\wizard(6).png", 137 , 74 , 59 , 161)
wizard7 = analyzed_img("GameplayAssets\\wizard(7).png", 136 , 67 , 56 , 160)
wizard8 = analyzed_img("GameplayAssets\\wizard(8).png", 138 , 67 , 63 , 160)
wizard9 = analyzed_img("GameplayAssets\\wizard(9).png", 136 , 70 , 67 , 158)
wizard10 = analyzed_img("GameplayAssets\\wizard(10).png", 136 , 70 , 67 , 158)
wizard11 = analyzed_img("GameplayAssets\\wizard(11).png", 164 , 79 , 65 , 152)
wizard12 = analyzed_img("GameplayAssets\\wizard(12).png", 164 , 79 , 65 , 152)
wizard13 = analyzed_img("GameplayAssets\\wizard(13).png", 167 , 98 , 86 , 146)
wizard14 = analyzed_img("GameplayAssets\\wizard(14).png", 192 , 96 , 69 , 144)
wizard15 = analyzed_img("GameplayAssets\\wizard(15).png", 192 , 96 , 69 , 144)
wizard16 = analyzed_img("GameplayAssets\\wizard(16).png", 192 , 96 , 69 , 144)
wizard17 = analyzed_img("GameplayAssets\\wizard(17).png", 192 , 96 , 69 , 144)
wizard18 = analyzed_img("GameplayAssets\\wizard(18).png", 163 , 94 , 85 , 159)
wizard19 = analyzed_img("GameplayAssets\\wizard(19).png", 164 , 80 , 94 , 150)
wizard20 = analyzed_img("GameplayAssets\\wizard(20).png", 135 , 71 , 88 , 160)
wizard21 = analyzed_img("GameplayAssets\\wizard(21).png", 183 , 77 , 72 , 162)
wizard22 = analyzed_img("GameplayAssets\\wizard(22).png", 183 , 77 , 72 , 162)
wizard23 = analyzed_img("GameplayAssets\\wizard(23).png", 177 , 65 , 73 , 187)
wizard24 = analyzed_img("GameplayAssets\\wizard(24).png", 177 , 65 , 73 , 187)
wizard25 = analyzed_img("GameplayAssets\\wizard(25).png", 163 , 59 , 70 , 160)
wizard26 = analyzed_img("GameplayAssets\\wizard(26).png", 141 , 64 , 76 , 150)
wizard27 = analyzed_img("GameplayAssets\\wizard(27).png", 132 , 87 , 75 , 155)
wizard28 = analyzed_img("GameplayAssets\\wizard(28).png", 149 , 84 , 73 , 158)
wizard_to_magic_ball = analyzed_img("GameplayAssets\\wizard_to_magicball.png",   332 , 104 , 57 , 39)


magic_ball1= analyzed_img("GameplayAssets\\magic_ball(1).png", 261 , 42 , 137 , 154)
magic_ball2 = analyzed_img("GameplayAssets\\magic_ball(2).png", 261 , 42 , 137 , 154)
magic_ball3 = analyzed_img("GameplayAssets\\magic_ball(3).png", 261 , 42 , 137 , 154)
magic_ball4 = analyzed_img("GameplayAssets\\magic_ball(4).png", 261 , 42 , 137 , 154)
magic_ball5 = analyzed_img("GameplayAssets\\magic_ball(5).png", 261 , 42 , 137 , 154)
magic_ball6 = analyzed_img("GameplayAssets\\magic_ball(6).png" , 251 , 45 , 143 , 145)
magic_ball7 = analyzed_img("GameplayAssets\\magic_ball(7).png" , 294 , 85 , 105 , 86)
magic_ball8 = analyzed_img("GameplayAssets\\magic_ball(8).png" , 339 , 94 , 62 , 72)
magic_ball9 = analyzed_img("GameplayAssets\\magic_ball(9).png" , 369 , 101 , 40 , 40)

straw_doll = analyzed_img("GameplayAssets\straw_doll.png", 68 , 17 , 105 , 257)

dizzy_effect1 = analyzed_img("GameplayAssets\\dizzy_effect(1).png", 27 , 58 , 522 , 290)
dizzy_effect2 = analyzed_img("GameplayAssets\\dizzy_effect(2).png", 27 , 58 , 522 , 290)
dizzy_effect3 = analyzed_img("GameplayAssets\\dizzy_effect(3).png", 27 , 58 , 522 , 290)
dizzy_effect4 = analyzed_img("GameplayAssets\\dizzy_effect(4).png", 27 , 58 , 522 , 290)
dizzy_effect5 = analyzed_img("GameplayAssets\\dizzy_effect(5).png", 27 , 58 , 522 , 290)
dizzy_effect6 = analyzed_img("GameplayAssets\\dizzy_effect(6).png", 27 , 58 , 522 , 290)
dizzy_effect7 = analyzed_img("GameplayAssets\\dizzy_effect(7).png", 27 , 58 , 522 , 290)
dizzy_effect8 = analyzed_img("GameplayAssets\\dizzy_effect(8).png", 27 , 58 , 522 , 290)
dizzy_effect9 = analyzed_img("GameplayAssets\\dizzy_effect(9).png", 27 , 58 , 522 , 290)

soul1 = analyzed_img("GameplayAssets\soul(1).png", 241 , 109 , 221 , 201)
soul2 = analyzed_img("GameplayAssets\soul(2).png", 241 , 109 , 221 , 201)
soul3 = analyzed_img("GameplayAssets\soul(3).png", 241 , 109 , 221 , 201)
soul4 = analyzed_img("GameplayAssets\soul(4).png", 241 , 109 , 221 , 201)
soul5 = analyzed_img("GameplayAssets\soul(5).png", 241 , 109 , 221 , 201)
soul6 = analyzed_img("GameplayAssets\soul(6).png", 241 , 109 , 221 , 201)
soul7 = analyzed_img("GameplayAssets\soul(7).png", 241 , 109 , 221 , 201)
soul8 = analyzed_img("GameplayAssets\soul(8).png", 241 , 109 , 221 , 201)


