from bs4 import BeautifulSoup
import requests
import pprint

res = requests.get("https://news.ycombinator.com/newest")

soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titleline')
subtext = soup.select('.subtext')
#votes = soup.select('.score')

def custom_hn(l, v):
    hn = []
    for idx, link in enumerate(l):
        title = link.getText()
        href = link.get('href', None)
        vote = v[idx].select('.score')
        if len(vote):
            point = int(vote[0].getText().split(' ')[0])
            if point > 2:
                hn.append({'title': title, 'href': href , 'votes': point})

    return hn

pprint.pprint(custom_hn(links, subtext))
