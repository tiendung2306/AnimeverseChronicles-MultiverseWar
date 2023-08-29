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

nexus_test = analyzed_img("GameplayAssets\\nexus_test.png", 63 , 117 , 235 , 314)

sword_man1_1  = analyzed_img("GameplayAssets\\sword_man1(1).png", 77 , 153 , 163 , 464)
sword_man1_2  = analyzed_img("GameplayAssets\\sword_man1(2).png", 88 , 154 , 156 , 477)
sword_man1_3  = analyzed_img("GameplayAssets\\sword_man1(3).png", 79 , 123 , 131 , 495)
sword_man1_4  = analyzed_img("GameplayAssets\\sword_man1(4).png", 93 , 133 , 158 , 484)

sword_man2_1  = analyzed_img("GameplayAssets\\sword_man2(1).png",700 - 77 - 163, 153 , 163 , 464)   
sword_man2_2  = analyzed_img("GameplayAssets\\sword_man2(2).png",700 - 88 - 156, 154 , 156 , 477)
sword_man2_3  = analyzed_img("GameplayAssets\\sword_man2(3).png",700 - 79 - 131, 123 , 131 , 495)
sword_man2_4  = analyzed_img("GameplayAssets\\sword_man2(4).png",700 - 93 - 158, 133 , 158 , 484)

sword_man1 = analyzed_img("GameplayAssets\sword_man(1).png", 254 , 352 , 108 , 239)
sword_man2 = analyzed_img("GameplayAssets\sword_man(2).png", 254 , 352 , 108 , 239)
sword_man3 = analyzed_img("GameplayAssets\sword_man(3).png", 254 , 352 , 108 , 239)
sword_man4 = analyzed_img("GameplayAssets\sword_man(4).png", 254 , 352 , 108 , 239)
sword_man5 = analyzed_img("GameplayAssets\sword_man(5).png", 254 , 352 , 108 , 239)
sword_man6 = analyzed_img("GameplayAssets\sword_man(6).png", 254 , 352 , 108 , 239)
sword_man7 = analyzed_img("GameplayAssets\sword_man(7).png", 254 , 352 , 108 , 239)
sword_man8 = analyzed_img("GameplayAssets\sword_man(8).png", 254 , 352 , 108 , 239)
sword_man9 = analyzed_img("GameplayAssets\sword_man(9).png", 252 , 340 , 116 , 249)
sword_man10 = analyzed_img("GameplayAssets\sword_man(10).png", 250 , 347 , 113 , 246)
sword_man11 = analyzed_img("GameplayAssets\sword_man(11).png", 249 , 348 , 122 , 247)
sword_man12 = analyzed_img("GameplayAssets\sword_man(12).png", 249 , 348 , 122 , 247)
sword_man13 = analyzed_img("GameplayAssets\sword_man(13).png", 231 , 350 , 131 , 242)
sword_man14 = analyzed_img("GameplayAssets\sword_man(14).png", 231 , 350 , 131 , 242)
sword_man15 = analyzed_img("GameplayAssets\sword_man(15).png", 231 , 350 , 131 , 242)
sword_man16 = analyzed_img("GameplayAssets\sword_man(16).png", 240 , 348 , 125 , 244)
sword_man17 = analyzed_img("GameplayAssets\sword_man(17).png", 244 , 353 , 127 , 238)
sword_man18 = analyzed_img("GameplayAssets\sword_man(18).png", 244 , 353 , 127 , 238)
sword_man19 = analyzed_img("GameplayAssets\sword_man(19).png", 253 , 346 , 121 , 246)
sword_man20 = analyzed_img("GameplayAssets\sword_man(20).png", 247 , 355 , 117 , 236)
sword_man21 = analyzed_img("GameplayAssets\sword_man(21).png", 247 , 355 , 117 , 236)
sword_man22 = analyzed_img("GameplayAssets\sword_man(22).png", 250 , 352 , 123 , 238)
sword_man23 = analyzed_img("GameplayAssets\sword_man(23).png", 251 , 355 , 113 , 236)
sword_man24 = analyzed_img("GameplayAssets\sword_man(24).png", 251 , 355 , 113 , 236)
sword_man25 = analyzed_img("GameplayAssets\sword_man(25).png", 251 , 355 , 113 , 236)
sword_man26 = analyzed_img("GameplayAssets\sword_man(26).png", 258 , 392 , 109 , 203)
sword_man27 = analyzed_img("GameplayAssets\sword_man(27).png", 253 , 394 , 108 , 203)
sword_man28 = analyzed_img("GameplayAssets\sword_man(28).png", 253 , 394 , 108 , 203)
sword_man29 = analyzed_img("GameplayAssets\sword_man(29).png", 250 , 382 , 117 , 208)
sword_man30 = analyzed_img("GameplayAssets\sword_man(30).png", 232 , 386 , 129 , 208)
sword_man31 = analyzed_img("GameplayAssets\sword_man(31).png", 249 , 362 , 124 , 229)
sword_man32 = analyzed_img("GameplayAssets\sword_man(32).png", 257 , 352 , 107 , 239)
sword_man33 = analyzed_img("GameplayAssets\sword_man(33).png", 259 , 385 , 124 , 209)
sword_man34 = analyzed_img("GameplayAssets\sword_man(34).png", 259 , 385 , 124 , 209)
sword_man35 = analyzed_img("GameplayAssets\sword_man(35).png", 259 , 385 , 124 , 209)
sword_man36 = analyzed_img("GameplayAssets\sword_man(36).png", 259 , 385 , 124 , 209)
sword_man37 = analyzed_img("GameplayAssets\sword_man(37).png", 251 , 377 , 88 , 214)
sword_man38 = analyzed_img("GameplayAssets\sword_man(38).png", 246 , 354 , 122 , 239)

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

