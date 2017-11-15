class ChessPiece:
	def __init__(self, pieceType, position, board, down):
		"""
		参数1：pieceType 为棋子的种类
			值   name    value
			0   帅       0
			1   士       170
			2   象       160
			3   马       450
			4   车       1000
			5   炮       450
			6   卒       60
		"""
		self.pieceType = pieceType
		pieceName = ["帅", "士", "象", "马", "车", "炮", "卒"]
		if down:
			self.name = '('+pieceName[pieceType]+')'
		else:
			self.name = '['+pieceName[pieceType]+']'
		pieceValue = [0, 1, 2, 4, 10, 5, 2]
		self.value = pieceValue[pieceType]
		self.alive = True
		self.x = position[0]
		self.y = position[1]
		self.board = board
		self.board[self.x][self.y] = self
		self.down = down

	def move(self, toX, toY):
		die = None
		self.board[self.x][self.y] = None
		if self.board[toX][toY]:
			self.board[toX][toY].alive = False
			die = self.board[toX][toY]
		self.x = toX
		self.y = toY
		self.board[self.x][self.y] = self
		return die

	def inRange(self, x, y):
		if self.pieceType <= 1:
			if self.down:
				if 0 <= x <= 2 and 3 <= y <= 5:
					return True
				else:
					return False
			else:
				if 7 <= x <= 9 and 3 <= y <= 5:
					return True
				else:
					return False
		else:
			if 0 <= x <= 9 and 0 <= y <= 8:
				return True
			else:
				return False

	def inWay(self, x, y):
		if self.pieceType == 2:
			if self.board[int((x+self.x)/2)][int((y+self.y)/2)]:
				return False
		elif self.pieceType == 3:
			if abs(x-self.x) == 1:
				if self.board[self.x][int((y+self.y)/2)]:
					return False
			else:
				if self.board[int((x+self.x)/2)][self.y]:
					return False
		return True

	def getMoves(self):
		back = []
		if self.pieceType == 0:
			moveList = ((-1, 0), (1, 0), (0, -1), (0, 1))
			moveList = [(self.x+i[0], self.y+i[1]) for i in moveList]
		elif self.pieceType == 1:
			moveList = ((-1, -1), (-1, 1), (1, -1), (1, 1))
			moveList = [(self.x+i[0], self.y+i[1]) for i in moveList]
		elif self.pieceType == 2:
			moveList = ((-2, -2), (-2, 2), (2, -2), (2, 2))
			moveList = [(self.x+i[0], self.y+i[1]) for i in moveList]
		elif self.pieceType == 3:
			moveList = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
			moveList = [(self.x+i[0], self.y+i[1]) for i in moveList]
		elif self.pieceType == 4:
			moveList = []
			for x in range(self.x+1, 10):
				moveList.append((x, self.y))
				if self.board[x][self.y]:
					break
			for x in range(self.x-1, -1, -1):
				moveList.append((x, self.y))
				if self.board[x][self.y]:
					break
			for y in range(self.y+1, 9):
				moveList.append((self.x, y))
				if self.board[self.x][y]:
					break
			for y in range(self.y-1, -1, -1):
				moveList.append((self.x, y))
				if self.board[self.x][y]:
					break
		elif self.pieceType == 5:
			moveList = []
			if self.inRange(self.x+1, self.y):
				for x in range(self.x+1, 10):
					if self.board[x][self.y]:
						break
					moveList.append((x, self.y))
				x += 1
				while x <= 9 and not self.board[x][self.y]:
					x += 1
				moveList.append((x, self.y))
			if self.inRange(self.x-1, self.y):
				for x in range(self.x-1, -1, -1):
					if self.board[x][self.y]:
						break
					moveList.append((x, self.y))
				x -= 1
				while x >= 0 and not self.board[x][self.y]:
					x -= 1
				moveList.append((x, self.y))
			if self.inRange(self.x, self.y+1):
				for y in range(self.y+1, 9):
					if self.board[self.x][y]:
						break
					moveList.append((self.x, y))
				y += 1
				while y <= 8 and not self.board[self.x][y]:
					y += 1
				moveList.append((self.x, y))
			if self.inRange(self.x, self.y-1):
				for y in range(self.y-1, -1, -1):
					if self.board[self.x][y]:
						break
					moveList.append((self.x, y))
				y -= 1
				while y >= 0 and not self.board[self.x][y]:
					y -= 1
				moveList.append((self.x, y))
		elif self.pieceType == 6:
			if self.down:
				if self.x <= 4:
					moveList = [(1, 0)]
				else:
					moveList = [(1, 0), (0, -1), (0, 1)]
			else:
				if self.x >= 5:
					moveList = [(-1, 0)]
				else:
					moveList = [(-1, 0), (0, -1), (0, 1)]
			moveList = [(self.x+i[0], self.y+i[1]) for i in moveList]
		#print(moveList)
		for move in moveList:
			#print(move)
			#print(self.inRange(move[0], move[1]))
			#print(((not self.board[move[0]][move[1]]) or self.board[move[0]][move[1]].down ^ self.down))
			#print(self.inWay(move[0], move[1]))
			if self.inRange(move[0], move[1]) and \
				((not self.board[move[0]][move[1]]) or self.board[move[0]][move[1]].down ^ self.down) and \
				self.inWay(move[0], move[1]):
				back.append(move)
		return back
