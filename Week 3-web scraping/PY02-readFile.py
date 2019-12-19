from bs4 import BeautifulSoup

with open("carviewer.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

print (soup.prettify())