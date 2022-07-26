import socket
from time import sleep
from _thread import start_new_thread

HOST = "localhost"
PORT = 8080
MAX_BUFFER = 2000
SLEEP_TIME = 5


def workload():
    sleep(SLEEP_TIME)


def generate_response(buf):
    items = buf.decode().split(",")
    items_int = map(int, items)
    resp = sum(items_int)
    return str(resp).encode()


def threaded(conn):
    workload()
    buf = conn.recv(MAX_BUFFER)
    conn.send(generate_response(buf))


def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen()
    return sock


def accept_connections(sock):
    conn, addr = sock.accept()
    with conn:
        start_new_thread(threaded, (conn,))


def main():
    with start_server() as sock:
        while True:
            try:
                accept_connections(sock)
            except KeyboardInterrupt:
                break


if __name__ == '__main__':
    main()