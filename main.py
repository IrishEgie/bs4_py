from bs4 import BeautifulSoup
import requests as rq

response = rq.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

# Find all titles
titles_soup = soup.find_all(name="h3", class_="title")

title_list = [title.getText() for title in titles_soup]

with open("top-100-movies-list.txt", "w") as file:
    
    for title in reversed(title_list):
        file.writelines(f"{title}\n")