import socket
from datetime import date
from server_settings import ServerSettings as s


def sendData(connection, data):
    connection.send(data.encode())


def server():

    server_socket = socket.socket()

    server_socket.bind((s.host, s.port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    sendData(conn, "Successfully Connected\n1. Get Date\n0. Exit\nEnter Your Choice: ")

    while True:
        dataReceived = conn.recv(1024).decode()
        data = str(dataReceived)
        if data == "0":
            print("Request To Close Connection from " + str(address))
            break
        elif data == "1":
            print("Request To Send Date from " + str(address))
            sendData(conn, "\nDate: " + str(date.today()))
        else:
            print("Invalid Request: " + data + " from " + str(address))
            sendData(conn, "Invalid Request... Try Again")
        sendData(conn, "\n1. Get Date\n0. Exit\nEnter Your Choice: ")

    sendData(conn, "\nClosing Connection...\nBye (:\n\n")
    conn.close()


if __name__ == '__main__':
    server()
