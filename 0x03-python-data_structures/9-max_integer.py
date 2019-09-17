#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    for currmax in my_list:
        for i, data in enumerate(my_list):
            if data > currmax:
                break
            if i == len(my_list) - 1:
                return currmax
    return 0
