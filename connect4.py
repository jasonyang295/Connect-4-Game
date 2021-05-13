import numpy as np
def create_board():
	 board = np.zeros((6,7))
	 return board

board = create_board()
turn = 0
game_over = False
while not game_over: 
	if turn == 0: 
		selection = input("Player 1 make your selection *0-6):")