#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
and 
"""

import requests

if __name__ == '__main__':
    data = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print(f"\t- type: {type(data.text)}")
    print(f"\t- content: {data.text}")
