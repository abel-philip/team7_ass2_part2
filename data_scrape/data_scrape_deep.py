from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen
import requests
from requests import get
import numpy as np
from time import sleep
from random import randint
from selenium import webdriver

# write this as environment variable
WEBPAGE_URL = "https://seekingalpha.com/earnings/earnings-call-transcripts"
DOMAIN_NAME = "https://seekingalpha.com"
TEST_CLASS_NAME = "list-group-item-heading"
ARTICLE_CLASS_NAME = "list-group-item article"
TAG_CLASS_NAME = "article-symbols"
DIV_CLASS_NAME = "article-desc"
ANCHOR_CLASS_NAME = "dashboard-article-link"

def scrap_webpage():
    req = Request(WEBPAGE_URL, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()

    # headers = {"Accept-Language": "en-US, en;q=0.5"}
    # page = requests.get(WEBPAGE_URL, headers=headers)
    
    soup = BeautifulSoup(page, "html.parser")
    links = soup.find_all('a', {'class': ANCHOR_CLASS_NAME})
    
    for link in links:
        WEBPAGE_URL_INSIDE = DOMAIN_NAME + link.get('href')
        sleep(randint(10, 15))
        print(WEBPAGE_URL_INSIDE)
        req_inside = Request(WEBPAGE_URL_INSIDE, headers={'User-Agent': 'Mozilla/5.0'})
        page_inside = urlopen(req_inside).read()

        # headers = {"Accept-Language": "en-US, en;q=0.5"}
        # page_inside = requests.get(WEBPAGE_URL_INSIDE, headers=headers)

        soup_inside = BeautifulSoup(page_inside.text, "html.parser")

        # news_row = soup.find('div', {'id': "content-rail"})
        # print(news_row)


    return True

if __name__ == "__main__":
    # execute only if run as a script
    scrap_webpage()
