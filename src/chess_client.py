import socket
import select
from time import sleep
from raylib import *
from chess import ChessGame

SCREEN_W = 800
SCREEN_H = 600
MOVE_TEMPLATE = b"00,00"

def play_chess(game_socket: socket.socket, team):
	InitWindow(SCREEN_W, SCREEN_H, "Net Chess")

	game = ChessGame()
	game.new_game()
	game.view = team
	camera = Camera2D(Vector2(SCREEN_W/2, SCREEN_H/2),Vector2(game.board.x + game.board.width/2,game.board.y+game.board.height/2), 0, 1)

	while not WindowShouldClose():		
		if IsWindowResized():
			camera.offset.x, camera.offset.y = GetScreenWidth()/2, GetScreenHeight()/2

		camera.rotation = (game.view == 0) * 180
		
		select_result = select.select([game_socket], [game_socket], [])
		disconnected = False
		msg_bytes = None
		if len(select_result[0]):
			msg_bytes = game_socket.recv(len(MOVE_TEMPLATE))
			disconnected = (msg_bytes == b"")
		
		if game.turn == game.view:
			game.update(camera)
			if game.turn != game.view and len(select_result[1]):
				game_socket.sendall(f"{game.moves_played[-1][0]},{game.moves_played[-1][1]}".encode("utf-8") )
		else:
			game.update(camera)
			# Just ignore piece selection when other client's move
			game.piece_selected = None
			if msg_bytes and not disconnected:
				move_str = bytes.decode(msg_bytes)
				moves = move_str.split(",")
				game.execute_move(int(moves[0]), int(moves[1]))
		
		if disconnected:
			game_socket.detach()
			CloseWindow()

		BeginDrawing()
		ClearBackground(RAYWHITE)
		
		BeginMode2D(camera)
		game.draw_2D()
		EndMode2D()

		game.draw_overlay()

		EndDrawing()

	CloseWindow()

if __name__ == "__main__":
	sock = socket.socket()
	print("Waiting for host at localhost:4242. . .")
	
	while sock.connect_ex(("localhost", 4242)) != 0: {
		sleep(0.1)
	}
	print("Connected. Playing Chess.")

	play_chess(sock, 1)