import sys,random
def check_winner(game_board):
    if game_board[0][0] == game_board[0][1] == game_board[0][2]:
        if game_board[0][0]== game_board[0][1] == game_board[0][2]=='X':
            print("\nComputer won\n")
            return True
        elif game_board[0][0]== game_board[0][1] == game_board[0][2]=='O':
            print("\nHuman won\n")
            return True
    elif game_board[1][0] == game_board[1][1] == game_board[1][2]:
        if game_board[1][0]== game_board[1][1] == game_board[1][2]=='X':
            print("\nComputer won\n")
            return True
        elif game_board[1][0]== game_board[1][1] == game_board[1][2]=='O':
            print("Human won\n")
            return True
    elif game_board[2][0] == game_board[2][1] == game_board[2][2]:
        if game_board[2][0]== game_board[2][1] == game_board[2][2]=='X':
            print("\nComputer won\n")
            return True
        elif game_board[2][0]== game_board[2][1] == game_board[2][2]=='O':
            print("\nHuman won\n")
            return True
    
    elif game_board[0][0] == game_board[1][0] == game_board[2][0]:
        if game_board[0][0] == game_board[1][0] == game_board[2][0]=='X':
            print("\nComputer won\n")
            return True
        elif game_board[0][0] == game_board[1][0] == game_board[2][0]=='O':
            print("\nHuman won")
            return True
    elif game_board[0][1] == game_board[1][1] == game_board[2][1]:
        if game_board[0][1] == game_board[1][1] == game_board[2][1]=='X':
            print("\nComputer won\n")
            return True
        elif game_board[0][1] == game_board[1][1] == game_board[2][1]=='O':
            print("\nHuman won\n")
            return True
    elif game_board[0][2] == game_board[1][2] == game_board[2][2]:
        if game_board[0][2] == game_board[1][2] == game_board[2][2]=='X':
            print("\nComputer won\n")
            return True
        elif game_board[0][2] == game_board[1][2] == game_board[2][2]=='O':
            print("\nHuman won\n")
            return True
   
    elif game_board[0][0]==game_board[1][1]==game_board[2][2]:
        if game_board[0][0]==game_board[1][1]==game_board[2][2]=='X':
            print("\nComputer won\n")
            return True
        elif game_board[0][0]==game_board[1][1]==game_board[2][2]=='O':
            print("\nHuman won\n")
            return True
    
    elif game_board[0][2]==game_board[1][1]==game_board[2][0]:
        if game_board[2][0]==game_board[0][2]==game_board[1][1]=='X':
            print("\nComputer won\n")
            return True
        elif  game_board[2][0]==game_board[0][2]==game_board[1][1]=='O':
            print("\nHuman won\n")
            return True
    else:
        return False

def win_possibilities(game_board):
    if game_board[0][0] == game_board[0][1] == game_board[0][2]=='O':
        return True
    elif game_board[1][0] == game_board[1][1] == game_board[1][2]=='O':
        return True
    elif game_board[2][0] == game_board[2][1] == game_board[2][2]=='O':
        return True

    elif game_board[0][0] == game_board[1][0] == game_board[2][0]=='O':
        return True
    elif game_board[0][1] == game_board[1][1] == game_board[2][1]=='O':
        return True
    elif game_board[0][2] == game_board[1][2] == game_board[2][2]=='O':
        return True
   
    elif game_board[0][0]==game_board[1][1]==game_board[2][2]=='O':
        return True
    elif  game_board[2][0]==game_board[0][2]==game_board[1][1]=='O':
        return True
    else:
        return False

def display(game_board): 
    for i in range(3):
        if i>=1:
            print("\n----+-----+-----")
        for j in range(3):
            if j>=1:
                print(" |",end=' ')
            print(" "+game_board[i][j],end=' ')
    print("\n")
    
