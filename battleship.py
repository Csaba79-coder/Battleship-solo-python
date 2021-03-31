"""Battleship game
Python TeamWork @ Codecool Budapest
The week of Easter - 2 days less on project! - all together 2 days of teamwork
made by: Zoltan Beke
         Csaba Vadasz
uploaded to Github
"""

import dinamic_board as db
import menu


def main():
    intro = menu.intro()
    welcome_text = menu.menu()
    # menu if it will exist
    dinamic_board = db.select_board_size() # this operates for import!
    


    # size = select_board_size()
    # board = init_board(size)
    # print_board(board, size)
    # new_board = init_board(size)
    # new_board[0][0] = 'X'
    # print_board(new_board, size)


    
# def replace_user_guess_on_board():
#     for n in range(2): # hány hajót akarsz letenni!!! 
#         print("Where do you want ship ", n + 1, "?")
#         row_number, column_number = ask_user_for_board_position()
# # hogyan cserélje ki x-re a 0 
#     # Check that there are no repeats
#         # if board[row_number][column_number] == '0':
#         #     print("That spot already has a battleship in it!")

#         # board[row_number][column_number] = '0'
#         # print_board(board)


if __name__ == '__main__':
    main()
