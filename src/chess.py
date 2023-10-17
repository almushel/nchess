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

def main():
	SCREEN_W = 800
	SCREEN_H = 600
	GRID_SIZE = 50	

	InitWindow(SCREEN_W, SCREEN_H, "Net Chess")
	
	board_size = GRID_SIZE * 8
	left = (SCREEN_W - board_size) / 2
	top = (SCREEN_H - board_size) / 2
	board_colors = (WHITE, BLACK)

	piece_labels = ["" for i in range(Piece.QUEEN.value + 1)]
	piece_labels[Piece.PAWN] 	= "P"
	piece_labels[Piece.ROOK] 	= "R"
	piece_labels[Piece.KNIGHT] 	= "N"
	piece_labels[Piece.BISHOP] 	= "B"
	piece_labels[Piece.KING] 	= "K"
	piece_labels[Piece.QUEEN] 	= "Q"

	board = {
		"pieces": array("B", [0 for i in range(8 * 8)]),
		"teams": array("B", [0 for i in range(8 * 8)])
	}

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
			if piece is not Piece.NONE:
				index = y * 8 + x
				if y < 4: board["teams"][index] = Team.BLACK
				board["pieces"][index] = piece

				piece = Piece.NONE

	while not WindowShouldClose():
		BeginDrawing()
		
		ClearBackground(RAYWHITE)

		font_size = GRID_SIZE / 2
		font_color = GRAY
		for x in range(8):
			padding_x = left + (GRID_SIZE - MeasureText("abcdefgh"[x], font_size)) / 2
			padding_y = top + (GRID_SIZE - font_size) / 2
			DrawText("abcdefgh"[x], padding_x + GRID_SIZE * x, padding_y - GRID_SIZE, font_size, font_color)
			DrawText("abcdefgh"[x], padding_x + GRID_SIZE * x, padding_y + GRID_SIZE*8, font_size, font_color)

		for y in range(8):
			padding_x = left + (GRID_SIZE - MeasureText("12345678"[x], font_size)) / 2
			padding_y = top + (GRID_SIZE - font_size) / 2

			DrawText("12345678"[y], padding_x - GRID_SIZE, padding_y + GRID_SIZE*y, font_size, font_color)
			DrawText("12345678"[y], padding_x + GRID_SIZE*8, padding_y + GRID_SIZE*y, font_size, font_color)

		DrawRectangleLinesEx(Rectangle(left-2, top-2, GRID_SIZE*8 + 4, GRID_SIZE*8 + 4), 4, BLACK)
		square_color = 0
		for y in range(8):
			for x in range(8):
				draw_x = left + x * GRID_SIZE
				draw_y = top + y * GRID_SIZE
				index = y * 8 + x

				DrawRectangle(draw_x, draw_y, GRID_SIZE, GRID_SIZE, board_colors[square_color])
				if board["pieces"][index] != Piece.NONE:
					team = board["teams"][index]
					piece = board["pieces"][index]
					padding = (GRID_SIZE - MeasureText(piece_labels[piece], GRID_SIZE)) / 2
					p_color_1 = board_colors[int(not team)].rgba
					p_color_2 = board_colors[square_color].rgba
					p_color_2.a = 0
					
					DrawCircleGradient(draw_x + GRID_SIZE/2, draw_y + GRID_SIZE/2, GRID_SIZE/1.5, p_color_1, p_color_2)
#					DrawCircle(draw_x + GRID_SIZE/2, draw_y + GRID_SIZE/2, GRID_SIZE/2, board_colors[int(not team)])
					DrawText(piece_labels[piece], padding + draw_x, draw_y, GRID_SIZE, board_colors[team])

				square_color = int(not square_color)
			square_color = int(not square_color)

		EndDrawing()

	CloseWindow()

main()