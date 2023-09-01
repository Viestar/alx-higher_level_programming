#!/usr/bin/python3
"""
Script lists 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”
"""

from sys import argv
import requests

if __name__ == '__main__':
    rep = argv[1]
    user = argv[2]
    data = requests.get(f'https://api.github.com/repos/{rep}/{user}/commits')
    commits = data.json()

    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
