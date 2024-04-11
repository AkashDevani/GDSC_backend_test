from flask import jsonify
from . import app
from .news_api import fetch_news

@app.route('/api/news', methods=['GET'])
def get_news():
    # Fetch news data from the News API
    news_data = fetch_news()
    if news_data:
        return jsonify({'status': 'success', 'articles': news_data})
    else:
        return jsonify({'status': 'error', 'message': 'Failed to fetch news data'}), 500
