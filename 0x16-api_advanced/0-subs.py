#!/usr/bin/python3
""" Write a function that queries the Reddit API and
    returns the number of subscriber
"""
import requests


def number_of_subscribers(subreddit):
    """ The fuction returns the number of subscribers """
    url_r = "https://api.reddit.com/r/{}/about".format(subreddit)
    request_t = requests.get(url_r, headers={'User-Agent': 'Python3'})
    if str(request_t) == '<Response [200]>':
        return request_t.json().get('data').get('subscribers')
    return 0
