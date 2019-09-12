#!/usr/bin/python3
import sys
j = 0
size = len(sys.argv) - 1
if size == 0:
        print("{:d} arguments.".format(size))
else:
    if size == 1:
        print("{:d} argument:".format(size))
    else:
        print("{:d} arguments:".format(size))
for i in sys.argv:
    if i != sys.argv[0]:
        print("{:d}: {}".format(j, i))
    j += 11
