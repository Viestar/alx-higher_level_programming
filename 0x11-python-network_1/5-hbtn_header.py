#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the
value of the variable X-Request-Id in the response header
"""

import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) > 1:
        data = requests.get(sys.argv[1])
        if 'X-Request-Id' in data.headers:
            print(data.headers['X-Request-Id'])
    else:
        sys.exit()
