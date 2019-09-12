#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    vsigne = False
    signes = "+-*/"
    signe = ""
    if (len(argv) - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    vsigne = argv[2] in signes
    if (vsigne):
        a = int(argv[1])
        b = int(argv[3])
        signe = argv[2]
        if signe == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif signe == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif signe == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        else:
            print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
