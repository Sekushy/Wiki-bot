import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    URL = 'https://en.wikipedia.org/wiki/Wikipedia:Unusual_articles'
    page = requests.get(URL).content
    soup = BeautifulSoup(page, "lxml")
    tables = soup.find_all("table", "wikitable")
    print(tables[0].find_all('a'))