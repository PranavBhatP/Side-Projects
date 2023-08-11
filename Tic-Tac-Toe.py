#Tic Tac Toe
#Objectives in this project
#2 players should be able to play this game on the same computer
#The board should be printed out every time a player makes a move
#You should be able to  accept input of the user and place a symbol on the board.

from IPython.display import clear_output
import random
test_board = ['X','O','X','O','X','O','X','O','X']
initial_board = ['', '', '', '', '', '','', '','']
board_entry = []
def display_board(board):
    board_outlay =  """ 
                     {a} | {b} | {c}
                     ------
                     {d} | {e} | {f}    
                     ------
                     {g} | {h} | {i}

                    """.format(a = board[0], b= board[1],c = board[2], d = board[3], e = board[4], f = board[5], g = board[6], h = board[7], i = board[8])
    print(board_outlay)



def player_input():

    while p1 not in ['X','O']:
        p1= input("Player 1, choose your symbol: X or O: ")
        if p1 not in ['X','O']:
            print("Player 1, enter the correct symbol: X or O: ")
    
    if p1 == "X":
        p2 = 'O'
    else:
        p2 = 'X'
    return p1, p2

def place_marker(board, marker, positon):
    board[positon-1] = marker

def win_check(board, marker):
    #There are 3+3+2 possibilities for a symbol to win.
    return (board[0] == marker and board[1] == marker and board[2] == marker) or (board[3] == marker and board[4] == marker and board[5] == marker) or (board[6] == marker and board[7] == marker and board[8] == marker) or (board[0] == marker and board[4] == marker and board[7] == marker and board[8] == marker) or (board[2] == marker and board[4] == marker and board[6] == marker) or (board[0] == marker and board[3] == marker and board[6] == marker) or (board[1] == marker and board[4] == marker and board[7] == marker) or (board[2] == marker and board[5] == marker and board[8] == marker)
    
def choose_first():
    randno = random.randint(1,2)
    if randno == 1:
        print("Player 1 goes first")
    else:
        print("Player 2 goes first")
    return randno

def space_check(board, position):
    return board[position-1] == ''

def full_board_check(board):
    for i in board:
        if i == '':
            return False
    return True

def player_choice(board, player):
    choice = "something"
    while choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        choice = input("Player {} ,Please enter a position from 1-9:".format(str(player)))
        if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Player {} ,Enter the position from 1-9 correctly:".format(str(player)))
    if space_check(board, int(choice)):
        board_entry.append(choice)
        if player == 1:
            place_marker(board, player_input()[0], int(choice))
        elif player == 2:
            place_marker(board, player_input()[1], int(choice))
        
def win_dec():
    if board_entry[-1] == player_input()[0]:
        print("Player 1 is the winner!")
        game_on = False
    else:
        print("Player 2 is the winner!")
        game_on  = False

def replay():
    playagain = True
    user_choice = 'something'
    while user_choice not in ['Y','N']:
        user_choice = input("Do you want to play again:(Y or N): ")
        if user_choice not in ['Y','N']:
            print("enter a valid input:(Y or N): ")
    
    if user_choice == 'Y':
        playagain = True
    elif user_choice == 'N':
        playagain = False

    return playagain

#Hardest part

print("Welcome to tic tac toe!")



display_board(initial_board)
player_input()

game_on = True
player_chosen = choose_first()
if player_chosen == 1:
    print("Player 1: Your turn is first!")
    player_choice(initial_board, 1)
    display_board(initial_board)
else:
    print("Player 2: Your turn is first!")
    player_choice(initial_board, 2)
    display_board(initial_board)

while game_on:
    if not win_check(initial_board, board_entry[-1]):
        if not full_board_check(initial_board):
            if player_chosen == 2:
                player_choice(initial_board,1)
                display_board(initial_board)
                if not win_check(initial_board, board_entry[-1]):
                    player_choice(initial_board,2)
                    display_board(initial_board)
                else:
                    win_dec()
                    
            else:
                player_choice(initial_board,2)
                display_board(initial_board)
                if not win_check(initial_board, board_entry[-1]):
                    player_choice(initial_board,1)
                    display_board(initial_board)
                else:
                    win_dec()
        else:
            print("It is a draw")
    
    else:
        win_dec()
        
        
    

               




