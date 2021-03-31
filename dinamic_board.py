# Dinamic board --> Battleship
import string


# def handle_user input


def main():
    size = select_board_size()

    # list_of_ships(size)

    board = init_board(size)
    print_board(board, size)
    print(board)
   

    # hided_board = hided_board(board)
    row =  ship_coordinates_row(size)
    col = ship_coordinates_column(size)
    
    guesses(board, row, col)
    # new_board = []
    # new_board = new_board.append(board[row][col], board[row])
    # guesses_board = guesses(board, row, col)

    print("hided board:")
    hided_board(board, size, col, row)

    # print(new_board)
    # size_of_ship = input_for_ship_size()
    # print(size_of_ship)

    # number_of_ships = number_of_ships(size)
    # print(number_of_ships)

    # new_board = init_board(size)
    # new_board[0][0] = 'X' # 0 and 0 will be col and row as user input
    # first starting coordinate than direction (vert - hor) left or right or up and down (maybe only down and right)
    # print_board(new_board, size)

    # print(display_board)
    # place_ships(board, board_display, *ship_cords)
    # print(place_ships(board, board_display, *ship_cords))
# def list_of_ships(size):
#     list = init_board(size)

# back with empty board


def hided_board(board, size, col, row):
    # put your ship on the board, and hide it!!! (hided to )
    board = init_board(size)
    print(board)
    # place the ship and hide again!



def guesses(board, row, col):
    board = [['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0']]
    if board[row][col] == 'H' or board[row][col] == 'S' or board[row][col] == 'M':
        print("You have already guessed that place!")

    # Check that there are no repeats
    if board[row][col] == 'X':
        print("HIT!")
        board[row][col] = 'H'
    else:
        board[row][col] = '0'
        print("MISS!")
        board[row][col] = 'M'

    # sunk is not defined!


def determinate_direction():
    # horizontal = vízszintes = H
    # vertical = függőleges! = V
    pass


def place_ships(board, board_display, *ship_cords):
    for row, col in ship_cords:
        board_display[row][col] = "X"
        board[row][col] = f"{len(ship_cords)}"


def ship_coordinates_row(size):
    row = input("Please enter row (letters of board): ").lower()
    while row not in string.ascii_letters or string.ascii_letters.index(row) > size:
        print("Invalid input")
        row = input("Please enter row (letters of board): ").lower()
    row_index = 0
    if row in string.ascii_letters:
        row_index = string.ascii_letters.index(row)
    return row_index

    
def ship_coordinates_column(size):
    while True:
        try:
            col = int(input("Please enter column (numbers of board): "))
            if col in range(1, size + 1): # range(1, 6)
                print(col - 1)
                return col -1
            else:
                print("Invalid input")
                continue
        except:
            print("Invalid input")
            continue


def number_of_ships(size):
    result = 1
    if size <= 10:
        num = size / 3
        print("result1")
        # print(result)
        return result
    # else:
    #     num = size / 5
    #     print("result2")
    #     print(result)
    #     return result


def input_for_ship_size(): # ship size
    while True:
        try:
            num = int(input("Please select ship size: "))
            return num
        except:
            print("Invalid input")
            continue
    

def determine_size_of_ships(size_of_ship):
    pass


def init_board(size):
    board = []
    for row_index in range(size):
        row = []
        for col_index in range(size):
           row.append('0')
        board.append(row)
    return board


def get_header(size):
    header = "  "
    for index in range(size):
        header += f'{index + 1} '
    return header


def get_row(row, row_index):
    line = f"{string.ascii_uppercase[row_index]} "
    for element in row:
        line += f'{element} '
    return line


def print_board(board, size):
    # fejléc
    header = get_header(size)
    print(header)
    # sorok (1-5) -> tartalom
    for row_index in range(size):
        row = get_row(board[row_index], row_index)
        print(row)


def select_board_size():
    while True:
        try:
            num = int(input("Please select board size (recommended: 5): "))
            return num
        except:
            print("Invalid input")
            continue


if __name__=='__main__':
    main()