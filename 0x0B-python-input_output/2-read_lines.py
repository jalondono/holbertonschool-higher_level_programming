# !/usr/bin/python3
"""Function to read a given number of lines"""

number_of_lines = __import__('1-number_of_lines').number_of_lines


def read_lines(filename="", nb_lines=0):
    """
    read a print a given number of lines
    :param filename:
    :param nb_lines:
    :return:
    """
    with open(filename, encoding='utf-8') as myFile:
        if nb_lines <= 0 or nb_lines >= number_of_lines(filename):
            print(myFile.read())
        else:
            for i in range(0, nb_lines):
                line = myFile.readline()
                print(line, end='')
