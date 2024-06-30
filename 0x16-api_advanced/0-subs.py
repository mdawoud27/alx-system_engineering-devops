#!/usr/bin/python3
""""""
import requests

subreddit = 'python'
limit = 100
timeframe = 'month'
listing = 'top'

def get_reddit(subreddit, listing, limit, timeframe):
    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
        request = requests.get(base_url, headers = {'user-agent':'madbot'})
    except:
        print('An error occured')
    return request.json()

r = get_reddit(subreddit, listing, limit, timeframe)
# print(r)

def get_post_titles(r):
    '''
    Get a List of post titles
    '''
    posts = []
    for post in r['data']['children']:
        x = post['data']['title']
        posts.append(x)
    return posts

posts = get_post_titles(r)
print(posts)

