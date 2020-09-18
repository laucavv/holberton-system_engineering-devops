#!/usr/bin/python3
""" function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """  prints the titles of the first 10 hot posts listed
         for a given subreddit.
     """
    url_r = "https://api.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    request_t = requests.get(url_r, headers={'User-Agent': 'Python3'})
    if str(request_t) == '<Response [200]>':
        children = request_t.json().get('data').get('children')
        list_t = ''
        for data_c in children:
            list_t += data_c.get('data').get('title') + '\n'
        print(list_t, end="")
    else:
        print(None)
