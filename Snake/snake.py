import pygame
import random
import math
from pygame import mixer 

#initialization
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

#icon
pygame.display.set_caption("Snakes")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

#snake-head
headImg = pygame.image.load('head.png')
headX = 370
headY = 380
pygame.transform.rotate(headImg,90)
#snake-body
bodyImg = pygame.image.load('body.png')
bodyX = 300
bodyY = 300

accelaration = 0.5 

def move(headX):
    headX =headX + accelaration 

def head(x,y):
    #blit means drawing
    
    screen.blit(headImg ,(x,y))

running = True
while running:
    #Background colour
    
    #screen.blit(background, (0,0))

    #Termination
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                accelaration +=1 


    screen.fill((0, 0, 0))
    #head

    headX += accelaration
    if headX >= 800:
        headX = 0

    head(headX,headY)
    
    pygame.display.update()
