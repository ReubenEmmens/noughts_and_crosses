'''This is the main file for the noughts and crosses game containing all related functions.'''
from random import randrange

def display_board(board):
    '''This function prints out the board that it was passed.'''
    counter = 0
    row = 0
    for counter in range(13):
        if counter % 4 == 0:
            print('+-------+-------+-------+')
        elif counter % 2 == 0:
            print(f'|   {board[row][0]}   |   {board[row][1]}   |   {board[row][2]}   |')
            row += 1
        else:
            print('|       |       |       |')

def enter_move(board, sign):
    '''This function takes the user's move, checks if it is valid and then updates the board.'''
    while True:
        try:
            move = int(input('Which square would you like to choose?\n'))
        except ValueError:
            print('The input was not a valid number, please try again.')
        except Exception: # pylint: disable=broad-exception-caught
            print('Something went wrong.')
        else:
            for row in board:
                if move in row:
                    row_index, column_index = board.index(row), row.index(move)
                    board[row_index][column_index] = sign
                    return board
            print('This numbered square has already been used, please try again.')
            enter_move(board, sign)

def make_list_of_free_fields(board):
    '''This function browses the board and builds a list of all the free squares;'''
    free_squares = []

    for row in board:
        for value in row:
            if isinstance(value, int):
                free_squares.append((board.index(row), row.index(value)))

    return free_squares


def victory_for(board, sign): #pylint: disable=redefined-outer-name
    '''This function checks the board to see if there is a winner, or there are no more free spaces left.''' # pylint: disable=line-too-long
    def eval_pattern(board):

        won = False

        # Vertical
        if board[0][0] == board[1][0] == board[2][0]:
            won = True
        elif board[0][1] == board[1][1] == board[2][1]:
            won = True
        elif board[0][2] == board[1][2] == board[2][2]:
            won = True

        # Horizontal
        elif board[0][0] == board[0][1] == board[0][2]:
            won = True
        elif board[1][0] == board[1][1] == board[1][2]:
            won = True
        elif board[2][0] == board[2][1] == board[2][2]:
            won = True

        # Diagonal
        elif board[0][0] == board[1][1] == board[2][2]:
            won = True
        elif board[0][2] == board[1][1] == board[2][0]:
            won = True

        return won

    if eval_pattern(board):
        print(f"Congratulations player \"{sign}\" on your victory.")
        return True

    elif len(make_list_of_free_fields(board)) == 0:
        print("It's a draw! There are no more free spaces. Try again :)")
        return True

    else:
        return False

def draw_move(board, turn, sign):
    '''The function draws the computer's move and updates the board.'''

    if turn == 0:
        board[1][1] = "x"
    else:
        free_squares = make_list_of_free_fields(board)
        row_index, column_index = free_squares[randrange(len(free_squares))]
        board[row_index][column_index] = sign
    display_board(board)

    return board

def rotate_player(sign):
    '''This function rotates the player after each turn.'''

    if sign == 'x':
        sign = 'o'
    else:
        sign = 'x'

    return sign

def main():
    '''This is the main function that runs the game.'''

    sign = 'x'
    turn = 0
    _board = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    print("Welcome to my super-fun game of noughts and crosses...")

    while True:
        draw_move(_board, turn, sign)
        if victory_for(_board, sign):
            break
        sign = rotate_player(sign)
        enter_move(_board, sign)
        if victory_for(_board, sign):
            break
        sign = rotate_player(sign)
        turn += 1

if __name__ == "__main__":
    main()
