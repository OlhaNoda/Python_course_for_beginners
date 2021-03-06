# task2_150321
"""
Requests using asyncio and aiohttp
Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
As a result, store all comments in chronological order in JSON and dump it to a file.
For this task use asyncio and aiohttp libraries for making requests to Reddit API.
"""
import json
import aiohttp
import asyncio
import time


async def load(url, subreddit):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params={"subreddit": subreddit}) as resp:
            data = await resp.json()
            return data


def get_content(url, subreddits):
    start = time.time()
    loop = asyncio.get_event_loop()
    data = asyncio.gather(*[load(url, subreddit) for subreddit in subreddits])
    content = loop.run_until_complete(data)
    loop.close()
    print('Start asyncio_get_content: {} Time taken: {}'.format(start, time.time() - start))
    return content


def write_data_to_file(data):
    with open('comments.json', 'w') as f:
        json.dump(data, f)


def main(url, subreddits):

    data = get_content(url, subreddits)
    write_data_to_file(data)


if __name__ == '__main__':
    my_url = "https://api.pushshift.io/reddit/comment/search/"
    my_subreddits = ("Pikabu", "distantsocializing")
    main(my_url, my_subreddits)
