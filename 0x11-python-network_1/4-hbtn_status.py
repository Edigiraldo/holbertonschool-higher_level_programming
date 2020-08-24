#!/usr/bin/python3
""" What's my status? """
import requests

if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status')
    html = response.text
    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
