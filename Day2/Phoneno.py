import re

phone_no=input("Enter your phone number:")
pattern="\D\d{3}\D \d{3}-\d{4}|\d{10}"
if (re.match(pattern, phone_no)):
    print("valid phone number")
else:
    print("invalid phone number")