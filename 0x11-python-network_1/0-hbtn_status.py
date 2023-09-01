#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status with urllib """

import urllib.request as purl

if __name__ == "__main__":
    with purl.urlopen('https://intranet.hbtn.io/status') as pool:
        html = pool.read()
        print('Body response:')
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode('utf-8')}")
