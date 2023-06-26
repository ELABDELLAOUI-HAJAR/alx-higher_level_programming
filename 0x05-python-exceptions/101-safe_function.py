#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    result = 0
    try:
        result = fct(*args)
    except Exception as e:
        stderr.write("Exception: {}\n".format(e))
        result = None
    return result
