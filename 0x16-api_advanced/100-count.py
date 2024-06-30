#!/usr/bin/python3
"""100-count.py"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """ecursive function that queries the Reddit API, parses the title of all
    hot articles, and prints a sorted count of given keywords"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'user-Agent': 'Too Many Requests'}
    params = {'after': after, 'limit': 100}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    # Normalize word list to lowercase
    word_list = [word.lower() for word in word_list]

    for post in posts:
        title = post.get('data', {}).get('title', '').lower()
        for word in title.split():
            # Remove non alphanumeric chars
            cleaned_word = ''.join(char for char in word if char.isalnum())
            if cleaned_word in word_list:
                if cleaned_word in word_count:
                    word_count[cleaned_word] += 1
                else:
                    word_count[cleaned_word] = 1

    after = data.get('data', {}).get('after')
    if after:
        return count_words(subreddit, word_list, after, word_count)
    else:
        if not word_count:
            return None
        else:
            sorted_words = sorted(
                word_count.items(), key=lambda kv: (-kv[1], kv[0])
            )
            for word, count in sorted_words:
                print(f'{word}: {count}')
            return word_count
