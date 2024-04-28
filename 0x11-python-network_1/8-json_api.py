#!/usr/bin/python3

"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    letter = ""
    if len(sys.argv) > 1:
        letter = sys.argv[1]

    values = {"q": letter}
    res = requests.post(url, values)

    try:
        body = res.json()
        if body:
            print(f"[{body['id']}] {body['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
