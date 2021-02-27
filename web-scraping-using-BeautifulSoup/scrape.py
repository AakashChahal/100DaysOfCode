import requests
from bs4 import BeautifulSoup
import pprint

def pages_request(pages):
    for page in range(1, pages + 1):
        res = requests.get(f'https://news.ycombinator.com/news?p={page}')
        soup = BeautifulSoup(res.text, 'html.parser')
        if page == 1:
            links = soup.select('.storylink')
            sub = soup.select('.subtext')
        else:
            links = soup.select('.storylink')
            sub = soup.select('.subtext')
    return custom_news(links, sub)

def sort_news(news_list):
    return sorted(news_list, key = lambda k: k['votes'], reverse=True)

def custom_news(links, subtext):
    news = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        link = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                news.append({'title': title, 'link': link, 'votes': points})
    return sort_news(news)

if __name__ == '__main__':
    p = int(input('How many pages: '))
    pprint.pprint(pages_request(p))
