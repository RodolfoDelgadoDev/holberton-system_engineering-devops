#!/usr/bin/python3
"""
function that queries the Reddit
API and returns the number of subscribers
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = requests.get(url, headers={'User-Agent': 'Rochos'})
    if r.status_code == 200:
        di = r.json()
        return di['data']['subscribers']
    else:
        return 0
