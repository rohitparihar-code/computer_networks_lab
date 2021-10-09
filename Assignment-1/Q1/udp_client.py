import socket
from server_settings import ServerSettings as s


def udp_client():

    bytesToSend = str.encode("Hi")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = '127.0.0.1'
    if s.host != '':
        host = s.host
    client_socket.sendto(bytesToSend, (host, s.port))
    data = client_socket.recv(s.bufferSize).decode()
    print(data)


if __name__ == '__main__':
    udp_client()
