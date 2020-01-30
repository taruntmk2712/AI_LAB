import random
def check_winner(game_board):
    if game_board[0][0] == game_board[0][1] == game_board[0][2]:
        if game_board[0][0]=='X':
           return "Player 1 Winner"
        elif game_board[0][0]=='O':
            return "Player 2 Winner"
    if game_board[1][0] == game_board[1][1] == game_board[1][2]:
        if game_board[0][0]=='X':
           return "Player 1 Winner"
        elif game_board[0][0]=='O':
            return "Player 2 Winner"
    if game_board[2][0] == game_board[2][1] == game_board[2][2]:
        if game_board[0][0]=='X':
           return "Player 1 Winner"
        elif game_board[0][0]=='O':
            return "Player 2 Winner"
    
    if game_board[0][0] == game_board[1][0] == game_board[2][0]:
        if game_board[0][0]=='X':
           return "Player 1 Winner"
        elif game_board[0][0]=='O':
            return "Player 2 Winner"
    if game_board[0][1] == game_board[1][1] == game_board[2][1]:
        if game_board[0][1]=='X':
           return "Player 1 Winner"
        elif game_board[0][1]=='O':
            return "Player 2 Winner"
    if game_board[0][2] == game_board[1][2] == game_board[2][2]:
        if game_board[0][2]=='X':
           return "Player 1 Winner"
        elif game_board[0][2]=='O':
            return "Player 2 Winner"
   
    if game_board[0][0]==game_board[1][1]==game_board[2][2] or game_board[0][2]==game_board[1][1]==game_board[2][0]:
        if game_board[0][0]=='X' or game_board[2][0]=='X':
            return "Player 1 Winner"
        elif game_board[0][0]=='O' or game_board[2][0]=='O':
            return "Player 2 Winner"
    else:
        return "Draw/Tie"

def display(game_board):
    for i in range(3):
        for j in range(3):
            print(game_board[i][j],end='  ')
        print("\n")
    

def play_game():
    game_board=[[None,None,None],[None,None,None],[None,None,None]]
    count=0
    a=['X','O','~']
    for i in range(3):
        for j in range(3):
            game_board[i][j]=random.choice(a)
    winner=check_winner(game_board)
    display(game_board)
    print(winner)
                    
        

play_game()
