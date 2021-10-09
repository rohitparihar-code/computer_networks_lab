from os import error
import socket

TARGET_HOST = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def scan_port(port) -> bool:
    try:
        con = s.connect((TARGET_HOST, port))
        return True
    except:
        return False

if __name__ == '__main__':
    start = int(input("Enter the Start port: "))
    end = int(input("Enter the end port: "))
    for port in range(start, end+1):
        print(f"Port {port}:", end=" ")
        if scan_port(port):
            print("Open")
        else:
            print("Close")
        
    
    print("\nScanned All The Ports")