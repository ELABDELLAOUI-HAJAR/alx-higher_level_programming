#!/usr/bin/python3
# 5-text_indentation.py
# Author : HAJAR EL ABDELLAOUI
"""Define text_indentation function"""


def text_indentation(text):
    """Definition of text_indentation function
    that prints a text with 2 new lines after each of these
    characters: `.` `?` `:`

    Args:
        text : must be a string

    Exceptions:
        TypeError with msg : 'text must be a string'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    idx = 0
    while idx < len(text) and text[idx] == ' ':
        idx += 1

    while idx < len(text):
        print(text[idx], end="")
        if text[idx] in ".?:" or text[idx] == '\n':
            if text[idx] in ".?:":
                print("\n")
            idx += 1
            while idx < len(text) and text[idx] == ' ':
                idx += 1
            continue
        idx += 1
