from PIL import Image
import pygame 
from pygame.locals import *

pygame.init()

path = "C:\\Users\\Hoang Anh Tuan\\Desktop\\tmp\\pixelart-cute-online-video-cutter.com_000\\pixelart-cute (online-video-cutter.com)_000.png"


def save():
    img  = Image.open(path)
    size = img_oringinal.get_size()
    pixel_map = img.load()
    for i in range(1,size[0] + 1):
        for j in range(1,size[1] + 1):
            # (a,b,c,d) = 
            pixel_map[i ,j] = (0,0,0)
    img.save("C:\\Users\\Hoang Anh Tuan\\Desktop\\tmp\\siuu.png")




path = "GameplayAssets\\none.png"

img  = Image.open(path)
pixel_map = img.load()

print(pixel_map[100,100])

img.save("C:\\Users\\Hoang Anh Tuan\\Desktop\\tmp\\siuu.png", 32)
# img.save("",)








# img_oringinal = pygame.image.load(path)
# img = pygame.image.load(path)
# img_rate = float(img.get_height() / img.get_width())
# (a,b) = img.get_size()
# scale = 1000 / a
# window_size = (int(a * scale) , int(b * scale))
# img = pygame.transform.scale(img, window_size)
# WIN  = pygame.display.set_mode(window_size)
# img_topleft = (0,0)
# img_flag = (0,0)
# screen_flag = (0,0)

# Flag = True
# Flag1 = Flag2 = False
# while Flag:
    
#     for event in pygame.event.get():
#         if event.type == KEYDOWN:
#             if event.key == 9 :
#                 Flag = False
#         if event.type == MOUSEWHEEL:
#             (x,y) = pygame.mouse.get_pos()
#             img_flag = ((x - img_topleft[0]) / img.get_width(), (y - img_topleft[1]) / img.get_height())
#             screen_flag = (x , y)
#             img = pygame.transform.scale(img_oringinal, (img.get_width() + 30 * event.y, (img_rate * (img.get_width() + 30 * event.y))))
#             img_flag = (img_flag[0] * img.get_width(), img_flag[1] * img.get_height())
#             img_topleft = (screen_flag[0] - img_flag[0], screen_flag[1] - img_flag[1])
        
#         if event.type == KEYDOWN:
#             if event.key == 1073742048 :
#                 Flag1 = True
            
#             if event.key == 115:
#                 Flag2 = True
    
#     if Flag1 and Flag2:
#         save()
    

#     WIN.fill((0,0,0))
#     WIN.blit(img, img_topleft)
#     # WIN.fill()
#     # print(WIN.get_at((100,100)))
#     pygame.display.update()