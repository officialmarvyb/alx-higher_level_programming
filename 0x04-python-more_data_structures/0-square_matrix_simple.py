#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matr = []
    a = 0
    for i in matrix:
        new_matr.append([])
        for x in matrix[a]:
            new_matr[a].append(x**2)
        a += 1
    return (new_matr)
