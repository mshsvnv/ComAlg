from Table import Table
import numpy as np
from scipy.misc import derivative
from matplotlib import pyplot as plt

def calculateDividedDiffNewton(myTable: Table):

    myTable.columns = myTable.polyPow + 2

    for j in range(myTable.polyPow):
        myTable.data = np.append(myTable.data, np.zeros((myTable.rows, 1)), axis = 1)

    for j in range(myTable.polyPow):
        for i in range(myTable.columns - j - 2):
            myTable.data[i, j + 2] = (myTable.data[i, j + 1] - myTable.data[i + 1, j + 1]) / (myTable.data[i, 0] - myTable.data[j + i + 1, 0])

def getPolyValue(myTable, xValue):

    yValue = myTable.data[0, -1]

    for i in range(1, myTable.columns - 1): 
        yValue = myTable.data[0, myTable.columns - i - 1] + (xValue - myTable.data[myTable.rows - i - 1, 0]) * yValue
    return yValue

def calculateSplineCoefs(myTable, beg, end):

    myTable.columns = 6

    for i in range(4):
        myTable.data = np.append(myTable.data, np.zeros((myTable.rows, 1)), axis = 1)
    
    myTable.data[:, 2] = myTable.data[:, 1] 

    getC(myTable, beg, end)
    getBnD(myTable)    

def getBnD(myTable):
    
    for i in range(1, myTable.rows):

        h = myTable.data[i, 0] - myTable.data[i - 1, 0]
        
        myTable.data[i - 1, 3] = (myTable.data[i, 1] - myTable.data[i - 1, 1]) / h - \
                                (h * (myTable.data[i, 4] + 2 * myTable.data[i - 1, 4]) / 3)
        myTable.data[i - 1, 5]   = (myTable.data[i, 4] - myTable.data[i - 1, 4]) / (3 * h)

    h = myTable.data[-1, 0] - myTable.data[-2, 0]

    myTable.data[-1, 3] = (myTable.data[-1, 1] - myTable.data[-2, 1]) / h - \
                        ((h * 2 * myTable.data[-1, 4]) / 3)
    myTable.data[-1, 5] = -myTable.data[-1, 4] / (3 * h)

def getC(myTable, beg, end):

    myTable.data[0, 4] = beg

    xi = [beg]
    theta = [beg]

    for i in range(2, myTable.rows):
        h_2 = myTable.data[i, 0] - myTable.data[i - 1, 0]
        h_1 = myTable.data[i - 1, 0] - myTable.data[i - 2, 0]

        phi = getPhi(myTable.data[i - 2, 1], myTable.data[i - 1, 1], myTable.data[i, 1], h_1, h_2)
        
        xiCur = getXi(xi[i - 2], h_1, h_2)

        thetaCur = getTheta(phi, theta[i - 2], xi[i - 2], h_1, h_2)
        
        xi.append(xiCur)
        theta.append(thetaCur)

    myTable.data[-1, 4] = end

    for i in range(myTable.rows - 2, 0, -1):
        myTable.data[i - 1, 4] = xi[i - 1] * myTable.data[i, 4] + theta[i - 1]

def getPhi(y1, y2, y3, h1, h2):
    return 3 * ((y3 - y2) / h2 - (y2 - y1) / h1)

def getXi(xi, h1, h2):
    return - h2 / (h1 * xi + 2 * (h2 + h1))

def getTheta(phi, tetha, xi, h1, h2):
    return (phi - h1 * tetha) / (h1 * xi + 2 * (h2 + h1))

def getIndex(myTable, xValue):

    index = 1

    while (index < myTable.rows and myTable.data[index, 0] < xValue):
        index += 1

    return index - 1

def getSplineValue(myTable, xValue):

    index = getIndex(myTable, xValue)

    h = xValue - myTable.data[index, 0]
    y = 0

    for i in range(4):
        y += myTable.data[index, i + 2] * (h ** i)

    return y

def getNewtonDerivative(number):
    
    NewtonTable = Table()
    NewtonTable.readData("./data/data.csv")
    NewtonTable.makeConfiguration(NewtonTable.data[number, 0], 3)
    calculateDividedDiffNewton(NewtonTable)

    def aprocFunc(xValue):
        return getPolyValue(NewtonTable, xValue)
    
    yDerivative = derivative(aprocFunc, NewtonTable.data[number, 0], n = 2, dx = 1e-6)

    return yDerivative

def drawGraph(Newton, spline):

    xList = np.linspace(np.min(Newton.data[:, 0]), np.max(Newton.data[:, 0]), 100)
    yList = np.array([getPolyValue(Newton, x) for x in xList])
    
    plt.plot(xList, yList, color='r', label = "Newton")

    xList = np.linspace(np.min(spline.data[:, 0]), np.max(spline.data[:, 0]), 1000)
    yList = np.array([getSplineValue(spline, x) for x in xList])
    
    plt.plot(xList, yList, "blue", label = "Spline")

    xList = spline.data[:, 0]
    yList = np.array([getSplineValue(spline, x) for x in xList])
    
    plt.plot(xList, yList, "green", marker = ".")
    
    plt.legend()
    plt.show()
