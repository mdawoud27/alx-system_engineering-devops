#!/usr/bin/python3
"""0-subs.py"""
import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API and
    returns the number of subscribers"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'user-Agent': 'Too Many Requests'}

    response = requests.get(url=url, headers=headers)
    if response.status_code != 200:
        return 0

    data = response.json()
    subscribers = data.get('data', {}).get('subscribers', 0)

    return subscribers
