import pygame 
from pygame.locals import *
from color import *


def reverse(analyzed_IMG):
    (a, b, c, d ) = analyzed_IMG.data
    tmp = pre_analyze_img()
    tmp.img_name = analyzed_IMG.img
    tmp.img = pygame.transform.flip(analyzed_IMG.img, True, False)
    tmp.data = (tmp.img.get_width() - a - c,b,c,d)        
    return tmp

class  pre_analyze_img():
    def __init__(self) -> None:
        pass
    # def __init__(self,img,a,b,c,d):
    #     self.img_name = img
    #     self.img = None
    #     self.data = (a,b,c,d)

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
    
class analyzed_img():
    def __init__(self,img,a,b,c,d):
        self.img_name = img
        self.img = pygame.image.load(img)
        self.data = (a,b,c,d)        
        self.reverse = reverse(self)

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


nexus = analyzed_img("GameplayAssets\\nexus.png",85 , 46 , 160 , 531)
# sword_man1_1  = analyzed_img("GameplayAssets\\sword_man1(1).png", 77 , 153 , 163 , 464)
# sword_man1_2  = analyzed_img("GameplayAssets\\sword_man1(2).png", 88 , 154 , 156 , 477)
# sword_man1_3  = analyzed_img("GameplayAssets\\sword_man1(3).png", 79 , 123 , 131 , 495)
# sword_man1_4  = analyzed_img("GameplayAssets\\sword_man1(4).png", 93 , 133 , 158 , 484)

# sword_man2_1  = analyzed_img("GameplayAssets\\sword_man2(1).png",700 - 77 - 163, 153 , 163 , 464)   
# sword_man2_2  = analyzed_img("GameplayAssets\\sword_man2(2).png",700 - 88 - 156, 154 , 156 , 477)
# sword_man2_3  = analyzed_img("GameplayAssets\\sword_man2(3).png",700 - 79 - 131, 123 , 131 , 495)
# sword_man2_4  = analyzed_img("GameplayAssets\\sword_man2(4).png",700 - 93 - 158, 133 , 158 , 484)


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
sword_man39 = analyzed_img("GameplayAssets\sword_man(39).png", 246 , 354 , 122 , 239)
sword_man40 = analyzed_img("GameplayAssets\sword_man(40).png", 246 , 354 , 122 , 239)
sword_man41 = analyzed_img("GameplayAssets\sword_man(41).png", 246 , 354 , 122 , 239)
sword_man50 = analyzed_img("GameplayAssets\sword_man(50).png", 246 , 354 , 122 , 239)


# archer1_1 = analyzed_img("GameplayAssets\\archer1(1).png", 66 , 40 , 60 , 164)
# archer1_2 = analyzed_img("GameplayAssets\\archer1(2).png", 67 , 40 , 58 , 170)
# archer1_3 = analyzed_img("GameplayAssets\\archer1(3).png", 70 , 40 , 54 , 162)

# archer2_1 = analyzed_img("GameplayAssets\\archer2(1).png", 200 - 66 - 60, 40 , 60 , 164)
# archer2_2 = analyzed_img("GameplayAssets\\archer2(2).png", 200 - 67 - 58, 40 , 58 , 170)
# archer2_3 = analyzed_img("GameplayAssets\\archer2(3).png", 200 - 70 - 54, 40 , 54 , 162)

archer1 = analyzed_img("GameplayAssets\\archer(1).png", 166 , 285 , 113 , 212)
archer2 = analyzed_img("GameplayAssets\\archer(2).png", 166 , 285 , 113 , 212)
archer3 = analyzed_img("GameplayAssets\\archer(3).png", 166 , 285 , 113 , 212)
archer4 = analyzed_img("GameplayAssets\\archer(4).png", 166 , 285 , 113 , 212)
archer5 = analyzed_img("GameplayAssets\\archer(5).png", 166 , 285 , 113 , 212)
archer6 = analyzed_img("GameplayAssets\\archer(6).png", 166 , 285 , 113 , 212)
archer7 = analyzed_img("GameplayAssets\\archer(7).png", 166 , 285 , 113 , 212)
archer8 = analyzed_img("GameplayAssets\\archer(8).png", 166 , 285 , 113 , 212)
archer9 = analyzed_img("GameplayAssets\\archer(9).png", 166 , 285 , 113 , 212)
archer10 = analyzed_img("GameplayAssets\\archer(10).png", 166 , 285 , 113 , 212)
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
archer31 = analyzed_img("GameplayAssets\\archer(31).png", 199 , 298 , 69 , 192)
archer32 = analyzed_img("GameplayAssets\\archer(32).png", 199 , 298 , 69 , 192)
archer33 = analyzed_img("GameplayAssets\\archer(33).png", 199 , 298 , 69 , 192)
archer40 = analyzed_img("GameplayAssets\\archer(40).png", 199 , 298 , 69 , 192)


