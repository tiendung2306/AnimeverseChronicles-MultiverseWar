#CODE BEN DUOI DE TAO HIT BOX TU AN



import pygame 
from pygame.locals import *
from color import *




a = b = c = d = 0
Flag = True
flag2 = False
counter = 1
img = pygame.image.load("GameplayAssets\\archer({}).png".format(counter))
WIN = pygame.display.set_mode(img.get_size())
while Flag:
    WIN.fill(Black)
    WIN.blit(img,(0,0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            print("archer{}".format(counter),"GameplayAssets\\archer({}).png".format(counter),a,",",b,",",c - a,",",d - b)
            
            counter += 1
            img = pygame.image.load("GameplayAssets\\archer({}).png".format(counter))
            if event.key == 9:
                Flag = False
            # if event.key == 32 :
            #     print(counter)
        if event.type == MOUSEBUTTONDOWN:
            c = d = 0
            (a,b) = pygame.mouse.get_pos()
            flag2 = True
        if  event.type == MOUSEBUTTONUP:
             flag2 = False
    if flag2:
        (c,d) = pygame.mouse.get_pos()
    else:
        (m,n) = pygame.mouse.get_pos()
        hcn1 = pygame.Rect(0,n,WIN.get_size()[0],1)
        hcn2 = pygame.Rect(m,0,1,WIN.get_size()[1])
        pygame.draw.rect(WIN,Yellow,hcn1)
        pygame.draw.rect(WIN,Yellow,hcn2)
    pygame.draw.rect(WIN,Yellow,pygame.Rect(a,b,c - a,d - b),1)
    pygame.display.update()

for i in range(32,39):
    print("tanker",i)
