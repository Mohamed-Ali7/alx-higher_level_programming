#!/usr/bin/python3

"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys
if __name__ == "__main__":
    url = "https://api.github.com/user"

    username = sys.argv[1]
    password = sys.argv[2]

    res = requests.get(url, auth=(username, password))
    body = res.json()
    print(body.get("id"))
