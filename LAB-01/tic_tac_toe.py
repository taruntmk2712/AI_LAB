import sys
def check_winner(game_board,count):
    if game_board[0][0] == game_board[0][1] == game_board[0][2]:
        if game_board[0][0]== game_board[0][1] == game_board[0][2]=='X':
            print("Player 1 won")
            return True
        elif game_board[0][0]== game_board[0][1] == game_board[0][2]=='O':
            print("Player 2 won")
            return True
    elif game_board[1][0] == game_board[1][1] == game_board[1][2]:
        if game_board[1][0]== game_board[1][1] == game_board[1][2]=='X':
            print("Player 1 won")
            return True
        elif game_board[1][0]== game_board[1][1] == game_board[1][2]=='O':
            print("Player 2 won")
            return True
    elif game_board[2][0] == game_board[2][1] == game_board[2][2]:
        if game_board[2][0]== game_board[2][1] == game_board[2][2]=='X':
            print("Player 1 won")
            return True
        elif game_board[2][0]== game_board[2][1] == game_board[2][2]=='O':
            print("Player 2 won")
            return True
    
    elif game_board[0][0] == game_board[1][0] == game_board[2][0]:
        if game_board[0][0] == game_board[1][0] == game_board[2][0]=='X':
            print("Player 1 won")
            return True
        elif game_board[0][0] == game_board[1][0] == game_board[2][0]=='O':
            print("Player 2 won")
            return True
    elif game_board[0][1] == game_board[1][1] == game_board[2][1]:
        if game_board[0][1] == game_board[1][1] == game_board[2][1]=='X':
            print("Player 1 won")
            return True
        elif game_board[0][1] == game_board[1][1] == game_board[2][1]=='O':
            print("Player 2 won")
            return True
    elif game_board[0][2] == game_board[1][2] == game_board[2][2]:
        if game_board[0][2] == game_board[1][2] == game_board[2][2]=='X':
            print("Player 1 won")
            return True
        elif game_board[0][2] == game_board[1][2] == game_board[2][2]=='O':
            print("Player 2 won")
            return True
   
    elif game_board[0][0]==game_board[1][1]==game_board[2][2]:
        if game_board[0][0]==game_board[1][1]==game_board[2][2]=='X':
            print("Player 1 won")
            return True
        elif game_board[0][0]==game_board[1][1]==game_board[2][2]=='O':
            print("Player 2 won")
            return True
    
    elif game_board[0][2]==game_board[1][1]==game_board[2][0]:
        if game_board[2][0]==game_board[0][2]==game_board[1][1]=='X':
            print("Player 1 won")
            return True
        elif  game_board[2][0]==game_board[0][2]==game_board[1][1]=='O':
            print("Player 2 won")
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
    
def play(game_board,pos,count):   
    if pos==1:
        if count%2==0:
            game_board[0][0]='X'
        elif count%2==1:
            game_board[0][0]='O'
    elif pos==2:
        if count%2==0:
            game_board[0][1]='X'
        elif count%2==1:
            game_board[0][1]='O'
    elif pos==3:
        if count%2==0:
            game_board[0][2]='X'
        elif count%2==1:
            game_board[0][2]='O'
    elif pos==4:
        if count%2==0:
            game_board[1][0]='X'
        elif count%2==1:
            game_board[1][0]='O'
    elif pos==5:
        if count%2==0:
            game_board[1][1]='X'
        elif count%2==1:
            game_board[1][1]='O'
    elif pos==6:
        if count%2==0:
            game_board[1][2]='X'
        elif count%2==1:
            game_board[1][2]='O'
    elif pos==7:
        if count%2==0:
            game_board[2][0]='X'
        elif count%2==1:
            game_board[2][0]='O'
    elif pos==8:
        if count%2==0:
            game_board[2][1]='X'
        elif count%2==1:
            game_board[2][1]='O'
    elif pos==9:
        if count%2==0:
            game_board[2][2]='X'
        elif count%2==1:
            game_board[2][2]='O'
    
    if check_winner(game_board,count):
        display(game_board)
        print("Game Over")
        sys.exit()
    elif count==8 and not check_winner(game_board,count):
        print("Draw")
        display(game_board)
        print("Game Over")
        sys.exit()      

count = 0
positions =[1,2,3,4,5,6,7,8,9]
verif=[]
game_board=[['~','~','~'],['~','~','~'],['~','~','~']]
for i in range(9):
    display(game_board)
    print("Position you want to enter Player",count%2+1)
    pos=int(input())
    if pos in positions:
        if pos not in verif:
            verif.append(pos)
        else:
            pos=int(input("Invalid Input.Enter again...!\n"))
    play(game_board,pos,count)
    count+=1
