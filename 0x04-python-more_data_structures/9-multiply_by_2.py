#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return None
    newdic = a_dictionary.copy()
    for i in newdic:
        newdic.update({i: newdic.get(i) * 2})
    return newdic
