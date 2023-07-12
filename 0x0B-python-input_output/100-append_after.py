#!/usr/bin/python3
"""Define append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """Definition of append_after function that
     inserts a line of text to a file, after each line containing
     a specific string

     Args:
        filename: The name of the file
        search_string: the string that we will search for it
        new_string: the string to be added after the specific str
    """
    with open(filename, "r", encoding="utf-8") as file:
        my_text = ""
        for line in file:
            my_text += line
            if search_string in line:
                my_text += new_string
        with open(filename, "w", encoding="utf-8") as f:
            f.write(my_text)
