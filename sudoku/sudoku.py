import pygame
import random
import math
from pygame import mixer 

pygame.init()

#calculating answer
value = [[-1,7,-1,8,9,-1,-1,-1,-1],
        [-1,5,-1,-1,-1,-1,3,-1,4],
        [-1,2,-1,-1,4,-1,-1,1,-1],
        [5,6,8,9,-1,-1,4,7,2],
        [-1,-1,-1,6,-1,-1,-1,-1,-1],
        [1,-1,7,-1,5,-1,6,3,8],
        [7,3,-1,1,-1,2,-1,8,-1],
        [6,-1,-1,4,7,-1,1,-1,-1],
        [2,-1,9,-1,3,8,7,-1,6]]


def check_row(x,value,ans):

    if ans in value[x]:
        return False
    else:
        return True

def check_box(x,y,value,ans):
    Xcor = x//3
    Ycor = y//3
    
    if ans in value[(Xcor*3)][(Ycor*3):((Ycor+1)*3)] or ans in value[((Xcor*3)+1)][(Ycor*3):((Ycor+1)*3)] or ans in value[((Xcor*3)+2)][(Ycor*3):((Ycor+1)*3)]:
        return False
    else:
        return True
            
def check_col(y,value,ans):
    for j in range(9):        
        if ans == value[j][y]:
            return False
    return True
    
def check_for(x,y,value,ans):
    if check_box(x,y,value,ans) and check_col(y,value,ans) and check_row(x,value,ans):
        return True
    else:
        return False

        
        

def empty_locator(value,l):
    for i in range(9):
        for j in range(9):
            if value[i][j] == -1:
                l[0] = i
                l[1] = j
                return True
    return False


def solve(value):

    l=[0,0]

    # Ending condition
    if not empty_locator(value,l):
        return True

    for ans in range(1,10):
        
        if check_for(l[0],l[1],value,ans):
            value[l[0]][l[1]] = ans

            if solve(value):
                return True
            else:
                value[l[0]][l[1]] = -1
    return False

#PYGAME interface

solve(value)
screen = pygame.display.set_mode((576,576))
screen.fill((255, 255, 255))
rectX=0
rectY=0
size = 64
def section():
#vertical lines
    pygame.draw.line(screen, (0,0,0), (screen.get_width()/3,0),(screen.get_width()/3,screen.get_height()),5)
    pygame.draw.line(screen, (0,0,0), ((screen.get_width()*2)/3,0),((2*screen.get_width())/3,screen.get_height()),5)

#horizontal lines
    pygame.draw.line(screen, (0,0,0), (0,(screen.get_height()*2)/3),(screen.get_width(),(2*screen.get_height())/3),5)
    pygame.draw.line(screen, (0,0,0), (0,screen.get_height()/3),(screen.get_width(),screen.get_height()/3),5)

#permanent values
fixed_v = [
    [7,1,0], [8,3,0], [9,4,0] , 
    [5,1,1], [3,6,1] , [4,8,1],
    [2,1,2], [4,4,2] ,[1,7,2],
    [5,0,3],[6,1,3], [8,2,3] , [9,3,3],[4,6,3], [7,7,3] , [2,8,3],
    [6,3,4],
    [1,0,5] , [7,2,5] , [5,4,5] , [6,6,5], [3,7,5] , [8,8,5],
    [7,0,6] , [3,1,6] ,[1,3,6], [2,5,6] , [8,7,6],
    [6,0,7] , [4,3,7] , [7,4,7] ,[1,6,7],
    [2,0,8], [9,2,8], [3,4,8], [8,5,8] , [7,6,8], [6,8,8]
]

new_v = []
font = pygame.font.Font('freesansbold.ttf',40)

def show_grid(rectX,rectY):
    while rectY < 576 :
        pygame.draw.rect(screen,(0,0,0),(rectX,rectY,size,size),1)
        if rectX > 576:
            rectX = 0
            rectY += size
        else:
            rectX += size
#show pre-entered value
def show_fixed_value(val,fixed_valueX,fixed_valueY):
    fixed_valueX= fixed_valueX*64
    fixed_valueY= fixed_valueY*64
    fixed_val = font.render(str(val) ,True ,(0,0,0))
    screen.blit(fixed_val ,(fixed_valueX+15,fixed_valueY+15))

def show_input_no(val,Xcor,Ycor):
    Xcor= Xcor*64
    Ycor= Ycor*64
    input_val = font.render(val ,True ,(0,0,0))
    screen.blit(input_val ,(Xcor+15,Ycor+15))
Xcor = 0
Ycor = 0
input_no = ""
temp2=[]
already_present= False
already_present_in_new_v= False
right_answer = False
wrong_answer = False
running = True
while running:
    
    #drawing squares
    
    #screen.blit(background, (0,0))

    
    for event in pygame.event.get():
    #Termination
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if not already_present :    
                if event.key == pygame.K_RETURN:
                    #take input and save
                    new_v.append([int(input_no),Xcor,Ycor])
                    temp2= [int(input_no),Xcor,Ycor]
                    input_no=""
                    already_present_in_new_v=True
                    
                elif event.key == pygame.K_BACKSPACE:
                    input_no = ""
                else:
                    
                    temp1 = event.unicode
                    if not already_present_in_new_v:
                        input_no= temp1
                    else:
                        new_v.remove(temp2)
                        already_present_in_new_v=False
                        input_no=temp1
    screen.fill((255, 255, 255))

    show_grid(0,0)
    show_input_no(input_no,Xcor,Ycor)               
    section()
                
    
    
    #showing fixed values   
    for pos in fixed_v:
        val = pos[0]
        fixed_valueX = pos[1]
        fixed_valueY = pos[2]

        show_fixed_value(val , fixed_valueX , fixed_valueY)
    #selecting a box
    if pygame.mouse.get_pressed()[0]:
            
        xpos,ypos  = pygame.mouse.get_pos()
        pygame.draw.rect(screen,(0,0,0),((Xcor*64),(Ycor*64),size,size),2)
        already_present= False
        already_present_in_new_v = False
        right_answer = False
        wrong_answer =  False

        input_no=""
        Xcor = xpos//64
        Ycor = ypos//64
        for i in range(1,10):
            checker =[i,Xcor,Ycor]
            if checker in fixed_v:
                already_present = True
                break
            if checker in new_v:
                already_present_in_new_v = True
                temp2= checker


    if not already_present:    
        pygame.draw.rect(screen,(0,0,255),((Xcor*64),(Ycor*64),size,size),2)
    #showing new_v
    for pos in new_v:
        val = pos[0]
        fixed_valueX = pos[1]
        fixed_valueY = pos[2]
        if value[fixed_valueX][fixed_valueY] == val:
            right_answer=True
        else:
            wrong_answer= True
    show_fixed_value(val , fixed_valueX , fixed_valueY)
        
    

    if right_answer and not already_present:
        pygame.draw.rect(screen,(0,255,0),((Xcor*64),(Ycor*64),size,size),2)
    if wrong_answer and not already_present:
        pygame.draw.rect(screen,(255,0,0),((Xcor*64),(Ycor*64),size,size),2)
        
        

        
        




    pygame.display.update()