import socket
import threading
import os
from server_settings import ServerSettings as s


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((s.host, s.port))
print(f"Server Started @ {s.host}:{s.port}")

clients_list = []
clients = {}

def closeAll():
    server_socket.close()
    print("Closing Connection...")
    os._exit(1)

def listener():
    while True:
        data = server_socket.recvfrom(s.bufferSize)
        message = data[0].decode()
        address = data[1]
        if address in clients.keys():
            print(f"{clients[address]}: {message}")
            if message == "quit":
                closeAll()
            print("->", end=" ")
        else:
            print(f"New Connection: {message}")
            clients_list.append(address)
            clients[address] = message
            server_socket.sendto("Successfully Registered in the server".encode(), address)

def sender():
    while True:
        data = input("-> ")
        if len(clients_list) > 0:
            for x in clients_list:
                server_socket.sendto(data.encode(), x)
        if data == "quit":
            closeAll()

t1 = threading.Thread(target=listener)
t2 = threading.Thread(target=sender)

t1.start()
t2.start()
