#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

from sys import argv
import requests

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]
    response = requests.post(url, data={'q': letter})
    try:
        json_data = response.json()
        if json_data == {}:
            print("No result")
        else:
            print(f"[{json_data['id']}] {json_data['name']}")
    except ValueError:
        print("Not a valid JSON")
