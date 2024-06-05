#!/usr/bin/python3
'''
Script that queries the Reddit API and prints the titles of the first 10 hot
posts listed for a given subreddit.
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    '''
    user = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    response = requests.get(url, headers=user, allow_redirects=False)
    if response.status_code == 200:
        try:
            data = response.json()
            for post in data['data']['children']:
                print(post['data']['title'])
        except (ValueError, KeyError) as e:
            print(None)
    else:
        print(None)


if __name__ == "__main__":
    if len(argv) > 1:
        top_ten(argv[1])
    else:
        print("Usage: {} <subreddit>".format(argv[0]))
