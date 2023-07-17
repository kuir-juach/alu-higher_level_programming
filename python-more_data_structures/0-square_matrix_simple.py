#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None 
    retrun[[num * num for num in row] for row in matrix]
