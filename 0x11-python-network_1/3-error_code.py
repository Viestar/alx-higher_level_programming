#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""

from sys import argv
import sys
from urllib.request import urlopen
from urllib.error import HTTPError

if __name__ == '__main__':
    if len(argv) > 1:
        try:
            with urlopen(argv[1]) as data:
                html = data.read()
                utf8 = html.decode('utf-8')
                print(utf8)
        except HTTPError:
            print(f"Error code: {HTTPError.code}")
    else:
        sys.exit()
