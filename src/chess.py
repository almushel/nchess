from raylib import *
from math import *
from enum import IntEnum, auto, unique
from array import array

# NOTE: Currently raises AttributeError on import, which can be fixed by removing attributes after and including "Drawing" in __all__
SCREEN_W = 800
SCREEN_H = 600
GRID_SIZE = 50

class Piece(IntEnum):
	NONE 	= 0
	PAWN 	= auto()
	ROOK 	= auto()
	KNIGHT 	= auto()
	BISHOP 	= auto()
	KING 	= auto()
	QUEEN 	= auto()

class Team(IntEnum):
	WHITE = 0
	BLACK = auto()

class ChessBoard:
	def __init__(self, position, dimensions, grid_size, colors=(WHITE, BLACK)):
		self.position = position
		self.dimensions = dimensions
		self.grid_size = grid_size
		self.colors = colors

		self.width = grid_size * self.dimensions.x
		self.height = grid_size * self.dimensions.y
		
		self.pieces = array("B", [0 for i in range(8 * 8)])
		self.teams = array("B", [0 for i in range(8 * 8)])
		
	@property
	def x(self):
		return self.position.x
	
	@property
	def y(self):
		return self.position.y
	
	@property
	def cols(self):
		return int(self.dimensions.x)

	@property
	def rows(self):
		return int(self.dimensions.y)

	def reset(self):
		piece = Piece.NONE
		for y in range(8):
			for x in range(8):
				if y == 1 or y == 6:
					piece = Piece.PAWN
				elif y == 0 or y == 7:
					if x == 0 or x == 7:
						piece = Piece.ROOK
					if x == 1 or x == 6:
						piece = Piece.KNIGHT
					if x == 2 or x == 5:
						piece = Piece.BISHOP
					if x == 3:
						piece = Piece.KING
					if x == 4:
						piece = Piece.QUEEN
				if piece != Piece.NONE:
					index = y * 8 + x
					if y > 4: self.teams[index] = Team.BLACK
					self.pieces[index] = piece
					piece = Piece.NONE
		
		self.rooks_moved = [[False, False] for i in range(Team.BLACK+1)]
		self.kings_moved = [False for i in range(Team.BLACK+1)]

	def world_to_board_pos(self, pos):
		result = Vector2(
			(pos.x - self.x) // self.grid_size,
			(pos.y - self.y) // self.grid_size
		)
		return result
	
	def piece_index_at_world_pos(self, pos):
		result = -1

		grid_pos = self.world_to_board_pos(pos)

		if (0 <= grid_pos.x < self.cols) and (0 <= grid_pos.y < self.rows):
			index = grid_pos.y * self.cols + grid_pos.x
			if index >= 0 and index < self.cols * self.rows:
				result = index

		return int(result)
	
	def piece_index_to_grid_pos(self, index):
		result = Vector2(
			index % self.cols,
			(index - (index % self.cols)) // self.rows
		)

		return result

	def draw_board(self):
		# TO-DO: Pass in piece sprites as images (probably in __init__)
		# To-DO: handle consistent piece rotation and labels for black/white board views
		piece_labels = ["" for i in range(Piece.QUEEN.value + 1)]
		piece_labels[Piece.PAWN] 	= "P"
		piece_labels[Piece.ROOK] 	= "R"
		piece_labels[Piece.KNIGHT] 	= "N"
		piece_labels[Piece.BISHOP] 	= "B"
		piece_labels[Piece.KING] 	= "K"
		piece_labels[Piece.QUEEN] 	= "Q"

		draw_x = self.x
		draw_y = self.y

		DrawRectangleLinesEx(Rectangle(draw_x-2, draw_y-2, self.width+4, self.height+4), 4, BLACK)
		
		index = int(0)
		square_color = 0
		for y in range(8):
			for x in range(8):

				DrawRectangle(draw_x, draw_y, self.grid_size, self.grid_size, self.colors[square_color])
				
				if self.pieces[index] != Piece.NONE:
					team = self.teams[index]
					piece = self.pieces[index]
					padding = (self.grid_size - MeasureText(piece_labels[piece], self.grid_size)) / 2
					p_color_1 = self.colors[int(not team)].rgba
					p_color_2 = self.colors[square_color].rgba
					p_color_2.a = 0
					
					DrawCircleGradient(draw_x + self.grid_size/2, draw_y + self.grid_size/2, self.grid_size/1.5, p_color_1, p_color_2)

					piece_rotation = 180
					offset = Vector2(MeasureText(piece_labels[piece], self.grid_size), self.grid_size)

					DrawTextPro(
						GetFontDefault(), piece_labels[piece], 
				 		Vector2(padding + draw_x, draw_y), offset, 
						piece_rotation, self.grid_size, 0, 
						self.colors[team]
						)

				draw_x += self.grid_size
				index += 1
				square_color = int(not square_color)
			draw_x = self.x
			draw_y += self.grid_size
			square_color = int(not square_color)

	def draw_labels(self):		
		font_size = self.grid_size / 2
		font_color = GRAY
		offside_color = font_color.rgba
		offside_color.a //= 2

		padding_y = self.y + (self.grid_size - font_size) / 2
		for i in range(8):
			width = MeasureText("abcdefgh"[i], font_size)
			padding_x = self.x + (self.grid_size - width) / 2

			# NOTE: offside_color current assumes white side view
			DrawText("abcdefgh"[7-i], padding_x + self.grid_size*i, padding_y + self.height, font_size, offside_color)
			DrawTextPro(GetFontDefault(), "abcdefgh"[7-i], Vector2(padding_x + self.grid_size*i, padding_y - self.grid_size), Vector2(width,font_size), 180, font_size, 0, font_color)

			width = MeasureText("12345678"[i], font_size)
			padding_x = self.x + (self.grid_size - width) / 2
			DrawText("12345678"[i], padding_x - self.grid_size, padding_y + self.grid_size*i, font_size, offside_color)
			DrawTextPro(GetFontDefault(), "12345678"[i], Vector2(padding_x + self.width, padding_y + self.grid_size*i), Vector2(width,font_size), 180, font_size, 0, font_color)

	def draw(self):
		self.draw_board()
		self.draw_labels()

