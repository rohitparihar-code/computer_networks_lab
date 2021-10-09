import socket
from server_settings import ServerSettings as s


def udp_server():

    # SOCK_DGRAM creates a UDP connection
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((s.host, s.port))

    try:
        bytesAddressPair = server_socket.recvfrom(s.bufferSize)
        address = bytesAddressPair[1]
        clientIp = "{}".format(address)
        greeting = "\nHi " + clientIp + \
            " you have successfully connected to " + \
            str(s.host) + ":" + str(s.port) + " on UDP!\n"
        server_socket.sendto(greeting.encode(), address)
        print("Successfully sent greeting....")
    except:
        print("Error Occurred...")
        exit()


if __name__ == '__main__':
    udp_server()
