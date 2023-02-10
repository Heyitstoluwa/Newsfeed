from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)


def get_top_headlines(client):
    top_headlines = client.get_top_headlines()
    # print(top_headlines)
    articles = top_headlines['articles']
    # titles = {}
    # images = {}
    # for item in articles:
    #     titles.append(item["title"])
    #     images.append(item["urlToImage"])
    # data = zip(title,images)
    return articles

def get_sources(client):
    response = client.get_sources()
    return response["sources"]


@app.route('/')
def Index():

    newsapi = NewsApiClient(api_key="67267a48db3c4a44ab6c63bbaaf62040")
    sources = get_sources(newsapi)
    headlines = get_top_headlines(newsapi)
    
    # for s in sources:
    #     print(s["url"])
    return render_template('news.html', context = sources )

@app.route('/articles')
def Articles():
    newsapi = NewsApiClient(api_key="67267a48db3c4a44ab6c63bbaaf62040")
    articles = get_top_headlines(newsapi)

    return render_template('articles.html', context = articles)



if __name__ == "__main__":
    app.run(debug = True)
