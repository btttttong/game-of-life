from board import Board

game_on = True
board = Board(10, 10)
board.place_cell(0, 1)
board.place_cell(1, 1)
board.place_cell(2, 1)
print(board.print_board())
board.flip_cell(10, 10)

# while game_on:
#     new_board = Board(6, 3)

print(board.print_board())