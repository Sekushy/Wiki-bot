from bs4 import BeautifulSoup
import requests, random, csv
import pandas as pd

def pull_articles():
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
    return titles, final_links

def generate_csv(titles, links):
    df = pd.DataFrame()
    df['Title'] = titles
    df['Link'] = links
    df.to_csv('Unusual_articles.csv',index=False)
 
def get_random_article():
    csvfile = (pd.read_csv('Unusual_articles.csv')).sample()
    title = csvfile['Title'].values[0]
    link = 'https://en.wikipedia.org' + csvfile['Link'].values[0]
    return 'Your random article of the day about {}: {}'.format(title, link)