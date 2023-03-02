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

    for i in range(5):

        polyPow = i + 1
        NewtonTable = Table("Newton")                       
        HermitTable = Table("Hermit")

        NewtonTable.readData("data/data.csv")
        HermitTable.readData("data/data.csv")

        if i == 0:
            NewtonTable.printTable("Initial Table")
            xValue =  inputData()

        NewtonTable.makeConfiguration(xValue, polyPow)
        ca.calculateDividedDiffNewton(NewtonTable)

        HermitTable.makeConfiguration(xValue, polyPow)
        HermitTable.duplicateConfiguration()
        ca.calculateDividedDiffHermit(HermitTable)

        yValueNewton = ca.getPolyValue(NewtonTable, xValue)
        yValueHermit = ca.getPolyValue(HermitTable, xValue)

        dataAll.append([yValueNewton, yValueHermit])
    
    print("X: {:.3f}".format(xValue))
    Table.printData(dataAll)

    # NewtonTable = Table("Newton")                       
    # HermitTable = Table("Hermit")

    # NewtonTable.readData("data/data.csv")
    # HermitTable.readData("data/data.csv")

    # NewtonTable.printData("\nInit table: ")

    # xValue, polyPow = inputData("X")

    # NewtonTable.makeConfiguration(xValue, polyPow)
    # ca.calculateDividedDiffNewton(NewtonTable)

    # HermitTable.makeConfiguration(xValue, polyPow)
    # HermitTable.duplicateConfiguration()
    # ca.calculateDividedDiffHermit(HermitTable)

    # NewtonTable.printData("\nNewton's method:")
    # HermitTable.printData("\nHermit's method:")

    # ca.getPolyValue(NewtonTable, xValue, True)
    # ca.getPolyValue(HermitTable, xValue, True)

def reverseInterpolation():

    print("\nReverse interpolation:\n")

    dataAll = list()
    xValue = 0

    for i in range(5):
        polyPow = i + 1
        NewtonTable = Table("Newton")                       
        HermitTable = Table("Hermit")

        NewtonTable.readData("data/data.csv", "reverse")
        HermitTable.readData("data/data.csv", "reverse")

        NewtonTable.makeConfiguration(xValue, polyPow)
        ca.calculateDividedDiffNewton(NewtonTable)

        HermitTable.makeConfiguration(xValue, polyPow)
        HermitTable.duplicateConfiguration()
        ca.calculateDividedDiffHermit(HermitTable)

        yValueNewton = ca.getPolyValue(NewtonTable, xValue)
        yValueHermit = ca.getPolyValue(HermitTable, xValue)

        dataAll.append([yValueNewton, yValueHermit] )
    
    print("Y: {:.3f}".format(xValue))
    Table.printData(dataAll, "reverse")

    # NewtonTableReverse = Table("Newton")                
    # HermitTableReverse = Table("Hermit")

    # NewtonTableReverse.readData("data/data.csv", "reverse")
    # HermitTableReverse.readData("data/data.csv", "reverse")

    # xValue, polyPow = inputData("Y", False)

    # NewtonTableReverse.makeConfiguration(xValue, polyPow)
    # ca.calculateDividedDiffNewton(NewtonTableReverse)

    # HermitTableReverse.makeConfiguration(xValue, polyPow)
    # HermitTableReverse.duplicateConfiguration()
    # ca.calculateDividedDiffHermit(HermitTableReverse)

    # NewtonTableReverse.printData("\nNewton's method:")
    # HermitTableReverse.printData("\nHermit's method:")

    # ca.getPolyValue(NewtonTableReverse, xValue, True, "reverse")
    # ca.getPolyValue(HermitTableReverse, xValue, True, "reverse")

def solveSystem():

    print("\nSystem solution:\n")

    dataAll = list()

    for i in range(5):

        polyPow = i + 1
        xValue = 0

        tableFirst = Table("Tabel_1")                      
        tableFirst.readData("data/data_1.csv")

        tableSecond = Table("Table_2")
        tableSecond.readData("data/data_2.csv")

        tableFirst.makeConfiguration(tableFirst.data[tableFirst.rows // 2, 0], tableFirst.rows - 1)
        ca.calculateDividedDiffNewton(tableFirst)
        
        newY = tableFirst.makeNewTable(tableSecond)
        tableSecond.addDifferences(newY)

        # tableSecond.printData("\nNew Table")

        tableSecond.makeConfiguration(xValue, polyPow)
        ca.calculateDividedDiffNewton(tableSecond)

        # print("\nAnswer for System:")
        
        xValue = ca.getPolyValue(tableSecond, xValue)
        yValue = ca.getPolyValue(tableFirst, xValue)

        dataAll.append([xValue, yValue])

    Table.printData(dataAll, "system")

    # tableFirst = Table("Tabel_1")                      
    # tableFirst.readData("data/data_1.csv")
    # tableFirst.printData("\nx(y)")

    # tableSecond = Table("Table_2")
    # tableSecond.readData("data/data_2.csv")
    # tableSecond.printData("\ny(x)")
    
    # xValue, polyPow = inputData("Y", False)

    # tableFirst.makeConfiguration(tableFirst.data[tableFirst.rows // 2, 0], tableFirst.rows - 1)
    # ca.calculateDividedDiffNewton(tableFirst)
    
    # newY = tableFirst.makeNewTable(tableSecond)
    # tableSecond.addDifferences(newY)

    # tableSecond.printData("\nNew Table")

    # tableSecond.makeConfiguration(xValue, polyPow)
    # ca.calculateDividedDiffNewton(tableSecond)

    # print("\nAnswer for System:")
    
    # xValue = ca.getPolyValue(tableSecond, xValue, True, "reverse")
    # ca.getPolyValue(tableFirst, xValue, True)

if __name__ == "__main__":
    directInterpolation()

    reverseInterpolation()

    solveSystem()