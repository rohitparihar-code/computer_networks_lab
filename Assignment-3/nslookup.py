import os

s = []

try:
    input_file = open("input.txt", "r")
except:
    print("Error Loading File")

try:
    s = input_file.readlines()
except:
    print("Error Reading Contents of the file")

try:
    for domain in s:
        res = os.system(f"nslookup {domain}")
        print(res)
except:
        print("Invalid Domain")

input_file.close()