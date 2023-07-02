#!/usr/bin/python3
# 2-matrix_divided.py
# HAJAR EL ABDELLAOUI
"""Define one function called matrix_divided"""


def matrix_divided(matrix, div):
    """Definition of matrix_divided function
    that divides all elemnts of a matrix by div

    args:
        matrix: is a list of a list of integers/floats
        div: is a number (integer/float)
    Exceptions:
        Invalid matrix : TypeError with msg : 'matrix must
        be a matrix (list of lists) of integers/floats'

        when matrix rows have not the same size: TypeError
        with msg : 'Each row of the matrix must have the
        same size'

        when div is not number: TypeError with msg: 'div
        must be a number'

        when div == 0: ZeroDivisionError with msg :
        'division by zero'

    Return:
        new matrix with all elements are the result of
        the division of matrix element by div rounded to 2
        decimal places
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(elm, (int, float))
                    for elm in (x for row in matrix for x in row))):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
