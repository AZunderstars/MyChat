import socket

hostName = "localhost"
serverPort = 8088


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((hostName, serverPort))
        s.listen()
        conn, addr = s.accept()
        with conn:
            data = conn.recv(2000).decode()
            numbers = data.split(',')
            result = sum(map(int, numbers))
            conn.sendall(str(result).encode())
            conn.close()
        s.close()


if __name__ == "__main__":
    main()
