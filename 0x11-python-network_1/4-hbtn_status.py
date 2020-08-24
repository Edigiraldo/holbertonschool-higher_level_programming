#!/usr/bin/python3
""" What's my status? """
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read().decode('utf-8')
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
