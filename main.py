from bs4 import BeautifulSoup

with open("website.html") as web:
    content=web.readlines()
    # print(content)

soup = BeautifulSoup(content)