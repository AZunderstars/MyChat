import socket

HOST = "localhost"
PORT = 8088
MAX_BUFFER = 2000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"1,2,3,4")
    data = s.recv(MAX_BUFFER)
print(data.decode())
