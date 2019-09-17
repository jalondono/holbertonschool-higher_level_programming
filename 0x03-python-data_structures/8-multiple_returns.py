#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return 0, None
    size = len(sentence)
    if size == 0:
        char = ''
        return size, char
    char = sentence[0]
    return size, char