arrow = analyzed_img("GameplayAssets\\arrow.png", 279 , 332 , 132 , 20)
special_arrow = analyzed_img("GameplayAssets\\special_arrow.png", 279 , 332 , 132 , 20)

# arrow1 =  analyzed_img("GameplayAssets\\arrow1.png", 142 , 79 , 65 , 10)
# arrow2 =  analyzed_img("GameplayAssets\\arrow2.png",200 - 142 - 65, 79 , 65 , 10)

# tanker1_1 = analyzed_img("GameplayAssets\\tanker1(1).png", 107 , 68 , 187 , 390)
# tanker1_2 = analyzed_img("GameplayAssets\\tanker1(2).png", 107 , 67 , 191 , 390)
# tanker1_3 = analyzed_img("GameplayAssets\\tanker1(3).png", 137 , 66 , 159 , 391)
# tanker1_4 = analyzed_img("GameplayAssets\\tanker1(4).png", 138 , 66 , 160 , 393)

# tanker2_1 = analyzed_img("GameplayAssets\\tanker2(1).png", 451 - 107 - 187 , 68 , 187 , 390)
# tanker2_2 = analyzed_img("GameplayAssets\\tanker2(2).png", 451 - 107 - 191 , 67 , 191 , 390)
# tanker2_3 = analyzed_img("GameplayAssets\\tanker2(3).png", 451 - 137 - 159 , 66 , 159 , 391)
# tanker2_4 = analyzed_img("GameplayAssets\\tanker2(4).png", 451 - 138 - 160 , 66 , 160 , 393)

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
tanker20 = analyzed_img("GameplayAssets\\tanker(20).png" , 260 , 73 , 98 , 207 )
tanker21 = analyzed_img("GameplayAssets\\tanker(21).png" , 260 , 73 , 98 , 207 )
tanker22 = analyzed_img("GameplayAssets\\tanker(22).png" , 260 , 73 , 98 , 207 )
tanker23 = analyzed_img("GameplayAssets\\tanker(23).png", 240 , 62 , 56 , 219)
tanker24 = analyzed_img("GameplayAssets\\tanker(24).png" , 211 , 62 , 89 , 216 )
tanker25 = analyzed_img("GameplayAssets\\tanker(25).png" , 211 , 62 , 89 , 216 )
tanker26 = analyzed_img("GameplayAssets\\tanker(26).png" , 211 , 62 , 89 , 216 )
tanker27 = analyzed_img("GameplayAssets\\tanker(27).png" , 263 , 60 , 67 , 218 )
tanker28 = analyzed_img("GameplayAssets\\tanker(28).png" , 263 , 60 , 67 , 218 )
tanker29 = analyzed_img("GameplayAssets\\tanker(29).png" , 263 , 60 , 67 , 218 )
tanker30 = analyzed_img("GameplayAssets\\tanker(30).png" , 214 , 61 , 102 , 220 )
tanker31 = analyzed_img("GameplayAssets\\tanker(31).png" , 214 , 61 , 102 , 220 )
tanker32 = analyzed_img("GameplayAssets\\tanker(32).png", 217 , 77 , 94 , 203)
tanker33 = analyzed_img("GameplayAssets\\tanker(33).png", 410 , 186 , 0 , 0)
tanker34 = analyzed_img("GameplayAssets\\tanker(34).png", 256 , 80 , 75 , 199)
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
wizard29 = analyzed_img("GameplayAssets\\wizard(29).png", 149 , 84 , 73 , 158)
wizard30 = analyzed_img("GameplayAssets\\wizard(30).png", 149 , 84 , 73 , 158)
wizard31 = analyzed_img("GameplayAssets\\wizard(31).png", 149 , 84 , 73 , 158)
wizard32 = analyzed_img("GameplayAssets\\wizard(32).png", 149 , 84 , 73 , 158)

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

