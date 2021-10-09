import socket
import threading
from server_settings import ServerSettings as s


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((s.host,s.port))
server_socket.listen(s.numberOfClients)

print(f"Server Up and Running {s.host}:{s.port}...")

socket_list = []

def listen_for_new_connection():
    while True:
        client_socket, client_addr = server_socket.accept()
        client_socket.send("Connected To Server...".encode())
        print(f"New Connection from: {client_addr}")
        socket_list.append(client_socket)
        t = threading.Thread(target=listen_and_forward_message, args=(client_socket, client_addr))
        t.start()


def listen_and_forward_message(client_socket, client_addr):
    while True:
        try:
            data = client_socket.recv(s.bufferSize).decode()
            print(f"{client_addr}: {data}")
            if data == "quit":
                print(f"{client_addr} is Closing The Connection")
                socket_list.remove(client_socket)
                client_socket.close()
                break
            for x in socket_list:
                if x != client_socket:
                    x.send(f"{client_addr}: {data}".encode())
        except:
            print(f"{client_addr} is closing Connection....")
            socket_list.remove(client_socket)
            client_socket.close()
            break

if __name__ == '__main__':
    listen_for_new_connection()