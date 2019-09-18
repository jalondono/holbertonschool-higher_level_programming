#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    max = my_list[0]
    for data in my_list:
        if data > max:
            max = data
    return max
    return 0
