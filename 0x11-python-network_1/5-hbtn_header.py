#!/usr/bin/python3
import requests
from sys import argv

"""Write a Python script that takes in a URL,
 sends a request to the URL and displays the
  value of the variable X-Request-Id"""

if __name__ == "__main__":
    header = 'X-Request-Id'
    r = requests.get(argv[1])
    print(r.headers.get(header))
