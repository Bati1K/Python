import requests
from bs4 import BeautifulSoup # Import BeautifulSoup for parsing HTML

# URL of the webpage to scrape
url = "https://www.frontendmentor.io/challenges"

# Send an HTTP GET request to the URL and get the response
response = requests.get(url)

html = response.content # Get the content of the response
soup = BeautifulSoup(html, 'html.parser') # Parse the HTML content using BeautifulSoup


# Find all posts on the webpage with the specified class
posts = soup.find_all('div', class_="Content__Wrapper-sc-f0243o-0 lmXsSl")

for post in posts:
    post = post.find('a', class_="Text__Wrapper-sc-zbm6r7-0 Link__Wrapper-sc-1e3vyao-0 dlUsuD jYwppH").get_text()
    langTag = post.find('li', class_="Text__Wrapper-sc-zbm6r7-0 kxGznp")

    print(post.get_text())