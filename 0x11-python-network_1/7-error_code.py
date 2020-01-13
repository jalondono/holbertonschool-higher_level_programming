#!/usr/bin/python3
import requests
from sys import argv

"""Write a Python script that takes in a URL
 and an email address, sends a POST request to the passed URL
  with the email as a parameter, and finally displays
   the body of the response."""

if __name__ == "__main__":
    url = argv[1]
    try:
        r = requests.get(url)
        r.raise_for_status()
        r = requests.get(url)
        print(r.text)

    except requests.exceptions.RequestException as e:
        print("Error code: {}".format(e.response.status_code))
