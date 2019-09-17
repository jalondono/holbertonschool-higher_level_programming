#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    auxlist = []
    if my_list is None:
        return None
    for i in my_list:
        if i % 2 == 0:
            auxlist.append(True)
        else:
            auxlist.append(False)
    return auxlist
