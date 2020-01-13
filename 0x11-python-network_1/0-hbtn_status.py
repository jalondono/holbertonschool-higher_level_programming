#!/usr/bin/python3
import urllib.request
"""Write a Python script that
fetches https://intranet.hbtn.io/status"""

if __name__ == "__main__":
	req = urllib.request.Request('https://intranet.hbtn.io/status')
	with urllib.request.urlopen(req) as response:
		the_page = response.read()
		print("\t- type: {}".format(type(the_page)))
		print("\t- content: {}".format(the_page))
		print("\t- utf8 content: {}".format(the_page.decode('utf-8')))
