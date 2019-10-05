#!/usr/bin/python3

"""
This is the "5-text_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):

    """text_indentation function
       Args:  text is the text to be printed
       Prints:  text """

    characters = ['?', '.', ':']
    string = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for idx, chara in enumerate(text):

        if chara in characters:
            string += text[idx] + "\n\n"
        else:
            if ((idx != 0 and text[idx - 1] in characters) and text[idx] == ' ') or\
                    text[idx] == ' ' and text[idx - 1] == ' ':
                pass
            else:
                string += chara
    print(string, end='')