def play(game_board,pos,flag):   
    if pos==1:
        if flag:
            game_board[0][0]='X'
        elif not flag:
            game_board[0][0]='O'
    elif pos==2:
        if flag:
            game_board[0][1]='X'
        elif not flag:
            game_board[0][1]='O'
    elif pos==3:
        if flag:
            game_board[0][2]='X'
        elif not flag:
            game_board[0][2]='O'
    elif pos==4:
        if flag:
            game_board[1][0]='X'
        elif not flag:
            game_board[1][0]='O'
    elif pos==5:
        if flag:
            game_board[1][1]='X'
        elif not flag:
            game_board[1][1]='O'
    elif pos==6:
        if flag:
            game_board[1][2]='X'
        elif not flag:
            game_board[1][2]='O'
    elif pos==7:
        if flag:
            game_board[2][0]='X'
        elif not flag:
            game_board[2][0]='O'
    elif pos==8:
        if flag:
            game_board[2][1]='X'
        elif not flag:
            game_board[2][1]='O'
    elif pos==9:
        if flag:
            game_board[2][2]='X'
        elif not flag:
            game_board[2][2]='O'  
    
    if check_winner(game_board):
        display(game_board)
        print("GAME OVER")
        sys.exit()
    '''elif count==1 and not check_winner(game_board):
        print("Draw")
        display(game_board)
        print("GAME OVER")
        sys.exit()'''

countD = 0
compvshuman = [0,1]
positions =[1,2,3,4,5,6,7,8,9]
flag=True
pos=0
game_board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
game_board_1=[['1','2','3'],['4','5','6'],['7','8','9']]
print("\n\n\t\t\t\t\tWELCOME TO A.I. TIC TAC TOE")
print("\n\nBOARD:")
display(game_board_1)
#level =input(("Enter Difficulty Level(E/H)"))
if random.choice(compvshuman)==0:
    print("\nComputer goes first")
    flag=True
else:
    print("\nHuman goes first")
    flag=False
print("\nGAME BEGIN:")
for i in range(9):
    if flag:
        print("\nComputer's turn")
        for j in positions:
            pos=None
            if j==1:
                game_board[0][0]='O'
                if win_possibilities(game_board):
                    pos=j
                    game_board[0][0]=' '
                    positions.remove(pos)
                    break
                else:
                    game_board[0][0]=' '
                    #continue
            if j==2:
                game_board[0][1]='O'
                if win_possibilities(game_board):
                    pos=j
                    game_board[0][1]=' '
                    positions.remove(pos)
                    break
                else:
                    game_board[0][1]=' '
                    #continue
            if j==3:
                game_board[0][2]='O'
                if win_possibilities(game_board):
                    pos=j
                    game_board[0][2]=' '
                    positions.remove(pos)
                    break
                else:
                    game_board[0][2]=' '
                    #continue
            if j==4:
                game_board[1][0]='O'
                if win_possibilities(game_board):
                    pos=j
                    game_board[1][0]=' '
                    positions.remove(pos)
                    break
                else:
                    game_board[1][0]=' '
                    #continue
            if j==5:
                game_board[1][1]='O'
                if win_possibilities(game_board):
                    pos=j
                    game_board[1][1]=' '
                    positions.remove(pos)
                    break
                else:
                    game_board[1][1]=' '
                    #continue
            if j==6:
                game_board[1][2]='O'
                if win_possibilities(game_board):
                    pos=j
                    game_board[1][2]=' '
                    positions.remove(pos)
                    break
                else:
                    game_board[1][2]=' '
                    #continue
            if j==7:
                game_board[2][0]='O'
                if win_possibilities(game_board):
                    pos=j
                    game_board[2][0]=' '
                    positions.remove(pos)
                    break
                else:
                    game_board[2][0]=' '
                    #continue
            if j==8:
                game_board[2][1]='O'
                if win_possibilities(game_board):
                    pos=j
                    game_board[2][1]=' '
                    positions.remove(pos)
                    break
                else:
                    game_board[2][1]=' '
            if j==9:
                game_board[2][2]='O'
                if win_possibilities(game_board):
                    pos=j
                    game_board[2][2]=' '
                    positions.remove(pos)
                    break
                else:
                    game_board[2][2]=' '
        if pos == None:
            pos = random.choice(positions)
            positions.remove(pos)
        play(game_board,pos,flag)
        print("\nGAME BOARD:\n")
        display(game_board)
        flag = False
    elif not flag:
        print("\nHuman's turn")
        pos=int(input("\nHuman enter option:"))
        if pos in positions:
            positions.remove(pos)
        else:
            pos=int(input("\nInvalid Input.Enter again...!"))
            positions.remove(pos)
        play(game_board,pos,flag)
        print("\nGAME BOARD:\n")
        display(game_board)
        flag = True   

for i in range(3):
    for j in range(3):
        if game_board[i][j] != ' ':
            countD+=1
if countD == 9:
    print("\nDraw\n\nGAME OVER")
 
