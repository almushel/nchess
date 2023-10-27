#import argparse
import socket
import multiprocessing
from chess_client import play_chess


def main():
	server_socket = socket.socket()
	server_socket.bind(("localhost", 4242))
	server_socket.listen(1)

#	while True:
	clientsocket, address = server_socket.accept()
	client = multiprocessing.Process(target=play_chess, args=(clientsocket, 0))
	client.start()
	client.join()

main()