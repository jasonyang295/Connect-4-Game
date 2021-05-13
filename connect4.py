import numpy as np
from numpy.lib.function_base import piecewise
ROW_COUNT = 6
COL_COUNT = 7
def create_board():
	 board = np.zeros((6,7))
	 return board

def drop_piece(board, row, col, piece):
    board[row][col] == piece

def is_valid_location():
    return board[5][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
    		if board[r][col] == 0:
    				return r



board = create_board()
turn = 0
game_over = False
while not game_over: 
	#ask for player 1 input
	if turn == 0: 
		col = int(input("Player 1, please make your selection (0-6):"))
		if is_valid_location(board, col):
    			row = get_next_open_row(board, col)
			drop_piece(board, row, col, 1)
	

	#ask for player 2 input
	else: 
		col = int(input("Player 2, please make your selection (0-6):"))
		if is_valid_location(board, col):
    			row = get_next_open_row(board, col)
			drop_piece(board, row, col, 2)
	



	turn += 1
	turn = turn % 2
