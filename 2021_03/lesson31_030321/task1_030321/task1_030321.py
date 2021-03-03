# task1_030321
"""
Robots.txt
Download and save to file robots.txt from wikipedia, twitter websites etc.
"""

import requests

url = 'https://uk.wikipedia.org/robots.txt'
ret = requests.get(url)
with open('uk_wikipedia_org_robots.txt', 'wb') as f:
    f.write(ret.content)
