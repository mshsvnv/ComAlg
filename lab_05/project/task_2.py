import numpy as np
import math

from scipy.integrate import simps

def f(x):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-(x ** 2) / 2)

def simpson(func, xCur, steps, xStart = 0):
    step = (xCur - xStart) / (steps * 2)

    xValues = np.array([i * step for i in range(steps * 2 + 1)])
    funcValues = np.array([func(x_i) for x_i in xValues])

    sumX1 = 4 * np.sum([funcValues[2 * i - 1] for i in range(1, steps)])
    sumX2 = 2 * np.sum([funcValues[2 * i] for i in range(1, steps - 1)])

    return (step / 3) * (funcValues[0] + funcValues[-1] + sumX1 + sumX2)

def calculate(func, xCur, xStart = 0):
    steps = 1
    integ, integPrev = 1e4, 0
    eps = 1e-5

    while np.abs(integ - integPrev) > eps:
        integPrev = integ
        integ = simpson(func, xCur, steps, xStart)
        steps += 1

    return integ

xCur = np.abs(float(input("\nEnter current x: ")))
xStart = 0

ans = calculate(f, xCur, xStart)

x = np.arange(0, 2)
y = np.array([f(x_i) for x_i in x])

# print(f"\nAmount of iterations is: {steps}")
print(f"Answer for {xCur:.5f} is: {ans:.5f}")
print(f"Answer for {xCur:.5f} with builtin function is: {simps(y, x):.5f}")
