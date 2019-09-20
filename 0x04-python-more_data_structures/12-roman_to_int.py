#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not type(roman_string) is str:
        return 0

    acum = 0
    anterior = 0
    j = 0
    dicc = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in roman_string:
        for letra in dicc:
            if i == letra:
                if j == 0:
                    anterior = dicc[letra]
                if anterior < dicc[letra]:
                    acum = acum - anterior * 2 + dicc[letra]
                else:
                    acum += dicc[letra]
                anterior = dicc[letra]
                continue
        j += 1

    return acum
