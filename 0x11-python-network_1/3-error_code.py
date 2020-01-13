#!/usr/bin/python3
import urllib.request
import urllib.error
from sys import argv


""" Python script that takes in a URL, 
sends a request to the URL and displays
"""
if __name__ == "__main__":
	url = argv[1]
	req = urllib.request.Request(url)
	try:
		with urllib.request.urlopen(req) as response:
			the_page = response.read()
			print(the_page.decode('utf-8'))
	except urllib.error.HTTPError as e:
		print("Error code: {}".format(e.code))
