import requests
from beautifulsoup4 import bs4

page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
soup = bs4(page.content, 'html.parser')
print(soup.prettify())