'''
OUTPUT:

#HUMAN WIN CONDITION


                                        WELCOME TO A.I. TIC TAC TOE


BOARD:
 1  |  2  |  3
----+-----+-----
 4  |  5  |  6
----+-----+-----
 7  |  8  |  9


Human goes first

GAME BEGIN:

Human's turn

Human enter option:1

GAME BOARD:

 O  |     |
----+-----+-----
    |     |
----+-----+-----
    |     |


Computer's turn

GAME BOARD:

 O  |     |
----+-----+-----
    |  X  |
----+-----+-----
    |     |


Human's turn

Human enter option:9

GAME BOARD:

 O  |     |
----+-----+-----
    |  X  |
----+-----+-----
    |     |  O


Computer's turn

GAME BOARD:

 O  |  X  |
----+-----+-----
    |  X  |
----+-----+-----
    |     |  O


Human's turn

Human enter option:7

GAME BOARD:

 O  |  X  |
----+-----+-----
    |  X  |
----+-----+-----
 O  |     |  O


Computer's turn

GAME BOARD:

 O  |  X  |
----+-----+-----
 X  |  X  |
----+-----+-----
 O  |     |  O


Human's turn

Human enter option:8

Human won

 O  |  X  |
----+-----+-----
 X  |  X  |
----+-----+-----
 O  |  O  |  O

GAME OVER




#COMPUTER WIN CONDITION


                                        WELCOME TO A.I. TIC TAC TOE


BOARD:
 1  |  2  |  3
----+-----+-----
 4  |  5  |  6
----+-----+-----
 7  |  8  |  9


Human goes first

GAME BEGIN:

Human's turn

Human enter option:1

GAME BOARD:

 O  |     |
----+-----+-----
    |     |
----+-----+-----
    |     |


Computer's turn

GAME BOARD:

 O  |     |
----+-----+-----
    |  X  |
----+-----+-----
    |     |


Human's turn

Human enter option:6

GAME BOARD:

 O  |     |
----+-----+-----
    |  X  |  O
----+-----+-----
    |     |


Computer's turn

GAME BOARD:

 O  |     |
----+-----+-----
 X  |  X  |  O
----+-----+-----
    |     |


Human's turn

Human enter option:2

GAME BOARD:

 O  |  O  |
----+-----+-----
 X  |  X  |  O
----+-----+-----
    |     |


Computer's turn

GAME BOARD:

 O  |  O  |  X
----+-----+-----
 X  |  X  |  O
----+-----+-----
    |     |


Human's turn

Human enter option:9

GAME BOARD:

 O  |  O  |  X
----+-----+-----
 X  |  X  |  O
----+-----+-----
    |     |  O


Computer's turn

Computer won

 O  |  O  |  X
----+-----+-----
 X  |  X  |  O
----+-----+-----
 X  |     |  O

GAME OVER



#DRAW CONDITION

                                        WELCOME TO A.I. TIC TAC TOE


BOARD:
 1  |  2  |  3
----+-----+-----
 4  |  5  |  6
----+-----+-----
 7  |  8  |  9


Human goes first

GAME BEGIN:

Human's turn

Human enter option:5

GAME BOARD:

    |     |
----+-----+-----
    |  O  |
----+-----+-----
    |     |


Computer's turn

GAME BOARD:

    |     |
----+-----+-----
 X  |  O  |
----+-----+-----
    |     |


Human's turn

Human enter option:1

GAME BOARD:

 O  |     |
----+-----+-----
 X  |  O  |
----+-----+-----
    |     |


Computer's turn

GAME BOARD:

 O  |     |
----+-----+-----
 X  |  O  |
----+-----+-----
    |     |  X


Human's turn

Human enter option:3

GAME BOARD:

 O  |     |  O
----+-----+-----
 X  |  O  |
----+-----+-----
    |     |  X


Computer's turn

GAME BOARD:

 O  |  X  |  O
----+-----+-----
 X  |  O  |
----+-----+-----
    |     |  X


Human's turn

Human enter option:8

GAME BOARD:

 O  |  X  |  O
----+-----+-----
 X  |  O  |
----+-----+-----
    |  O  |  X


Computer's turn

GAME BOARD:

 O  |  X  |  O
----+-----+-----
 X  |  O  |
----+-----+-----
 X  |  O  |  X


Human's turn

Human enter option:6

GAME BOARD:

 O  |  X  |  O
----+-----+-----
 X  |  O  |  O
----+-----+-----
 X  |  O  |  X


Draw

GAME OVER
