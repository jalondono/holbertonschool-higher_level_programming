#!/usr/bin/python3
def print_last_digit(number):
    numaux = 0
    if number < 0:
        numaux = -number % 10
        print("{:d}".format(numaux), end='')
        return numaux
    else:
        print("{:d}".format(number % 10), end='')
        return number % 10
