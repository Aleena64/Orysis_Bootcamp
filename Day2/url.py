import re

url_id = input("Enter the required url : ")
pattern = re.compile(r"https?://(www\.)?([a-zA-Z0-9.-]+\b)") 
print("Domain : ", pattern.match(url_id).group(2))