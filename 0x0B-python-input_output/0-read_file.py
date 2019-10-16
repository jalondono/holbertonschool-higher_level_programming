#!/usr/bin/python3
"""Function de read and print a file"""


def read_file(filename=""):
    """
    printing a file
    :param filename:
    :return:
    """
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read())
