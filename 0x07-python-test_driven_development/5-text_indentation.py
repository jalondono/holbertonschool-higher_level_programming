#!/usr/bin/python3

"""
This is the "5-text_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):

    """text_indentation function
       Args:  text is the text to be printed
       Prints:  text """

    caracteres = ['?', '.', ':']
    string = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for idx, chara in enumerate(text):

        if chara in caracteres:
            string += text[idx] + "\n\n"
        else:
            if ((idx != 0 and text[idx - 1] in caracteres) and text[idx] == ' ') or\
                    text[idx] == ' ' and text[idx - 1] == ' ':
                pass
            else:
                string += chara
    print(string, end='')
