#!/usr/bin/python3
"""comment."""
import requests
from sys import argv

if __name__ == "__main__":

    repository = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/' + owner +\
          '/' + repository + '/commits'

    response = requests.get(url)
    list = response.json()
    for i in range(0, 10):
        sha = list[i].get('sha')
        name = list[i].get('commit').get('author').get('name')
        print(sha, name)
