#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status with urllib """

import urllib.request

# if __name__ == "__main__":
#     response = urllib.request.Request('https://intranet.hbtn.io/status')
#     with urllib.request.urlopen(response) as data:
#         html = data.read()
#         print('Body response:')
#         print(f"\t- type: {type(html)}")
#         print(f"\t- content: {html}")
#         print(f"\t- utf8 content: {html.decode('utf-8')}")


if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
