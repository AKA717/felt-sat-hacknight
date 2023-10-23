from scrape import fetch_news

if __name__ == "__main__":
    news_list = fetch_news()
    print(news_list)