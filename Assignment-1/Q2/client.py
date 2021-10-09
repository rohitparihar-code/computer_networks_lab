import socket
from server_settings import ServerSettings as s


def client():

    client_socket = socket.socket()
    client_socket.connect((s.host, s.port))

    message = "1"
    while message == "1":
        data = client_socket.recv(s.bufferSize).decode()
        print(data)
        message = input("-> ")
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print("Message from Server: " + str(data))

    client_socket.close()


if __name__ == '__main__':
    client()
