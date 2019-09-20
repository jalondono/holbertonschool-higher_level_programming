#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    newdic = a_dictionary.copy()
    for i in newdic:
        newdic.update({i: newdic.get(i) * 2})
    return newdic
