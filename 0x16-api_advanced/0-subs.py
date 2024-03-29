#!/usr/bin/python3
'''
Queries the Reddit API and returns the number of subscribers for a given
subreddit. If an invalid subreddit is given, the function should return 0
'''
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers to the subreddit"""

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    # if subreddit is None or not isinstance(subreddit, str):
    #     return 0
    # if subreddit is None or type(subreddit) is not str:
    #     return 0
    response = requests.get(url, headers=headers, allow_redirects=False)
    # print(response.status_code)
    if response.status_code == 200:
        json_data = response.json()
        data_results = json_data.get("data")
        subscribers = data_results.get("subscribers")
        return subscribers
    else:
        return 0
