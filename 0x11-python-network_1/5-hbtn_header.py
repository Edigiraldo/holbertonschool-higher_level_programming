#!/usr/bin/python3
"""Response header value - X-Request-Id."""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    try:
        var = response.headers['X-Request-Id']
        print(var)
    except:
        pass
