import pygame
import random
import math
from pygame import mixer 
#initialization
pygame.init()

#creat the screen
screen = pygame.display.set_mode((800,600))

#Title and Icon
#use flaticon for icon and download 32 px .png file
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("/data/ufo.png")
pygame.display.set_icon(icon)

#background
background = pygame.image.load('data/background.png')

#background sound
mixer.music.load("data/background.wav")
mixer.music.play(-1)
# Player
playerImg = pygame.image.load('data/player.png')
playerX =370
playerY = 480
playerX_change =0

# enemy
#multiple enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 6

for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load('data/enemy.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

    

#bullet

bulletImg = pygame.image.load("data/bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state= "ready"

#Score 

score_value =0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10
over_font = pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score = font.render("Score : " + str(score_value), True , (255,255,255))
    screen.blit(score, (x,y))

def game_over_text():
    got = over_font.render("GAME OVER", True , (255,255,255))
    screen.blit(got, (160 , 250))

#player function
def player(x,y):
    #blit means drawing
    screen.blit(playerImg ,(x,y))

#enemy function
def enemy(x,y,i):
    #blit means drawing
    screen.blit(enemyImg[i] ,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x + 16 , y + 10))

#collision
def is_collision(enemyX,enemyY,bulletX, bulletY ):
    distance =  math.sqrt( ((enemyX-bulletX)**2) + ((enemyY-bulletY)**2))
    if distance <= 27:
        return True
    else:
        return False
#Game Loop
running = True
while running:
    #Background colour
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))

    #Termination
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    
        #moving left and right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("data/laser.wav")
                    bullet_sound.play()
                    bulletX= playerX
                    fire_bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            playerX_change = 0


    # moving player
    playerX += playerX_change  

    if playerX <= 0:
        playerX=0
    elif playerX >=736:
        playerX=736
    
    #moving enemies
    for i in range(len(enemyImg)):

        #Game over
        if enemyY[i] > 400:
            for j in range(num_of_enemy):
                enemyY[j]= 2000
            game_over_text()    

        enemyX[i] += enemyX_change[i]  

        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >=736:
            enemyX_change[i] = -4
            enemyY[i] +=enemyY_change[i]

        collision = is_collision(enemyX[i],enemyY[i],bulletX, bulletY )
        if collision:
            collision_sound = mixer.Sound("data/explosion.wav")
            collision_sound.play()
            bulletY = 480
            bullet_state= "ready"
            score_value+=1
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(50,150)

        enemy(enemyX[i],enemyY[i],i)

    #bullet movement
    if bulletY <=0:
        bulletY=480
        bullet_state= "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    
    show_score(textX,textY)


    #call player
    player(playerX,playerY)
    
    #most important line in pygame
    pygame.display.update()


