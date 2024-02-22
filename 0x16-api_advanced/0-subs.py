#!/usr/bin/python3
'''
Queries the Reddit API and returns the number of subscribers for a given
subreddit. If an invalid subreddit is given, the function should return 0
'''

import json
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers to the subreddit"""

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': 'Muchoki'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    # print(response.status_code)
    if response.status_code == 404:
        return 0
    json_data = response.json()
    subscribers = json_data['data']['subscribers']
    return subscribers
