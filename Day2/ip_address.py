import re
ip_address = input("Enter ip address : ")
pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

if(re.match(pattern,ip_address)):
    print("Valid IPv4 address.")
else:
    print("Invalid IPv4 address.")