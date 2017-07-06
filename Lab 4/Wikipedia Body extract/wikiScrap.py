import requests
from bs4 import BeautifulSoup
import os

#created by saria goudarzvand
def search_spider(sea, lim):
    url = "https://en.wikipedia.org/w/index.php?limit="+lim+"&offset=0&search="+sea
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    result_list = soup.findAll('div', {'class': "mw-search-result-heading"})
    print(result_list)
    for div in result_list:
        link = div.find('a')
        href = "https://en.wikipedia.org"+link.get('href')
        if (link.get('href').startswith("http")):
            href=link.get('href')
        get_data(href)


def get_data(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    title = soup.find('h1', {'id': 'firstHeading'})
    file_title = search + '/' + str(title.string) + ".txt"
    file = open(file_title,'w')
    file.write(str(title.string) + '\n')
    for para in soup.findAll('p'):
        file.write(str(para.string))

search = input('type something to search in wiki: ')
limit = input('how many results do you want to get?: ')

if not os.path.exists(search):
    print("Creating folder " + search)
    os.makedirs(search)

searc = search.replace(' ', '+')
search_spider(searc, limit)