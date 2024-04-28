#!/usr/bin/python3

"""This module sent a request to a specific website and print it's response"""

import urllib.request


url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read()
    print("Body response:")
    print(f"    - type: {type(body)}")
    print(f"    - content: {body}")
    print(f"    - utf8 content: {body.decode('utf-8')}")
