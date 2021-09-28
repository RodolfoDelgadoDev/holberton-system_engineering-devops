#!/usr/bin/python3
"""
recursive function that queries the Reddit API
and returns a list containing the titles of all
hot articles for a given subreddit.
"""
import requests


def rec(subreddit, url, di, l, hot_list, i):
        if i == len(l) and di['data']['after']:
                url = 'https://www.reddit.com/r/{}/hot.json?after={}'\
                      .format(subreddit, di['data']['after'])
                r = requests.get(url, headers={'User-Agent': 'Rochos'})
                di = r.json()
                l = di['data']['children']
                i = 0
                return rec(subreddit, url, di, l, hot_list, i)
        elif i == len(l) and di['data']['after'] is None:
                return hot_list
        else:
            hot_list.append(l[i]['data']['title'])
            i = i + 1
            return rec(subreddit, url, di, l, hot_list, i)


def recurse(subreddit, hot_list=[]):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(url, headers={'User-Agent': 'Rochos'})
    if r.status_code == 200:
        di = r.json()
        l = di['data']['children']
        hot_list = []
        i = 0
        lista = rec(subreddit, url, di, l, hot_list, i)
        if len(lista) == 0:
                return None
        return lista
    else:
        return None
