#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status with urllib """

from urllib import request

if __name__ == "__main__":
    data = request.Request('https://intranet.hbtn.io/status')
    with request.urlopen(data) as pool:
        html = pool.read()
        print('Body response:')
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode('utf-8')}")
