# task3_060321
"""
Requests using multiprocessing
Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
As a result, store all comments in chronological order in JSON and dump it to a file.
For this task use Threads for making requests to reddit API.
"""
import requests
import json
import datetime


def transform_unix_time(unix_time):
    value = datetime.datetime.fromtimestamp(unix_time)
    return value.strftime('%Y-%m-%d %H:%M:%S')


def get_content(url, author):
    ret = requests.get(url, params={"author": author})
    data = ret.json()
    return data


def get_comments(data):
    comments = []
    comment_number = 1
    for entry in data['data']:
        comment = {'#': comment_number, 'author': entry['author'], 'time': transform_unix_time(entry['created_utc']), 'text': entry['body']}
        comments.append(comment)
        comment_number += 1
    return comments


def set_key_sort_by_time(value):
    return value['time']


def sort_comments_by_time(comments):
    comments.sort(key=set_key_sort_by_time)
    return comments


def write_data_to_file(data):
    with open('comments.json', 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    my_url = "https://api.pushshift.io/reddit/comment/search/"
    my_author = "YogaG5"
    my_comments = get_comments(get_content(my_url, my_author))
    sorted_comments = sort_comments_by_time(my_comments)
    write_data_to_file(sorted_comments)
    for comment in sorted_comments:
        print(comment)
