import requests, random, csv, re
from bs4 import BeautifulSoup
import pandas as pd


def generate_csv():
    URL = 'https://en.wikipedia.org/wiki/Wikipedia:Unusual_articles'
    page = requests.get(URL).content
    soup = BeautifulSoup(page, "lxml")
    tables = soup.find_all("table", "wikitable")

    final_links = []
    titles = []

    for i in range(0, len(tables)):
        table_rows = tables[i].find_all('b')
        for i in range(len(table_rows)):
            links = table_rows[i].find_all('a')
            for link in links:
                final_links.append(link.get('href'))
                titles.append(link.get('title'))

    df = pd.DataFrame()
    df['Title'] = titles
    df['Link'] = final_links
    df.to_csv('Unusual_articles.csv',index=False)

def get_random_article():
    csvfile = (pd.read_csv('Unusual_articles.csv')).sample()
    title = csvfile['Title'].values[0]
    link = 'https://en.wikipedia.org' + csvfile['Link'].values[0]
    return title, link

if __name__ == "__main__":
    #generate_csv()
    title_of_article, link_of_article = get_random_article()
    print('Your random article of the day about {}: {}'.format(title_of_article, link_of_article))