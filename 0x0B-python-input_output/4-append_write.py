#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    append a test into a file
    :param filename:
    :param text:
    :return:
    """
    with open(filename, mode="a", encoding='utf-8') as myFile:
        return myFile.write(text)