tanker1 = analyzed_img("GameplayAssets\\tanker(1).png", 229 , 60 , 85 , 222)
tanker2 = analyzed_img("GameplayAssets\\tanker(2).png", 229 , 60 , 85 , 222)
tanker3 = analyzed_img("GameplayAssets\\tanker(3).png", 229 , 60 , 85 , 222)
tanker4 = analyzed_img("GameplayAssets\\tanker(4).png", 229 , 60 , 85 , 222)
tanker5 = analyzed_img("GameplayAssets\\tanker(5).png", 223 , 59 , 76 , 220)
tanker6 = analyzed_img("GameplayAssets\\tanker(6).png", 223 , 59 , 76 , 220)
tanker7 = analyzed_img("GameplayAssets\\tanker(7).png", 223 , 59 , 76 , 220)
tanker8 = analyzed_img("GameplayAssets\\tanker(8).png", 236 , 60 , 73 , 222)
tanker9 = analyzed_img("GameplayAssets\\tanker(9).png", 224 , 62 , 69 , 216)
tanker10 = analyzed_img("GameplayAssets\\tanker(10).png", 218 , 62 , 84 , 221)
tanker11 = analyzed_img("GameplayAssets\\tanker(11).png", 221 , 61 , 96 , 220)
tanker12 = analyzed_img("GameplayAssets\\tanker(12).png", 219 , 62 , 76 , 216)
tanker13 = analyzed_img("GameplayAssets\\tanker(13).png", 261 , 72 , 70 , 205)
tanker14 = analyzed_img("GameplayAssets\\tanker(14).png", 261 , 72 , 70 , 205)
tanker15 = analyzed_img("GameplayAssets\\tanker(15).png", 257 , 66 , 65 , 215)
tanker16 = analyzed_img("GameplayAssets\\tanker(16).png", 243 , 65 , 56 , 210)
tanker17 = analyzed_img("GameplayAssets\\tanker(17).png", 262 , 75 , 60 , 204)
tanker18 = analyzed_img("GameplayAssets\\tanker(18).png", 266 , 77 , 70 , 201)
tanker19 = analyzed_img("GameplayAssets\\tanker(19).png", 249 , 71 , 71 , 207)
tanker20 = analyzed_img("GameplayAssets\\tanker(20).png", 265 , 71 , 57 , 213)
tanker21 = analyzed_img("GameplayAssets\\tanker(21).png", 258 , 72 , 59 , 208)
tanker22 = analyzed_img("GameplayAssets\\tanker(22).png", 248 , 70 , 63 , 209)
tanker23 = analyzed_img("GameplayAssets\\tanker(23).png", 240 , 62 , 56 , 219)
tanker24 = analyzed_img("GameplayAssets\\tanker(24).png", 240 , 62 , 56 , 219)
tanker25 = analyzed_img("GameplayAssets\\tanker(25).png", 240 , 62 , 56 , 219)
tanker26 = analyzed_img("GameplayAssets\\tanker(26).png", 240 , 62 , 56 , 219)
tanker27 = analyzed_img("GameplayAssets\\tanker(27).png", 261 , 64 , 66 , 215)
tanker28 = analyzed_img("GameplayAssets\\tanker(28).png", 261 , 64 , 66 , 215)
tanker29 = analyzed_img("GameplayAssets\\tanker(29).png", 261 , 64 , 66 , 215)
tanker30 = analyzed_img("GameplayAssets\\tanker(30).png", 243 , 60 , 73 , 217)
tanker31 = analyzed_img("GameplayAssets\\tanker(31).png", 243 , 60 , 73 , 217)
tanker32 = analyzed_img("GameplayAssets\\tanker(32).png", 410 , 186 , 0 , 0)
tanker33 = analyzed_img("GameplayAssets\\tanker(33).png", 410 , 186 , 0 , 0)
tanker34 = analyzed_img("GameplayAssets\\tanker(34).png", 410 , 186 , 0 , 0)
tanker35 = analyzed_img("GameplayAssets\\tanker(35).png", 410 , 186 , 0 , 0)
tanker36 = analyzed_img("GameplayAssets\\tanker(36).png", 410 , 186 , 0 , 0)
tanker37 = analyzed_img("GameplayAssets\\tanker(37).png", 410 , 186 , 0 , 0)
tanker38 = analyzed_img("GameplayAssets\\tanker(38).png", 410 , 186 , 0 , 0)

nexus1 = analyzed_img("GameplayAssets\\nexus1.png", 111 , 328 , 517 , 582)
nexus2 = analyzed_img("GameplayAssets\\nexus2.png", 186 , 209 , 457 , 769)


wizard1 = analyzed_img("GameplayAssets\\wizard(1).png", 170 , 56 , 68 , 179)
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


