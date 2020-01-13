#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    name = argv[1]
    url = 'https://swapi.co/api/people/?search=' + name
    r = requests.get(url)
    output = r.json()
    count = output.get('count')
    print("Number of results: {:d}".format(count))
    results = output.get('results')
    for names in results:
        print(names['name'])
