#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return None
    keys = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            keys.append(i)
    for j in keys:
        a_dictionary.pop(j)
    return a_dictionary
