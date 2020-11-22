from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen

# write this as environment variable
WEBPAGE_URL = "https://seekingalpha.com/earnings/earnings-call-transcripts"
TEST_CLASS_NAME = "list-group-item-heading"
ARTICLE_CLASS_NAME = "list-group-item article"
TAG_CLASS_NAME = "article-symbols"
DIV_CLASS_NAME = "article-desc"


def scrap_webpage():
    req = Request(WEBPAGE_URL, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, "html.parser")
   
    #Test Code
    # search all html lines containing table data
    # news_row = soup.find_all('h3', {'class': TEST_CLASS_NAME})
    # print("news_row",news_row)
    # print(CLASS_NAME)
    # news = []  
    # for story in news_row:
    #     # print("story",story)
    #     news.append(story.find('a').contents[0])
    # df = pd.DataFrame.from_dict(news)
    
    news_row = soup.find_all('li', {'class': ARTICLE_CLASS_NAME})
    column_names = ["heading", "tag", "timestamp"]
    df = pd.DataFrame(columns = column_names)
    # time_row.find('a').contents[0]}
    row_values = []
    for story in news_row:
        tag_row = story.find('span', {'class': TAG_CLASS_NAME})
        time_row = story.find('div', {'class': DIV_CLASS_NAME})
        row_values.append({"heading": story.find('a').contents[0], "tag": tag_row.find('a').contents[0], "timestamp": time_row.text})
    df = df.append(row_values, ignore_index=True)
    df = df.reset_index(drop=True)
    print(df)
    scraped_data = pd.DataFrame.to_csv(df, path_or_buf="../scraped_data/data.csv")

    return df

if __name__ == "__main__":
    # execute only if run as a script
    scrap_webpage()
