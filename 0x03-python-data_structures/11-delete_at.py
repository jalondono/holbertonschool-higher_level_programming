#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list is None:
        return None
    size = len(my_list)
    if size < 0 or idx > size - 1 or idx < 0:
        return my_list
    del my_list[idx]
    return my_list
