import socket
import threading
import os
from server_settings import ServerSettings as s


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((s.host, s.port))
print("Server Started @ " + str(s.host) + ":" + str(s.port))
server_socket.listen(s.numberOfClients)
conn, address = server_socket.accept()
print(f"Connection from: {address}")

def closeAll():
    print("Closing Connection")
    conn.close()
    server_socket.close()

def listener():
    while True:
        data = conn.recv(s.bufferSize).decode()
        print(f"Client: {data}")
        if data == "quit":
            closeAll()
            os._exit(1)
        print("->", end=" ")


def sender():
    while True:
        msg = input("-> ")
        conn.sendall(msg.encode())
        if msg == "quit":
            closeAll()
            os._exit(1)

t1 = threading.Thread(target = listener)
t2 = threading.Thread(target = sender)

t1.start()
t2.start()