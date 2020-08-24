#!/usr/bin/python3
"""POST an email"""
import requests
from sys import argv

if __name__ == "__main__":

    url = argv[1]
    email = argv[2]

    response = requests.post(url, data={'email': email})
    body = response.text
    print(body)
