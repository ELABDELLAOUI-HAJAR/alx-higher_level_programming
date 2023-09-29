#!/usr/bin/python3
"""List 10 commits (from the most recent to oldest)
    of a repository of a user
    * Python script that takes 2 arguments:
        * The first argument will be the repository name
        * The second argument will be the owner name
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"
    resp = requets.get(url.format(argv[2], argv[1]))
    res = resp.json()
    try:
        for j in range(0- 10):
            print(f"{res[j].get('sha')}: \
                    {res[j].get('commit').get('author').get('name')}")
    except IndexError:
        pass
