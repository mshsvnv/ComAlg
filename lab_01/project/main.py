import calcAlg as ca
from classTable import Table

def inputData():

    xValue = input("\nInput X: ")

    try:
        xValue = float(xValue)
    except:
        raise ValueError("Wrong type of value!") from None
    
    return xValue

def directInterpolation():

    print("\nDirect interpolation:\n")

    dataAll = list()
    xValue = None

    for i in range(3):

        polyPow = i + 1
        NewtonTable = Table("Newton")                       
        HermitTable = Table("Hermit")

        NewtonTable.readData("data/data_new.csv")
        HermitTable.readData("data/data_new.csv")

        if i == 0:
            NewtonTable.printTable("Initial Table")
            xValue =  inputData()
            NewtonTable.drawGraph()

        NewtonTable.makeConfiguration(xValue, polyPow, 1)
        ca.calculateDividedDiffNewton(NewtonTable)

        HermitTable.makeConfiguration(xValue, polyPow, 1)
        HermitTable.duplicateConfiguration()
        ca.calculateDividedDiffHermit(HermitTable)

        yValueNewton = ca.getPolyValue(NewtonTable, xValue)
        yValueHermit = ca.getPolyValue(HermitTable, xValue)

        dataAll.append([yValueNewton, yValueHermit])
    
    print("X: {:.3f}".format(xValue))
    Table.printData(dataAll)

def reverseInterpolation():

    print("\nReverse interpolation:\n")

    dataAll = list()
    xValue = 0

    for i in range(3):

        polyPow = i + 1
        NewtonTable = Table("Newton")                       
        HermitTable = Table("Hermit")

        NewtonTable.readData("data/data_new.csv", "reverse")
        HermitTable.readData("data/data_new.csv", "reverse")

        NewtonTable.makeConfiguration(xValue, polyPow, 0)
        ca.calculateDividedDiffNewton(NewtonTable)

        HermitTable.makeConfiguration(xValue, polyPow, 0)
        HermitTable.duplicateConfiguration()
        ca.calculateDividedDiffHermit(HermitTable)

        yValueNewton = ca.getPolyValue(NewtonTable, xValue)
        yValueHermit = ca.getPolyValue(HermitTable, xValue)
        
        dataAll.append([yValueNewton, yValueHermit] )
    
    print("Y: {:.3f}".format(xValue))
    Table.printData(dataAll)

def solveSystem():

    print("\nSystem solution:\n")

    dataAll = list()

    for i in range(5):
        len_n = i

        polyPow = i + 1
        xValue = 0

        tableFirst = Table("Tabel_1")                      
        tableFirst.readData("data/data_1.csv")

        tableSecond = Table("Table_2")
        tableSecond.readData("data/data_2.csv")

        if i + 1 == tableFirst.rows:
            break

        tableFirst.makeConfiguration(tableFirst.data[tableFirst.rows // 2, 0], tableFirst.rows - 1)
        ca.calculateDividedDiffNewton(tableFirst)
        
        newY = tableFirst.makeNewTable(tableSecond)
        tableSecond.addDifferences(newY)

        tableSecond.makeConfiguration(xValue, polyPow)
        ca.calculateDividedDiffNewton(tableSecond)
        
        xValue = ca.getPolyValue(tableSecond, xValue)
        yValue = ca.getPolyValue(tableFirst, xValue)

        dataAll.append([xValue, yValue])

    Table.printData(dataAll, "system")

if __name__ == "__main__":
    directInterpolation()

    reverseInterpolation()

    solveSystem()