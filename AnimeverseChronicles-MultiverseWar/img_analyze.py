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












