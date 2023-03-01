from classTable import Table
import numpy as np
import matplotlib.pyplot as plt

def calculateDividedDiffNewton(myTable: Table):  # divided differences for Newton Polynom

    myTable.columns = myTable.polyPow + 2

    myTable.data[:, -1] = 0

    for j in range(myTable.polyPow - 1):
        myTable.data = np.append(myTable.data, np.zeros((myTable.rows, 1)), axis = 1)

    for j in range(myTable.polyPow):
        for i in range(myTable.columns - j - 2):
            myTable.data[i, j + 2] = (myTable.data[i, j + 1] - myTable.data[i + 1, j + 1]) / (myTable.data[i, 0] - myTable.data[j + i + 1, 0])

def calculateDividedDiffHermit(myTable: Table):  # divided differences for Newton Polynom

    myTable.columns = myTable.polyPow * 2 + 3

    myTable.data[-1, -1] = 0

    for j in range(myTable.polyPow * 2):
        myTable.data = np.append(myTable.data, np.zeros((myTable.rows, 1)), axis = 1)

    for j in range(myTable.polyPow * 2 + 1):
        for i in range(myTable.columns - j - 2):
            
            if myTable.data[i, 0] - myTable.data[j + i + 1, 0] == 0:
                myTable.data[i, j + 2] = myTable.data[i, 2]
            else:
                myTable.data[i, j + 2] = (myTable.data[i, j + 1] - myTable.data[i + 1, j + 1]) / (myTable.data[i, 0] - myTable.data[j + i + 1, 0])    

def getPolyValue(myTable, xValue, output: False, type = "direct"):

    yValue = myTable.data[0, -1]

    for i in range(1, myTable.columns - 1): 
        yValue = myTable.data[0, myTable.columns - i - 1] + (xValue - myTable.data[myTable.rows - i - 1, 0]) * yValue

    if output:
        if type == "reverse":
            print("\nX by {}: {:.6f}".format(myTable.method, yValue))
        else:
            print("\nY by {}: {:.6f}".format(myTable.method, yValue))
    
    return yValue

# def drawGraphs(table1, table2):

    plt.style.use('classic')

    fig, axes = plt.subplots()

    x = table1.data[:, 0]
    y = table1.data[:, 1]

    axes.plot(x, y, "red")

    x = table2.data[:, 0]
    y = table2.data[:, 1]

    axes.plot(x, y, "blue")

    axes.grid(True)
    plt.show()
