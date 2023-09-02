#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status with urllib """

import urllib

if __name__ == "__main__":
    response = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(response) as data:
        print('Body response:')
        print(f"\t- type: {type(data.read())}")
        print(f"\t- content: {data.read()}")
        print(f"\t- utf8 content: {(data.read()).decode('utf-8')}")
