#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not type(roman_string) is str:
        return None
    acum = 0
    dicc = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in roman_string:
        for letra in dicc:
            if i == letra:
                acum += dicc[letra]
                continue
    return acum
