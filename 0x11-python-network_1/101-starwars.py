#!/usr/bin/python3`
import requests
from sys import argv
"""Write a Python script that takes in a string
and sends a search request to the Star Wars API"""
if __name__ == "__main__":

    if len(argv) != 2:
        name = ""
        print("No result")
    else:
        name = argv[1]
        list_names = []
        url = 'https://swapi.co/api/people/?search=' + name
        r = requests.get(url)
        output = r.json()
        count = output.get('count')
        results = output.get('results')
        print("Number of results: {:d}".format(count))
        for names in results:
            print(names.get("name"))
        while output.get('next'):
            r = requests.get(output.get('next'))
            output = r.json()
            results = output.get('results')
            for names in results:
                print(names.get("name"))
