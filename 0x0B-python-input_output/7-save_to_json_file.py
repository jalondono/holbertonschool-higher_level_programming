#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """function to save an object in a json file"""
    with open(filename, mode='w', encoding='utf-8') as myFile:
        json.dump(my_obj, myFile, ensure_ascii=False)
