import socket
import os
import threading
from server_settings import ServerSettings as s


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((s.host, s.port))
print("Connected With Server\nEnter 'quit' to stop connection\n")

def closeAll():
    print("Closing Connection")
    client_socket.close()

def listener():
    while True:
        data = client_socket.recv(s.bufferSize).decode()
        print(f"Server: {data}")
        if data == "quit":
            closeAll()
            os._exit(1)
        print("->", end=" ")


def sender():
    while True:
        data = input("-> ")
        client_socket.sendall(data.encode())
        if data == "quit":
            closeAll()
            os._exit(1)


t1 = threading.Thread(target = listener)
t2 = threading.Thread(target = sender)

t1.start()
t2.start()

