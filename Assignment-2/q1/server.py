import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

fin = open('index.html')
content = fin.read()
fin.close()
RESPONSE = 'HTTP/1.1 200 OK\n\n' + content

def my_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))

    server_socket.listen()
    print(f"Listening to Port: {SERVER_PORT}")

    while True:
        try:
            client_socket, client_addr = server_socket.accept()
            print(f"{client_addr} Connected...")
            data = client_socket.recv(1024).decode()
            x = data.split()
            if x[0] == "GET":
                client_socket.sendall(RESPONSE.encode())
            else:
                client_socket.sendall("HTTP/1.1 400 Bad Request\n\nNot a valid Method".encode())
            client_socket.close()
        except:
            client_socket.sendall("HTTP/1.1 404 Not Found\n\nError Not Found".encode())
            print(f"Connection Closed Abruptly for {client_addr}")
            client_socket.close()
        print(f"{client_addr} Closing Connection...")

    server_socket.close()

if __name__ == '__main__':
    my_server()