knock_back1 = analyzed_img("GameplayAssets\knock_back(1).png", 283 , 198 , 143 , 84)
knock_back2 = analyzed_img("GameplayAssets\knock_back(2).png", 287 , 180 , 195 , 101)
knock_back3 = analyzed_img("GameplayAssets\knock_back(3).png", 291 , 160 , 189 , 120)
knock_back4 = analyzed_img("GameplayAssets\knock_back(4).png", 291 , 160 , 189 , 120)
knock_back5 = analyzed_img("GameplayAssets\knock_back(5).png", 291 , 160 , 189 , 120)
knock_back6 = analyzed_img("GameplayAssets\knock_back(6).png", 378 , 147 , 83 , 115)

flying1 = analyzed_img("GameplayAssets\\flying(1).png",  199 , 259 , 270 , 105)
flying2 = analyzed_img("GameplayAssets\\flying(2).png",  199 , 259 , 270 , 105)
flying3 = analyzed_img("GameplayAssets\\flying(3).png",  199 , 259 , 270 , 105)
flying4 = analyzed_img("GameplayAssets\\flying(4).png",  199 , 259 , 270 , 105)
flying5 = analyzed_img("GameplayAssets\\flying(5).png",  199 , 259 , 270 , 105)
flying6 = analyzed_img("GameplayAssets\\flying(6).png",  199 , 259 , 270 , 105)
flying7 = analyzed_img("GameplayAssets\\flying(7).png",  199 , 259 , 270 , 105)
flying8 = analyzed_img("GameplayAssets\\flying(8).png",  199 , 259 , 270 , 105)

soul1 = analyzed_img("GameplayAssets\soul(1).png", 241 , 109 , 221 , 201)
soul2 = analyzed_img("GameplayAssets\soul(2).png", 241 , 109 , 221 , 201)
soul3 = analyzed_img("GameplayAssets\soul(3).png", 241 , 109 , 221 , 201)
soul4 = analyzed_img("GameplayAssets\soul(4).png", 241 , 109 , 221 , 201)
soul5 = analyzed_img("GameplayAssets\soul(5).png", 241 , 109 , 221 , 201)
soul6 = analyzed_img("GameplayAssets\soul(6).png", 241 , 109 , 221 , 201)
soul7 = analyzed_img("GameplayAssets\soul(7).png", 241 , 109 , 221 , 201)
soul8 = analyzed_img("GameplayAssets\soul(8).png", 241 , 109 , 221 , 201)

goku1 = analyzed_img("GameplayAssets\goku(1).png ",139 , 90 , 110 , 226)
goku2 = analyzed_img("GameplayAssets\goku(2).png ",139 , 90 , 110 , 226)
goku3 = analyzed_img("GameplayAssets\goku(3).png ",139 , 90 , 110 , 226)
goku4 = analyzed_img("GameplayAssets\goku(4).png ",139 , 90 , 110 , 226)
goku5 = analyzed_img("GameplayAssets\goku(5).png ",102 , 137 , 201 , 136)
goku6 = analyzed_img("GameplayAssets\goku(6).png ",102 , 137 , 201 , 136)
goku7 = analyzed_img("GameplayAssets\goku(7).png ",102 , 137 , 201 , 136)
goku8 = analyzed_img("GameplayAssets\goku(8).png ",102 , 137 , 201 , 136)
goku9 = analyzed_img("GameplayAssets\goku(9).png ",135 , 166 , 99 , 151)
goku10 = analyzed_img("GameplayAssets\goku(10).png", 179 , 131 , 97 , 175)
goku11 = analyzed_img("GameplayAssets\goku(11).png", 161 , 126 , 85 , 198)
goku12 = analyzed_img("GameplayAssets\goku(12).png", 161 , 126 , 85 , 198)
goku13 = analyzed_img("GameplayAssets\goku(13).png", 161 , 126 , 85 , 198)
goku14 = analyzed_img("GameplayAssets\goku(14).png", 161 , 126 , 85 , 198)
goku15 = analyzed_img("GameplayAssets\goku(15).png", 208 , 137 , 116 , 203)
goku16 = analyzed_img("GameplayAssets\goku(16).png", 224 , 120 , 130 , 211)
goku17 = analyzed_img("GameplayAssets\goku(17).png", 224 , 120 , 130 , 211)
goku18 = analyzed_img("GameplayAssets\goku(18).png", 224 , 120 , 130 , 211)
goku19 = analyzed_img("GameplayAssets\goku(19).png", 224 , 120 , 130 , 211)
goku20 = analyzed_img("GameplayAssets\goku(20).png", 224 , 120 , 130 , 211)
goku21 = analyzed_img("GameplayAssets\goku(21).png", 224 , 120 , 130 , 211)
goku22 = analyzed_img("GameplayAssets\goku(22).png", 224 , 120 , 130 , 211)
goku23 = analyzed_img("GameplayAssets\goku(23).png", 224 , 120 , 130 , 211)
goku24 = analyzed_img("GameplayAssets\goku(24).png", 224 , 120 , 130 , 211)
goku25 = analyzed_img("GameplayAssets\goku(25).png", 224 , 120 , 130 , 211)
goku50 = analyzed_img("GameplayAssets\goku(50).png", 224 , 120 , 130 , 211)
goku51 = analyzed_img("GameplayAssets\goku(51).png", 224 , 120 , 130 , 211)
goku52 = analyzed_img("GameplayAssets\goku(52).png", 224 , 120 , 130 , 211)
goku53 = analyzed_img("GameplayAssets\goku(53).png", 224 , 120 , 130 , 211)


