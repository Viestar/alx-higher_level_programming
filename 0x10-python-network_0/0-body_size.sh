#!/usr/bin/env bash

# A Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

if [ "$#" -eq 2 ]; then
    size=$(curl -s "$1" | wc -c)
    echo "$size"
else
    exit 1
fi
