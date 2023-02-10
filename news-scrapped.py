import requests
from bs4 import BeautifulSoup

# function to crawl from different news sources
# function for the sources to get the news from
def get_container(url : str, parser): 
    if 'ndtv.com' in url:
        return parser.find(id='ins_storybody')
    elif 'cnn.com' in url:
        return parser.find(class_ = 'article__content')
    else:
        return None

def get_news_data(url: str):
    page = requests.get(url)
    parser = BeautifulSoup(page.content, 'html.parser')
    container = get_container(url,parser)
    if container is None:
        return "Unknown url"
    paragraphs = container.select('p')
    news_data=''
    for p in paragraphs:
        news_data += p.text + '\n'
    return news_data

news = get_news_data("https://www.ndtv.com/india-news/no-pressure-from-adani-group-gvk-boss-gv-sanjay-reddy-refutes-rahul-gandhi-charge-3761900")
# soup = BeautifulSoup(news.content, 'html.parser')
# story_body = soup.find(id='ins_storybody')
# paragraph = story_body.select('p')
# for p in paragraph:
print(news)

print("\n\nSECOND NEWS\n\n")


news2 = get_news_data("https://edition.cnn.com/2023/02/06/china/china-response-suspected-spy-balloon-intl-hnk/index.html")
# soup2 = BeautifulSoup(news2.content, 'html.parser')
# story_body2 = soup2.find(class_ = 'article__content')
# paragraph2 = story_body2.select('p')
# for line in paragraph2:
print(news2)

print("\n\nTHIRD NEWS\n\n")

# news3 = get_news_data("https://www.bbc.co.uk/news/uk-wales-64424723")
# print(news3)

# news4 = get_news_data("https://www.theguardian.com/music/2023/feb/07/pink-floyd-lyricist-calls-roger-waters-an-antisemite-and-putin-apologist")
# print(news4)