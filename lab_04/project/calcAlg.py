import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt
from scipy.special import erfi
import math

def funcA(x):
    return 0.5 * x ** 3 - 0.648

def funcB(x, y):
    return 2 * x ** 2 - 2 * y ** 2

def getPolynomLine(x, koefs):

    dim = np.shape(x)
    
    y = np.zeros(dim)

    for i in range(dim[0]):

        j = 0
        for a in koefs:
            y[i] += a * x[i] ** j
            j += 1

    return y

def getPolynomSurface(x, y, koefs: list):
   
    if np.shape(koefs)[0] == 3:
        z = koefs[0] + koefs[1] * x + koefs[2] * y
    else:
        z = koefs[0] + koefs[1] * x + koefs[2] * y + koefs[3] * x * y + koefs[4] * x ** 2 + koefs[5] * y ** 2 

    return z

def solveSystemOne(table, power):

    # A * X = B
    # x = A^(-1) * B

    dim = power + 1
    
    koefsA = np.zeros((dim, dim))
    koefsB = np.zeros((dim, 1))

    for i in range(dim):
        for j in range(dim):
            koefsA[i, j] = np.sum(table.weight * table.x ** (i + j))

        koefsB[i, 0] = np.sum(table.weight * table.y * table.x ** i)

    koefs = solve(koefsA, koefsB)

    return koefs.reshape((dim, ))
    
def solveSystemTwo(table, power):

    if power == 1:
        dim = 3

        koefsA = np.array([
            [
            np.sum(table.weight),
            np.sum(table.weight * table.x),
            np.sum(table.weight * table.y)
            ],
            [
            np.sum(table.weight * table.x),
            np.sum(table.weight * table.x ** 2),
            np.sum(table.weight * table.y * table.x)
            ],
            [
            np.sum(table.weight * table.y),
            np.sum(table.weight * table.x * table.y),
            np.sum(table.weight * table.y ** 2)
            ]
        ])

        koefsB = np.array([
            [np.sum(table.weight * table.z)],
            [np.sum(table.weight * table.z * table.x)],
            [np.sum(table.weight * table.z * table.y)]
        ])
    else:
        dim = 6

        koefsA = np.array([
            [
            np.sum(table.weight),
            np.sum(table.weight * table.x),
            np.sum(table.weight * table.y),
            np.sum(table.weight * table.x * table.y),
            np.sum(table.weight * table.x ** 2),
            np.sum(table.weight * table.y ** 2)
            ],
            [
            np.sum(table.weight * table.x),
            np.sum(table.weight * table.x ** 2),
            np.sum(table.weight * table.y * table.x),
            np.sum(table.weight * table.x ** 2 * table.y),
            np.sum(table.weight * table.x ** 3),
            np.sum(table.weight * table.y ** 2 * table.x)
            ],
            [
            np.sum(table.weight * table.y),
            np.sum(table.weight * table.x * table.y),
            np.sum(table.weight * table.y ** 2),
            np.sum(table.weight * table.x * table.y ** 2),
            np.sum(table.weight * table.x ** 2 * table.y),
            np.sum(table.weight * table.y ** 3)
            ],
            [
            np.sum(table.weight * table.x * table.y),
            np.sum(table.weight * table.x ** 2 * table.y),
            np.sum(table.weight * table.y ** 2 * table.x),
            np.sum(table.weight * table.x ** 2 * table.y ** 2),
            np.sum(table.weight * table.x ** 3 * table.y),
            np.sum(table.weight * table.y ** 3 * table.x)
            ],
            [
            np.sum(table.weight * table.x ** 2),
            np.sum(table.weight * table.x ** 3),
            np.sum(table.weight * table.y * table.x ** 2),
            np.sum(table.weight * table.x ** 3 * table.y),
            np.sum(table.weight * table.x ** 4),
            np.sum(table.weight * table.y ** 2 * table.x ** 2)
            ],
            [
            np.sum(table.weight * table.y ** 2),
            np.sum(table.weight * table.x * table.y ** 2),
            np.sum(table.weight * table.y ** 3),
            np.sum(table.weight * table.x * table.y ** 3),
            np.sum(table.weight * table.x ** 2 * table.y ** 2),
            np.sum(table.weight * table.y ** 4)
            ]
        ])

        koefsB = np.array([
            [np.sum(table.weight * table.z)],
            [np.sum(table.weight * table.z * table.x)],
            [np.sum(table.weight * table.z * table.y)],
            [np.sum(table.weight * table.z * table.x * table.y)],
            [np.sum(table.weight * table.z * table.x ** 2)],
            [np.sum(table.weight * table.z * table.y ** 2)]
        ])
    
    koefs = solve(koefsA, koefsB)
    
    return koefs.reshape((dim, ))

############################ solve ODE ############################

def getPolynom(x, n: int, koefs: list):

    if n == 2:
        return 1 - x + koefs[0] * x * (1 - x) + koefs[1] * x ** 2 * (1 - x)
    else:
        return 1 - x + koefs[0] * x * (1 - x) + koefs[1] * x ** 2 * (1 - x) + koefs[2] * x ** 3 * (1 - x)

def getInitFunc(x):
    return (math.exp(-x**2/2) * ((1 + math.exp(x**2/2) * x) * erfi(1/math.sqrt(2)) - (1 + math.sqrt(math.e)) * erfi(x/math.sqrt(2))))/erfi(1/math.sqrt(2))

def solveODE():

    xStart = -0.5
    xEnd = 2
    n = 10

    x = np.linspace(xStart, xEnd, n)
    y = np.array([getInitFunc(x_i) for x_i in x])

    # m = 2

    alphas = -2 + 2 * x - 3 * x ** 2
    bethas = 2 - 6 * x + 3 * x ** 2 - 4 * x ** 3
    alphas_bethas = alphas * bethas
    
    koefsA = np.array([[np.sum(alphas ** 2), np.sum(alphas_bethas)],
                       [np.sum(alphas_bethas), np.sum(bethas ** 2)]])
   
    sum_1 = alphas * (4 * x - 1)
    sum_2 = bethas * (4 * x - 1)
    
    koefsB = np.array([[np.sum(sum_1)],
                       [np.sum(sum_2)]])
    
    koefsX_2 = solve(koefsA, koefsB).reshape((2, ))
    print(koefsX_2)

    y_2 = getPolynom(x, 2, koefsX_2)

    # m = 3

    gammas = 6 * x - 12 * x ** 2 + 4 * x ** 3 - 5 * x ** 4
    alphas_gammas = alphas * gammas
    bethas_gammas = bethas * gammas

    koefsA = np.array([[np.sum(alphas ** 2), np.sum(alphas_bethas), np.sum(alphas_gammas)],
                       [np.sum(alphas_bethas), np.sum(bethas ** 2), np.sum(bethas_gammas)],
                       [np.sum(alphas_gammas), np.sum(bethas_gammas), np.sum(gammas ** 2)]])
    
    sum_3 = gammas * (4 * x - 1)
    
    koefsB = np.array([[np.sum(sum_1)],
                       [np.sum(sum_2)],
                       [np.sum(sum_3)]])

    koefsX_3 = solve(koefsA, koefsB).reshape((3, ))
    print(koefsX_3)

    y_3 = getPolynom(x, 3, koefsX_3)

    plt.grid(True)

    plt.plot(x, y_2, color = "blue", label = "m = 2")
    plt.plot(x, y_3, color = "red", label = "m = 3")
    plt.plot(x, y, color = "green", label = "Init func")

    plt.legend()

    plt.show()