#!/usr/bin/python3
"""
recursive function that queries the Reddit API
and returns a list containing the titles of all
hot articles for a given subreddit.
"""
import requests


def rec(l, hot_list, i):
        if i == len(l):
            return hot_list
        else:
            hot_list.append(l[i]['data']['title'])
            i = i + 1
            return rec(l, hot_list, i)


def recurse(subreddit, hot_list=[]):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(url, headers={'User-Agent': 'Rochos'})
    if r.status_code == 200:
        di = r.json()
        l = di['data']['children']
        hot_list = []
        i = 0
        return rec(l, hot_list, i)
    else:
        return None
