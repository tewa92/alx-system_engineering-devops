#!/usr/bin/python3
"""
Script that queries the Reddit API and returns the titles of all hot articles
for a given subreddit using recursion.
"""
import requests
from sys import argv


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of titles of all hot
    articles for a given subreddit.
    """
    user_agent = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after, 'limit': 100}  # limit to 100 results per request

    response = requests.get(url,
                            headers=user_agent,
                            params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json().get('data')
    if not data:
        return None

    children = data.get('children')
    for child in children:
        hot_list.append(child['data']['title'])

    after = data.get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list


if __name__ == "__main__":
    if len(argv) > 1:
        recurse(argv[1])
    else:
        print("Usage: {} <subreddit>".format(argv[0]))
