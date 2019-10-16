#!/usr/bin/python3


def write_file(filename="", text=""):
    """
    write a text in a file
    :param filename:
    :param text:
    :return:
    """
    with open(filename, mode='w', encoding='utf-8') as myFile:
        myFile.write(text)
        return len(text)
