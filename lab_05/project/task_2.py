import numpy as np
import math

from scipy.integrate import simps

def f(x):
    return (2 / math.sqrt(2 * math.pi)) * math.exp(-(x ** 2) / 2)

def calculate(func, xCur, steps):
    step = xCur / steps

    xValues = np.linspace(0, xCur, steps * 2)
    funcValues = np.array([func(x_i) for x_i in xValues])

    sumX1 = np.sum([funcValues[2 * i - 1] for i in range(1, steps)])
    sumX2 = np.sum([funcValues[2 * i] for i in range(1, steps - 1)])

    return (step / 3) * (4 * funcValues[0] + funcValues[-1] + sumX1 + sumX2)

def simpson(func, xCur):
    integ, integPrev = 100, 0
    eps = 1e-5
    steps = 1

    while np.abs(integ - integPrev) > eps:
        integPrev = integ
        integ = calculate(func, xCur, steps)
        steps += 1

    return integ, steps

xCur = np.abs(float(input("\nEnter current x: ")))

ans, steps = simpson(f, xCur)

print(f"\nAmount of iterations is: {steps}")
print(f"Answer for {xCur:.5f} is: {ans:.5f}")
# print(f"Answer for {xCur:.5f} with builtin function is: {simps():.5f}")


