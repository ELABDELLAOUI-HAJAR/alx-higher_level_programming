#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    list_sum = 0
    for i in my_set:
        list_sum += i
    return list_sum
