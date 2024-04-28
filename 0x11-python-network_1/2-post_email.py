#!/usr/bin/python3

"""
This module sent a post request to a specific website
and print it's response
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values).encode("ascii")

    with urllib.request.urlopen(url, data=values) as response:
        email = response.read().decode("utf-8")
        print(f"Your email is: {email}")
