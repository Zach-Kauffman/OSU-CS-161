
def display(board):
	print()
	num = 1
	for i in range(3):
		for j in range(3):
			if j != 2:
				print(" " + board[i][j] + " |", end = '')
			else:
				print(" " + board[i][j] + "     ", end = '')
				for k in range(3):
					if k != 2:
						print(" " + str(num) + " |", end = '')
					else:
						print(" " + str(num))
					num += 1
		if i != 2:
			print("-----------    -----------")
	print()
	return

def reset(board):
	for i in range(3):
		for j in range(3):
			board[i][j] = " "
	return 'X'

def turn(board, player, x, o):
	display(board)
	location = "BAD"
	if player == 'X':
		name = x
	else:
		name = o
	while True:
		location = str(input(str(name) + "'s turn. Choose a spot.  "))
		if inputcheck(location, 1, "123456789") == False:
			print("Please input a number between 1 and 9")
		else:
			break
	y = int(location) - 1
	x = y // 3
	while y > 2:
		y -= 3
	if board[x][y] == ' ':
		board[x][y] = player
	else:
		turn(board, player, x, o)
	return 0

def inputcheck(string, length, chars):
	for char in string:
		if str(char) not in str(chars):
			return False
	if len(str(string)) != int(length):
		return False
	return True

def switchplayer(player):
	if player == 'X':
		return 'O'
	return 'X'

def wincheck(board, player):
	for i in range(3):
		if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != " ":
			return player
	for i in range(3):
		if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != " ":
			return player
	if board[1][1] == board[0][0] and board[1][1] == board[2][2] and board[1][1] != " ":
		return player
	if board[1][1] == board[2][0] and board[1][1] == board[0][2] and board[1][1] != " ":
		return player
	for i in range(3):
		for j in range(3):
			if board[i][j] == " ":
				return "not done"
	return "No one"
	
def game(board, player, wins, x, o):
	while(wincheck(board, player) == "not done"):
		turn(board, player, x, o)
		player = switchplayer(player)
	display(board)
	if wincheck(board, player)  == 'X':
		name = o
	elif wincheck(board, player) == 'O': 
		name = x
	else:
		name = "No one"
	print("\n" + name + " wins!\n")
	incwins(board, player, wins, x, o)
	rematch = str(input("Play again? y/n: "))
	if rematch == 'y':
		player = reset(board)
		game(board, player, wins, x, o)
	print("Thanks for playing!")
	return

def incwins(board, player, wins, x, o):
	if wincheck(board, player) == "O":
		wins[0] += 1
	if wincheck(board, player) == "X":
		wins[1] += 1
	if wincheck(board, player) == "No one":
		wins[2] += 1
	print(x + " wins: " + str(wins[0]) + "\n" + o + " wins: " + str(wins[1]) + "\nTies: " + str(wins[2]) + "\n")
	return
	

def main():
	name1 = str(input("X input name: "))
	name2 = str(input("O input name: "))
	wins = [0,0,0]
	board = [[1,2,3], [4,5,6], [7,8,9]]
	player = reset(board)
	game(board, player, wins, name1, name2)

main()	
