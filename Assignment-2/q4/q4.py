from requests.api import get
from datetime import datetime


def printDetails(url):
    try:
        startTime = datetime.now()
        res = get(url)
        elapsedTime = datetime.now() - startTime
        print(f"\nRequest: {res.request}")
        print(f"\nStatus Code: {res.status_code}")
        print(f"\nStatus Message: {res.reason}")
        print(f"\nElapsed Time: {elapsedTime}")
        print(f"\nHeaders")
        for x in res.headers:
            print("\t" + x + ": " + res.headers[x])
        
        print(f"\nEncoding: {res.apparent_encoding}")
    except:
        print("\nUnknown Error Occurred\nTry again")


if __name__ == '__main__':
    while True:
        print("\n1. Enter a new Url\n0. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                url = input("\nEnter URL: ")
                printDetails(url)
            else:
                print("\nClosing Program...\n")
                break
        except:
            print("\nInvalid Input...\nTry again")