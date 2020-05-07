#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda f, x: list(map(f, x)),
                         len(matrix) * [lambda x: x ** 2], matrix))
