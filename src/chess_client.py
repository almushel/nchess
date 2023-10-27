import socket
from multiprocessing import Process
from raylib import *
from chess import ChessGame

SCREEN_W = 800
SCREEN_H = 600
MOVE_TEMPLATE = "00,00"

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
		
		if game.turn == game.view:
			game.update(camera)
			if game.turn != game.view:
				game_socket.sendall(f"{game.moves_played[-1][0]},{game.moves_played[-1][1]}".encode("utf-8") )
		else:
			msg_bytes = game_socket.recv(len(MOVE_TEMPLATE))
			move_str = bytes.decode(msg_bytes)
			moves = move_str.split(",")
			game.execute_move(int(moves[0]), int(moves[1]))

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
	print("Connecting to localhost:4242")
	sock.connect(("localhost", 4242))
	print("Connected. Playing Chess")

	p = Process(target=play_chess, args=(sock, 1))
	p.start()
	p.join()