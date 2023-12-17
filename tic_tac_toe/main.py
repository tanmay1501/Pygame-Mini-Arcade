import pygame


#INITIALISATION
pygame.init()

#SCREEN
screen = pygame.display.set_mode((400,400))
screen.fill((255,255,255))

#vertical lines
pygame.draw.line(screen, (0,0,0), (screen.get_width()/3,0),(screen.get_width()/3,screen.get_height()),5)
pygame.draw.line(screen, (0,0,0), ((screen.get_width()*2)/3,0),((2*screen.get_width())/3,screen.get_height()),5)

#horizontal lines
pygame.draw.line(screen, (0,0,0), (0,(screen.get_height()*2)/3),(screen.get_width(),(2*screen.get_height())/3),5)
pygame.draw.line(screen, (0,0,0), (0,screen.get_height()/3),(screen.get_width(),screen.get_height()/3),5)


#SET NAME AND ICON
pygame.display.set_caption("TIC-TAC-TOE")
icon = pygame.image.load("tic_tac_toe/tic-tac-toe.png")
pygame.display.set_icon(icon)


#CROSS
crossImage= pygame.image.load("tic_tac_toe/cross.png")
crossX=70
crossY=70

#circle
circleImage= pygame.image.load("tic_tac_toe/circle.png")
circleX=50
circleY=50


#game loop
running= True
while running:
    
    #TERMINATION     
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False 

        if event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos
            circleX, circleY = pos  # update circle's position

    # Draw a circle at the new position
    pygame.draw.circle(screen, (255, 0, 0), (circleX, circleY), 50)

    pygame.display.update()
