from os import error
import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TARGET_HOST = ''  # IP address only


def scan_port(start_port, end_port):
    for port in range(start_port, end_port+1):
        try:
            s.connect((TARGET_HOST, port))
            print(f"Port {port}: OPEN")
        except:
            print(f"Port {port}: close")


if __name__ == '__main__':
    start = int(input("Enter the Start port: "))
    end = int(input("Enter the end port: "))

    mid = int((start + end)/2)

    t1 = threading.Thread(target=scan_port, args=(start, mid))
    t2 = threading.Thread(target=scan_port, args=(mid, end))

    t1.start()
    t2.start()
