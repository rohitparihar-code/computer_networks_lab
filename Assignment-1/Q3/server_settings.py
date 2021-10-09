import socket


class ServerSettings:
    host = socket.gethostname()
    port = 5000
    bufferSize = 1024  # bytes
    numberOfClients = 1
