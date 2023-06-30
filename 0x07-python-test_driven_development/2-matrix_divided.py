#!/usr/bin/python3

"""A function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """list of int: Divides all elements of a matrix"""

    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(col, (int, float))
                    for col in [x for row in matrix for x in row])):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    tmp_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(round((matrix[i][j]/div), 2))
        tmp_matrix.append(row)

    return tmp_matrix
