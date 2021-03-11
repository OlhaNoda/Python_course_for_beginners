# task2_130321
"""
Requests using concurrent and multiprocessing libraries
Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
As a result, store all comments in chronological order in JSON and dump it to a file.
For this task use concurrent and multiprocessing libraries for making requests to Reddit API.
"""

import requests
import json
import multiprocessing


def get_content(url, subreddit):
    ret = requests.get(url, params={"subreddit": subreddit})
    data = ret.json()
    return data


def get_comments(data):
    comments = []
    for entry in data['data']:
        comment = {'author': entry['author'], 'time': entry['created_utc'], 'text': entry['body']}
        comments.append(comment)
    return comments


def write_data_to_file(data):
    with open('comments.json', 'w') as f:
        json.dump(data, f)


def load_data(url, author):
    print("start main func")
    data = get_content(url, author)
    comments = get_comments(data)
    write_data_to_file(comments)
    print("end main func")


def process_load_data(url, author):
    t = multiprocessing.Process(target=load_data, args=(url, author))
    t.start()
    print("Process is started")
    t.join()
    print("Process is completed")
    return t


if __name__ == '__main__':
    my_url = "https://api.pushshift.io/reddit/comment/search/"
    my_subreddit = "Pikabu"
    process_load_data(my_url, my_subreddit)
