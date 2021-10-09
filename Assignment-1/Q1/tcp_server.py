import socket
from server_settings import ServerSettings as s


def tcp_server():

    # SOCK_STREAM creates a TCP connection
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((s.host, s.port))

    server_socket.listen(1)
    conn, address = server_socket.accept()
    try:
        print("Connection from: " + str(address))
        greeting = "\nHi " + str(address[0]) + ":" + str(address[1]) + \
            " you have successfully connected to " + \
            str(s.host) + ":" + str(s.port) + " on TCP!\n"
        conn.sendall(greeting.encode())
        print("Successfully sent greeting\nClosing connection....")
    finally:
        conn.close()


if __name__ == '__main__':
    tcp_server()
