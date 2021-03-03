# task2_030321
"""
Load data
Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
As a result, store all comments in chronological order in JSON and dump it to a file.
"""

import requests
import json
import datetime


def transform_unix_time(unix_time):
    value = datetime.datetime.fromtimestamp(unix_time)
    return value.strftime('%Y-%m-%d %H:%M:%S')


def get_comments(url, author):
    response = requests.get(url, {"author": author})
    data = response.json()
    comments = []
    for entry in data['data']:
        comment = {'time': transform_unix_time(entry['created_utc']), 'text': entry['body']}
        comments.append(comment)
    return comments


def write_data_to_file(data):
    with open('comments.json', 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    my_url = "https://api.pushshift.io/reddit/comment/search/"
    my_author = "YogaG5"
    write_data_to_file(get_comments(my_url, my_author))
