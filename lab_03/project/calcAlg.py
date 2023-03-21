from Table import Table
import numpy as np
from scipy.misc import derivative
from matplotlib import pyplot as plt

def makeMultiDimInterpolationNewton(myTable: Table):
    
    zValues = np.array([])
    for i in range(myTable.z.shape[0]):
        
        yValues = np.array([])
        for j in range(myTable.y.shape[0]):
            
            xValues = np.array([])
            for k in range(myTable.x.shape[0]):
                xValues = np.append(xValues, [myTable.x[k], myTable.func[i][j][k]])

            xValues = xValues.reshape(xValues.shape[0] // 2, 2)

            funcValue = getNewtonValue(xValues, myTable.values[0], int(myTable.powers[0]))
            yValues = np.append(yValues, [myTable.y[j], funcValue])

        yValues = yValues.reshape(yValues.shape[0] // 2, 2)

        funcValue = getNewtonValue(yValues, myTable.values[1], int(myTable.powers[1]))
        zValues = np.append(zValues, [myTable.z[i], funcValue])

    zValues = zValues.reshape(zValues.shape[0] // 2, 2)

    funcValue = getNewtonValue(zValues, myTable.values[2], int(myTable.powers[2]))
    return funcValue

def makeMultiDimInterpolationNewton(myTable: Table):
    
    zValues = np.array([])
    for i in range(myTable.z.shape[0]):
        
        yValues = np.array([])
        for j in range(myTable.y.shape[0]):
            
            xValues = np.array([])
            for k in range(myTable.x.shape[0]):
                xValues = np.append(xValues, [myTable.x[k], myTable.func[i][j][k]])

            xValues = xValues.reshape(xValues.shape[0] // 2, 2)

            funcValue = getSplineValue(xValues, myTable.values[0], int(myTable.powers[0]))
            yValues = np.append(yValues, [myTable.y[j], funcValue])

        yValues = yValues.reshape(yValues.shape[0] // 2, 2)

        funcValue = getSplineValue(yValues, myTable.values[1], int(myTable.powers[1]))
        zValues = np.append(zValues, [myTable.z[i], funcValue])

    zValues = zValues.reshape(zValues.shape[0] // 2, 2)

    funcValue = getSplineValue(zValues, myTable.values[2], int(myTable.powers[2]))
    return funcValue


def getNewtonValue(pointTable, xValue, polyPower):

    pointTable = makeConfiguration(pointTable, xValue, polyPower)
    pointTable = calculateDividedDiffNewton(pointTable, polyPower)
    
    return getPolyValue(pointTable, xValue)

def makeConfiguration(pointTable, xValue, polyPower):
    
    rows = pointTable.shape[0]
    index = 0

    for i in range(1, rows):
        if pointTable[i - 1, 0] <= xValue <= pointTable[i, 0]: 
            index = i
            break

    i = 0
    beg, end = index, index

    while (i != polyPower):
        if beg != 0:
            beg -= 1
            i += 1

        if (i == polyPower):
            break

        if end != rows - 1:
            end += 1
            i += 1

    for i in range(beg):
        pointTable = np.delete(pointTable, 0, axis = 0)

    for i in range(end + 1, rows):
        pointTable = np.delete(pointTable, -1, axis = 0)
    
    return pointTable

def calculateDividedDiffNewton(pointTable, polyPower):

    rows = pointTable.shape[0]
    columns = polyPower + 2

    for j in range(polyPower):
        pointTable = np.append(pointTable, np.zeros((rows, 1)), axis = 1)
        
    for j in range(polyPower):
        for i in range(columns - j - 2):
            pointTable[i, j + 2] = (pointTable[i, j + 1] - pointTable[i + 1, j + 1]) / (pointTable[i, 0] - pointTable[j + i + 1, 0])

    return pointTable

def getPolyValue(pointTable, xValue):

    yValue = pointTable[0, -1]

    rows = pointTable.shape[0]
    columns = pointTable.shape[1]

    for i in range(1, columns - 1): 
        yValue = pointTable[0, columns - i - 1] + (xValue - pointTable[rows - i - 1, 0]) * yValue
    return yValue

def getSplineValue(pointTable, xValue):
    pass

# def calculateSplineCoefs(myTable, beg, end):

#     myTable.columns = 6

#     for i in range(4):
#         myTable.data = np.append(myTable.data, np.zeros((myTable.rows, 1)), axis = 1)
    
#     myTable.data[:, 2] = myTable.data[:, 1] 

#     getC(myTable, beg, end)
#     getBnD(myTable)    

# def getBnD(myTable):
    
#     for i in range(1, myTable.rows):

#         h = myTable.data[i, 0] - myTable.data[i - 1, 0]
        
#         myTable.data[i - 1, 3] = (myTable.data[i, 1] - myTable.data[i - 1, 1]) / h - \
#                                 (h * (myTable.data[i, 4] + 2 * myTable.data[i - 1, 4]) / 3)
#         myTable.data[i - 1, 5]   = (myTable.data[i, 4] - myTable.data[i - 1, 4]) / (3 * h)

#     h = myTable.data[-1, 0] - myTable.data[-2, 0]

#     myTable.data[-1, 3] = (myTable.data[-1, 1] - myTable.data[-2, 1]) / h - \
#                         ((h * 2 * myTable.data[-1, 4]) / 3)
#     myTable.data[-1, 5] = -myTable.data[-1, 4] / (3 * h)

# def getC(myTable, beg, end):

#     myTable.data[0, 4] = beg / 2

#     xi = [beg]
#     theta = [beg]

#     for i in range(2, myTable.rows):
#         h_2 = myTable.data[i, 0] - myTable.data[i - 1, 0]
#         h_1 = myTable.data[i - 1, 0] - myTable.data[i - 2, 0]

#         phi = getPhi(myTable.data[i - 2, 1], myTable.data[i - 1, 1], myTable.data[i, 1], h_1, h_2)
        
#         xiCur = getXi(xi[i - 2], h_1, h_2)

#         thetaCur = getTheta(phi, theta[i - 2], xi[i - 2], h_1, h_2)
        
#         xi.append(xiCur)
#         theta.append(thetaCur)

#     myTable.data[-1, 4] = end / 2

#     for i in range(myTable.rows - 2, 0, -1):
#         myTable.data[i - 1, 4] = xi[i - 1] * myTable.data[i, 4] + theta[i - 1]


# def getPhi(y1, y2, y3, h1, h2):
#     return 3 * ((y3 - y2) / h2 - (y2 - y1) / h1)

# def getXi(xi, h1, h2):
#     return - h2 / (h1 * xi + 2 * (h2 + h1))

# def getTheta(phi, tetha, xi, h1, h2):
#     return (phi - h1 * tetha) / (h1 * xi + 2 * (h2 + h1))

# def getIndex(myTable, xValue):

#     index = 1

#     while (index < myTable.rows and myTable.data[index, 0] < xValue):
#         index += 1

#     return index - 1

# def getSplineValue(myTable, xValue):

#     index = getIndex(myTable, xValue)

#     h = xValue - myTable.data[index, 0]
#     y = 0

#     for i in range(4):
#         y += myTable.data[index, i + 2] * (h ** i)

#     return y

# def getNewtonDerivative(number):
    
#     NewtonTable = Table()
#     NewtonTable.readData("./data/data.csv")
#     NewtonTable.makeConfiguration(NewtonTable.data[number, 0], 3)
#     calculateDividedDiffNewton(NewtonTable)

#     def aprocFunc(xValue):
#         return getPolyValue(NewtonTable, xValue)
    
#     yDerivative = derivative(aprocFunc, NewtonTable.data[number, 0], n = 2, dx = 1e-6)

#     return yDerivative

