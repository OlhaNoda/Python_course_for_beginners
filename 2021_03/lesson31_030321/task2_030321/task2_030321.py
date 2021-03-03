# task2_030321
"""
Load data
Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
As a result, store all comments in chronological order in JSON and dump it to a file.
"""

import requests
import json

url = "https://api.pushshift.io/reddit/comment/search/"
author = "YogaG5"

response = requests.get(url, {"author": author})
data = response.json()

with open('comments.json', 'w') as f:
    json.dump(data['data'], f)
