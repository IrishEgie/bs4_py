from bs4 import BeautifulSoup
import lxml


with open("website.html") as web:
    content=web.read()
    # print(content)

soup = BeautifulSoup(content, "html.parser")

# print(soup.title.string)
# print(soup)

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.get("href"))

# heading =  soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_ = "heading")
print(section_heading)