from Table import Table
import numpy as np

def makeMultiDimInterpolationNewton(myTable: Table):
    
    zValues = np.array([])
    for i in range(myTable.z.shape[0]):
        
        yValues = np.array([])
        for j in range(myTable.y.shape[0]):
            
            xValues = np.array([])
            for k in range(myTable.x.shape[0]):
                xValues = np.append(xValues, [myTable.x[k], myTable.func[i][j][k]])

            xValues = xValues.reshape(xValues.shape[0] // 2, 2)

            funcValue = NewtonMethod(xValues, myTable.values[0], int(myTable.powers[0]))
            yValues = np.append(yValues, [myTable.y[j], funcValue])

        yValues = yValues.reshape(yValues.shape[0] // 2, 2)

        funcValue = NewtonMethod(yValues, myTable.values[1], int(myTable.powers[1]))
        zValues = np.append(zValues, [myTable.z[i], funcValue])

    zValues = zValues.reshape(zValues.shape[0] // 2, 2)

    funcValue = NewtonMethod(zValues, myTable.values[2], int(myTable.powers[2]))
    return funcValue

def makeMultiDimInterpolationSpline(myTable: Table):
    
    zValues = np.array([])
    for i in range(myTable.z.shape[0]):
        
        yValues = np.array([])
        for j in range(myTable.y.shape[0]):
            
            xValues = np.array([])
            for k in range(myTable.x.shape[0]):
                xValues = np.append(xValues, [myTable.x[k], myTable.func[i][j][k]])

            xValues = xValues.reshape(xValues.shape[0] // 2, 2)

            funcValue = splineMethod(xValues, myTable.values[0])
            yValues = np.append(yValues, [myTable.y[j], funcValue])

        yValues = yValues.reshape(yValues.shape[0] // 2, 2)

        funcValue = splineMethod(yValues, myTable.values[1])
        zValues = np.append(zValues, [myTable.z[i], funcValue])

    zValues = zValues.reshape(zValues.shape[0] // 2, 2)

    funcValue = splineMethod(zValues, myTable.values[2])
    return funcValue

def makeMultiDimInterpolationBoth(myTable: Table):
    
    zValues = np.array([])
    for i in range(myTable.z.shape[0]):
        
        yValues = np.array([])
        for j in range(myTable.y.shape[0]):
            
            xValues = np.array([])
            for k in range(myTable.x.shape[0]):
                xValues = np.append(xValues, [myTable.x[k], myTable.func[i][j][k]])

            xValues = xValues.reshape(xValues.shape[0] // 2, 2)

            funcValue = splineMethod(xValues, myTable.values[0])
            yValues = np.append(yValues, [myTable.y[j], funcValue])

        yValues = yValues.reshape(yValues.shape[0] // 2, 2)

        funcValue = NewtonMethod(yValues, myTable.values[1], int(myTable.powers[1]))
        zValues = np.append(zValues, [myTable.z[i], funcValue])

    zValues = zValues.reshape(zValues.shape[0] // 2, 2)
    funcValue = splineMethod(zValues, myTable.values[2])
    return funcValue

def NewtonMethod(pointTable, xValue, polyPower):

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

def splineMethod(pointTable, xValue):

    beg = 0
    end = 0

    pointTable = calculateSplineCoefs(pointTable, beg, end)
    return getSplineValue(pointTable, xValue)

def calculateSplineCoefs(pointTable, beg, end):

    columns = 6
    rows = pointTable.shape[0]

    for i in range(columns - 2):
        pointTable = np.append(pointTable, np.zeros((rows, 1)), axis = 1)
    
    pointTable[:, 2] = pointTable[:, 1] 

    pointTable = getC(pointTable, beg, end)
    pointTable = getBnD(pointTable)    

    return pointTable

def getBnD(pointTable):

    rows = pointTable.shape[0]
    
    for i in range(1, rows):

        h = pointTable[i, 0] - pointTable[i - 1, 0]
        
        pointTable[i - 1, 3] = (pointTable[i, 1] - pointTable[i - 1, 1]) / h - \
                                (h * (pointTable[i, 4] + 2 * pointTable[i - 1, 4]) / 3)
        pointTable[i - 1, 5]   = (pointTable[i, 4] - pointTable[i - 1, 4]) / (3 * h)

    h = pointTable[-1, 0] - pointTable[-2, 0]

    pointTable[-1, 3] = (pointTable[-1, 1] - pointTable[-2, 1]) / h - \
                        ((h * 2 * pointTable[-1, 4]) / 3)
    pointTable[-1, 5] = -pointTable[-1, 4] / (3 * h)

    return pointTable

def getC(pointTable, beg, end):

    rows = pointTable.shape[0]
    pointTable[0, 4] = beg / 2

    xi = [0, beg]
    theta = [0, beg]

    for i in range(2, rows):
        h_2 = pointTable[i, 0] - pointTable[i - 1, 0]
        h_1 = pointTable[i - 1, 0] - pointTable[i - 2, 0]

        phi = getPhi(pointTable[i - 2, 1], pointTable[i - 1, 1], pointTable[i, 1], h_1, h_2)
        
        xiCur = getXi(xi[i - 1], h_1, h_2)

        thetaCur = getTheta(phi, theta[i - 1], xi[i - 1], h_1, h_2)
        
        xi.append(xiCur)
        theta.append(thetaCur)

    pointTable[-2, 4] = theta[-1]

    for i in reversed(range(1, rows - 1)):
        pointTable[i - 1, 4] = xi[i] * pointTable[i, 4] + theta[i]

    return pointTable

def getPhi(y1, y2, y3, h1, h2):
    return 3 * ((y3 - y2) / h2 - (y2 - y1) / h1)

def getXi(xi, h1, h2):
    return - h2 / (h1 * xi + 2 * (h2 + h1))

def getTheta(phi, tetha, xi, h1, h2):
    return (phi - h1 * tetha) / (h1 * xi + 2 * (h2 + h1))

def getIndex(pointTable, xValue):

    rows = pointTable.shape[0]
    index = 1

    while (index < rows and pointTable[index, 0] < xValue):
        index += 1

    return index - 1

def getSplineValue(pointTable, xValue):

    index = getIndex(pointTable, xValue)

    h = xValue - pointTable[index, 0]
    y = 0

    for i in range(4):
        y += pointTable[index, i + 2] * (h ** i)

    return y
