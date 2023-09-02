#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""

from sys import argv
import sys
import urllib.request
import urllib.error
if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
# if __name__ == '__main__':
#     if len(argv) > 0:
#         data_url = Request(argv[1])
#         try:
#             with urlopen(data_url) as data:
#                 html = data.read()
#                 utf8 = html.decode('utf-8')
#                 print(utf8)
#         except HTTPError :
#             print(f"Error code: {HTTPError.code}")
#     else:
#         sys.exit()
