import requests
from bs4 import BeautifulSoup


url = "https://www.frontendmentor.io/challenges"

response = requests.get(url)

html = response.content
soup = BeautifulSoup(html, 'html.parser')

posts = soup.find_all('div', class_="Content__Wrapper-sc-f0243o-0 lmXsSl")

for post in posts:
    post = post.find('a', class_="Text__Wrapper-sc-zbm6r7-0 Link__Wrapper-sc-1e3vyao-0 dlUsuD jYwppH").get_text()
    langTag = post.find('li', class_="Text__Wrapper-sc-zbm6r7-0 kxGznp")

    print(post.get_text())
