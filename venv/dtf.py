from bs4 import BeautifulSoup
import requests

url = 'https://dtf.ru/cinema'


def get_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news = soup.find_all('div', class_='content-title content-title--short l-island-a')
    for el in news:
        print(el.text.replace('Статьи редакции'+'/n',''))


get_news(url)
# for i in range(2,11):
#     get_news('https://habr.com/ru/all/page'+str(i))
