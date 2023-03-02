import calcAlg as ca
from Table import Table

def inputData():

    xValue = input("\nInput X: ")

    try:
        xValue = float(xValue)
    except:
        raise ValueError("Wrong type of value!") from None
    
    return xValue

def splineInterpolation(xValue):

    splineTable = Table()
    splineTable.readData("./data/data.csv")

    print("\nSpline:")

    beg, end = 0, 0

    for i in range(3):
        if i == 1:
            beg = ca.getNewtonDerivative(0)
        elif i == 2:
            end = ca.getNewtonDerivative(-1)

        ca.calculateSplineCoefs(splineTable, beg, end)
        yValue = ca.getSplineValue(splineTable, xValue)

        if i == 0:
            print("\t0 and 0:             {}".format(yValue))
        elif i == 1:
            print("\tP''(x0) and 0:       {}".format(yValue))
        else:
            print("\tP''(x0) and P''(xn): {}".format(yValue))

def NewtonInterpolation(xValue):

    NewtonTable = Table()
    NewtonTable.readData("./data/data.csv")
    NewtonTable.makeConfiguration(xValue, 3)
    ca.calculateDividedDiffNewton(NewtonTable)

    yValue = ca.getPolyValue(NewtonTable, xValue)

    print("\nNewton: {:.6f}".format(yValue))

if __name__ == "__main__":
    initTable = Table()
    initTable.readData("./data/data.csv")
    Table.printData(initTable.data, "init")

    xValue = inputData()

    NewtonInterpolation(xValue)
    splineInterpolation(xValue)

