#!/usr/bin/python3
import requests
from sys import argv

"""Get request to get the last commits of a github repository"""

if __name__ == "__main__":
    repo_name = argv[1]
    owner_name = argv[2]
    param = {"per_page": "10"}
    url = "https://api.github.com/repos/" + owner_name + "/" + repo_name + "/commits"
    response = requests.get(url, params=param)
    output = response.json()
    for commit in output:
        sha = commit['sha']
        author = commit['commit']['author']['name']
        print("{}: {}".format(sha, author))
