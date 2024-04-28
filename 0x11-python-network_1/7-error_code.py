#!/usr/bin/python3

"""
takes in a URL, sends a request to the URL and displays
the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    res = requests.get(url)

    try:
        res.raise_for_status()
        print(res.text)
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {res.status_code}")
