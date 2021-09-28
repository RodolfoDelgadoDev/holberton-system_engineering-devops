#!/usr/bin/python3
"""
function that queries the Reddit API and
prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(url, headers={'User-Agent': 'Rochos'})
    pichu = 1
    if r.status_code == 200:
        di = r.json()
        for i in di['data']['children']:
            if pichu == 10:
                break
            else:
                print(i['data']['title'])
                pichu = pichu + 1
    else:
        print("None")
