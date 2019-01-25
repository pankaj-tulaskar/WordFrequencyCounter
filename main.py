import requests
from bs4 import BeautifulSoup
import operator

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
        symbols = "🚧 ⚑★🚙#🚘~!@🌟✔👍$%^&*()_+`-={}|:\">?[]\;',./'"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)

    create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)

start("https://newyork.craigslist.org/d/automotive-services/search/aos")