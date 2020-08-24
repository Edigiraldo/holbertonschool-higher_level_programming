#!/usr/bin/python3
"""Response header value - X-Request-Id."""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    var = response.headers.get['X-Request-Id']
    print(var)
