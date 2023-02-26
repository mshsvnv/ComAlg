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

def drawGraphs(table, table2):

    plt.style.use('classic')

    fig, axes = plt.subplots()

    y = table.data[:, 0]
    x = table.data[:, 1]

    axes.plot(x, y)

    x = table2.data[:, 0]
    y = table2.data[:, 1]

    axes.plot(x, y)

    # fig, axes = plt.subplots(1, 2)

    # xNew = np.linspace(np.amin(NewtonTable.data[:, 0]), np.amax(NewtonTable.data[:, 0]), 20)

    # yNewNewton = np.array([getPolyValue(NewtonTable, xValue, False) for xValue in xNew])
    # yNewHermit = np.array([getPolyValue(HermitTable, xValue, False) for xValue in xNew])

    # axes[0].plot(xNew, yNewNewton, label = 'polynom', color = 'black')
    # axes[1].plot(xNew, yNewHermit, label = 'polynom', color = 'black')

    # plt.title("My Plot")

    # for i in range(2):
    #     axes[i].set_xlabel("X")
    #     axes[i].set_ylabel("Y")

    #     axes[i].scatter(NewtonTable.data[:, 0],NewtonTable.data[:, 1], label = 'init points', linewidth = 3, color = 'red')
   
    #     axes[i].legend()

    #     axes[i].grid(True)

    plt.show()
