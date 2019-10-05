#!/usr/bin/python3

"""
This is the "2-matrix_divided" module.
The 2-matrix_divided module supplies one function, matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):

    """Matrix division function
       Args:  matrix: matrix div: divisor
       Returns:  A new matrix """

    message = "matrix must be a matrix (list of lists) of integers/floats"
    lastvalue = 0
    current = 0
    newlist = []
    templist = []
    flag = 0
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i, row in enumerate(matrix):
        if not isinstance(row, list):
            raise TypeError(message)

        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        templist.clear()
        for idx, data in enumerate(row):
            if type(data) is float or type(data) is int:
                templist.append(round((data / div), 2))
            else:
                raise TypeError(err)
        newlist.append(templist.copy())

    return newlist
