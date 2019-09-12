#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = 0
    auxnum = 0

    for i in argv:
        if i != argv[0]:
            num = int(i)
            auxnum = auxnum + num
    print(auxnum)
