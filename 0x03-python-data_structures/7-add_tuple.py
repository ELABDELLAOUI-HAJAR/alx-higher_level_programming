#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        for i in range(len(tuple_a), 2):
            tuple_a += (0, )
    if len(tuple_b) < 2:
        for i in range(len(tuple_b), 2):
            tuple_b += (0, )
    my_tuple = tuple(tuple_a[i] + tuple_b[i] for i in range(2))
    return my_tuple
