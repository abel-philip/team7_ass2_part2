from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen

# write this as environment variable
WEBPAGE_URL = "https://seekingalpha.com/earnings/earnings-call-transcripts"
CLASS_NAME = "list-group-item-heading"

def scrap_webpage():
    req = Request('https://seekingalpha.com/earnings/earnings-call-transcripts', headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, "html.parser")
    # search all html lines containing table data
    news_row = soup.find_all('h3', {'class': CLASS_NAME})
    # print("news_row",news_row)
    # print(CLASS_NAME)
    news = []
    for story in news_row:
        # print("story",story)
        news.append(story.find('a').contents[0])

    df = pd.DataFrame.from_dict(news)
    # print(df)
    scraped


    # def dataframe_sum_words(words, dataframe):
    #     summary = []
    #     print(words)
    #     for each in words:
    #         print(each)
    #         count = df[0].str.count('\\b'+each+'\\b', re.I).sum()
    #         summary.append([str(each), str(count)])
    #         summary_df = pd.DataFrame.from_records(summary, columns=['word','count'])
    #     return summary_df

    # summary = dataframe_sum_words(["CEO"], df)
    # write_data = summary.to_csv(index=False)

    return df

if __name__ == "__main__":
    # execute only if run as a script
    scrap_webpage()
