import dns.resolver

domain = input("Enter Domain: ")
print()
try:
    for x in dns.resolver.query(domain, 'MX'):
        print(x)
except:
    print("Error, Verify the input and try again...")
print()