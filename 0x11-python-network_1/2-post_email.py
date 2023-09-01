#!/usr/bin/python3
"""
A Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""

from sys import argv
import sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen

if __name__ == '__main__':
    if len(argv) > 2:
        coded_url = urlencode({'email': argv[2]}).encode('ascii')
        query = Request(argv[1], coded_url)
        with urlopen(query) as response:
            print(response.read().decode('utf-8'))
    else:
        sys.exit()
