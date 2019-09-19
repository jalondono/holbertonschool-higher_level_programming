#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    newmatrix = []
    for i in matrix:
        newmatrix.append(list(map(lambda x: x ** 2, i)))
    return newmatrix
