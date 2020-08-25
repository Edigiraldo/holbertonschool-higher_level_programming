#!/usr/bin/python3
"""POST: Search API with a letter."""
import requests
from sys import argv

if __name__ == "__main__":

    q = ""
    if len(argv) > 1:
        q = argv[1]

    url = 'http://a82acf3b689c.9790342a.hbtn-cod.io:5000/search_user'
    response = requests.post(url, data={'q': q})
    try:
        json = response.json()
        if not bool(json):  # if empty dict
            print("No result")
        else:
            id = json['id']
            name = json['name']
            print("[{}] {}".format(id, name))
    except ValueError:
        print("Not a valid JSON")
