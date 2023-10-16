from bs4 import BeautifulSoup
import request

file=open("index.html")
contents=file.read()
file.close()
#print(contents)

soup=BeautifulSoup(contents, "html.parser")
#print(soup.prettify())
#print(soup.h1)
#print(soup.find_all(name="a"))
#print(soup.h1.text)
'''print(soup.find(name="a").get("href"))
all_links=soup.find_all(name="a")
for link in all_links:
    print(link.getText)'''

'''first_heading=soup.find(name="h1", id="first heading")
print(first_heading.getText())'''

first_heading=soup.find(class_="small-para")
print(first_heading)