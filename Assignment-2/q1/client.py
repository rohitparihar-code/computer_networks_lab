import socket


SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

client_socket.send("GET / HTTP/1.1".encode())

data = client_socket.recv(1024).decode()

print(f"{data}")

client_socket.close()
