import socket
import threading
from server_settings import ServerSettings as s

client_socket = socket.socket()
client_socket.connect((s.host, s.port))
print("Type 'quit' to close connection\n")

def listen_for_msgs():
    while True:
        try:
            data = client_socket.recv(s.bufferSize).decode()
            print(f"{data}")
        except:
            print("Closing Connectin...")
            client_socket.close()
            break

def send_msgs():
    while True:
        try:
            data = input("-> ")
            client_socket.sendall(data.encode())
            if data == "quit":
                print("Closing Connection...")
                client_socket.close()
                break
        except:
            print("Closing Connectin...")
            client_socket.close()
            break

t1 = threading.Thread(target=listen_for_msgs)
t2 = threading.Thread(target=send_msgs)

t1.start()
t2.start()