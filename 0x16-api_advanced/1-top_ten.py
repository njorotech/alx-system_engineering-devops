#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts listed
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints titles of the first 10 hot posts"""

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=9'
    headers = {
        'User-Agent': 'Muchoki'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    # print(response.status_code)
    if response.status_code == 200:
        json_data = response.json()
        # print(json.dumps(json_data, indent=4))
        for item in json_data["data"]["children"]:
            print(item["data"]["title"])
    else:
        print("None")
