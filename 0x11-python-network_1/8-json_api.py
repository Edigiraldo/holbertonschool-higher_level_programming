#!/usr/bin/python3
"""POST: Search API with a letter."""
import requests
from sys import argv

if __name__ == "__main__":

    letter = ""
    if len(argv) > 1:
        letter = argv[1]

    url = 'http://a82acf3b689c.9790342a.hbtn-cod.io:5000/search_user'
    response = requests.post(url, data={'q': letter})
    try:
        json = response.json()
    except:
        print("Not a valid JSON")
    else:
        if not bool(json):  # if empty dict
            print("No result")
        else:
            print(json['id'], json['name'])
