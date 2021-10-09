import socket
from server_settings import ServerSettings as s


def tcp_client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    if s.host != '':
        host = s.host
    client_socket.connect((host, s.port))

    data = client_socket.recv(s.bufferSize).decode()
    print(data)

    client_socket.close()


if __name__ == '__main__':
    tcp_client()
