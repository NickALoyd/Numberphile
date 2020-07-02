import random
#board = [[0 for i in range(10)] for i in range(10)] #this is going to be the initial condition
#we are going to start with a random board
#board = [[random.randint(0,1) for i in range(10)] for i in range(10)]
boardStates = set()

def gameOfLife(board):
	boardSizeX = len(board)
	boardSizeY = len(board[0])
	if str(board) in boardStates:
		return None
	boardStates.add(str(board))
	printBoard(board)
	newBoard = [[0 for i in range(boardSizeY)] for i in range(boardSizeX)]
	for x in range(1,boardSizeX-1):
		for y in range(1,boardSizeY-1):
			newBoard[x][y] = rulesForXY(x,y,board)
	gameOfLife(newBoard)
	return board

def printBoard(board):
	print()
	for line in board:
		print(line)

def countNeighbors(x,y,board):
	t = sum(board[x-1][y-1:y+2])
	t += sum(board[x+1][y-1:y+2])
	t += board[x][y-1]
	t += board[x][y+1]
	return t

def isCellAlive(x,y,board):
	return board[x][y] == 1

def rulesForXY(x,y,board):
	neighbors = countNeighbors(x,y,board)
	if isCellAlive(x,y,board):
		if neighbors <= 1: return 0 #isolation
		if neighbors >= 4: return 0 #overcrowding
		return 1 					#sirvival
	if neighbors == 3: return 1 	#birth
	return 0 						#stays dead

board = [[random.randint(0,1) for i in range(20)] for i in range(24)] #this is going to be the initial condition

gameOfLife(board)

