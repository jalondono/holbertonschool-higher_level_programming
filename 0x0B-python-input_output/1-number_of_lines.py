#!/usr/bin/python3
"""Function to count the number of lines insede a file"""


def number_of_lines(filename=""):
    linenum = 0
    """
    printing a file
    :param filename:
    :return: number of lines
    """
    with open(filename, encoding="utf-8") as myFile:
        while True:
            line = myFile.readline()
            if not line:
                break
            linenum += 1
        return linenum
