#!/usr/bin/python3
"""1-top_ten.py"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'user-Agent': 'Too Many Requests'}

    response = requests.get(url, headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    for post in posts:
        print(post.get('data', {}).get('title', None))
