#!/usr/bin/python3
import requests
from sys import argv

"""Write a Python script that takes
 in a letter and sends a POST request to
  http://0.0.0.0:5000/search_user with the letter as
   a parameter.
"""

if __name__ == "__main__":
    letter = ""
    if len(argv) != 2:
        print("No result")
    else:
        letter = argv[1]
        url = 'http://0.0.0.0:5000/search_user'
        values = {'q': letter}
        try:
            r = requests.post(url, values)
            output = r.json()
            if output:
                print("[{}] {}".format(output.get('id'), output.get('name')))
            else:
                print("No result")
        except Exception:
            print("Not a valid JSON")
