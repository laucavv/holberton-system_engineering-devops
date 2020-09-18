#!/usr/bin/python3
""" function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """  list containing the titles of all hot articles for a given subreddit
     """
    if after is None:
        return []
    url_r = "https://api.reddit.com/r/{}/".format(subreddit)
    url_r += "hot.json?limit=100&after={}".format(after)
    request_t = requests.get(url_r, headers={'User-Agent': 'Python3'})
    if str(request_t) == '<Response [200]>':
        children = request_t.json().get('data').get('children')
        after = request_t.json().get('data').get('after')
        for data_c in children:
            hot_list.append(data_c.get('data').get('title'))
        return hot_list + recurse(subreddit, [], after)

    else:
        return(None)
