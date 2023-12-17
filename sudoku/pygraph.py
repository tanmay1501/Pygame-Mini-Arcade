#pygraph
import pygame
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((640,480))
x=0
y=0
size=16
screen.fill((255,255,255))
pygame.draw.line(screen, (0,0,0), (screen.get_width()/2,0),(screen.get_width()/2,screen.get_height()),5)
pygame.draw.line(screen, (0,0,0), (0,screen.get_height()/2),(screen.get_width(),screen.get_height()/2),5)
running =True
while running:
    while y<480:
        pygame.draw.rect(screen,(0,0,0),(x,y,size,size),1)
        if x>640:
            x=0
            y+=size
            pygame.draw.rect(screen,(0,0,0),(x,y,size,size),1)
        x+=size
    for e in pygame.event.get():
        #termination
        if e.type==QUIT:
            running= False
        if e.type==KEYUP:
            if e.key==K_SPACE:
                x=0
                y=0
                screen.fill((255,255,255))
                pygame.draw.line(screen, (0,0,0), (screen.get_width()/2,0),(screen.get_width()/2,screen.get_height()),5)
                pygame.draw.line(screen, (0,0,0), (0,screen.get_height()/2),(screen.get_width(),screen.get_height()/2),5)
                size=int(input('Enter size: ')) 
    pygame.display.flip()