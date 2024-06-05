#!/usr/bin/python3
"""
Script that queries the Reddit API, parses the titles of all hot articles,
and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Queries the Reddit API and counts the occurrences of each keyword in
    word_list in the titles of hot articles for a given subreddit.
    """
    user_agent = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after, 'limit': 100}

    response = requests.get(url,
                            headers=user_agent,
                            params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print("Error: Received status code", response.status_code)
        return None

    data = response.json().get('data')
    if not data:
        print("Error: No data found in response")
        return None

    children = data.get('children')
    if not children:
        print("Error: No children found in data")
        return None

    for child in children:
        title = child['data']['title'].lower()
        for word in word_list:
            word_lower = word.lower()
            counts[word_lower] = counts.get(word_lower, 0) +
            title.split().count(word_lower)

    after = data.get('after')
    if after:
        return count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(),
                               key=lambda item: (-item[1],
                               item[0]))
        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))
        return counts


if __name__ == "__main__":
    from sys import argv

    if len(argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(argv[0]))
        print("Ex: {} programming 'python java javascript'".format(argv[0]))
    else:
        subreddit = argv[1]
        word_list = argv[2].split()
        count_words(subreddit, word_list)
