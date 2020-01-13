#!/usr/bin/python3
import urllib.request
from sys import argv
"""Python script that takes in a URL
, sends a request to the URL and displays
the value of the X-Request-Id"""

if __name__ == "__main__":
	url = argv[1]
	header_tofind = 'X-Request-Id'
	req = urllib.request.Request(url)
	with urllib.request.urlopen(req) as response:
		header_info = response.info()
		print(header_info['X-Request-Id'])
