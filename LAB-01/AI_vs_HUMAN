import sys,random
def check_winner(game_board):
    if game_board[0][0] == game_board[0][1] == game_board[0][2]:
        if game_board[0][0]== game_board[0][1] == game_board[0][2]=='X':
            print("Computer won")
            return True
        elif game_board[0][0]== game_board[0][1] == game_board[0][2]=='O':
            print("Human won")
            return True
    elif game_board[1][0] == game_board[1][1] == game_board[1][2]:
        if game_board[1][0]== game_board[1][1] == game_board[1][2]=='X':
            print("Comp won")
            return True
        elif game_board[1][0]== game_board[1][1] == game_board[1][2]=='O':
            print("Human won")
            return True
    elif game_board[2][0] == game_board[2][1] == game_board[2][2]:
        if game_board[2][0]== game_board[2][1] == game_board[2][2]=='X':
            print("Comp won")
            return True
        elif game_board[2][0]== game_board[2][1] == game_board[2][2]=='O':
            print("Human won")
            return True
    
    elif game_board[0][0] == game_board[1][0] == game_board[2][0]:
        if game_board[0][0] == game_board[1][0] == game_board[2][0]=='X':
            print("Comp won")
            return True
        elif game_board[0][0] == game_board[1][0] == game_board[2][0]=='O':
            print("Human won")
            return True
    elif game_board[0][1] == game_board[1][1] == game_board[2][1]:
        if game_board[0][1] == game_board[1][1] == game_board[2][1]=='X':
            print("Comp won")
            return True
        elif game_board[0][1] == game_board[1][1] == game_board[2][1]=='O':
            print("Human won")
            return True
    elif game_board[0][2] == game_board[1][2] == game_board[2][2]:
        if game_board[0][2] == game_board[1][2] == game_board[2][2]=='X':
            print("Comp won")
            return True
        elif game_board[0][2] == game_board[1][2] == game_board[2][2]=='O':
            print("Human won")
            return True
   
    elif game_board[0][0]==game_board[1][1]==game_board[2][2]:
        if game_board[0][0]==game_board[1][1]==game_board[2][2]=='X':
            print("Comp won")
            return True
        elif game_board[0][0]==game_board[1][1]==game_board[2][2]=='O':
            print("Human won")
            return True
    
    elif game_board[0][2]==game_board[1][1]==game_board[2][0]:
        if game_board[2][0]==game_board[0][2]==game_board[1][1]=='X':
            print("Comp won")
            return True
        elif  game_board[2][0]==game_board[0][2]==game_board[1][1]=='O':
            print("Human won")
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
    
def play(game_board,pos,count,flag):   
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
    elif count==8 and not check_winner(game_board):
        print("Draw")
        display(game_board)
        print("GAME OVER")
        sys.exit()      

count = 0
compvshuman = [0,1]
positions =[1,2,3,4,5,6,7,8,9]
flag=True
game_board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
game_board_1=[['1','2','3'],['4','5','6'],['7','8','9']]
print("\n\n\t\t\t\tWELCOME TO A.I. TIC TAC TOE")
print("\n\nBOARD:")
display(game_board_1)
if random.choice(compvshuman)==0:
    print("Computer goes first")
    flag=True
else:
    print("Human goes first")
    flag=False
print("\nGAME BEGIN:")
for i in range(9):
    if flag:
        print("Computer's turn")
        pos = random.choice(positions)
        positions.remove(pos)
        play(game_board,pos,count,flag)
        print("\nGAME BOARD:\n")
        display(game_board)
        flag = False
    else:
        print("Human's turn")
        pos=int(input("Human enter option:"))
        if pos in positions:
            positions.remove(pos)
        else:
            pos=int(input("Invalid Input.Enter again...!\n"))
            positions.remove(pos)
        play(game_board,pos,count,flag)
        print("\nGAME BOARD:\n")
        display(game_board)
        flag = True
    count+=1
    
'''
OUTPUT:
    
    

                                WELCOME TO A.I. TIC TAC TOE


BOARD:
 1  |  2  |  3
----+-----+-----
 4  |  5  |  6
----+-----+-----
 7  |  8  |  9

Computer goes first

GAME BEGIN:
Computer's turn

GAME BOARD:

    |     |
----+-----+-----
    |  X  |
----+-----+-----
    |     |

Human's turn
Human enter option:1

GAME BOARD:

 O  |     |
----+-----+-----
    |  X  |
----+-----+-----
    |     |

Computer's turn

GAME BOARD:

 O  |     |
----+-----+-----
 X  |  X  |
----+-----+-----
    |     |

Human's turn
Human enter option:6

GAME BOARD:

 O  |     |
----+-----+-----
 X  |  X  |  O
----+-----+-----
    |     |

Computer's turn

GAME BOARD:

 O  |     |
----+-----+-----
 X  |  X  |  O
----+-----+-----
 X  |     |

Human's turn
Human enter option:3

GAME BOARD:

 O  |     |  O
----+-----+-----
 X  |  X  |  O
----+-----+-----
 X  |     |

Computer's turn

GAME BOARD:

 O  |  X  |  O
----+-----+-----
 X  |  X  |  O
----+-----+-----
 X  |     |

Human's turn
Human enter option:9
Human won
 O  |  X  |  O
----+-----+-----
 X  |  X  |  O
----+-----+-----
 X  |     |  O

GAME OVER
'''
