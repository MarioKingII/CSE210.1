'''Tic-Tac-Toe
Author: Mario Rengel'''

def main():
    board = [1,2,3,4,5,6,7,8,9]
    W = False
    currentPlayer = 'X'
    Win = False
    Attempts = 0
    while W == CheckWinner(board) == CheckTie(Attempts,Win): 
        Attempts = Attempts + 1 
        draw_board(board)
        print(f"Player {currentPlayer}'s turn")
        selecion(board,currentPlayer)
        currentPlayer = CurrentPlayer(currentPlayer)
        CheckWinner(board)
        CheckTie(Attempts,Win)
    
    else:
        currentPlayer = CurrentPlayer(currentPlayer)
        print('---------------')
        print()
        if CheckTie(Attempts, Win) == True:
            print('Tie!\n')
            print('Nobody won, try again')
        else:
            print(f'******Player {currentPlayer} has won.*******\n')
        draw_board(board)
        print('Game Over, Thanks for playing')

#Draw the Board
def draw_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print('--+---+--')
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print('--+---+--')
    print(f"{board[6]} | {board[7]} | {board[8]}\n")

#Swicth The player
def CurrentPlayer(currentPlayer):
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
    return currentPlayer

# Update the player selection on the board
def selecion(board,currentPlayer):
    slot = int(input("Select a spot 1-9: "))
    if board[slot-1] != "X" or "O":
        board[slot-1] = currentPlayer
        return
    else:
        print("This spot is already taken.")

#Verify winner
def CheckWinner(board):
    if (board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or
        board[0] == board[3] == board[6] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8] or
        board[0] == board[4] == board[8] or
        board[2] == board[4] == board[6]):
        Win = True
        #print(f'Player {currentPlayer} has won!!!!!!!')
    else:
        Win = False
    return Win

#Verify Tie/ No winner
def CheckTie(Attempts,Win):
    if Attempts == 9:
        Win = True
    else:
        Win = False
    return Win

main()
