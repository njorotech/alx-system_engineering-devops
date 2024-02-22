#!/usr/bin/python3
"""a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. If no results
are found for the given subreddit, the function should return None.
"""

import requests


def recurse(subreddit, hot_list=[]):
    """Queries the Reddit Api and returns a list containing the titles of all
    hot articles for a given subreddit.
    """

    headers = {
        'User-Agent': 'Muchoki'
    }

    base_url = 'https://www.reddit.com/r/'
    url = f'{base_url}{subreddit}/hot.json'

    def recursive_request(url):
        """A function that calls itself"""

        r = requests.get(url, headers=headers, allow_redirects=False)
        if r.status_code == 200:
            json_data = r.json()
            after = json_data['data']['after']
            url = f'{base_url}{subreddit}/hot.json?after={after}'
            # print(json.dumps(json_data, indent=4))
            for item in json_data["data"]["children"]:
                title = item["data"]["title"]
                hot_list.append(title)
            if after is None:
                return
            return recursive_request(url)
            print("None")
    recursive_request(url)
    return hot_list
