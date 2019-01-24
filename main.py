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

        cleanup_list(word_list)

def cleanup_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "~!@$%^&*()_+`-={}|:\">?[]\;',./'"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)

start("https://newyork.craigslist.org/d/automotive-services/search/aos")