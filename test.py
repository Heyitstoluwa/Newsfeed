from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key="67267a48db3c4a44ab6c63bbaaf62040")


print(newsapi.get_top_headlines()['articles'])