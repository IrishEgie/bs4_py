from bs4 import BeautifulSoup
import requests as rq

# Fetch the webpage
response = rq.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web = response.text

# Parse the webpage
soup = BeautifulSoup(yc_web, "html.parser")

# Find all articles
articles = soup.find_all(name="a", class_="storylink")

# Extract the text and links
article_texts = [article_tag.getText() for article_tag in articles] 
article_links = [article_tag.get("href") for article_tag in articles]

# Find all upvotes and extract the text
upvotes = soup.find_all(name="span", class_="score")
article_upvotes = [int(score.getText().split()[0]) for score in upvotes]

# # Print the extracted data
# print(article_links, article_texts, article_upvotes)

largest_num = max(article_upvotes)
largest_id = article_upvotes.index(largest_num)

print(article_texts[largest_id])
print(article_links[largest_id])

























# with open("website.html") as web:
#     content=web.read()
#     # print(content)

# soup = BeautifulSoup(content, "html.parser")

# # print(soup.title.string)
# # print(soup)

# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)

# # for tag in all_anchor_tags:
# #     print(tag.get("href"))

# # heading =  soup.find(name="h1", id="name")
# # print(heading)

# section_heading = soup.find(name="h3", class_ = "heading")
# print(section_heading)