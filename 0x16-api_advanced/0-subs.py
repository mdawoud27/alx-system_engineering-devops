#!/usr/bin/python3
"""0-subs.py"""
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and
    returns the number of subscribers"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'user-Agent': 'Too Many Requests'}

    request = requests.get(url=url, headers=headers).json()
    subscribers = request.get('data', {}).get('subscribers', 0)

    return subscribers
