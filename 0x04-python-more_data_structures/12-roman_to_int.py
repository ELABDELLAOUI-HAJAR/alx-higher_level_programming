#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_dict = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}
    num = 0
    for index, value in enumerate(roman_string):
        if index + 1 == len(roman_string) \
                or roman_dict[value] >= roman_dict[roman_string[index + 1]]:
            num += roman_dict[value]
        else:
            num -= roman_dict[value]
    return num
