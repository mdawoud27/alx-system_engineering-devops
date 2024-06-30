#!/usr/bin/python3
"""2-recurse.py"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'user-Agent': 'Too Many Requests'}
    params = {'after': after, 'limit': 100}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    for post in posts:
        hot_list.append(post.get('data', {}).get('title'))

    after = data.get('data', {}).get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
