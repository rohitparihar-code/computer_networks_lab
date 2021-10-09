# Domain Name to host and vice versa
import socket


def dom_to_ip():
    try:
        domainName = input("\nEnter Domain Name: ")
        ip = socket.gethostbyname(domainName)
        print(f"IP Address: {ip}")
    except:
        print("Invalid Domain Name...")
    print("\n")


def ip_to_dom():
    try:
        ip = input("\nEnter IP Address: ")
        dom = socket.getfqdn(ip)
        print(f"Domain Name: {dom}")
    except:
        print("Error Occurred")
    print("\n")


if __name__ == '__main__':

    while True:
        print("1. Convert Domain Name To IP\n2. Convert IP to Domain Name\n0. Exit")
        choice = input("Enter Choice: ")
        if choice == "0":
            print("\nExiting Program...\n")
            break
        elif choice == "1":
            dom_to_ip()
        elif choice == "2":
            ip_to_dom()
        else:
            print("Invalid Choice...")