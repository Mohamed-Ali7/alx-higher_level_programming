#!/usr/bin/python3

"""
List 10 commits (from the most recent to oldest) of a repository
using Github API
"""
import requests
import sys

if __name__ == "__main__":

    repository = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    params = {'per_page': 10}

    res = requests.get(url, params=params)
    commits = res.json()

    for commit in commits:
        print(f"{commit['sha']}: {commit['commit']['author']['name']}")
