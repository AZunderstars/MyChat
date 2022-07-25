import socket

HOST = "localhost"
PORT = 8088  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"1,2,3,4")
    data = s.recv(1024)
print(data.decode())
