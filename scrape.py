import requests
import ast
from concurrent.futures import ThreadPoolExecutor

def insertion_sort(list):
    print(list)

def fetch_news():
    def fetch_single_news(news_id):
        news_url = f"https://hacker-news.firebaseio.com/v0/item/{news_id}.json?print=pretty"
        news_url_res = requests.get(news_url)
        
        if news_url_res.status_code == 200:
            news_data = ast.literal_eval(news_url_res.text)
            if 'score' in news_data and int(news_data['score']) >= 100:
                custom_dict = {}
                custom_dict['title'] = news_data.get('title', 'N/A')
                custom_dict['score'] = int(news_data.get('score', 0))
                custom_dict['url'] = news_data.get('url','N/A')
                return custom_dict
        return None

    # Define the URL of the page to scrape
    url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response and limit to the first 50 entries
        news_id_list = ast.literal_eval(response.text)[:50]

        # Fetch news items concurrently using ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=10) as executor:
            news_list = list(executor.map(fetch_single_news, news_id_list))
        
        # Filter out None values (failed requests)
        news_list = [news for news in news_list if news is not None]

        insertion_sort(news_list)
        return news_list

    else:
        print("Failed to fetch data. Status code:", response.status_code)
        return []

if __name__ == "__main__":
    news_list = fetch_news()
    #print(news_list)
