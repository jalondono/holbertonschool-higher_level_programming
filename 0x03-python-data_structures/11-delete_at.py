#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    auxlist = []
    j = 0
    size = len(my_list)
    if size < 0 or idx > size:
        return my_list
    del my_list[idx]
    return my_list
