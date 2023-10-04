#!/usr/bin/python3
"""
Script lists 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”
"""

from sys import argv
import requests
import sys
if __name__ == '__main__':
    if len(argv) > 2:
        rep = argv[1]
        user = argv[2]
        data = requests.get(f'https://api.github.com/repos/{user}/{rep}/commits')
        commits = data.json()
        try:
            for commit in range(10):
                print("{}: {}".format(
                    commits[commit].get("sha"),
                    commits[commit].get("commit").get("author").get("name")))
        except IndexError:
            pass
    else:
        print(sys.api_version)
        print(sys.copyright)
        print(sys.displayhook)
        print(sys.flags)
        print(sys.getsizeof(sys.api_version))

