#!/usr/bin/python3
import requests

""" Python script that takes in a URL,
sends a request to the URL and displays
"""
if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    print("\t type: {}".format(type(r.text)))
    print("\t content: {}".format(r.text))

