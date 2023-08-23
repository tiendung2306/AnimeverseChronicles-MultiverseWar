import pygame 
from pygame.locals import *
from color import *

class  analyzed_img():
    def __init__(self,img,a,b,c,d):
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


# wizard66 = analyzed_img("C:\\Users\\Hoang Anh Tuan\\Desktop\\ll\com-1--unscreen-66.png", 179 , 79 , 58 , 155)
# wizard71 = analyzed_img("C:\\Users\\Hoang Anh Tuan\\Desktop\\ll\com-1--unscreen-71.png", 181 , 81 , 52 , 145)
# wizard74 = analyzed_img("C:\\Users\\Hoang Anh Tuan\\Desktop\\ll\com-1--unscreen-74.png", 176 , 87 , 52 , 143)
# wizard79 = analyzed_img("C:\\Users\\Hoang Anh Tuan\\Desktop\\ll\com-1--unscreen-79.png", 168 , 89 , 53 , 145)
# wizard83 = analyzed_img("C:\\Users\\Hoang Anh Tuan\\Desktop\\ll\com-1--unscreen-83.png", 157 , 94 , 56 , 146)
# wizard86 = analyzed_img("C:\\Users\\Hoang Anh Tuan\\Desktop\\ll\com-1--unscreen-86.png", 149 , 97 , 55 , 147)
# wizard89 = analyzed_img("C:\\Users\\Hoang Anh Tuan\\Desktop\\ll\com-1--unscreen-89.png", 148 , 93 , 53 , 144)
# wizard94 = analyzed_img("C:\\Users\\Hoang Anh Tuan\\Desktop\\ll\com-1--unscreen-94.png", 147 , 86 , 53 , 147)
# wizard97 = analyzed_img("C:\\Users\\Hoang Anh Tuan\\Desktop\\ll\com-1--unscreen-97.png", 149 , 80 , 53 , 151)
# wizard101 = analyzed_img("C:\\Users\\Hoang Anh Tuan\\Desktop\\ll\com-1--unscreen-101.png", 149 , 80 , 53 , 151)
# wizard104 = analyzed_img("C:\\Users\\Hoang Anh Tuan\\Desktop\\ll\com-1--unscreen-104.png", 156 , 84 , 56 , 147)
# wizard108 = analyzed_img("C:\\Users\\Hoang Anh Tuan\\Desktop\\ll\com-1--unscreen-108.png", 163 , 90 , 56 , 143)

wizard1 = analyzed_img("GameplayAssets\wizard(1).png", 180 , 74 , 58 , 157)
wizard2 = analyzed_img("GameplayAssets\wizard(2).png", 187 , 83 , 51 , 157)
wizard3 = analyzed_img("GameplayAssets\wizard(3).png", 191 , 91 , 51 , 154)
wizard4 = analyzed_img("GameplayAssets\wizard(4).png", 175 , 96 , 53 , 127)
wizard5 = analyzed_img("GameplayAssets\wizard(5).png", 157 , 98 , 91 , 143)
wizard6 = analyzed_img("GameplayAssets\wizard(6).png", 137 , 74 , 59 , 161)
wizard7 = analyzed_img("GameplayAssets\wizard(7).png", 136 , 67 , 56 , 160)
wizard8 = analyzed_img("GameplayAssets\wizard(8).png", 138 , 67 , 63 , 160)
#CODE BEN DUOI DE TAO HIT BOX TU AN

# img = pygame.image.load("GameplayAssets\\wizard(4).png")
# WIN = pygame.display.set_mode(img.get_size())


# a = b = c = d = 0
# Flag = True
# flag2 = False
# counter = 4
# while Flag:
#     WIN.fill(Black)
#     WIN.blit(img,(0,0))
#     for event in pygame.event.get():
#         if event.type == KEYDOWN:
#             print("wizard{}".format(counter),"GameplayAssets\\wizard({}).png".format(counter),a,",",b,",",c - a,",",d - b)
            
#             img = pygame.image.load("GameplayAssets\\wizard({}).png".format(counter).format(counter))
#             if event.key == 9:
#                 Flag = False
#             if event.key == 32 :
#                 print(counter)
#             counter += 1
#         if event.type == MOUSEBUTTONDOWN:
#             c = d = 0
#             (a,b) = pygame.mouse.get_pos()
#             flag2 = True
#         if  event.type == MOUSEBUTTONUP:
#              flag2 = False
#     if flag2:
#         (c,d) = pygame.mouse.get_pos()
#     else:
#         (m,n) = pygame.mouse.get_pos()
#         hcn1 = pygame.Rect(0,n,WIN.get_size()[0],1)
#         hcn2 = pygame.Rect(m,0,1,WIN.get_size()[1])
#         pygame.draw.rect(WIN,Yellow,hcn1)
#         pygame.draw.rect(WIN,Yellow,hcn2)
#     pygame.draw.rect(WIN,Yellow,pygame.Rect(a,b,c - a,d - b),1)
#     pygame.display.update()


