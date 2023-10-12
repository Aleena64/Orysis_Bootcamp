import re

dates=input("Enter the required date:")
pattern="\d{2}/\d{2}/\d{4}"
if (re.match(pattern, dates)):
    print("valid date:", dates)
else:
    print("invalid date")