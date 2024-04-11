import requests

NEWS_API_KEY = "eec3a4f6b35f41c2a985d468764809fd"

def fetch_news(category='general', country='india'):
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey=eec3a4f6b35f41c2a985d468764809fd'
    response = requests.get(url)
    if response.status_code == 200:
        print("good")
        return response.json()['articles']
    else:
        print("bad")
        return None
