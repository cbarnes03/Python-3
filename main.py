'''
Game of life
Charles Barnes
'''

from board import Board 

def main():
        #assume the user types in a number
        user_rows = int(input('How many rows? '))
        user_columns = int(input('How many columns? '))

        #creat a board:
        game_of_life_board = Board(user_rows,user_columns)

        #run the first iteration of hte board:
        game_of_life_board.draw_board()

        user_action = ' '
        while user_action != 'q':
            user_action = input('Press enter to add generation or q to quit:')

            if user_action == '':
                game_of_life_board.update_board()
                game_of_life_board.draw_board()

main()