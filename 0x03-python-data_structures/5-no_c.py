#!/usr/bin/python3
def no_c(my_string):
    j = ''
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        j += i
    return j
