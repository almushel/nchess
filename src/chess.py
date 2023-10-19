from raylib import *
from enum import IntEnum, auto, unique
from array import array

# NOTE: Currently raises AttributeError on import, which can be fixed by removing attributes after and including "Drawing" in __all__

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
	BOARD_ROWS = 8
	BOARD_COLS = 8

	def __init__(self, grid_size, colors=(BLACK, WHITE)):
		self.grid_size = grid_size
		self.colors = colors

		self.width = grid_size * self.BOARD_COLS
		self.height = grid_size * self.BOARD_ROWS
		
		self.pieces = array("B", [0 for i in range(8 * 8)])
		self.teams = array("B", [0 for i in range(8 * 8)])
		self.piece_selected = None
		self.center()
		self.reset()
		
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
						if y == 0: piece = Piece.KING
						else: piece = Piece.QUEEN
					if x == 4:
						if y == 0: piece = Piece.QUEEN
						else: piece = Piece.KING
				if piece != Piece.NONE:
					index = y * 8 + x
					if y > 4: self.teams[index] = Team.BLACK
					self.pieces[index] = piece
					piece = Piece.NONE
	
	def center(self):
		self.x = (GetScreenWidth() - self.width) / 2
		self.y = (GetScreenHeight() - self.height) / 2

	def screen_to_board_pos(self, pos):
		result = Vector2(
			(pos.x - self.x) // self.grid_size,
			(pos.y - self.y) // self.grid_size
		)
		return result
	
	def piece_index_at_screen_pos(self, pos):
		result = -1

		grid_pos = self.screen_to_board_pos(pos)

		index = grid_pos.y * self.BOARD_COLS + grid_pos.x
		if index >= 0 and index < self.BOARD_COLS * self.BOARD_ROWS:
			result = index

		return result

	def get_valid_moves(self, index):
		result = []

		index = int(index)
		grid_pos = Vector2(
			index % self.BOARD_COLS,
			(index - (index % self.BOARD_COLS)) // self.BOARD_ROWS
		)
		piece = self.pieces[index]
		team = self.teams[index]
		
		moves = []
		match piece:
			case Piece.PAWN:
				first_row = False
				direction = None
				if team == Team.WHITE:
					direction = 1
				else:
					direction = -1

				moves = [
					Vector2(grid_pos.x, grid_pos.y+direction),
					Vector2(grid_pos.x, grid_pos.y+direction*2),
					Vector2(grid_pos.x+1, grid_pos.y+direction),
					Vector2(grid_pos.x-1, grid_pos.y+direction),
				]
#				if not first_row: del moves[1]

			case Piece.ROOK:
				for i in range(8):
					moves.append(Vector2(grid_pos.x+i, grid_pos.y))
					moves.append(Vector2(grid_pos.x-i, grid_pos.y))
					moves.append(Vector2(grid_pos.x, grid_pos.y+i))
					moves.append(Vector2(grid_pos.x, grid_pos.y-i))
			
			case Piece.BISHOP:
				for i in range(8):
					moves.append(Vector2(grid_pos.x+i, grid_pos.y+i))
					moves.append(Vector2(grid_pos.x-i, grid_pos.y-i))
					moves.append(Vector2(grid_pos.x+i, grid_pos.y-i))
					moves.append(Vector2(grid_pos.x-i, grid_pos.y+i))
			
			case Piece.KNIGHT:
				for i in range(-1, 2, 2):
					moves.append(Vector2(grid_pos.x+(2*i), grid_pos.y+(i)))
					moves.append(Vector2(grid_pos.x+(i), grid_pos.y+(2*i)))
					moves.append(Vector2(grid_pos.x+(2*i), grid_pos.y-(i)))
					moves.append(Vector2(grid_pos.x-(i), grid_pos.y+(2*i)))
			
			case Piece.KING:
				for i in range(-1, 2, 2):
					moves.append(Vector2(grid_pos.x+i, grid_pos.y+i))
					moves.append(Vector2(grid_pos.x-i, grid_pos.y+i))
					moves.append(Vector2(grid_pos.x+i, grid_pos.y))
					moves.append(Vector2(grid_pos.x, grid_pos.y+i))

			case Piece.QUEEN:
				for e in range(8):
					for d in range(-1, 2, 2):
						i = e*d
						moves.append(Vector2(grid_pos.x+i, grid_pos.y+i))
						moves.append(Vector2(grid_pos.x-i, grid_pos.y+i))
						moves.append(Vector2(grid_pos.x+i, grid_pos.y))
						moves.append(Vector2(grid_pos.x, grid_pos.y+i))
					
				

		for m in moves:
			if m.x >= 0 and m.x < self.BOARD_COLS and m.y >= 0 and m.y < self.BOARD_ROWS:
				index = int(m.y * self.BOARD_COLS + m.x)
				result.append(index)

		return result
				

	def update(self):
		if IsMouseButtonPressed(0):
			piece = self.piece_index_at_screen_pos(GetMousePosition())
			if piece >= 0:
				self.piece_selected = piece
			# elif handle valid moves
			else:
				self.piece_selected = None
	
	def draw_board(self):
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
		if self.piece_selected is not None:
			moves = self.get_valid_moves(self.piece_selected)
		else:
			moves = []
		for y in range(8):
			for x in range(8):

				DrawRectangle(draw_x, draw_y, self.grid_size, self.grid_size, self.colors[square_color])
				if index in moves:
					DrawRectangle(draw_x, draw_y, self.grid_size, self.grid_size, YELLOW)
				
				if self.pieces[index] != Piece.NONE:
					team = self.teams[index]
					piece = self.pieces[index]
					padding = (self.grid_size - MeasureText(piece_labels[piece], self.grid_size)) / 2
					p_color_1 = self.colors[int(not team)].rgba
					p_color_2 = self.colors[square_color].rgba
					p_color_2.a = 0

					if self.piece_selected == index:
						DrawRectangle(draw_x, draw_y, self.grid_size, self.grid_size, GREEN)
					
					DrawCircleGradient(draw_x + self.grid_size/2, draw_y + self.grid_size/2, self.grid_size/1.5, p_color_1, p_color_2)
					DrawText(piece_labels[piece], padding + draw_x, draw_y, self.grid_size, self.colors[team])

					if self.piece_selected == index:
						DrawRectangleLines(draw_x, draw_y, self.grid_size, self.grid_size, YELLOW)

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

			DrawText("abcdefgh"[i], padding_x + self.grid_size*i, padding_y + self.height, font_size, font_color)
			DrawTextPro(GetFontDefault(), "abcdefgh"[i], Vector2(padding_x + self.grid_size*i, padding_y - self.grid_size), Vector2(width,font_size), 180, font_size, 0, offside_color)

			width = MeasureText("87654321"[i], font_size)
			padding_x = self.x + (self.grid_size - width) / 2
			DrawText("87654321"[i], padding_x - self.grid_size, padding_y + self.grid_size*i, font_size, font_color)
			DrawTextPro(GetFontDefault(), "87654321"[i], Vector2(padding_x + self.width, padding_y + self.grid_size*i), Vector2(width,font_size), 180, font_size, 0, offside_color)

	def draw(self):
		self.draw_board()
		self.draw_labels()

def main():
	SCREEN_W = 800
	SCREEN_H = 600
	GRID_SIZE = 50

	InitWindow(SCREEN_W, SCREEN_H, "Net Chess")

	board = ChessBoard(GRID_SIZE)

	while not WindowShouldClose():		
		board.update()
		
		BeginDrawing()
		ClearBackground(RAYWHITE)
		
		board.draw()

		EndDrawing()

	CloseWindow()

main()