'''
OUTPUT:
#Player 1 Win Condition
 ~  |  ~  |  ~
----+-----+-----
 ~  |  ~  |  ~
----+-----+-----
 ~  |  ~  |  ~

Position you want to enter Player 1
1
 X  |  ~  |  ~
----+-----+-----
 ~  |  ~  |  ~
----+-----+-----
 ~  |  ~  |  ~

Position you want to enter Player 2
2
 X  |  O  |  ~
----+-----+-----
 ~  |  ~  |  ~
----+-----+-----
 ~  |  ~  |  ~

Position you want to enter Player 1
3
 X  |  O  |  X
----+-----+-----
 ~  |  ~  |  ~
----+-----+-----
 ~  |  ~  |  ~

Position you want to enter Player 2
4
 X  |  O  |  X
----+-----+-----
 O  |  ~  |  ~
----+-----+-----
 ~  |  ~  |  ~

Position you want to enter Player 1
5
 X  |  O  |  X
----+-----+-----
 O  |  X  |  ~
----+-----+-----
 ~  |  ~  |  ~

Position you want to enter Player 2
6
 X  |  O  |  X
----+-----+-----
 O  |  X  |  O
----+-----+-----
 ~  |  ~  |  ~

Position you want to enter Player 1
8
 X  |  O  |  X
----+-----+-----
 O  |  X  |  O
----+-----+-----
 ~  |  X  |  ~

Position you want to enter Player 2
7
 X  |  O  |  X
----+-----+-----
 O  |  X  |  O
----+-----+-----
 O  |  X  |  ~

Position you want to enter Player 1
9
Player 1 won
 X  |  O  |  X
----+-----+-----
 O  |  X  |  O
----+-----+-----
 O  |  X  |  X

Game Over

#Draw Condition
 ~  |  ~  |  ~
----+-----+-----
 ~  |  ~  |  ~
----+-----+-----
 ~  |  ~  |  ~

Position you want to enter Player 1
1
 X  |  ~  |  ~
----+-----+-----
 ~  |  ~  |  ~
----+-----+-----
 ~  |  ~  |  ~

Position you want to enter Player 2
2
 X  |  O  |  ~
----+-----+-----
 ~  |  ~  |  ~
----+-----+-----
 ~  |  ~  |  ~

Position you want to enter Player 1
3
 X  |  O  |  X
----+-----+-----
 ~  |  ~  |  ~
----+-----+-----
 ~  |  ~  |  ~

Position you want to enter Player 2
9
 X  |  O  |  X
----+-----+-----
 ~  |  ~  |  ~
----+-----+-----
 ~  |  ~  |  O

Position you want to enter Player 1
8
 X  |  O  |  X
----+-----+-----
 ~  |  ~  |  ~
----+-----+-----
 ~  |  X  |  O

Position you want to enter Player 2
7
 X  |  O  |  X
----+-----+-----
 ~  |  ~  |  ~
----+-----+-----
 O  |  X  |  O

Position you want to enter Player 1
4
 X  |  O  |  X
----+-----+-----
 X  |  ~  |  ~
----+-----+-----
 O  |  X  |  O

Position you want to enter Player 2
5
 X  |  O  |  X
----+-----+-----
 X  |  O  |  ~
----+-----+-----
 O  |  X  |  O

Position you want to enter Player 1
6
Draw
 X  |  O  |  X
----+-----+-----
 X  |  O  |  X
----+-----+-----
 O  |  X  |  O

Game Over

#Player 2 Win Condition
 ~  |  ~  |  ~
----+-----+-----
 ~  |  ~  |  ~
----+-----+-----
 ~  |  ~  |  ~

Position you want to enter Player 1
1
 X  |  ~  |  ~
----+-----+-----
 ~  |  ~  |  ~
----+-----+-----
 ~  |  ~  |  ~

Position you want to enter Player 2
9
 X  |  ~  |  ~
----+-----+-----
 ~  |  ~  |  ~
----+-----+-----
 ~  |  ~  |  O

Position you want to enter Player 1
5
 X  |  ~  |  ~
----+-----+-----
 ~  |  X  |  ~
----+-----+-----
 ~  |  ~  |  O

Position you want to enter Player 2
7
 X  |  ~  |  ~
----+-----+-----
 ~  |  X  |  ~
----+-----+-----
 O  |  ~  |  O

Position you want to enter Player 1
4
 X  |  ~  |  ~
----+-----+-----
 X  |  X  |  ~
----+-----+-----
 O  |  ~  |  O

Position you want to enter Player 2
8
Player 2 won
 X  |  ~  |  ~
----+-----+-----
 X  |  X  |  ~
----+-----+-----
 O  |  O  |  O

Game Over
'''
