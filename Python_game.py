
'''
Created on Sep 30, 2015

@author: Dhirendra
'''

def gridChar(i): 
    
    if(i==-1):
        return 'X';
    if(i==0):
        return ' ';
    if(i==1):
        return 'O';
    




def draw(b):
    print   str(gridChar(b[0]))+"   ,   "+str(gridChar(b[1]))+"   ,   "+ str(gridChar(b[2]))
    
    print str(gridChar(b[3]))+"   ,   "+str(gridChar(b[4]))+"   ,   "+ str(gridChar(b[5]))

    print  str(gridChar(b[6]))+"   ,   "+str(gridChar(b[7]))+"   ,   "+ str(gridChar(b[8]))




def checkboard(board):
    element=[]
    for i in range(0,8):
        element.append([])
    
    element[0].append(0)
    element[0].append(1)    
    element[0].append(2)
    element[1].append(3)
    element[1].append(4)
    element[1].append(5)
    element[2].append(6)
    element[2].append(7)
    element[2].append(8)
    element[3].append(0)
    element[3].append(3)
    element[3].append(6)
    element[4].append(1)
    element[4].append(4)    
    element[4].append(7)
    element[5].append(2)
    element[5].append(5)
    element[5].append(8)
    element[6].append(0)
    element[6].append(4)
    element[6].append(8)
    element[7].append(2)
    element[7].append(4)
    element[7].append(6)
    
    for i in range(0,8):
        if(board[element[i][0]] != 0 and (board[element[i][0]] == board[element[i][1]]) and (board[element[i][0]] == board[element[i][2]])):
            
            return board[element[i][2]]
    return 0    
    
    
def minimax(board,t):   #checks if a made a move before calling this functions what will be the best possbile move
    
    
    p=checkboard(board)
    if(p!=0):
        
        return t*p     # negative if first player wins (p==1 for him and t=-1 when he moves last) doesnt matter whose chance it was
    move=-1
    initialscore=-2;
    for i in range(0,9):
        if(board[i]==0):
            board[i]=t     #if first player chance then putting +1 else -1
            
            score=-minimax(board,(t*-1))
            '''print score'''
            if(score>initialscore):
                initialscore=score
                move=i;
            board[i]=0;     #making it zero for all possible combinations
            
    
    if(move==-1):return 0
    return initialscore









def movecomputer(board):
    
    move=-1
    initialscore=-2;
    for i in range(0,9):
        if(board[i]==0):
            board[i]=1
            score=-minimax(board,-1)
            
              
            board[i]=0
            if(score>initialscore):
                initialscore=score
                move=i
    
    board[move]=1
            

def movehuman(board):
    input1=15
    while(input1<0 or input1>8 or board[input1]!=0):
        input1=input("enter the square number where u want to put x(0...8)\n")
    
    
    
    board[input1]=-1
        







def main():
    board=[0,0,0,0,0,0,0,0,0]
    
    player=input("enter 1 if you want to play first or 2  for second\n")
    print "you will play as X and computer as 0\n"
    
    i=0;
    while(i<9 and checkboard(board)==0):
        
        if((i+player)%2==0):
            movecomputer(board)
            
        else:
            
            draw(board)
            movehuman(board)
        i=i+1   
        
    if(checkboard(board)==-1):
        print "human wins\n"
        draw(board)
    elif(checkboard(board)==1):
        print "machine wins wins\n"
        draw(board)
    else:
        print "it's a draw\n"
        draw(board)
                   
                
                   
    
    
    
if __name__=='__main__':
    main()    
    
    


