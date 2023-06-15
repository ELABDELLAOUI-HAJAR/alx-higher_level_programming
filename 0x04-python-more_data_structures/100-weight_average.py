#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    divisor = 0
    result = 0
    for binome in my_list:
        result += binome[0] * binome[1]
        divisor += binome[1]
    return result / divisor
