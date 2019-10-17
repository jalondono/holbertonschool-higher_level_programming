# !/usr/bin/python3
"""Function to read a given number of lines"""


def read_lines(filename="", nb_lines=0):
    """
    read a print a given number of lines
    :param filename:
    :param nb_lines:
    :return:
    """
    cont = 0
    with open(filename, encoding='utf-8') as myFile:
        for line in myFile:
            if (nb_lines <= 0) or (cont < nb_lines):
                print(line, end="")
                cont += 1
