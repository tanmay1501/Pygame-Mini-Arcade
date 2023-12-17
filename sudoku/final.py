import pygame as pg
from pygame import mixer
import time




#QUESTION

fixed_values = [[-1,7,-1,8,9,-1,-1,-1,-1],
        [-1,5,-1,-1,-1,-1,3,-1,4],
        [-1,2,-1,-1,4,-1,-1,1,-1],
        [5,6,8,9,-1,-1,4,7,2],
        [-1,-1,-1,6,-1,-1,-1,-1,-1],
        [1,-1,7,-1,5,-1,6,3,8],
        [7,3,-1,1,-1,2,-1,8,-1],
        [6,-1,-1,4,7,-1,1,-1,-1],
        [2,-1,9,-1,3,8,7,-1,6]]

#creating fixed values for pygame
value = [[-1,7,-1,8,9,-1,-1,-1,-1],
        [-1,5,-1,-1,-1,-1,3,-1,4],
        [-1,2,-1,-1,4,-1,-1,1,-1],
        [5,6,8,9,-1,-1,4,7,2],
        [-1,-1,-1,6,-1,-1,-1,-1,-1],
        [1,-1,7,-1,5,-1,6,3,8],
        [7,3,-1,1,-1,2,-1,8,-1],
        [6,-1,-1,4,7,-1,1,-1,-1],
        [2,-1,9,-1,3,8,7,-1,6]]
'''
for i in range(9):
    for j in range(9):
        if value[i][j] != -1:
            loc = [value[i][j],j,i]
            fixed_values.append(loc)   
'''  

#getting ans using backtracking

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
def show_fixed_value():
    for i in range(9):
        for  j in range(9):
            if fixed_values[i][j] != -1:
                val = fixed_values[i][j]
                fixed_valueX = j
                fixed_valueY = i
                fixed_valueX= fixed_valueX*64
                fixed_valueY= fixed_valueY*64
                fixed_val = font.render(str(val) ,True ,(0,0,0))
                screen.blit(fixed_val ,(fixed_valueX+15,fixed_valueY+15))



def solve_showing_off(value):
    
    l=[0,0]

    # Ending condition
    if not empty_locator(value,l):
        return True

    for ans in range(1,10):
        
        if check_for(l[0],l[1],value,ans):
            value[l[0]][l[1]] = ans
            #show_fixed_value()
            #time.sleep(0.1)
            if solve_showing_off(value):
                return True
            else:
                value[l[0]][l[1]] = -1
    return False

#Calling the method to get the answer
solve(value)

#####################################################################################################
############################################################################################################



#initialisation
pg.init()
#making a screen
screen = pg.display.set_mode((576,576))

#making variable for input values
user_answers = [[-1,7,-1,8,9,-1,-1,-1,-1],
        [-1,5,-1,-1,-1,-1,3,-1,4],
        [-1,2,-1,-1,4,-1,-1,1,-1],
        [5,6,8,9,-1,-1,4,7,2],
        [-1,-1,-1,6,-1,-1,-1,-1,-1],
        [1,-1,7,-1,5,-1,6,3,8],
        [7,3,-1,1,-1,2,-1,8,-1],
        [6,-1,-1,4,7,-1,1,-1,-1],
        [2,-1,9,-1,3,8,7,-1,6]]

#size of a grid 64*64
size = 64

#font maker
font = pg.font.Font('freesansbold.ttf',40)
#making lines
def section():
    #vertical lines
    pg.draw.line(screen, (0,0,0), (screen.get_width()/3,0),(screen.get_width()/3,screen.get_height()),5)
    pg.draw.line(screen, (0,0,0), ((screen.get_width()*2)/3,0),((2*screen.get_width())/3,screen.get_height()),5)

    #horizontal lines
    pg.draw.line(screen, (0,0,0), (0,(screen.get_height()*2)/3),(screen.get_width(),(2*screen.get_height())/3),5)
    pg.draw.line(screen, (0,0,0), (0,screen.get_height()/3),(screen.get_width(),screen.get_height()/3),5)


    
#making squares
def show_grid(rectX,rectY):
    while rectY < 576 :
        pg.draw.rect(screen,(0,0,0),(rectX,rectY,size,size),1)
        if rectX > 576:
            rectX = 0
            rectY += size
        else:
            rectX += size



def right_answer(val,i,j):
    if value[i][j] == val:
        return True
    else:
        return False


def show_user_answer():
    right_colour = (0,0,155)
    wrong_colour = (155,0,0)
    for i in range(9):
        for  j in range(9):
            if user_answers[i][j] != -1 and user_answers[i][j] != fixed_values[i][j]:
                val = user_answers[i][j]
                userX = j
                userY = i
                userX= userX*64
                userY= userY*64
                if right_answer(val,i,j):
                    user_val = font.render(str(val) ,True ,right_colour)
                else:
                    user_val = font.render(str(val) ,True ,wrong_colour)
                
                screen.blit(user_val ,(userX+15,userY+15))




running = True
already_present= False
already_present_in_user_answer = False
locX =0
locY =0
while running:

    #mentioning all the clicking event
    for event in pg.event.get():
        #Tremination
        if event.type == pg.QUIT:
            running = False
        if pg.mouse.get_pressed()[0]:

            cursorX,cursorY = pg.mouse.get_pos()
            #reset conditions
            already_present = False
            already_present_in_user_answer = False 
            input_no = ""
            locX = cursorX//64
            locY = cursorY//64    
            
            if fixed_values[locY][locX] != -1: 
                already_present = True
            
            if user_answers[locY][locX] != -1:
                already_present_in_user_answer = True
            
            #entering no
        if event.type == pg.KEYDOWN:
            #if event.key == pg.K_SPACE:
                #back_tracking()
                

            if not already_present :
                
                
                if event.key == pg.K_BACKSPACE:
                    user_answers[locY][locX] = -1
                else:
                    
                    temp1 = event.unicode
                    
                    input_no = temp1
                    numbers=['1','2','3','4','5','6','7','8','9']
                    if input_no in numbers:
                        user_answers[locY][locX] = int(input_no)
                    #print(user_answers[locY][locX])
                        

    
    #execution
        
    screen.fill((255,255,255))
    section()
    show_grid(0,0)
    show_fixed_value()
    
    #making the selected box blue
    if not already_present:    
        pg.draw.rect(screen,(0,0,255),((locX*64),(locY*64),size,size),2)
    
    #showing uservalues
    show_user_answer()

    
    pg.display.update()