#!/usr/bin/python3
def uppercase(str):
    flag = 0
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            flag = 32
        else:
            flag = 0
        print("{:c}".format(ord(i) - flag), end='')
    print("")
