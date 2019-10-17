#!/usr/bin/python3

if __name__ == "__main__":
    """
    function to add an item to a list and save like json
    """
    import sys
    import json

    load_from_json_file = \
        __import__('8-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
    filename = 'add_item.json'
    try:
        file = load_from_json_file(filename)
    except:
        file = []

    for args in sys.argv[1:]:
        file.append(args)
    save_to_json_file(file, filename)
