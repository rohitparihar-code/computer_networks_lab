import socket
import os
import threading
from server_settings import ServerSettings as s


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Send Message to Server\nEnter 'quit' to stop connection\n")
message = input("Enter UserName: ")
client_socket.sendto(message.encode(), (s.host, s.port))

def closeAll():
    print("Closing Connection...")
    client_socket.close()


def listener():
    while True:
        data = client_socket.recvfrom(s.bufferSize)
        message = data[0].decode()
        address = data[1]
        print(f"Server: {message}")
        if message == "quit":
            closeAll()
            os._exit(1)
        print("->", end=" ")

def sender():
    while True:
        data = input("-> ")
        client_socket.sendto(data.encode(), (s.host, s.port))
        if data == "quit":
            closeAll()
            os._exit(1)

t1 = threading.Thread(target=listener)
t2 = threading.Thread(target=sender)

t1.start()
t2.start()