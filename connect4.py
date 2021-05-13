import numpy as np
import pygame 

from numpy.lib.function_base import piecewise
ROW_COUNT = 6
COL_COUNT = 7

def checkwin(board, piece):
    	#check all horizontal locations
		for c in range(COL_COUNT - 3): #we subtract 3 bc the last 3 columns can't have winning horizontal moves
    			for r in range(ROW_COUNT):
    					if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece: #here we check if there are 4 consecutive pieces which = win
    							return True


		#now check vertical locations for win

		for c in range(COL_COUNT): 
			for r in range(ROW_COUNT - 3): #now we can't have the top rows for vertical win
				if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece: #here we check if there are 4 consecutive pieces which = win
    					return True

		#now we need to check for positively sloped diagonals 
		for c in range(COL_COUNT - 3): #this is cus diagonals stop at the 3rd to last row
			for r in range(ROW_COUNT - 3): #now we can't have the top rows for vertical win for the diagonals
				if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+4] == piece: #here we check if there are 4 consecutive pieces which = win
    					return True

		#now we check for negatively sloped diagonal
		for c in range(COL_COUNT -3): 
			for r in range(3, ROW_COUNT): #negatively sloped diagonals can only start so far up
				if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece: #here we check if there are 4 consecutive pieces which = win
    					return True

def create_board():
	 board = np.zeros((ROW_COUNT, COL_COUNT))
	 return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece
	#not double equals just one to assign

def is_valid_location():
    return board[5][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
    		if board[r][col] == 0:
    				return r

def print_board(board):
    	print(np.flip(board, 0))

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
		
		if checkwin(board, 1):
    			print("Player1 has won")

	#ask for player 2 input
	else: 
		col = int(input("Player 2, please make your selection (0-6):"))
		if is_valid_location(board, col):
    			row = get_next_open_row(board, col)
			drop_piece(board, row, col, 2)
			
		if checkwin(board, 2):
    			print("Player2 has won")



	turn += 1
	turn = turn % 2


#everything above is the cmd line version of c4

