from time import sleep
import socket
import select
import multiprocessing
import argparse

from raylib import *
from chess import *

SCREEN_W = 800
SCREEN_H = 600
DEFAULT_ADDRESS = "localhost"
DEFAULT_PORT = 4242
MOVE_TEMPLATE = b"00,00"

def host_game(address, port):
	server_socket = socket.socket()
	server_socket.bind((address, port))
	server_socket.listen(1)

	print(f"Waiting for client at {address}:{port}. . .")

	clientsocket, address = server_socket.accept()
	client = multiprocessing.Process(target=join_game, args=(clientsocket, 0))
	client.start()
	client.join()

def join_game(game_socket, team):
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

def play_game():
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

if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		prog="Net Chess",
		description="A simple networked chess game",
	)	
	parser.add_argument("-m", "--mode", choices=["host", "join"])
	parser.add_argument("-a", "--address")
	parser.add_argument("-p", "--port", type=int)

	args = parser.parse_args() 
	
	address = DEFAULT_ADDRESS
	if args.address is not None:
		address = args.address
	
	port = DEFAULT_PORT
	if args.port is not None:
		port = args.port

	if args.mode == "host":
		host_game(address, port)			 
	elif args.mode == "join": 
		sock = socket.socket()
		print(f"Waiting for host at {address}:{port}. . .")
		
		while sock.connect_ex((address, port)) != 0: {
			sleep(0.1)
		}
		print("Connected. Playing Chess.")

		join_game(sock, 1)
	else:
		play_game()