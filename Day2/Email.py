import re

email_id=input("Enter your email id:")
pattern="\w*@(?!yahoo|hotmail)\w*\.com"
if (re.match(pattern, email_id)):
    print("valid email")
else:
    print("invalid email")
    