#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numaux = abs(number) % 10
if numaux > 5:
        print("Last digit of {:d} is {:d}".format(number, numaux),
              "and is greater than 5")
elif numaux == 0:
        print("Last digit of {:d} is {:d}".format(number, (numaux)),
              "and is 0")
else:
        if number < 0:
                print("Last digit of {:d} is -{:d}".format(number, numaux),
                      "and is less than 6 and not 0")
        else:
                print("Last digit of {:d} is {:d}".format(number, numaux),
                      "and is less than 6 and not 0")
