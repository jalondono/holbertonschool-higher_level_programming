#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """function to save an object in a json file"""
    with open(filename, encoding='utf-8') as myFile:
        data = json.load(myFile)
        return data
