import numpy as np
# from Table import Table

def funcA(x):
    return x ** 2

def funcB(x, y):
    return x ** 2 + y ** 2

def solveLine(table, pow):
    pass

def solveNotLine(table, pow):

    # A * X = B
    # x = A^(-1) * B

    dim = pow + 1
    
    koefsA = np.zeros((dim, dim))
    koefsB = np.zeros((dim))

    for i in range(dim):
        for j in range(dim):
            koefsA[i, j] = sum[table.weight[i]* table.x[i] ** (i + j)]