class ChessGame:
	BOARD_ROWS = 8
	BOARD_COLS = 8
	PAWN_DIRS = (1, -1)
	DIAGONAL_MOVES = [Vector2(+1, +1), Vector2(-1, -1), Vector2(+1, -1), Vector2(-1, +1) ]
	ORTHOGONAL_MOVES = [ Vector2(1,0), Vector2(-1,0), Vector2(0,1), Vector2(0,-1) ]
	KNIGHT_MOVES = []

	def __init__(self):
		self.board = ChessBoard(Vector2(0,0), Vector2(self.BOARD_COLS, self.BOARD_ROWS), GRID_SIZE)
		self.moves = [[] for i in range(len(self.board.pieces))]
		self.piece_selected = None
		self.piece_rotation = 0

		self.rooks_moved = [[False, False] for i in range(Team.BLACK+1)]
		self.kings_moved = [False for i in range(Team.BLACK+1)]

		self.view = Team.WHITE
		self.turn = Team.WHITE
		self.check = False
		self.mate = False

	def debug_reset(board):
		# Clear the board to test individual piece moves
		#	for i in range(len(board.pieces)):
		#		board.pieces[i] = 0
		#		board.teams[i] = 0
		#	test_index = 4 * board.cols + 4
		#	board.pieces[test_index] = Piece.QUEEN
		#	board.teams[test_index] = Team.WHITE

		# Clear the back row to test King/Rook and castle moves	
		last_row = int((board.rows * board.cols) - board.cols)
		for i in range(8):
			if board.pieces[i] != Piece.ROOK and board.pieces[i] != Piece.KING:
				board.pieces[i] = Piece.NONE
			if board.pieces[last_row+i] != Piece.ROOK and board.pieces[last_row+i] != Piece.KING:
				board.pieces[last_row+i] = Piece.NONE
	
	def new_game(self):
		self.board.reset()
		self.turn = Team.WHITE
	
	def is_king_in_check(self, team):
		king = -1
		for pi in range(len(self.board.pieces)):
			if self.board.pieces[pi] == Piece.KING and self.board.teams[pi] == team:
				king = pi
				break
		
		if king < 0: return False
		
		grid_pos = self.board.piece_index_to_grid_pos(king)

		check_dirs = []
		for i in range(-1, 2, 1):
			check_dirs.append(	(Vector2(i, -1), 8))
			check_dirs.append(	(Vector2(i,  0), 8))
			check_dirs.append(	(Vector2(i,  1), 8))

		# Knight moves
		knight_moves = []
		for i in range(-1, 2, 2):
			knight_moves.append( ( Vector2( i  ,  2*i), 1) )
			knight_moves.append( ( Vector2( 2*i,  i  ), 1) )
			knight_moves.append( ( Vector2( 2*i, -i  ), 1) )
			knight_moves.append( ( Vector2(-i  ,  2*i), 1) )
		check_dirs += knight_moves

		for d in check_dirs:
			for i in range(1, d[1]+1):
				offset = Vector2(d[0].x * i, d[0].y * i)
				check_pos = Vector2(grid_pos.x + offset.x, grid_pos.y + offset.y)
				if check_pos.x < 0 or check_pos.x >= self.BOARD_COLS: break 
				if check_pos.y < 0 or check_pos.y >= self.BOARD_ROWS: break
				
				check_index = int(check_pos.y * self.BOARD_COLS + check_pos.x)
				if self.board.teams[check_index] != team:
					match self.board.pieces[check_index]:
						case Piece.KNIGHT:
							if d in knight_moves:
								return True
						case Piece.QUEEN:
							if d not in knight_moves:
								return True
						case Piece.BISHOP:
							if offset.x != 0 and offset.y != 0:
								return True		
						case Piece.ROOK:
							if (offset.x != 0 and offset.y == 0) or (offset.y != 0 and offset.x == 0):
								return True
						case Piece.KING:
							if abs(offset.x) <= 1 and abs(offset.y) <= 1:
								return True
						case Piece.PAWN:
							if abs(offset.x) <= 1 and abs(offset.y) <= 1:
								if offset.y == self.PAWN_DIRS[not team]:
									if offset.x != 0:
										return True
				# Even if the piece doesn't put the king in check, the path is blocked
				if self.board.pieces[check_index] > 0:
					break
		return False
	
	def get_valid_moves(self, index):
		result = []

		index = int(index)
		grid_pos = Vector2(
			index % self.BOARD_COLS,
			(index - (index % self.BOARD_COLS)) // self.BOARD_ROWS
		)
		piece = self.board.pieces[index]
		team = self.board.teams[index]
		
		moves = []
		directions = []
		limit = 1

		match piece:
			case Piece.PAWN:
				first_row = False
				if team == Team.WHITE:
					first_row = (grid_pos.y == 1)
				else: 
					first_row = (grid_pos.y == 6)

				# Pawns processed separately, because they have completely unique move/capture rules
				for i in range(1, 2 + int(first_row)):
					check_pos = Vector2(grid_pos.x, grid_pos.y + self.PAWN_DIRS[team]*i)
					check_index = int(check_pos.y * self.BOARD_COLS + check_pos.x)
					if self.board.pieces[check_index] == Piece.NONE:
						moves.append(check_pos)
					else: break

				for i in range(-1, 2, 2):
					check_pos = Vector2(grid_pos.x + i, grid_pos.y + self.PAWN_DIRS[team])
					if check_pos.x < 0 or check_pos.x >= self.BOARD_COLS:
						continue
					check_index = int(check_pos.y * self.BOARD_COLS + check_pos.x)
					if self.board.pieces[check_index] > Piece.NONE and self.board.teams[check_index] != team:
						moves.append(check_pos)

			case Piece.ROOK:
				limit = 8
				directions = self.ORTHOGONAL_MOVES
					
			case Piece.BISHOP:
				limit = 8
				directions = self.DIAGONAL_MOVES
			
			case Piece.KNIGHT:
				for i in range(-1, 2, 2):
					directions.append(Vector2( (i  ),  (2*i)))
					directions.append(Vector2( (2*i),  (i  )))
					directions.append(Vector2( (2*i), -(i  )))
					directions.append(Vector2(-(i  ),  (2*i)))
			
			case Piece.KING:
				directions = self.ORTHOGONAL_MOVES + self.DIAGONAL_MOVES
				if not self.kings_moved[team]:
					for i in range(-1, 2, 2):
						rook_index = index+i
						if not self.rooks_moved[team][int(i > 0)]:
							while (0 <= rook_index+1 < len(self.board.pieces)) and self.board.pieces[rook_index] == Piece.NONE:
								rook_index += i
							if self.board.pieces[rook_index] == Piece.ROOK:
								result.append(index+(2*i))			

			case Piece.QUEEN:
				limit = 8
				directions = self.ORTHOGONAL_MOVES + self.DIAGONAL_MOVES
				
		for d in directions:
			for i in range(1, limit+1):
				next = Vector2(grid_pos.x + d.x*i, grid_pos.y + d.y*i)
				next_index = int(next.y * self.BOARD_COLS + next.x)

				if 0 <= next_index < len(self.board.pieces):
					if self.board.pieces[next_index] > Piece.NONE:
						if self.board.teams[next_index] != team:
							moves.append(next)
						break
					else:
						moves.append(next)
				else:
					break

		for m in moves:
			if (0 <= m.x < self.BOARD_COLS) and (0 <= m.y < self.BOARD_ROWS):
				move_index = int(m.y * self.BOARD_COLS + m.x)

				undo = (self.board.pieces[move_index], self.board.teams[move_index])

				self.board.pieces[move_index], self.board.teams[move_index] = piece, team
				self.board.pieces[index], self.board.teams[index] = Piece.NONE, Team.WHITE

				if not self.is_king_in_check(team):
					result.append(move_index)

				self.board.pieces[move_index], self.board.teams[move_index] = undo[0], undo[1]
				self.board.pieces[index], self.board.teams[index] = piece, team
				
		return result
	
	def update(self, camera):
		board = self.board

		if IsKeyPressed(KEY_R):
			self.new_game()
			self.debug_reset(board)

		for i in range(len(self.moves)):
			self.moves[i] = self.get_valid_moves(i)

		self.check = self.is_king_in_check(self.turn)
		self.mate = True

		for i in range(len(board.pieces)):
			if board.teams[i] == self.turn and len(self.moves[i]): 
				self.mate = False
				break
		
		if IsMouseButtonPressed(0):
			piece = board.piece_index_at_world_pos(
				GetScreenToWorld2D(GetMousePosition(), camera)
			)

			if self.piece_selected is not None and self.piece_selected != piece:
				selected_moves = self.moves[self.piece_selected]
				if piece in selected_moves:
					board.pieces[piece] = board.pieces[self.piece_selected]
					board.teams[piece] = board.teams[self.piece_selected]

					# Handle castle moves
					if board.pieces[self.piece_selected] == Piece.KING:
						board.kings_moved[self.turn] = True
						for i in range(-1, 2, 2):
							if piece == self.piece_selected+(2*i):
								rook_index = piece
								while board.pieces[rook_index] != Piece.ROOK:
									rook_index += i
								board.pieces[rook_index] = Piece.NONE
								board.pieces[piece-i] = Piece.ROOK
								# Rook states are stored left to right, so can cast bool to int here
								board.rooks_moved[self.turn][int(rook_index < self.piece_selected)] = True
					# Update rook states after initial move
					# This will trigger if any rook was moved back to a board corner and moved again.
					# However, the rook_moved state would already be True and it will only be reset to False on new game,
					# so this check is correct when it needs to be
					elif board.pieces[self.piece_selected] == Piece.ROOK:
						rook_index = self.piece_selected
						rook_x = rook_index % board.cols
						if (
							rook_index == 0 or 
							rook_index == board.cols-1 or 
							rook_index == len(board.pieces)-1 or 
							rook_index == len(board.pieces)-board.cols
						):
							board.rooks_moved[self.turn][int(rook_x > board.cols//2)] = True
					
					board.pieces[self.piece_selected] = Piece.NONE
					self.piece_selected = None
					self.turn = int(not self.turn)

				elif piece >= 0 and board.teams[piece] == self.turn:
					self.piece_selected = piece
				else:
					self.piece_selected = None

			elif piece >= 0 and board.teams[piece] == self.turn:
				self.piece_selected = piece

	# Called in Mode2d
	def draw_2D(self):
		self.board.draw_board()

		if self.piece_selected is not None:
			grid_pos = self.board.piece_index_to_grid_pos(self.piece_selected)
			rect = Rectangle(grid_pos.x*GRID_SIZE, grid_pos.y*GRID_SIZE, GRID_SIZE, GRID_SIZE)
			DrawRectangleLinesEx(rect, 4, GREEN)

			for piece in self.moves[self.piece_selected]:
				grid_pos = self.board.piece_index_to_grid_pos(piece)
				rect = Rectangle(grid_pos.x*GRID_SIZE, grid_pos.y*GRID_SIZE, GRID_SIZE, GRID_SIZE)
				DrawRectangleLinesEx(rect, 4, YELLOW)

		self.board.draw_labels()

	#Called after Mode2D
	def draw_overlay(self):
		team_names = ("White", "Black")
		font_size = 24
		width = MeasureText(f"{team_names[self.turn]} player's turn", 24)
		DrawText(f"{team_names[self.turn]} player's turn", GetScreenWidth()/2 - width/2, font_size, font_size, BLACK)

		if self.check and self.mate:
			width = MeasureText("Checkmate!!!", 24)
			DrawText("Checkmate!!!", GetScreenWidth()/2 - width/2, GetScreenHeight()-font_size, font_size, RED)			
		elif self.check:
			width = MeasureText("Check!", 24)
			DrawText("Check!", GetScreenWidth()/2 - width/2, GetScreenHeight()-font_size, font_size, RED)
		elif self.mate:
			width = MeasureText("Draw!", 24)
			DrawText("Draw!", GetScreenWidth()/2 - width/2, GetScreenHeight()-font_size, font_size, ORANGE)

def main():
	InitWindow(SCREEN_W, SCREEN_H, "Net Chess")

	game = ChessGame()
	game.new_game()
	camera = Camera2D(Vector2(SCREEN_W/2, SCREEN_H/2),Vector2(game.board.x + game.board.width/2,game.board.y+game.board.height/2), 0, 1)

	while not WindowShouldClose():		
		if IsWindowResized():
			camera.offset.x, camera.offset.y = GetScreenWidth()/2, GetScreenHeight()/2

		camera.rotation = (game.view == Team.WHITE) * 180
		game.update(camera)
		
		BeginDrawing()
		ClearBackground(RAYWHITE)
		
		BeginMode2D(camera)
		game.draw_2D()
		EndMode2D()

		game.draw_overlay()

		EndDrawing()

	CloseWindow()

main()