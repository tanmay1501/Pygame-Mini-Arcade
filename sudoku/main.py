import random
import math

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
        
            
         


for i in value:
    print(*i)

solve(value)

for i in value:
    print(*i)

    


