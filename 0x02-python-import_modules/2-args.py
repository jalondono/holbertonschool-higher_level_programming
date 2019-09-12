#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    j = 0
    size = len(argv) - 1
    if size == 0:
        print("{:d} arguments.".format(size))
    else:
        if size == 1:
            print("{:d} argument:".format(size))
        else:
            print("{:d} arguments:".format(size))
    for i in argv:
        if i != argv[0]:
            print("{:d}: {}".format(j, i))
        j += 1