goku_to_kame = analyzed_img("GameplayAssets\goku(23).png", 315 , 251 , 5 , 4)
kame = pygame.image.load("GameplayAssets\\kame.png")

naruto1 = analyzed_img( "GameplayAssets\\naruto(1).png " , 296 , 346 , 74 , 176 )
naruto2 = analyzed_img( "GameplayAssets\\naruto(2).png " , 296 , 346 , 74 , 176 )
naruto3 = analyzed_img( "GameplayAssets\\naruto(3).png " , 296 , 346 , 74 , 176 )
naruto4 = analyzed_img( "GameplayAssets\\naruto(4).png " , 296 , 346 , 74 , 176 )
naruto5 = analyzed_img( "GameplayAssets\\naruto(5).png " , 296 , 346 , 74 , 176 )
naruto6 = analyzed_img( "GameplayAssets\\naruto(6).png " , 268 , 369 , 110 , 156 )
naruto7 = analyzed_img( "GameplayAssets\\naruto(7).png " , 295 , 341 , 78 , 177 )
naruto8 = analyzed_img( "GameplayAssets\\naruto(8).png " , 281 , 425 , 148 , 102 )
naruto9 = analyzed_img( "GameplayAssets\\naruto(9).png " , 281 , 425 , 148 , 102 )
naruto10 = analyzed_img( "GameplayAssets\\naruto(10).png " , 289 , 386 , 118 , 137 )
naruto11 = analyzed_img( "GameplayAssets\\naruto(11).png " , 324 , 335 , 93 , 185 )
naruto12 = analyzed_img( "GameplayAssets\\naruto(12).png " , 324 , 335 , 93 , 185 )
naruto13 = analyzed_img( "GameplayAssets\\naruto(13).png " , 292 , 349 , 96 , 178 )
naruto14 = analyzed_img( "GameplayAssets\\naruto(14).png " , 303 , 352 , 97 , 169 )
naruto15 = analyzed_img( "GameplayAssets\\naruto(15).png " , 306 , 340 , 97 , 183 )
naruto16 = analyzed_img( "GameplayAssets\\naruto(16).png " , 306 , 340 , 97 , 183 )
naruto17 = analyzed_img( "GameplayAssets\\naruto(17).png " , 322 , 361 , 102 , 164 )
naruto18 = analyzed_img( "GameplayAssets\\naruto(18).png " , 278 , 354 , 98 , 167 )
naruto19 = analyzed_img( "GameplayAssets\\naruto(19).png " , 295 , 362 , 77 , 158 )
naruto20 = analyzed_img( "GameplayAssets\\naruto(20).png " , 295 , 362 , 77 , 158 )
naruto21 = analyzed_img( "GameplayAssets\\naruto(21).png " , 295 , 362 , 77 , 158 )
naruto22 = analyzed_img( "GameplayAssets\\naruto(22).png " , 295 , 362 , 77 , 158 )
naruto23 = analyzed_img( "GameplayAssets\\naruto(23).png " , 295 , 362 , 77 , 158 )
naruto24 = analyzed_img( "GameplayAssets\\naruto(24).png " , 295 , 362 , 77 , 158 )
naruto25 = analyzed_img( "GameplayAssets\\naruto(25).png " , 295 , 362 , 77 , 158 )
naruto26 = analyzed_img( "GameplayAssets\\naruto(26).png " , 295 , 362 , 77 , 158 )
naruto27 = analyzed_img( "GameplayAssets\\naruto(27).png " , 162 , 339 , 331 , 187 )
naruto28 = analyzed_img( "GameplayAssets\\naruto(28).png " , 162 , 339 , 331 , 187 )
naruto29 = analyzed_img( "GameplayAssets\\naruto(29).png " , 162 , 339 , 331 , 187 )
naruto30 = analyzed_img( "GameplayAssets\\naruto(30).png " , 194 , 338 , 234 , 191 )
naruto31 = analyzed_img( "GameplayAssets\\naruto(31).png " , 194 , 338 , 234 , 191 )
naruto32 = analyzed_img( "GameplayAssets\\naruto(32).png " , 194 , 338 , 234 , 191 )
naruto33 = analyzed_img( "GameplayAssets\\naruto(33).png " , 194 , 338 , 234 , 191 )
naruto34 = analyzed_img( "GameplayAssets\\naruto(34).png " , 194 , 338 , 234 , 191 )
naruto35 = analyzed_img( "GameplayAssets\\naruto(35).png " , 165 , 337 , 326 , 191 )
naruto36 = analyzed_img( "GameplayAssets\\naruto(36).png " , 165 , 337 , 326 , 191 )
naruto37 = analyzed_img( "GameplayAssets\\naruto(37).png " , 165 , 337 , 326 , 191 )
naruto38 = analyzed_img( "GameplayAssets\\naruto(38).png " , 165 , 337 , 326 , 191 )
naruto39 = analyzed_img( "GameplayAssets\\naruto(39).png " , 278 , 310 , 112 , 222 )
naruto40 = analyzed_img( "GameplayAssets\\naruto(40).png " , 278 , 310 , 112 , 222 )
naruto41 = analyzed_img( "GameplayAssets\\naruto(41).png " , 278 , 310 , 112 , 222 )
naruto42 = analyzed_img( "GameplayAssets\\naruto(42).png " , 289 , 314 , 92 , 221 )
naruto43 = analyzed_img( "GameplayAssets\\naruto(43).png " , 289 , 314 , 92 , 221 )
naruto44 = analyzed_img( "GameplayAssets\\naruto(44).png " , 265 , 332 , 106 , 194 )
naruto45 = analyzed_img( "GameplayAssets\\naruto(45).png " , 265 , 332 , 106 , 194 )
naruto46 = analyzed_img( "GameplayAssets\\naruto(46).png " , 272 , 385 , 94 , 135 )
naruto47 = analyzed_img( "GameplayAssets\\naruto(47).png " , 276 , 371 , 106 , 154 )
naruto48 = analyzed_img( "GameplayAssets\\naruto(48).png " , 276 , 371 , 106 , 154 )
naruto49 = analyzed_img( "GameplayAssets\\naruto(49).png " , 276 , 371 , 106 , 154 )
naruto50 = analyzed_img( "GameplayAssets\\naruto(50).png " , 275 , 350 , 95 , 164 )
naruto51 = analyzed_img( "GameplayAssets\\naruto(51).png " , 284 , 315 , 90 , 202 )
naruto52 = analyzed_img( "GameplayAssets\\naruto(52).png " , 260 , 410 , 129 , 121 )
naruto53 = analyzed_img( "GameplayAssets\\naruto(53).png " , 263 , 326 , 121 , 195 )
naruto54 = analyzed_img( "GameplayAssets\\naruto(54).png " , 263 , 326 , 121 , 195 )
naruto55 = analyzed_img( "GameplayAssets\\naruto(55).png " , 263 , 326 , 121 , 195 )
naruto56 = analyzed_img( "GameplayAssets\\naruto(56).png " , 263 , 326 , 121 , 195 )
naruto57 = analyzed_img( "GameplayAssets\\naruto(57).png " , 260 , 432 , 132 , 99 )
naruto58 = analyzed_img( "GameplayAssets\\naruto(58).png " , 268 , 337 , 115 , 192 )
naruto59 = analyzed_img( "GameplayAssets\\naruto(59).png " , 267 , 309 , 120 , 215 )
naruto60 = analyzed_img( "GameplayAssets\\naruto(60).png " , 267 , 309 , 120 , 215 )
naruto61 = analyzed_img( "GameplayAssets\\naruto(61).png " , 267 , 309 , 120 , 215 )
naruto62 = analyzed_img( "GameplayAssets\\naruto(62).png " , 253 , 373 , 159 , 150 )
naruto63 = analyzed_img( "GameplayAssets\\naruto(63).png " , 253 , 373 , 159 , 150 )
naruto64 = analyzed_img( "GameplayAssets\\naruto(64).png " , 253 , 373 , 159 , 150 )
naruto65 = analyzed_img( "GameplayAssets\\naruto(65).png " , 253 , 373 , 159 , 150 )
naruto66 = analyzed_img( "GameplayAssets\\naruto(66).png " , 253 , 373 , 159 , 150 )
naruto67 = analyzed_img( "GameplayAssets\\naruto(67).png " , 253 , 373 , 159 , 150 )
naruto68 = analyzed_img( "GameplayAssets\\naruto(68).png " , 278 , 353 , 102 , 167 )
naruto69 = analyzed_img( "GameplayAssets\\naruto(69).png " , 278 , 353 , 102 , 167 )
naruto70 = analyzed_img( "GameplayAssets\\naruto(70).png " , 278 , 353 , 102 , 167 )
naruto71 = analyzed_img( "GameplayAssets\\naruto(71).png " , 259 , 353 , 90 , 172 )
naruto72 = analyzed_img( "GameplayAssets\\naruto(72).png " , 249 , 429 , 128 , 93 )
naruto73 = analyzed_img( "GameplayAssets\\naruto(73).png " , 239 , 464 , 176 , 102 )
naruto74 = analyzed_img( "GameplayAssets\\naruto(74).png " , 249 , 354 , 136 , 170 )
naruto75 = analyzed_img( "GameplayAssets\\naruto(75).png " , 194 , 338 , 234 , 191 )
naruto76 = analyzed_img( "GameplayAssets\\naruto(76).png " , 194 , 338 , 234 , 191 )
naruto77 = analyzed_img( "GameplayAssets\\naruto(77).png " , 194 , 338 , 234 , 191 )
naruto78 = analyzed_img( "GameplayAssets\\naruto(35).png " , 165 , 337 , 326 , 191 )
naruto79 = analyzed_img( "GameplayAssets\\naruto(79).png " , 165 , 337 , 326 , 191 )
naruto80 = analyzed_img( "GameplayAssets\\naruto(80).png " , 165 , 337 , 326 , 191 )
naruto81 = analyzed_img( "GameplayAssets\\naruto(81).png " , 165 , 337 , 326 , 191 )
naruto82 = analyzed_img( "GameplayAssets\\naruto(82).png " , 165 , 337 , 326 , 191 )


