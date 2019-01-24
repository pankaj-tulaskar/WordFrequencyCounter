import requests
from bs4 import BeautifulSoup

def start(url):
    word_list = []
    s_code = requests.get(url).text
    fetch = BeautifulSoup(s_code,"html.parser")
    for post_text in fetch.findAll('a', {'class': 'result-title hdrlnk'}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)

start("https://newyork.craigslist.org/d/automotive-services/search/aos")