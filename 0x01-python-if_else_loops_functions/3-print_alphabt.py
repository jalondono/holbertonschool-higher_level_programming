#!/usr/bin/python3
for i in range(0, 26):
    if i + 97 == 101 or i + 97 == 113:
        continue
    print("{:c}".format(i + 97), end='')