rasenshuriken1 = analyzed_img( "GameplayAssets\\rasenshuriken(1).png " , 363 , 351 , 320 , 135 )
rasenshuriken2 = analyzed_img( "GameplayAssets\\rasenshuriken(2).png " , 363 , 351 , 320 , 135 )
rasenshuriken3 = analyzed_img( "GameplayAssets\\rasenshuriken(3).png " , 363 , 351 , 320 , 135 )
rasenshuriken4 = analyzed_img( "GameplayAssets\\rasenshuriken(4).png " , 363 , 351 , 320 , 135 )
rasenshuriken5 = analyzed_img( "GameplayAssets\\rasenshuriken(5).png " , 363 , 351 , 320 , 135 )
rasenshuriken6 = analyzed_img( "GameplayAssets\\rasenshuriken(6).png " , 363 , 351 , 320 , 135 )

explosion_stage_1_1 = analyzed_img( "GameplayAssets\\explosion_stage_1(1).png " , 289 , 397 , 88 , 72 )
explosion_stage_1_2 = analyzed_img( "GameplayAssets\\explosion_stage_1(2).png " , 264 , 359 , 130 , 110 )
explosion_stage_1_3 = analyzed_img( "GameplayAssets\\explosion_stage_1(3).png " , 237 , 315 , 177 , 152 )
explosion_stage_1_4 = analyzed_img( "GameplayAssets\\explosion_stage_1(4).png " , 176 , 214 , 303 , 257 )

explosion_stage_2_1 = analyzed_img( "GameplayAssets\\explosion_stage_2(1).png " , 90 , 170 , 484 , 300 )
explosion_stage_2_2 = analyzed_img( "GameplayAssets\\explosion_stage_2(2).png " , 90 , 170 , 484 , 300 )
explosion_stage_2_3 = analyzed_img( "GameplayAssets\\explosion_stage_2(3).png " , 90 , 170 , 484 , 300 )

explosion_stage_3_1 = analyzed_img( "GameplayAssets\\explosion_stage_3(1).png " , 77 , 111 , 538 , 361 )
explosion_stage_3_2 = analyzed_img( "GameplayAssets\\explosion_stage_3(2).png " , 77 , 111 , 538 , 361 )





