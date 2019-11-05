import requests, re
from bs4 import BeautifulSoup
r = requests.get("https://www.barnesandnoble.com/w/toys-games-funkoverse-strategy-game-dc-4-pack/34119733?ean=0889698426282").content

soup = BeautifulSoup(r, 'html.parser')
h1 = soup.find("h1", itemprop="name")
span = soup.find("span", id="pdp-cur-price")
print(h1.text)
print(span.text)