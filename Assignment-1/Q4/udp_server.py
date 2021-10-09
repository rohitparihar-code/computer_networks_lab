import socket
import threading
import os
from server_settings import ServerSettings as s


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((s.host, s.port))
print(f"Server Started @ {s.host}:{s.port}")

clients_list = []
clients = {}

def removeClient(client_address):
    print(f"{clients[client_address]} is quiting....")
    clients_list.remove(client_address)
    del clients[client_address]

def listener():
    while True:
        data = server_socket.recvfrom(s.bufferSize)
        message = data[0].decode()
        address = data[1]
        if message == "quit":
            removeClient(address)
            continue
        if address in clients.keys():
            for x in clients_list:
                if x != address:
                    server_socket.sendto(f"{clients[address]}: {message}".encode(), x)
            print(f"{clients[address]}: {message}")
            print("->", end=" ")
        else:
            print(f"New Connection: {message}")
            clients_list.append(address)
            clients[address] = message
            server_socket.sendto("Successfully Registered in the server".encode(), address)

if __name__ == '__main__':
    listener()
