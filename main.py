import board
import socket
from threading import Thread

HOST = '192.168.1.103'
PORT = 65431


def close_sockets(conn, server_socket):
    if conn is None:
        server_socket.close()


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    print("Waiting for connection...")
    server_socket.listen()
    conn, addr = server_socket.accept()
    Thread(target=close_sockets(conn, server_socket)).start()
    print('Connected by', addr)
    return conn


def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    return s


if __name__ == '__main__':
    s_c = input("Server (s) or client (c)?")
    board.Board(server() if s_c == 's' else client())
