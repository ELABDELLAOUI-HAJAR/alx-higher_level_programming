#!/usr/bin/python3
# 100-matrix_mul.py
"""Define matrix_mul function"""


def matrix_mul(m_a, m_b):
    """Definition of matrix_mul function

    Args:
        m_a, m_b : must be an list of lists of
                integers or floats

    Exceptions:
        TypeError: m_a must be a list
        TypeError: m_b must be a list
        TypeError: m_a must be a list of lists
        TypeError: m_b must be a list of lists
        ValueError: m_a can't be empty
        ValueError: m_b can't be empty
        TypeError: m_a should contain only integers or floats
        TypeError: m_b should contain only integers or floats
        TypeError: each row of m_a must be of the same size
        TypeError: each row of m_b must be of the same size
        ValueError: m_a and m_b can't be multiplied

    Return a new matrix
    """
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(isinstance(x, (int, float)) for row in m_a for x in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(x, (int, float)) for row in m_b for x in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Inverser the m_b matrix
    inversed_m_b = []
    for i in range(0, len(m_b[0])):
        new_row = []
        for j in range(0, len(m_b)):
            new_row.append(m_b[j][i])
        inversed_m_b.append(new_row)

    # multiply m_a with inversed_m_b
    mul_matrix = []
    for row in m_a:
        new_row = []
        for col in inversed_m_b:
            product = 0
            for i in range(0, len(inversed_m_b[0])):
                product += row[i] * col[i]
            new_row.append(product)
        mul_matrix.append(new_row)

    return mul_matrix
