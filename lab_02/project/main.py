import calcAlg as ca
import numpy as np
from Table import Table

fileName = "./data/data.csv"

def inputData():

    xValue = input("\nInput X: ")

    try:
        xValue = float(xValue)
    except:
        raise ValueError("Wrong type of value!") from None
    
    return xValue

def splineInterpolation(xValue, repeats = 3):

    splineTable = Table()
    splineTable.readData(fileName)

    print("\nSpline:")

    beg, end = 0, 0

    for i in range(repeats):
        if i == 1:
            beg = ca.getNewtonDerivative(0)
        elif i == 2:
            end = ca.getNewtonDerivative(-1)
        # print(beg, end)

        ca.calculateSplineCoefs(splineTable, beg, end)
        yValue = ca.getSplineValue(splineTable, xValue)

        if i == 0:
            print("\t0 and 0:             {}".format(yValue))
        elif i == 1:
            print("\tP''(x0) and 0:       {}".format(yValue))
        else:
            print("\tP''(x0) and P''(xn): {}".format(yValue))

        # print(splineTable.data)

    return splineTable

def NewtonInterpolation(xValue, power):

    NewtonTable = Table()
    NewtonTable.readData(fileName)
    NewtonTable.makeConfiguration(xValue, power)
    ca.calculateDividedDiffNewton(NewtonTable)

    yValue = ca.getPolyValue(NewtonTable, xValue)

    print("\nNewton: {:.6f}".format(yValue))

    return NewtonTable

if __name__ == "__main__":
    initTable = Table()
    initTable.readData(fileName)
    Table.printData(initTable.data, "init")

    xValue = inputData()

    if not (np.amin(initTable.data[:, 0]) <= xValue <= np.amax(initTable.data[:, 0])):
        raise ValueError("Extrapolation is forbidden!") from None
    
    power = 2

    if initTable.rows >= 4:
        power = 3

    Newton = NewtonInterpolation(xValue, power)
    spline = splineInterpolation(xValue)

    ca.drawGraph(Newton, spline)
        

        

