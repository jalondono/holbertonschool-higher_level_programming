#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    size = 0
    if matrix is None:
        return None
    for idx, row in enumerate(matrix):
        size = len(row)
        if idx != 0:
            print('')
        for idxb, item in enumerate(row):
            if idxb != size and idxb != 0:
                print(' ', end='')
            print("{:d}".format(item), end='')
    print()
