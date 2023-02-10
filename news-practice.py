import requests
from bs4 import BeautifulSoup

# news = get_news_data("https://www.ndtv.com/india-news/no-pressure-from-adani-group-gvk-boss-gv-sanjay-reddy-refutes-rahul-gandhi-charge-3761900")
# soup = BeautifulSoup(news.content, 'html.parser')
# story_body = soup.find(id='ins_storybody')
# paragraph = story_body.select('p')
# for p in paragraph:
# print(news)

print("\n\nSECOND NEWS\n\n")


# news2 = get_news_data("https://edition.cnn.com/2023/02/06/china/china-response-suspected-spy-balloon-intl-hnk/index.html")
# soup2 = BeautifulSoup(news2.content, 'html.parser')
# story_body2 = soup2.find(class_ = 'article__content')
# paragraph2 = story_body2.select('p')
# for line in paragraph2:
# print(news2)

print("\n\n Third News")

news3 = requests.get("https://www.bbc.co.uk/news/uk-wales-64424723")
soup3 = BeautifulSoup(news3.content, 'html.parser')
story_body3 = soup3.find(class_ = 'ssrcss-1q0x1qg-Paragraph eq5iqo00')
paragraph3 = story_body3.select('p')
for l in paragraph3:
    print(news3)